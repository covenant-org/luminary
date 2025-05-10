# Pruebas de vuelo

Registro de las pruebas de vuelo que se realizan cada semana

---

## 06 - Mar - 2025


---

## 13 - Mar - 2025

- @jeduardofr: Build para la AppImage de la version modificada de QGC aunque no se probo debido a
 errores de dependencias
- @jeduardofr: Probar vuelo remoto con mavproxy con dron anclado al suelo, salieron varios detalles
 como que el dron parecia "perder" el control y se aceleraba por su cuenta sin recibir los comandos.
 La teoria esta en que es debido a como esta anclado el suelo y como el sistema de control reacciona.
 Sigue pendiente hacer la prueba con el dron ya en vuelo normal.
- @fairbrook: Hacer prueba con video con un servidor de video remoto. La prueba fue exitosa.
La dirección del servidor es: `http://159.54.131.60:8889/comma/` para webrtc 
y `rtsp://159.54.131.60:8554/comma/` para rtsp (util en qground) 
__!!! Estas direcciones van a cambiar en el futuro !!!__
- @fairbrook y @jeduardofr: Validación de connexión mediante red celular.
La comma no detectaba la tarjeta SIM, el modem no detectaba la SIM. 
El problema fue que el puerto SIM estaba dañado, al revisar a detalle, uno de los
pines del puerto estaba doblado y no hacía contacto correctamente.
Por lo que la solución fue doblar de vuelta a posición el pin y se corregieron los problemas.
Al finalizar la prueba fue exitosa.
Comando útiles para el módulo SIM:

```bash
mmcli -M # Escaneo de modems
mmcli -L # Lista de modems disponibles
mmcli -m 0 # Mostrar información del modem 0
mmcli -m 0 --messaging-create-sms="number=+523323191926,text='hola'" # Enviar sms a un numero
mmcli -m --messaging-list-sms # Listar sms (recibidos y enviados)
mmcli -m 0 -s 0 # Mostrar información del mensaje 0
mmcli -m 0 -s 0 --send # Enviar sms 0
```

---

## 20 - Mar - 2025

Este día fue mucho trabajo en equipo para hacer la prueba de vuelo con el dron 
anclado al suelo.

- Configuración de sistema de poleas y cuerdas para mantener al dron dento de 
un rango de movimiento seguro
- Prueba de vuelo exitosa con el sistema de poleas para prevenir caidas del dron al
activar el "kill switch"
- Prueba de vuelo exitosa con el sistema de cuerdas para prevenir colisiones
con paredes, objetos y personas
- Prueba de vuelo exitosa con el control remoto. Utilizando dos equipos 
(mavproxy y QGC) y mando de xbox. _El fallo de la semana anterior fue que el
dron no tenía espacio de movimiento en el eje Z_

---

## 24 - Mar - 2025

Plan de conexión para la cámara FPV. El diagrma a continuación ejemplifica las
interacciones entre los distintos componentees del sistema que permitiría la
visualización de la cámara 
[Moonlight](https://caddxfpv.com/products/walksnail-moonlight-kit?variant=47701308997934)
en QGC y de forma remota en cualquier
dispositivo

```mermaid
graph LR;
    D[Power Distribution Board] --> N
    D --> P
    P[Pixhawk] <-->|UART OSD MSP| TX[Moonlight VTX]
    N[Nuclea Power Board] --> TX[Moonlight VTX]
    TX --> RX[Avatar VRX]
    RX -->|HDMI| C[Capturadora]
    C -->|HDMI| M[Monitor]
    C -->|USB| PC[PC]
    PC -->|RTSP| MTX[Mediamtx]
    MTX -->|RTSP| QGC
```


## 25 - Mar -2025

- @fairbrook: Hacer prueba con video con un servidor de video remoto. La prueba fue exitosa.
Uitilizando OBS y WHIP se pudo hacer una transmisión de video con alta calidad y latencia
muy baja ~330ms. Al intentar hacer la transmisión de video utilizando el kit de
desarrollo Jetson Nano, la calidad fue menor y con una latencia de ~1.3s. Por lo
que se busca desarrollar un programa que permita la transmisión de video en la 
paltaforma Jetson Nano al utilizar "Hardware Encoding" y WHIP

---

## 01 - Abr - 2025

@fairbrook: Pruebas de latencia con video receptor y transmisor montado en dron y en estación de trabajo. Latencia aproximada de 800ms
@jeduardofr: Pruebas de vuelo remoto usando puro video (sin observar el dron) con version modificada de joystick (yaw, pitch & roll factors)

## 12 - Abr - 2025

@jeduardofr: Configuracion del sensor optico para mejor lectura de distancia vertical (altura). Mantenimiento
general del dron.

## 08 - May - 2025

@fairbrook: Configuración de antenas de telemetría P900

## 09 - May - 2025

@fairbrook: pruebas de vuelo y recalibracion del dron