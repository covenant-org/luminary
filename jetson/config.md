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

#### 4. Crear servicio y regla de udev

Cree los siguientes archivos en la ruta especificada. Estos son ejemplos y 
pueden cambiar de acuerdo a sus necesidades

:::code source="../static/wadi@.service" title="/etc/systemd/system/wadi\@.service" :::
[!file](../static/wadi@.service)

!!! warning
El archivo de servicio utiliza el comando sleep para esperar que el servicio
de pulseaudio se inicie. No es la mejor forma de hacerlo y puede causar problemas
!!!

:::code source="../static/99-wadi.rules" title="/etc/udev/rules.d/99-wadi.rules" :::
[!file](../static/99-wadi.rules)
