from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

# ======================================================
# 1. DEFINICIÓN DE COMPONENTES (Entidades)
# ======================================================
@dataclass
class ComponenteCabeza:
    descripcion: str
    material: str

@dataclass
class ComponenteVestimenta:
    tipo: str
    nivel_proteccion: int

@dataclass
class ComponenteHerramienta:
    nombre: str
    funcionalidad: str

# ======================================================
# 2. INVENTARIO DE PIEZAS (Componentes definidos)
# ======================================================
class InventarioComponentes:
    # Opciones de Cabeza
    CABEZA_BOMBERO = ComponenteCabeza("Casco de seguridad", "Polímero reforzado")
    CABEZA_PROFESOR = ComponenteCabeza("Lentes y sensores ópticos", "Vidrio/Metal")
    CABEZA_AVIADOR = ComponenteCabeza("Casco de vuelo", "Cuero sintético")
    
    # Opciones de Vestimenta
    VESTIMENTA_BOMBERO = ComponenteVestimenta("Traje térmico", 100)
    VESTIMENTA_PROFESOR = ComponenteVestimenta("Indumentaria formal", 10)
    VESTIMENTA_AVIADOR = ComponenteVestimenta("Chaqueta de aviación", 50)

    # Opciones de Herramientas
    HERRAMIENTA_BOMBERO = ComponenteHerramienta("Dispensador de agua", "Extinción")
    HERRAMIENTA_PROFESOR = ComponenteHerramienta("Puntero láser", "Señalización")
    HERRAMIENTA_AVIADOR = ComponenteHerramienta("Módulo GPS", "Navegación")

# ======================================================
# 3. PRODUCTO FINAL
# ======================================================
class RobotEducativo:
    def __init__(self) -> None:
        self.nombre: Optional[str] = None
        self.tipo: Optional[str] = None
        self.cabeza: Optional[ComponenteCabeza] = None
        self.vestimenta: Optional[ComponenteVestimenta] = None
        self.herramienta: Optional[ComponenteHerramienta] = None

    def __str__(self) -> str:
        # Representación técnica del estado del objeto
        return (f" Robot: {self.nombre} (Tipo: {self.tipo})\n"
                f"Especificaciones del Robot:\n"
                f" - Módulo Cabeza: {self.cabeza.descripcion}\n"
                f" - Vestimenta:    {self.vestimenta.tipo}\n"
                f" - Herramienta:   {self.herramienta.nombre}")

# ======================================================
# 4. INTERFAZ BUILDER (Abstracción del ensamblador)
# ======================================================
class BuilderRobot(ABC):
    @abstractmethod
    def reiniciar_proceso(self) -> None: 
        pass

    @abstractmethod
    def asignar_identidad(self, nombre: str, tipo: str) -> None:
        """Asigna nombre y tipo al robot"""
        pass

    @abstractmethod
    def ensamblar_cabeza(self, componente: ComponenteCabeza) -> None: 
        pass

    @abstractmethod
    def ensamblar_vestimenta(self, componente: ComponenteVestimenta) -> None: 
        pass

    @abstractmethod
    def ensamblar_herramienta(self, componente: ComponenteHerramienta) -> None: 
        pass
    
    @abstractmethod
    def obtener_resultado(self) -> RobotEducativo: 
        pass

# ======================================================
# 5. BUILDER CONCRETO (Implementación del mecanismo)
# ======================================================
class ConfiguradorRobot(BuilderRobot):
    def __init__(self) -> None:
        self._robot = RobotEducativo()

    def reiniciar_proceso(self) -> None:
        self._robot = RobotEducativo()

    def asignar_identidad(self, nombre: str, tipo: str) -> None:
        """Asigna nombre y tipo al robot"""
        self._robot.nombre = nombre
        self._robot.tipo = tipo

    def ensamblar_cabeza(self, componente: ComponenteCabeza) -> None:
        self._robot.cabeza = componente

    def ensamblar_vestimenta(self, componente: ComponenteVestimenta) -> None:
        self._robot.vestimenta = componente

    def ensamblar_herramienta(self, componente: ComponenteHerramienta) -> None:
        self._robot.herramienta = componente

    def obtener_resultado(self) -> RobotEducativo:
        producto = self._robot
        self.reiniciar_proceso()
        return producto

# ======================================================
# 6. DIRECTOR (Controlador del proceso estándar)
# ======================================================
class DirectorEnsamblaje:
    """
    Responsable de ejecutar la secuencia lógica de construcción.
    Recibe las especificaciones y delega la construcción al builder.
    """
    def construir_robot_personalizado(self, 
                                      builder: BuilderRobot,
                                      nombre: str,
                                      tipo: str,
                                      comp_cabeza: ComponenteCabeza, 
                                      comp_vestimenta: ComponenteVestimenta, 
                                      comp_herramienta: ComponenteHerramienta) -> None:
        
        # Inicio del procedimiento estandarizado
        builder.reiniciar_proceso()
        
        # Asignación de identidad (nombre y tipo)
        builder.asignar_identidad(nombre, tipo)

        # Secuencia de integración definida por el sistema
        builder.ensamblar_vestimenta(comp_vestimenta)
        builder.ensamblar_cabeza(comp_cabeza)
        builder.ensamblar_herramienta(comp_herramienta)

# ======================================================
# 7. EJECUCIÓN DEL SISTEMA
# ======================================================
if __name__ == "__main__":
    # Instanciación de los módulos principales
    director = DirectorEnsamblaje()
    configurador = ConfiguradorRobot()

    # Selección de componentes (Intercambiabilidad)
    # Ejemplo: Configuración híbrida (Profesor con casco de Bombero)
    seleccion_cabeza = InventarioComponentes.CABEZA_BOMBERO
    seleccion_vestimenta = InventarioComponentes.VESTIMENTA_PROFESOR
    seleccion_herramienta = InventarioComponentes.HERRAMIENTA_PROFESOR

    # Ejecución del proceso de construcción
    director.construir_robot_personalizado(
        configurador,
        nombre="RoboProfe-001",
        tipo="Profesor Híbrido",
        comp_cabeza=seleccion_cabeza,
        comp_vestimenta=seleccion_vestimenta,
        comp_herramienta=seleccion_herramienta
    )

    # Obtención del producto final
    robot_terminado = configurador.obtener_resultado()
    
    # Salida de datos
    print(robot_terminado)