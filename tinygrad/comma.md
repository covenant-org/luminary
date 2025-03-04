# YOLO en Comma3X

Página para alojar la documentación e investación de la utlización de un modelo
de YOLO en el proyecto Comma3X de la empresa Comma.ai

## Uso de la clase Thneed implementada en Python vs C++

En el proyecto **openpilot**, la clase **Thneed** se utiliza para ejecutar modelos compilados.  
Existen implementaciones tanto en **Python** como en **C++**, y aunque ambas comparten el mismo propósito,  
son **independientes** en su implementación.

### Independencia

Las implementaciones de **Thneed** en **Python** y **C++** son **independientes**.  
Aunque ambas tienen el mismo propósito (ejecutar modelos de aprendizaje automático),  
están diseñadas para **diferentes entornos y casos de uso**:

- **C++**:  
  - La implementación en **C++** está optimizada para el rendimiento en **dispositivos embebidos**, utilizando **OpenCL** para el procesamiento paralelo.  
  - Es probable que ofrezca un **rendimiento superior** en términos de **velocidad de ejecución** y **eficiencia** en el uso de recursos en dispositivos embebidos.  

- **Python**:  
  - Aunque la implementación en **Python** también utiliza **OpenCL**, puede no estar tan **optimizada** como la implementación en **C++** para dispositivos embebidos.  
  - **Python**, siendo un **lenguaje de alto nivel**, puede introducir cierta **sobrecarga** en comparación con **C++**, lo que puede afectar el **rendimiento** en tareas **intensivas en recursos**.  


### Uso en **ThneedModel**
La clase **ThneedModel** en **C++**, utilizada dentro del código [**modeld.py**](https://github.com/covenant-org/openpilot/blob/release3/selfdrive/modeld/modeld.py), que ejecuta el modelo original de Comma, "supercombo", emplea la implementación de **Thneed en C++** para la ejecución de modelos.
No existe una **dependencia directa** entre **ThneedModel** y la implementación de **Thneed en Python**.
