"""
Módulo ClaseNodo
================

Define la clase `ClaseNodo`, utilizada para representar los nodos
de un Árbol Binario de Búsqueda (ABB).

Características:
- Compatible con PEP 8 (estilo) y PEP 257 (docstrings).
- Usa atributos directos: hijo_izquierdo, hijo_derecho.
"""

from typing import Optional


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
        self.hijo_izquierdo: Optional["ClaseNodo"] = None
        self.hijo_derecho: Optional["ClaseNodo"] = None

    # ---------------- Métodos útiles ----------------
    def es_hoja(self) -> bool:
        """Indica si el nodo es una hoja (no tiene hijos)."""
        return self.hijo_izquierdo is None and self.hijo_derecho is None

    def tiene_un_hijo(self) -> bool:
        """Indica si el nodo tiene exactamente un hijo."""
        return (self.hijo_izquierdo is None) ^ (self.hijo_derecho is None)

    def __repr__(self) -> str:
        """Representación en cadena del nodo, útil para depuración."""
        return f"ClaseNodo(valor={self.valor})"
