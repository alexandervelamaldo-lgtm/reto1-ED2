"""
Módulo ClaseNodo
================

Define la clase `ClaseNodo`, utilizada para representar los nodos
de un Árbol Binario de Búsqueda (ABB).

Características:
- Compatible con PEP 8 (estilo) y PEP 257 (docstrings).
- Incluye alias (`izquierdo`, `derecho`) para mantener compatibilidad
  con implementaciones previas del árbol.
"""


class ClaseNodo:
    """Nodo de un Árbol Binario.

    Atributos:
        valor (int): valor almacenado en el nodo.
        hijo_izquierdo (ClaseNodo | None): referencia al hijo izquierdo.
        hijo_derecho (ClaseNodo | None): referencia al hijo derecho.
    """

    def __init__(self, valor: int) -> None:
        """Inicializa un nodo con un valor y sin hijos."""
        self.valor: int = valor
        self.hijo_izquierdo: "ClaseNodo | None" = None
        self.hijo_derecho: "ClaseNodo | None" = None

    # ---------------- Compatibilidad con ArbolBinario ----------------
    @property
    def izquierdo(self) -> "ClaseNodo | None":
        """Alias: retorna el hijo izquierdo."""
        return self.hijo_izquierdo

    @izquierdo.setter
    def izquierdo(self, nodo: "ClaseNodo | None") -> None:
        """Alias: asigna el hijo izquierdo."""
        self.hijo_izquierdo = nodo

    @property
    def derecho(self) -> "ClaseNodo | None":
        """Alias: retorna el hijo derecho."""
        return self.hijo_derecho

    @derecho.setter
    def derecho(self, nodo: "ClaseNodo | None") -> None:
        """Alias: asigna el hijo derecho."""
        self.hijo_derecho = nodo

    # ---------------- Métodos útiles ----------------
    def es_hoja(self) -> bool:
        """Indica si el nodo es una hoja (no tiene hijos)."""
        return self.hijo_izquierdo is None and self.hijo_derecho is None

    def __repr__(self) -> str:
        """Representación en cadena del nodo, útil para depuración."""
        return f"ClaseNodo(valor={self.valor})"

