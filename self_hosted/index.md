# Stack de self-host

- [wireguard](https://www.wireguard.com/): VPN
- [pangolin](https://github.com/fosrl/pangolin): Reverse proxy con tuneles
- [minio](https://github.com/minio/minio): Almacenamiento (como S3 de AWS)
- [beszel](https://beszel.dev/): Monitoreo
- [lxd](https://lxd.canonical) Contenedores para desarrollo 

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

## Recursos utiles

- [Beginners guide to traffic filtering with nftables](https://linux-audit.com/networking/nftables/nftables-beginners-guide-to-traffic-filtering/)
- [Differences between iptables and nftables explained](https://linux-audit.com/networking/nftables/differences-between-iptables-and-nftables-explained/)