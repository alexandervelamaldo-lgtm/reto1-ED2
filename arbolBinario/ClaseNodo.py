"""
Módulo ClaseNodo: Nodo para Árbol Binario.

Cumple PEP 8 (estilo) y PEP 257 (docstrings) y mantiene compatibilidad
con código que use atributos `izquierdo`/`derecho` y métodos tipo get/set.
"""


class ClaseNodo:
    """Nodo de un Árbol Binario.

    Atributos:
        valor (int): valor almacenado en el nodo.
        hijo_izquierdo (ClaseNodo | None): subárbol izquierdo.
        hijo_derecho (ClaseNodo | None): subárbol derecho.
    """

    def __init__(self, valor: int) -> None:
        """Inicializa un nodo con un valor y sin hijos."""
        self.valor: int = valor
        self.hijo_izquierdo: "ClaseNodo | None" = None
        self.hijo_derecho: "ClaseNodo | None" = None

    # ---------------- Compatibilidad con tu árbol ----------------
    # Alias de atributos: `izquierdo` / `derecho`
    @property
    def izquierdo(self) -> "ClaseNodo | None":
        """Alias de compatibilidad: retorna hijo_izquierdo."""
        return self.hijo_izquierdo

    @izquierdo.setter
    def izquierdo(self, nodo: "ClaseNodo | None") -> None:
        """Alias de compatibilidad: asigna hijo_izquierdo."""
        self.hijo_izquierdo = nodo

    @property
    def derecho(self) -> "ClaseNodo | None":
        """Alias de compatibilidad: retorna hijo_derecho."""
        return self.hijo_derecho

    @derecho.setter
    def derecho(self, nodo: "ClaseNodo | None") -> None:
        """Alias de compatibilidad: asigna hijo_derecho."""
        self.hijo_derecho = nodo

    # Alias de métodos tipo get/set (por si otros archivos los usan)
    def obtener_valor(self) -> int:
        """Alias de compatibilidad: retorna valor."""
        return self.valor

    def get_valor(self) -> int:
        """Retorna el valor del nodo (estilo PEP 8)."""
        return self.valor

    def set_valor(self, valor: int) -> None:
        """Asigna un nuevo valor al nodo (estilo PEP 8)."""
        self.valor = valor

    def get_hijo_izquierdo(self) -> "ClaseNodo | None":
        """Retorna el hijo izquierdo (estilo PEP 8)."""
        return self.hijo_izquierdo

    def get_hijo_derecho(self) -> "ClaseNodo | None":
        """Retorna el hijo derecho (estilo PEP 8)."""
        return self.hijo_derecho

    def set_hijo_izquierdo(self, nodo: "ClaseNodo | None") -> None:
        """Asigna el hijo izquierdo (estilo PEP 8)."""
        self.hijo_izquierdo = nodo

    def set_hijo_derecho(self, nodo: "ClaseNodo | None") -> None:
        """Asigna el hijo derecho (estilo PEP 8)."""
        self.hijo_derecho = nodo

    # ---------------- Utilidad ----------------
    def es_hoja(self) -> bool:
        """Retorna True si el nodo no tiene hijos."""
        return self.hijo_izquierdo is None and self.hijo_derecho is None

    def __repr__(self) -> str:
        """Representación para depuración."""
        return f"ClaseNodo(valor={self.valor})"
