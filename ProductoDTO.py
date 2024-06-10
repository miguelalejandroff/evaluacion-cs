from dataclasses import dataclass

@dataclass
class ProductoDTO:
    id: int = None
    nombre: str = None
    descripcion: str = None
    precio: float = None
    cantidad: int = None
    categoria: str = None
