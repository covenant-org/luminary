# WebRTC con HTTPS y STUN server

Para lograr configurar WebRTC con Pangolin (traefik & gerbil) se tuvo que
abrir los puertos del servidor de AWS para permitir trafico en el puerto
9189/udp. Tambien se abrio este puerto en gerbil directamente en nuestro
`docker-compose.yml` asi como en la config de `config/traefik/traefik`
