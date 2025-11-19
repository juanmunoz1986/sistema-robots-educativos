# Sistema de Construcción de Robots Educativos

## Descripción General

Este proyecto implementa un **sistema de fábrica de robots educativos** utilizando el patrón de diseño **Builder**. El sistema permite construir robots personalizados combinando diferentes componentes (cabeza, vestimenta y herramientas) de manera flexible y estructurada.

## Arquitectura del Sistema

El código está organizado en 7 secciones principales:

### 1. Componentes (Entidades)
Define las piezas básicas que pueden ensamblarse en un robot:
- **ComponenteCabeza**: Descripción y material del módulo de cabeza
- **ComponenteVestimenta**: Tipo de vestimenta y nivel de protección
- **ComponenteHerramienta**: Nombre y funcionalidad de la herramienta

### 2. Inventario de Componentes
Catálogo predefinido de componentes disponibles para tres tipos de robots:
- **Bombero**: Casco de seguridad, traje térmico, dispensador de agua
- **Profesor**: Lentes y sensores ópticos, indumentaria formal, puntero láser
- **Aviador**: Casco de vuelo, chaqueta de aviación, módulo GPS

### 3. Producto Final
La clase `RobotEducativo` representa el robot completo con:
- Nombre y tipo
- Componentes ensamblados (cabeza, vestimenta, herramienta)
- Método `__str__()` para visualización

### 4. Interfaz Builder
Clase abstracta `BuilderRobot` que define el contrato para construir robots:
- `reiniciar_proceso()`: Inicia un nuevo proceso de construcción
- `asignar_identidad()`: Asigna nombre y tipo al robot
- `ensamblar_cabeza()`: Ensambla el módulo de cabeza
- `ensamblar_vestimenta()`: Ensambla la vestimenta
- `ensamblar_herramienta()`: Ensambla la herramienta
- `obtener_resultado()`: Retorna el robot terminado

### 5. Builder Concreto
`ConfiguradorRobot` implementa la interfaz Builder:
- Mantiene una instancia de `RobotEducativo` durante la construcción
- Implementa todos los métodos abstractos
- Permite obtener el robot final y reiniciar para construir otro

### 6. Director
`DirectorEnsamblaje` orquesta el proceso de construcción:
- Define la secuencia estándar de ensamblaje
- Recibe especificaciones y delega al builder
- Garantiza un proceso consistente

### 7. Ejecución
Ejemplo de uso que demuestra:
- Creación de robots con componentes personalizados
- Combinación híbrida de componentes (ej: Profesor con casco de Bombero)
- Visualización del resultado final

## Patrón de Diseño: Builder

Este código implementa el patrón **Builder**, que permite:
- **Construcción paso a paso**: Los objetos complejos se construyen gradualmente
- **Flexibilidad**: Permite diferentes combinaciones de componentes
- **Reutilización**: El mismo proceso de construcción puede crear diferentes variantes
- **Separación de responsabilidades**: El Director maneja el proceso, el Builder la implementación

## Ejemplo de Uso

```python
# Crear director y configurador
director = DirectorEnsamblaje()
configurador = ConfiguradorRobot()

# Seleccionar componentes
cabeza = InventarioComponentes.CABEZA_BOMBERO
vestimenta = InventarioComponentes.VESTIMENTA_PROFESOR
herramienta = InventarioComponentes.HERRAMIENTA_PROFESOR

# Construir robot
director.construir_robot_personalizado(
    configurador,
    nombre="RoboProfe-001",
    tipo="Profesor Híbrido",
    comp_cabeza=cabeza,
    comp_vestimenta=vestimenta,
    comp_herramienta=herramienta
)

# Obtener resultado
robot = configurador.obtener_resultado()
print(robot)
```

## Características Principales

- ✅ **Modularidad**: Componentes intercambiables
- ✅ **Extensibilidad**: Fácil agregar nuevos componentes o tipos de robots
- ✅ **Flexibilidad**: Permite combinaciones híbridas
- ✅ **Claridad**: Código bien estructurado y documentado
- ✅ **Patrón de diseño**: Implementación correcta del patrón Builder

## Requisitos

- Python 3.7+ (usa `dataclasses` y `typing`)

## Ejecución

```bash
python fabrica.py
```

## Estructura del Proyecto

```
.
├── fabrica.py      # Código principal del sistema
└── README.md       # Este archivo
```

