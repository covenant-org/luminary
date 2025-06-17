# Kevin Research

## Controller

|Controller|Firmware|Advantages|Disadvantages|Store|
|--------------------------------------------------|
| Matrix 1S Brushless Flight Controller (5IN1) | Betaflight | <ul><li>Integrates ELRS, VTX, ESC and sensors in one board</li><li>Minimal Configuration</li></ul> | <ul><li>Cannot change each component independently</li><li>Made for specific drone Kits</li><li>Short flight time</li><li>No easy way of adding a companion computer</li><li>No redundant sensors</li><li>Need to include additional computer for onboard processing</li></ul> | [Betaflight](https://betafpv.com/collections/brushless-flight-controller/products/matrix-1s-brushless-flight-controller)|
| Cube orange | PX4 & Ardupilot | <ul><li>Compatibility with Pixhawk hardware and peripherals</li><li>Highly flexible configuration</li><li>Multiple general ports</li><li>Easily addition of companion computer</li><li>Redundant sensors</li><li>Multiple vendors</li></ul>|<ul><li>Needed to add external transmitters (VTX, telemetry, etc)</li><li>No ESC included</li><li>Need to include additional computer for onboard processing</li></ul>|[irlock](https://irlock.com/products/cube-orange-standard-set-ads-b-carrier-board?_pos=5&_sid=196826b7c&_ss=r) [Aliexpress mini](https://es.aliexpress.com/item/1005007591925042.html) [Aliexpress GPS](https://es.aliexpress.com/item/1005007672230054.html) [nwblue](https://nwblue.com/products/cube-orange-standard-set-ads-b-imu-v8)|
| ARKV6X | PX4 & Ardupilot | <ul><li>Compatibility with Pixhawk hardware and peripherals</li><li>Multiple sensors</li><li>Higghly flexible configuration</li><li>Multiple general ports</li><li>Jetson compatible board for both controller and Jetson</li><li>Redundant sensors</li><li>Single vendor complete ecosystem</li></ul> | <ul><li>Need to add external transmitters</li><li>No esc included</li><li>Need extra computer for full autonomy</li></ul> | [arkelectronics](https://arkelectron.com/product/arkv6x-bundle/) [arkelectronics + jetson carrier](https://arkelectron.com/product/ark-jetson-pab-carrier/)
| ARK Just a Jetson | Jetpack | <ul><li>High Compute capacity</li><li>Support for nvidia tooling and software</li><li>Single computer for control and processing</li></ul>|<ul><li>Reduced drone ports</li><li>Reduced sensors</li><li>Less specialized inputs</li><li>High power consumption</li></ul>| [arkelectronics](https://arkelectron.com/product/ark-just-a-jetson/)
| ARK Pi6X Flow | PX4 | <ul><li>High Compute capacity</li><li>Included video encoders and decoders</li><li>Multiple sensors and specialized connectors</li><li>Multiple general purpose connectors</li><li>Tight integration with companion computer</li><li>Single vendor ecosystem</li><li>Included optical flow</li></ul>|<ul><li>Expensive</li><li>Require external sensors and GNSS</li></ul>|[arkelectronics](https://arkelectron.com/product/ark-pi6x-flow/)
| Beale Bone Blue | Ardupilot, ROS, Debian, Cloud9 | <ul><li>Greate opensource community</li><li>Multiple firmware compatibility</li><li>Multiple actuator outputs</li><li>Included charger onboard</li><li>GGrapichs accelerator, FPU and A8 CPU</li></ul> | <ul><li>Not specifically designed for drones </li><li>Support for only 2-cell batteries</li><li>Few specialized connections</li></ul>|[Newark](https://mexico.newark.com/beagleboard/bbone-blue/beaglebone-blue-robotics-platform/dp/95Y0640?cfm=true)
| Navio 2 | Ardupilot & ROS | <ul><li>GNSS Included</li><li>Redundant power supply inputs</li><li>Redundant sensors</li><li>Versatile hat platform</li><li>Very active community</li><li>Full raspberry pi</li></ul> | <ul><li>Fewer extra serial ports</li><li>Requires a raspberry to work</li></ul> | [Mercado libre](https://www.mercadolibre.com.mx/navio2-piloto-automatico-para-dron-hat-para-raspberry-pi/up/MLMU589683356) [AM3D](https://am3d.topografia.digital/producto/navio2-piloto-automatico-para-dron-hat-para-raspberry-pi-potenciado-por-ardupilot-y-ros/)

### Summary
I would suggest the ARK Pi6x since it uses the already familiar PX4 platform and gives similar IO and sensor to the Pixhawk with the addition of a raspberry processing and memory capabilities, being the balance between compute power and light weight. The only drawback is the store as it is currently unstable and is uncertain if the controller would arrive on time.

A more cautious approach would be the Navio 2 as it still uses a raspberry but it is easier to get one. This time the drawback would be that is only the raspberry the one doing the control instead of the dedicated controller in the Pi6x

## Kits

### [3DR Quad zero kit](https://store.3dr.com/3dr-quad-zero-kit/)
The 3DR Quad Zero drone is a sub-250g focused on ultralight payloads and extended flight times (1hr). This kit is perfect as a development platform, educational or even a light show drone
We developed a telemetry radio around this platform to enhance its "developer platform" character, as it provides the hardware to include external sensors and send information over custom MAVLink messages, or on the contrary use those messages to push commands to any actuator without disrupting the flight stack or the autopilot's pinout.

## Frames

### [Kit Chasis F450](https://articulo.mercadolibre.com.mx/MLM-698668108-kit-chasis-f450-para-cuadricoptero-dron-_JM)
El marco principal es de fibra de vidrio, mientras que los brazos están fabricados con nylon de poliamida ultra resistente. Es una excelente opción para tomar video aérea o FPV volar sin el uso de los soportes de montaje adicionales.

• Cuenta con 4 brazos (2 blancos y 2 rojos) que son excelentes para la orientación ya que ayuda a mantener volando en la dirección correcta sin necesidad de diferentes hélices de colores
• También cuenta con conexiones de PCB integradas para la soldadura directa de sus ESC esto elimina la necesidad de una placa de distribución de energía o multicontactos desordenados manteniendo el diseño de su electrónica muy ordenada
• Este chasis V3 viene con brazos moldeados más fuertes que el V1 y V2

CARACTERÍSTICAS
• Material: Fibra de carbono de 2 mm y plástico
• Distancia entre ejes: 450 mm
• Dimensiones: 500 x 500 x 40 mm
• Peso: 265 g
