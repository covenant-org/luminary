---
icon: tools
---
# Configuraciones y herramientas

Documentación sobre las diferentes herarmientas y configuraciones que se
han utilizado para el desarrollo de los diferentes proyectos implementados
sobre la plataforma de desarrollo NVIDIA Jetson

## YOLO

Modelo de detección y segmentación de objetos enfocado en tiempo real, de la
mano de Ultralytics.

Para instalar exitosamente la la libreria de Ultralytics siga el siguiente
procedimiento:

#### 1. Actualizar los repositorios

```bash
sudo apt-get update
sudo apt install python3-pip -y
pip install -U pip
```

#### 4. Crear un entorno virtual (opcional)

```bash
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
```


#### 3. Instalar la libreria de ultralytics

```bash
pip install ultralytics[export]
```
!!! light
Se pude omitir _[export]_ si no se desea cambiar de formato los archivos de pesos
!!!

!!! warning
En versiones recientes de pip, el dependency resolver toma demasiado tiempo
para resolver la dependencia adicional de export de ultralytics.
Por lo que se recomienda agregar

```--use-deprecated=legacy-resolver```
!!!

#### 4. Instalar cusParselt

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/arm64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install libcusparselt0 libcusparselt-dev
```
!!! light
Los comandos mencionados son para las versiones específicas que se encuentran
en la jetson. Para posibles actualizaciones visitar el [sitio oficial](https://developer.nvidia.com/cusparselt-downloads)
!!!

#### 5. Instalar PyTorch y Torchvision

```bash
pip install https://developer.download.nvidia.cn/compute/redist/jp/v61/pytorch/torch-2.5.0a0+872d972e41.nv24.08.17622132-cp310-cp310-linux_aarch64.whl
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torchvision-0.20.0a0+afc54f7-cp310-cp310-linux_aarch64.whl
```

!!! light
Los whl son para la version 6.1 de Jetpack. Para posibles versiones visitar el sitio
oficial de [Nvidia](https://developer.download.nvidia.cn/compute/redist/jp/)
o la guía de [Ultralytics](https://docs.ultralytics.com/guides/nvidia-jetson/#install-pytorch-and-torchvision)
!!!

#### 6. Instalar onnxruntime

```bash
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/onnxruntime_gpu-1.20.0-cp310-cp310-linux_aarch64.whl
```
!!!
Onnx runtime cambia la versión de numpy por lo que se debe reinstalar una versión
en específico

```bash
pip install numpy==1.23.5
```
!!!


## Tensorrt

Librería de NVIDIA para C++ que facilita inferencias de alto desempeño en
unidades de procecsamiento graficas.TensorRT toma una red entrenada, compuesta
por una definición y un grupo de pesas y produce un motor de inferencia optimizado

Existen múltiples formas de instalar tensorrt en Jetson. Pero con la que se tuvo
éxito fue la siguiente:

```bash
wget https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/10.7.0/tars/TensorRT-10.7.0.23.l4t.aarch64-gnu.cuda-12.6.tar.gz
tar -xvzf TensorRT-10.7.0.23.l4t.aarch64-gnu.cuda-12.6.tar.gz
version=10.7.0.23
export LD_LIBRARY_PATH=${PWD}/TensorRT-${version}/lib:$LD_LIBRARY_PATH
cd TensorRT-${version}/python
pip install tensorrt-*-cp310-none-linux_aarch64.whl
```

## Jtop (Jetson Stats)

Programa que muestra estadisticas de la Jetson en tiempo real, como el uso
de GPU y que cuenta con interfaz programática en python

```bash
sudo pip3 install -U jetson-stats
```

> [:icon-mark-github: Jetson Stats](https://github.com/rbonghi/jetson_stats)


## Wadi

Wadi es un servicio de streaming que utiliza el protocolo WebRTC para transmitir
video en tiempo real a un servidor WHIP. Se utiliza para transmitir el video de
la cámara FPV a un servidor para su consumo remoto

#### 1. Clonar el repositorio [:icon-mark-github: Wadi](https://github.com/covenant-org/wadi)

```bash
git clone https://github.com/covenant-org/wadi.git
```

#### 2. Compilar el proyecto

```bash
cd wadi
cmake -B build -H. -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

#### 3. Copiar el ejectuable a la carpeta de binarios

```bash
sudo cp build/wadi /usr/bin
```

#### 4. Crear servicios y regla de udev

Cree los siguientes archivos en la ruta especificada. Estos son ejemplos y
pueden cambiar de acuerdo a sus necesidades

El siguiente servicio se ejecuta en espacio de usuario, observe la ruta

:::code source="../static/wadi.service" title="~/.config/systemd/user/wadi.service" :::
[!file](../static/wadi.service)

:::code source="../static/wadi.target" title="~/.config/systemd/user/wadi.target" :::
[!file](../static/wadi.target)

Recuerde que necesita habilitar el servicio mediante

```sh
systemctl --user enable wadi.service
systemctl --user enable wadi.target
```

:::code source="../static/elgato.service" title="/etc/systemd/system/elgato.service" :::
[!file](../static/elgato.service)

