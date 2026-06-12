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

## 26/11/2025
Se investigo el framework de SWUpdate, el cual es perfectapara la estacion por que cubre todas nuestras necesidades dichas en https://github.com/covenant-org/luminary/issues/9

## 1/12/2025
Instalacion de tuberias en oficina

## 02/12/2025
Acomodo de rags, oficina y cables de red

## 03/12/2025
Instalacion de tuberias para redes y acomodo de televisores

## 04/12/2025
Instalacion de final de cables de oficina de covenant y principal

## 05/12/2025
Investigacion de SWUpdate para actualizaciones de estacion

## 08/12/2025
Prototipo para archivo de configuracion de SWUpdate firmado

## 09/12/2025
SWupdate pausado e iniciado con enviar clips a servidor central, recibir seniales de MQTT

## 29/12/2025
Con las previews de galleon. Se intento extraer las previews directamente pero se vuelve demasiado complejo.
Las previews de frigate son recortes de videos de baja calidad de una hora de duracion guardados en storage/preview. Cuando estos no estan generados todavia (Por generarse cada hora) se usa frames que estan guardados en el cache del docker que contiene frigate, ademas de no ser persistentes, la unica referencia a estos frames es sacandolos directamente del docker y la unica manera de utilizarlos en galleon es mandarlos o armando un video con esos elementos en cache y enviarlo. 
Por la complejidad de ese video parece mejor armar el video al momento de enviarse al servidor, donde habra una version original y una a baja calidad como gif o mp4.

## 20/02/2026
Se investigo de nuevas mejoras a agregar en galleon y la jetson

## 27/05/2026
Se estuvo trabajando en la estacion, en armar las piezas faltantes para tener una primera version.
Por mi parte estuve trabajando junto a Kevin en el modulo de computacion, de acomodar todo y configurar los modulos para que a cada componente le llegue el voltaje correspondiente

## 28/05/2026
Se terminaron los ultimos detalles de la estacion y se llevo con el atlas para mostrarlo

## 08/06/2026 
Llegamos temprano a la oficina para terminar las estaciones y hacer la instalacion. Por contratiempos no se pudo hacer la instalacion del dia de hoy pero no hubo problemas para dejarlo listo para los siguientes dias.

## 10/06/2026 
El dia de hoy nos toco llegar temprano otra vez, teniamos casi todo listo, solo era cuestion de validar el flujo completo y hacer la instalacion. Fuimos a las instalaciones del Atlas, Paco hizzo la instalacion mientras nosotros dejabamos la configuracion lista con su sistema, quedaron los streams pendientes de funcionar pero eso se validara hasta el dia de maniana.

## 11/06/2026
Despues de estar dias trabajando tantas horas extra se decidio tomar el dia libre, aunque estuvimos aun asi validando que los streamings funcionaran durante el dia.
