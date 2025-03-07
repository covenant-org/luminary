# YOLO en Comma3X

Página para alojar la documentación e investación de la utlización de un modelo
de YOLO en el proyecto Comma3X de la empresa Comma.ai

# Reporte de Rendimiento del Modelo de Tinygrad en la Comma

## Introducción
Este reporte analiza el rendimiento de dos enfoques distintos para la ejecución de modelos de YOLO en la plataforma Comma. Se compararon:
1. **Compilación JIT en Tinygrad**: Se utilizó el repositorio de Tinygrad con la herramienta de compilación Just-In-Time (JIT) para optimizar la ejecución del modelo en tiempo real.
2. **Compilación a Thneed**: Se empleó el repositorio de OpenPilot con un proceso de compilación adaptado a la Comma, transformando el modelo en el formato Thneed para mejorar su eficiencia.

## Compilación JIT en Tinygrad
La compilación Just-In-Time (JIT) permite optimizar la ejecución del modelo en tiempo real, aplicando optimizaciones específicas según el contexto de uso. El codigo de ejemplo de su uso puede verse en el archivo [`yolov8_onnx_jit.py`](https://github.com/covenant-org/tinygrad/blob/master/examples/yolov8_onnx_jit.py#L275).

### Funcionamiento en Tinygrad
- **Captura de operaciones**: Tinygrad usa TinyJit para almacenar operaciones en **jit_cache** en lugar de ejecutarlas inmediatamente.
- **Optimización**: Se aplican técnicas como fusión de operaciones, eliminación de redundancias y planificación de memoria.
- **Compilación de kernels**: Se generan kernels optimizados para la GPU utilizando compiladores especializados (por ejemplo, NVCC para CUDA).
- **Ejecución**: Los kernels se ejecutan en la GPU, asegurando un alto rendimiento.
- **Reutilización**: Se almacenan resultados previos en caché para evitar cálculos innecesarios.

## Compilación Thneed en OpenPilot
### Introducción
El script [`compile2_nuclea.py`](https://github.com/covenant-org/openpilot/blob/30fe7be623366d5f12dd8b4f98f44cbaead074a9/tinygrad_repo/openpilot/compile2_nuclea.py) permite la conversión de modelos ONNX al formato Thneed, optimizando su ejecución en la plataforma Comma.

### Proceso de Compilación
1. **Carga del Modelo**:
   - Se obtiene el modelo ONNX desde una URL o un archivo local.
2. **Generación del Plan de Ejecución (Schedule)**:
   - Se ejecuta el modelo con una imagen de entrada.
   - Se extrae un plan de ejecución optimizado, eliminando operaciones innecesarias.
3. **Transformación a Formato Thneed**:
   - Se convierte el plan de ejecución en un formato compatible con Thneed.
   - Se guarda el modelo compilado en un archivo.
4. **Pruebas y Validación**:
   - Se compara el modelo Thneed con el modelo ONNX para garantizar la consistencia de los resultados.

### Funciones Clave
- `get_schedule`: Obtiene el plan de ejecución del modelo.
- `schedule_to_thneed`: Transforma el plan en formato Thneed.
- `thneed_test_onnx`: Valida la consistencia entre ONNX y Thneed.

## Resultados de Rendimiento
Se evaluaron ambos enfoques utilizando modelos de YOLO en formato ONNX con tres tamaños diferentes: mediano, pequeño y nano. Los tiempos de ejecución obtenidos fueron los siguientes:

|Tamaño del Modelo| JIT en Tinygrad| Compilación Thneed|
|-----------------|----------------|-------------------|
| Medium          | 914 ms         | 2.1 s             |
| Small           | 822 ms         | 951 ms            |
| Nano            | 308 ms         | 355 ms            |

### Análisis de Rendimiento
- La ejecución con **JIT en Tinygrad** fue en promedio un **13% más rápida** que la compilación con **Thneed**, sobre todo en modelos pequeños que no tienen mucho que optimizar.
- En general, la ejecución con JIT en Tinygrad fue en promedio más rápida que la compilación con Thneed, aprovechando mejor la GPU en cargas de trabajo más grandes como puede notarse con el modelo Medium.

## Conclusión
Los resultados muestran que ambos enfoques son viables para la ejecución de modelos en la Comma, con tiempos de respuesta eficientes en los tres tamaños de YOLO probados. Sin embargo, la compilación JIT en Tinygrad aprovechó mejor la GPU, obteniendo un rendimiento significativamente superior en modelos más grandes en comparación con Thneed.

Esto sugiere que, en aplicaciones donde la latencia es crítica, Tinygrad con JIT puede ser una opción más adecuada.


