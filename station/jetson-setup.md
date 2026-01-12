# Configuracion de la Jetson con finalidad de estacion

Asumimos que estamos usando la version de Jetpack >=6.1. Para conocer la version que
tenemos instalada, podemos usar lo siguiente:

	# revisar la salida del siguiente comando
	cat /etc/nv_tegra_release
	# R36 (release), REVISION: 4.2, GCID: 38685322, BOARD: generic, EABI: aarch64, DATE: Fri Dec 13 00:16:27 UTC 2024
	# KERNEL_VARIANT: oot
	TARGET_USERSPACE_LIB_DIR=nvidia
	TARGET_USERSPACE_LIB_DIR_PATH=usr/lib/aarch64-linux-gnu/nvidia

A partir de la salida, armamos la version que tenemos concatenando la version de Release y Revision
que nos da: 36.4.2. Revisamos en la [siguiente liga](https://developer.nvidia.com/embedded/jetpack-archive)
y podemos confirmar que estamos usando la version Jetpack 6.1.

## Instalacion de Docker

Antes de proceder con la instalacion, asegurarnos que el sistema no cuenta con nada instalado
relacionado a docker. Si esto justo despues de la instalacion de Jetpack no deberia de hacer falta
pero vale la pena asegurarnos.

	sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc podman-docker containerd runc | cut -f1)

Para esto usamos un repositorio que ya cuenta con los scripts para instalar docker
y configurar el runtime con nvidia. Clonamos:

	git clone https://github.com/jetsonhacks/install-docker.git
	cd install-docker

Y procedemos a instalar docker mas el runtime de nvidia para docker

	bash ./install_nvidia_docker.sh

Confirmar que podemos correr un contenedor de docker:

	docker run hello-world

Si el contenedor corre sin problemas podemos pasar al siguiente paso. Si nos regresa un error como el siguiente:

	docker run hello-world
	Unable to find image 'hello-world:latest' locally
	latest: Pulling from library/hello-world
	198f93fd5094: Pull complete
	95ce02e4a4f1: Download complete
	Digest: sha256:d4aaab6242e0cace87e2ec17a2ed3d779d18fbfd03042ea58f2995626396a274
	Status: Downloaded newer image for hello-world:latest
	docker: Error response from daemon: failed to set up container networking: failed to create endpoint hardcore_haibt on network bridge: Unable to enable DIRECT ACCESS FILTERING - DROP rule:  (iptables failed: iptables --wait -t raw -A PREROUTING -d 172.17.0.2 ! -i docker0 -j DROP: iptables v1.8.7 (legacy): can't initialize iptables table `raw': Table does not exist (do you need to insmod?)
	Perhaps iptables or your kernel needs to be upgraded.
	 (exit status 3))

	Run 'docker run --help' for more information

Es un [error conocido](https://forums.developer.nvidia.com/t/iptables-error-message/333007) en
versiones de Jetpack 6.1 y 6.2. De momento se puede solucionar al bajar la version de docker
de nuestro sistema. Para esto ejecutamos el siguiente comando:

	sudo apt-get install -y docker-ce=5:27.5* docker-ce-cli=5:27.5* --allow-downgrades

Configuramos el runtime de nvidia con docker:

	bash ./configure_nvidia_docker.sh
