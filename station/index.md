# Estación de aterrizaje

La estación de aterrizaje es un proyecto de hardware desarrollado por
covenant con el propósito de ofrecer una plataforma de aterrizaje, despegue
y monitoreo de un quadricoptero

## Manual (WIP)

Manual de usuario y técnico que servirá como referencia a futuro

### Inicio rápido

#### VPN

Para conectarse de forma sencilla y remota a la estación, es necesario 
ser parte de la VPN ZeroTier de covenant. 

Si no se es parte, comunicarse con el equipo de desarrollo.

#### QGroundControl

QGroundControl es el sistem de control de tierra que se utiliza para
comunicarse con el dron. Se puede desrcargar de su repositorio [https://github.com/mavlink/qgroundcontrol/releases](Releases)

Al ejecutarlo debería conectarse de forma automática al dron, de no hacerlo
vea la sección de Troubleshooting


#### Video

Para ver una vista general del estado del dron sin descargar QGroundControl, 
puede acceder a esta liga [Cherum](https://cherum.covenant.space)
Donde si habilita WEBGPU en su navegador podrá observar la cámara del dron si se encuentra activa

Para ver únicamente el video puede visitar [Video Server](http://159.54.131.60:8889/wadi/)

#### Arquitectura

Se plantea tener 4 componentes en nuestro sistema:

- API: Administracion de usuarios, estaciones, etc.
- Video: Almacenamiento de video y stream hacia clientes
- App: Enfocado en los clientes y desde la cual van a poder administrar estaciones, ver alertas, etc.
- Estacion: Frigate custom mas software de monitoreo y actualizaciones.

En la imagen a continuacion se puede observar a mas detalle la arquitectura:

![Arquitectura de la Estacion V1](/static/ArchitectureV1.png)

## Bitácora

### 05 - 12 - 2025

Investigación sobre OSS para las actualizaciones de la estación (Mender & swupdate) y comienzo del prototipo de servidor. 

## 06 - 01 - 2026

@jeduardofr: Review de codigo, planeacion de video historico y puestos de PAP para ITESO

## 07 - 01 - 2026

@jeduardofr: Planeacion, frigate para ambiente de pruebas con zeus y configuraciones
de pangolin para abrir plataforma hacia el internet.

## 08 - 01 - 2026

@jeduardofr: Actualizar pangolin a la version 1.14.0

## 09 - 01 - 2026

@jeduardofr: Review de codigo, configuracion de mqtt para telemetria de DJI

## 04 - 02 - 2026

@jeduardofr: Reviews de codigo

## 05 - 02 - 2026

@jeduardofr: Reviews de Código 

## 09 - 02 - 2026

@jeduardofr: Pruebas de hardware con la estacion

## 10 - 02 - 2026

@jeduardofr: Pruebas de hardware con la estacion y Reviews de Codigo

## 11 - 02 - 2026

@jeduardofr: Misiones con dron DJI, mapeo de El Cajon, reviews de codigo y documentacion de PDAL para procesamiento de nube de puntos.

## 13 - 02 - 2026

@jeduardofr: Reviews, pruebas con PDAL para nubes de puntos

## 16 - 02 - 2026

@jeduardofr: Definicion de area para mapeos de El Cajon usando QGIS, Google Earth Pro y CloudCompare para limpieza y generacion. Reviews de covenant

## 18 - 02 - 2026

@jeduardofr: Pruebas de NTRIP con Matrice 400, presentacion para la charla en el TEC del 19/02/26

## 19 - 02 - 2026

@jeduardofr: Reviews, QGIS para mision del Cajon, ambientes para estacion, presentacion del TEC.

## 20 - 02 - 2026

@jeduardofr: Procesamiento de misiones de El Cajon por cuadrantes para evitar que Terra se queda estancado, hasta el momento ha funcionado bien.

## 22 - 02 - 2026

@jeduardofr: Procesamiento de misiones mas investigacion sobre los crashes de Cronos al procesar los vuelos, todo indica a que la temperatura de la oficina sin aire acondicionado esta siendo un problema.

## 27 - 02 - 2026

@jeduardofr: Pruebas con QGIS para la clasificacion de la nube de puntos
