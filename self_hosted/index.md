# Stack de self-host

- [wireguard](https://www.wireguard.com/): VPN
- [pangolin](https://github.com/fosrl/pangolin): Reverse proxy con tuneles
- [minio](https://github.com/minio/minio): Almacenamiento (como S3 de AWS)
- [beszel](https://beszel.dev/): Monitoreo
- [lxd](https://canonical.com/lxd) Contenedores para desarrollo 

## Programas utiles para conexiones de red

- nc (netcat): conexiones con TCP y UDP
- iptables: firewall
- tcpdump: inspeccionar trafico de redes

## Ejemplos de comandos

Permitir trafico hacia `puerto`, proveniente  de `ip`, con protocolo `p` (tcp, udp, etc.)

**Nota**: Este comando pondra la regla hasta arriba del listado, lo que significa que se procesara antes
que el resto de reglas que se tengan definidas.

```
sudo iptables -I INPUT -m $p -p $p -s $ip --dport $puerto -j ACCEPT
```

Hacer una conexion hacia host con `ip` y `puerto`
```
nc -zv $ip $puerto
```

Escuchar por trafico en cierta `interfaz` de red hacia cierto `puerto`

```
sudo tcpdump -ni $interfaz port $puerto
```

## Compartir red local a traves de wireguard (distinta a la red del wireguard)

1. Modificar configuracion de algunos de los peer que tiene acceso a la red que nos interesa compartir
y agregar las siguientes lineas en el apartado de `Interface`:

```
PostUp = iptables -A FORWARD -i interfaz-de-wireguard -j ACCEPT; iptables -t nat -A POSTROUTING -o interfaz-a-compartir -j MASQUERADE
PostDown = iptables -D FORWARD -i interfaz-de-wireguard -j ACCEPT; iptables -t nat -D POSTROUTING -o interfaz-a-compartir -j MASQUERADE
```

Las interfaces se pueden consultar con `ip addr`.

2. Modificar la configuracion del servidor para el peer que publico la nueva red, lo que se tiene que hacer
es agregar la red local al peer o la ip del equipo (para mayor control, sobre lo que se comparte) en
`AllowedIPs` seperado por comas, por ejemplo se podria ver:

```
AllowedIPs = 10.50.44.2/32, 192.168.10.90/24
```

Recordar reiniciar el servicio con `sudo systemctl restart wg-quick@wg0`, modificar el wg0 con la interfaz
correcta.

3. Modificar archivo del peer que quiere tener acceso a esta red y al igual solo agregar la direccion
local del peer que la expuso, por ejemplo:

```
AllowedIPs = 10.50.44.0/24, 192.168.10.0/24
```

Recordar reiniciar la conexion de wireguard para que los cambies tomen efecto con
`sudo wg-quick down wg0 && sudo wg-quick up wg0` y cambiar la interfaz por la correcta.


## Ambientes de trabajo virtual (Isaacsim + VNC)

### LXC

LXC será nuestra herramienta de contenerización ya que nos permite tener un ambiente muy similar al que tendríamos con una máquina virtual, es decir, por defecto tenemos acceso a un usuario no root, systemd y los paquetes estandar de ubuntu server. Instalarlo es muy sencillo

```bash
sudo snap install lxd
sudo lxd init
```

Al instalar le pedirá un tamaño para el sistema de archivos internos, nosotros decidimos utilizar 200GB por instancia, planea acorde

Una guía más afondo para la instalación se puede encontrar [aquí](https://canonical.com/lxd/install)

Para lanzar la instancia base utilizamos la imagen ubuntu:22.04

```bash
lxc launch ubuntu:22.04 workstation
lxc config device add workstation gpu gpu
```

### Lightdm

Este display manager es el encargado de inicializar el servidor de Xorg que utilizará posteriormente VirtualGL para renderizar por hardware el ambiente gráfico

```bash
sudo apt install lightdm
```
!!!
Si tiene instalado otro display manager es necesario desinstalarlo, por ejemplo
```bash
sudo apt purge gdm3
```
!!!

### Nvidia drivers

Si bien, en teoría cualquier drivers de nvidia funcionan, encontramos que los drivers oficiales en su versión __MIT__ son los que hacían funcionar a todo el setup

```bash
wget https://us.download.nvidia.com/XFree86/Linux-x86_64/570.169/NVIDIA-Linux-x86_64-570.169.run  
chmod +x NVIDIA-Linux-x86_64-570.169.run
sudo ./NVIDIA-Linux-x86_64-570.169.run
```
!!!warn
Tanto el host como el contenedor deberán contar con exactamente la misma versión de drivers para funcionar
!!!


### Virtual desktop

Para permitir que todo funcione sin que se tenga un display físico conectado, es necesario crear un dispositivo virtual en el contenedor por lo que podemos reemplazar el contenido de __/etc/X11/xorg.conf__

```bash
Section "ServerLayout"
    Identifier     "Layout0"
    Screen      0  "Screen0" 0 0
    InputDevice    "Keyboard0" "CoreKeyboard"
    InputDevice    "Mouse0" "CorePointer"
EndSection

Section "Module"
    Load           "glx"
EndSection

Section "InputDevice"

    # generated from default
    Identifier     "Keyboard0"
    Driver         "kbd"
EndSection

Section "InputDevice"

    # generated from default
    Identifier     "Mouse0"
    Driver         "mouse"
    Option         "Protocol" "auto"
    Option         "Device" "/dev/mouse"
    Option         "Emulate3Buttons" "no"
    Option         "ZAxisMapping" "4 5"
EndSection

Section "Monitor"
    Identifier     "Monitor0"
    VendorName     "Unknown"
    ModelName      "Unknown"
    Option         "DPMS"
EndSection

Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
EndSection
```

Para mantener consistentes los permisos es necesario reconstruir la configuración de xorg

```bash
sudo nvidia-xconfig
sudo reboot
```

### Virtual GL

Este software permite añadir soporte para renderización por hardare de las llamadas a OpenGL desde la VNC. Para instalarlo es más fácil siendo __sudo__

```bash
wget -q -O- https://packagecloud.io/dcommander/virtualgl/gpgkey | gpg --dearmor >/etc/apt/trusted.gpg.d/VirtualGL.gpg
cd /etc/apt/sources.list.d
wget https://raw.githubusercontent.com/VirtualGL/repo/main/VirtualGL.list
apt update
apt install virtualgl
```

Una vez instalado es necesario configurarlo para que tenga acceso a las interfaces de la tarjeta gráfica

```bash
sudo systemctl stop lightdm
sudo /opt/VirtualGL/bin/vglserver_config
sudo systemctl start ligthdm
```

En nuestro caso no restringimos a los usuarios de utilizar los dispositivos de nvida a pesar de que esto implique peor seguridad ya que estamos dentro de una red privada y en contenedores pero cambie las opciones de acuerdo a sus necesidades

### Turbo VNC

Se eligió este servidor de VNC ya que está diseñado específicamente para funcionar con VirtualGL. Al igual que con VirtualGL, estos pasos deberán seguirse con el usuario sudo

```bash
wget -q -O- https://packagecloud.io/dcommander/turbovnc/gpgkey | gpg --dearmor >/etc/apt/trusted.gpg.d/TurboVNC.gpg
cd /etc/apt/sources.list.d
wget https://raw.githubusercontent.com/TurboVNC/repo/main/TurboVNC.list
apt update
apt install turbovnc
```
Puede utilizar cualquier window manager que desee, en nuestro caso utilizamo mate más por gusto que por otra razón

```bash
sudo apt install mate-desktop-environment
```

Para facilitar que el vnc siempre se encienda con el contenedor y demás amenidades, creamos el siguiente servicio en __/etc/systemd/user/turbo-vnc@.service__

```
[Unit]
Description=VNC server for hardware acceleration

[Service]
Type=forking
ExecStart=/bin/bash -c "/opt/TurboVNC/bin/vncserver %i -vgl -geometry 1920x1080"
ExecStartPost=/bin/bash -c "DISPLAY=%i xhost +"
ExecStop=/opt/TurboVNC/bin/vncserver -kill %i

[Install]
WantedBy=default.target
ubuntu@covenant-workstation
```
Para habilitarlo y ejecutarlo utilice el siguiente commando desde el usuario deseado

```bash
systemctl --user enable turbo-vnc@:1
systemctl --user start turbo-bnc@:1
```
Para acceder al vnc desde fuera del contenedor y host es necesario crear un proxy desde lxc

```bash
lxc config device add test proxy-ws proxy listen=tcp:<host public ip>:5901 connect=tcp:<container ip >:5901 bind=host
```
El cliente de VNC recomendado es remmina o el mismo Turbo VNC

### Isaac sim

Ya que utilizamos PX4, decidimos utilizar [Pegasus Simulator](https://pegasussimulator.github.io/PegasusSimulator/) como bridge de comunicación con el simulador y la versión de isaac compatible es la 4.2

```bash
mkdir isaac-sim-4.2
cd isaac-sim-4.2
wget https://download.isaacsim.omniverse.nvidia.com/isaac-sim-standalone%404.2.0-rc.18%2Brelease.16044.3b2ed111.gl.linux-x86_64.release.zip
unzip isaac-sim-standalone@4.2.0-rc.18+release.16044.3b2ed111.gl.linux-x86_64.release.zip 
```

No fuimos capaces de hacer funcionar Isaac Sim directamente con nuestro entorno de VNC por lo que decidimos utilizar su función de streaming como medida temporal. Esperamos que con las próximas versiones estos problemas se solucionen o encontremos otra forma de hacer esto

Para descargar el cliente de webrtc de isaac sim ejecute los siguientes comandos

```bash
wget https://download.isaacsim.omniverse.nvidia.com/isaacsim-webrtc-streaming-client-1.0.6-linux-x64.AppImage
chmod +x isaacsim-webrtc-streaming-client-1.0.6-linux-x64.AppImage
```
Finalmente para ejecutar el simulador podemos ejecutar

```bash
./isaac-sim.headless.webrtc.sh
```

Y en otra terminal ya que se haya terminado de inicializar isaac sim ejecutamos el cliente de webrtc

```bash
./isaacsim-webrtc-streaming-client-1.0.6-linux-x64.AppImage --enable-unsafe-switfshader
```

### Tutorial para iniciar la simulación

[!embed](https://drive.google.com/file/d/1xF0_sIDWwL8dzvwKLmfPKI627ReZcwpK/preview)

## Recursos utiles

- [Beginners guide to traffic filtering with nftables](https://linux-audit.com/networking/nftables/nftables-beginners-guide-to-traffic-filtering/)
- [Differences between iptables and nftables explained](https://linux-audit.com/networking/nftables/differences-between-iptables-and-nftables-explained/)
