# Manuelo247

## 06/10/2025
Inicie con el uso de la libreria Reall3dViewer para visualizar los escaneos de los vuelos en una pagina hosteada por nosotros mismos

## 07/10/2025
Primeras pruebas de carga de modelos, comprobacion y transformacion de archivos de las pruebas de vuelo. Los .ply tienen que ser generados como gaussian splatting o no se podra transformar al formato compatible.

## 08/10/2025
Terra tiene soporte para 3dgs(3D Gaussian Splatting) pero unicamente cuando se hace fotogrametria, el vuelo fue exitoso y contiene datos de la rtk.

## 09/10/2025
Primera visualizacion exitosa del modelo con la libreria, la version 'full' de la prueba del vuelo del dia 03/10/25 tiene varios bloques (Dividido gracias al tamaño del escaneo), estos pueden ser fusionados y visualizarse a distintas calidades.

## 10/10/2025 
Se preparo la pagina para visualizacion de varios modelos con seleccion para cambiar entre ellos. Se vio un limitante de _Fetch_ al momento de descargar o subir archivos, se hicieron pruebas para solucionarlo pero no hubo exito. Se cree que puede deberse a una propia limitante del codigo y de la capacidad de la gpu de cada maquina.