Recuerde que necesita habilitar el servicio mediante

```sh
sudo systemctl enable elgato.service
```

:::code source="../static/99-wadi.rules" title="/etc/udev/rules.d/99-wadi.rules" :::
[!file](../static/99-wadi.rules)


## ZED SDK

El SDK de ZED es una herramienta de desarrollo que permite interactuar con
la cámara ZED de manera programática. Se utiliza para capturar y procesar
la información visual de la cámara ZED.


#### 1. Instalar el SDK de ZED

Descargar el SDK desde su página [:icon-device-camera-video: ZED SDK](https://www.stereolabs.com/en-mx/developers/release#nvidia-jetson-504616ef8d38)

!!!
De preferencia descargar las versiones que no sean Release Candidates (RC)
!!!

```bash
chmod +x ZED_SDK_Tegra_L4T_38.0.101.76.run # Reemplazar con la version correcta
./ZED_SDK_Tegra_L4T_38.0.101.76.run
```

!!! warning
Se probó con la versión de Jetpack 6.1 (la version 6.2 da algunos errores de instalación)
!!!


#### 2. Instalar el controlador de monolink

```bash
wget https://stereolabs.sfo2.cdn.digitaloceanspaces.com/utils/drivers/ZEDX/1.3.0/R36.4/stereolabs-zedlink-mono_1.3.0-SL-MAX9296-all-L4T36.4.0_arm64.deb
sudo dpkg -i stereolabs-zedlink-mono_1.3.0-SL-MAX9296-all-L4T36.4.0_arm64.deb
```

!!!
Despues de instalar el controlador de monolink se debe reiniciar la Jetson
!!!

#### 3. Conectar la cámara

_3.1._ Conectar flex al puerto de cam1 de la Jetson

_3.2._ Conectar flex a la tarjeta monolink de ZED

_3.3._ Conectar el cable GMSL2 a la tarjeta monolink de ZED

_3.4._ Conectar el cable GMSL2 a la cámara ZED

_3.5._ Energizar la tarjeta monolink de ZED (12v-19v min 2w)

_3.6._ Energizar la Jetson

_3.7._ Ejecutar el visor ZED_Explorer en la Jetson (opcional)

## Wireguard

Due to compatibility reasons, the version distributed by default of `wireguard` doesn't work
when trying to up the interface defined by our conf file. To fix this we can use the following
clone which works on:

```sh
nuclea@ubuntu:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.5 LTS
Release:	22.04
Codename:	jammy
nuclea@ubuntu:~$ uname -r
5.15.148-tegra
```

[Use this version](https://github.com/MrVasquez96/wireguard-linux-compat) but run the steps
from the [Official Wireguard Site](https://www.wireguard.com/compilation/).

## Sierra WWAN EM7455 USB Modem

Este módulo permite establecer una conexión de datos a redes 4G/3G/2G. Y 
en linux requiere de drivers distribuidos por sierra. Los pasos para instalar
dichos drivers se detalla a continuación

#### 1. Verificar que se tengan las herramientas de compilación

Se requiere un compilador de c como gc y make. Ambos se encuentran en la
paqueteria `build-essential`

```bash
sudo apt update
sudo apt install build-essential
```

#### 2. Verificar que se tengan las cabeceras de Linux

En Jetson se encuentran en /usr/src/linux-headers-5.15.148-tegra/3rdparty/canonical
y por lo general se encuentran en la instalación por defecto

#### 3. Descargar los drivers de Sierra

Se pueden descagar los drivers directo de la página oficial de Sierra 
[aqui](https://source.sierrawireless.com/resources/airprime/software/mbpl/mbpl-software-latest/)
con la única desventaja que en Tegra parece faltar un par de módulos (cdc-wdm,cdc_mbim)
por lo que se deben agregar a los módulos a compilar. El paquete con los módulos faltantesel siguiente comando en la carpeta donde se encuentran los archivos "usb"

```bash
make
sudo make install
```

#### 5. Configurar el módulo

En teoría el módulo debería configurarse automáticamente con los datos del 
proveedor del chip, sin embargo en pruebas esto no ocurría por lo que se debe 
configurar de manera manual mediante Network Manager.

A continuación se detallan los comandos para configurar el módulo con el 
proveedor telcel. Se deberá reconfigurar si se cambia de proveedor

```bash
sudo nmcli c add con-name "wwan" type gsm ifname "*" apn "internet.itelcel.com"
sudo nmcli c mod wwan connection.autoconnect yes
sudo nmcli c mod mycon gsm.username "webgpr"
sudo nmcli c mod mycon gsm.password "webgprs2002"
# show the connection
sudo cat /etc/NetworkManager/system-connections/wwan
# start the connection
sudo nmcli c up mycon
```

#### 6. Visualizar el estado del módulo

```bash
mmcli -m 0
```

#### Comandos útiles

```bash
# Listar los módulos
mmcli -L
# Listar la información de conexión
mmcli -b 0
# Probar ping con la interfaz de wwan
ping -I wwan0 8.8.8.8
```
