# Stack de self-host

- [wireguard](https://www.wireguard.com/): VPN
- [pangolin](https://github.com/fosrl/pangolin): Reverse proxy con tuneles
- [minio](https://github.com/minio/minio): Almacenamiento (como S3 de AWS)
- [beszel](https://beszel.dev/): Monitoreo

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