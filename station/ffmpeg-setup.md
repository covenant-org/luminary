# Compilación de FFmpeg con soporte NVMPI

Asumimos Jetpack >= 6.1 (ver `jetson-setup.md` para confirmar la versión) con los
SDK Components instalados (CUDA 12.6, cuDNN, TensorRT) y Ubuntu 22.04.

## ¿Por qué compilar FFmpeg?

El FFmpeg que viene por `apt` en Ubuntu **no** trae soporte para los codecs por
hardware de la Jetson. En Tegra, el encoder/decoder por hardware (NVENC/NVDEC) se
accede a través de la API L4T Multimedia (`nvmpi`), no por los `h264_nvenc` /
`cuvid` de escritorio. El daemon de Vergil (`daemon/stream/decoder.py`) usa
`hevc_nvmpi` / `h264_nvmpi` para decodificar — y en equipos con NVENC, como el AGX
Orin, también para codificar — por hardware. Por eso necesitamos un build propio.

Resultado esperado: un binario en `~/deps/ffmpeg/ffmpeg` que provee los encoders
`h264_nvmpi` y `hevc_nvmpi`, los decoders `h264/hevc/mpeg2/mpeg4/vp8/vp9_nvmpi`, y
los software `libx264` / `libx265`.

## Prerequisitos

Confirmar que la API L4T Multimedia está presente (la instalan los SDK Components):

	ls /usr/src/jetson_multimedia_api/include/nvbufsurface.h

Si no existe, instalarla:

	sudo apt-get install -y nvidia-l4t-jetson-multimedia-api

Herramientas de compilación (`clang` es necesario para `--enable-cuda-llvm`):

	sudo apt-get install -y ccache clang nasm yasm cmake build-essential \
	  pkg-config libx264-dev libx265-dev git

Todo el trabajo vive dentro de `~/deps`:

	mkdir -p ~/deps && cd ~/deps

## 1. Librería NVMPI (`libnvmpi.so`)

Provee `libnvmpi.so` + `nvmpi.pc`, que es contra lo que enlaza FFmpeg. Usamos el
fork de Keylost.

	cd ~/deps
	git clone --depth=1 https://github.com/Keylost/jetson-ffmpeg.git
	cd jetson-ffmpeg
	mkdir -p build && cd build
	cmake ..
	make -j"$(nproc)"
	sudo make install
	sudo ldconfig

CMake autodetecta la API de NvUtils via
`/usr/src/jetson_multimedia_api/include/nvbufsurface.h`. Verificar:

	pkg-config --cflags --libs nvmpi
	# -I/usr/local/include -L/usr/local/lib -lnvmpi

## 2. Headers ffnvcodec

Para `--enable-ffnvcodec`. Se instalan en un `PREFIX` no estándar para que no
opaquen los headers reales de CUDA:

	cd ~/deps
	git clone https://github.com/FFmpeg/nv-codec-headers.git
	cd nv-codec-headers
	sudo make install PREFIX=/usr/lib/ffmpeg/jetson

Esto deja el `.pc` en `/usr/lib/ffmpeg/jetson/lib/pkgconfig/ffnvcodec.pc`; le
apuntamos a `configure` via `PKG_CONFIG_PATH` en el siguiente paso.

## 3. FFmpeg + patch NVMPI

	cd ~/deps
	git clone -b release/6.0 --depth=1 https://github.com/FFmpeg/FFmpeg.git ffmpeg
	cd ffmpeg
	git apply ~/deps/jetson-ffmpeg/ffmpeg_patches/ffmpeg6.0_nvmpi.patch

El patch agrega `libavcodec/nvmpi_dec.c` / `nvmpi_enc.c` y la opción
`--enable-nvmpi`. Imprime warnings de whitespace; se ignoran. `configure`:

	PKG_CONFIG_PATH=/usr/lib/ffmpeg/jetson/lib/pkgconfig:$PKG_CONFIG_PATH \
	./configure \
	  --cc='ccache gcc' --cxx='ccache g++' \
	  --enable-shared --disable-static \
	  --enable-gpl --enable-libx264 --enable-libx265 \
	  --enable-nvmpi --enable-ffnvcodec --enable-cuda-llvm \
	  --disable-cuvid --disable-nvenc --disable-nvdec

> Si `configure` falla con `cuda_llvm requested but not found`, casi siempre es
> que falta `clang` (el error real en `ffbuild/config.log` es `clang: not found`).

## 4. Compilar e instalar

	make -j"$(nproc)"
	sudo make install
	sudo ldconfig

`sudo make install` es necesario aunque solo se quiera correr el binario in-place
desde `~/deps/ffmpeg/ffmpeg`, porque enlaza dinámicamente contra
`libavcodec.so.60`, etc., que deben estar en el loader path. De lo contrario:
`error while loading shared libraries: libavdevice.so.60`.

## Verificación

	~/deps/ffmpeg/ffmpeg -version | head -3
	~/deps/ffmpeg/ffmpeg -hide_banner -encoders 2>/dev/null | grep nvmpi
	~/deps/ffmpeg/ffmpeg -hide_banner -decoders 2>/dev/null | grep nvmpi

Encoders esperados (2): `h264_nvmpi`, `hevc_nvmpi`. Decoders esperados (6): h264,
hevc, mpeg2, mpeg4, vp8, vp9 (todos `_nvmpi`).

Prueba rápida por hardware (encode + decode de un patrón sintético):

	# encode por hardware
	~/deps/ffmpeg/ffmpeg -hide_banner -f lavfi -i testsrc=size=1280x720:rate=30 \
	  -t 3 -c:v h264_nvmpi -y /tmp/nvmpi_test.mp4
	# decode por hardware
	~/deps/ffmpeg/ffmpeg -hide_banner -c:v h264_nvmpi -i /tmp/nvmpi_test.mp4 -f null -

En los logs veremos mensajes de NVMPI como `NvMMLiteOpen ... BlockType` y
`NvVideo: bBlitMode is set to TRUE`, que confirman que se está usando el codec por
hardware.

> Nota: este build usa `-timeout` (no `-stimeout`) para el timeout de la demuxer
> RTSP — el nombre viejo `-stimeout` no existe aquí.

## Integración con Vergil

El daemon lee la ruta del binario de FFmpeg desde la variable `PROCESS_COMMAND` en
`/etc/vergil/variables.conf`. Apuntarla al build (reemplazar `<usuario>` por el
usuario real, p.ej. `covenant`):

	sudo sed -i.bak \
	  's#^PROCESS_COMMAND=.*#PROCESS_COMMAND=/home/<usuario>/deps/ffmpeg/ffmpeg#' \
	  /etc/vergil/variables.conf
	sudo systemctl restart daemon.service

Confirmar que el decoder en vivo usa los codecs por hardware:

	ps -eo args | grep '[f]fmpeg' | grep -oE 'hevc_nvmpi|h264_nvmpi|libx264'

En el AGX Orin (con NVENC) el decoder debe mostrar `hevc_nvmpi`/`h264_nvmpi` tanto
en decode como en encode. En equipos sin NVENC (p.ej. Orin Nano) el encode cae a
`libx264` por CPU.
