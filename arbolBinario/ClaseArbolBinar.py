"""
Árbol Binario de Búsqueda (ABB) simple, sin balanceo.

- Inserción: O(h)
- Búsqueda: O(h)
- Recorridos y conteo: O(n)
donde h es la altura; en el peor caso (desbalanceado) h ≈ n.

Este archivo sigue PEP 8 (estilo) y PEP 257 (docstrings).
"""

from __future__ import annotations
from typing import Generator, Optional

from ClaseNodo import ClaseNodo


class ArbolBinario:
    """Implementación de un Árbol Binario de Búsqueda sencillo.

    Invariante:
        Para cualquier nodo:
        todos los valores del subárbol izquierdo < nodo.valor < subárbol derecho.
    """

    def __init__(self) -> None:
        """Crea un árbol vacío."""
        self.raiz: Optional[ClaseNodo] = None

    # -------------------- Inserción --------------------
    def insertar(self, valor: int) -> None:
        """Inserta `valor` preservando el invariante del ABB.

        Si el valor es duplicado, por simplicidad se inserta en el subárbol derecho.
        """
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(
        self, raiz_aux: Optional[ClaseNodo], valor: int
    ) -> ClaseNodo:
        """Función auxiliar recursiva para insertar un valor."""
        if raiz_aux is None:
            return ClaseNodo(valor)

        if valor < raiz_aux.valor:
            raiz_aux.izquierdo = self._insertar_recursivo(raiz_aux.izquierdo, valor)
        else:
            raiz_aux.derecho = self._insertar_recursivo(raiz_aux.derecho, valor)
        return raiz_aux

    # -------------------- Búsqueda --------------------
    def buscar(self, valor: int) -> bool:
        """Retorna True si `valor` existe en el árbol; False en caso contrario."""
        nodo = self.raiz
        while nodo:
            if valor == nodo.valor:
                return True
            nodo = nodo.izquierdo if valor < nodo.valor else nodo.derecho
        return False

    # -------------------- Conteo --------------------
    def contar_nodos(self) -> int:
        """Retorna la cantidad total de nodos del árbol (O(n))."""
        return self._contar_nodos_recursivo(self.raiz)

    def _contar_nodos_recursivo(self, raiz_aux: Optional[ClaseNodo]) -> int:
        """Función auxiliar recursiva para contar nodos."""
        if raiz_aux is None:
            return 0
        return (
            1
            + self._contar_nodos_recursivo(raiz_aux.izquierdo)
            + self._contar_nodos_recursivo(raiz_aux.derecho)
        )

    # -------------------- Estado / Propiedades --------------------
    def is_vacio(self) -> bool:
        """Retorna True si el árbol no contiene nodos."""
        return self.raiz is None

    def altura(self) -> int:
        """Altura del árbol (número de aristas del camino más largo).

        Un árbol vacío tiene altura -1.
        """
        def _h(n: Optional[ClaseNodo]) -> int:
            if n is None:
                return -1
            return 1 + max(_h(n.izquierdo), _h(n.derecho))

        return _h(self.raiz)

    def minimo(self) -> Optional[int]:
        """Retorna el valor mínimo del árbol o None si está vacío."""
        n = self.raiz
        if n is None:
            return None
        while n.izquierdo:
            n = n.izquierdo
        return n.valor

    def maximo(self) -> Optional[int]:
        """Retorna el valor máximo del árbol o None si está vacío."""
        n = self.raiz
        if n is None:
            return None
        while n.derecho:
            n = n.derecho
        return n.valor

    # -------------------- Recorridos --------------------
    def inorden(self) -> Generator[int, None, None]:
        """Genera los valores del árbol en orden ascendente (inorden)."""
        def _in(n: Optional[ClaseNodo]):
            if n:
                yield from _in(n.izquierdo)
                yield n.valor
                yield from _in(n.derecho)

        yield from _in(self.raiz)

    def preorden(self) -> Generator[int, None, None]:
        """Genera los valores del árbol en preorden."""
        def _pre(n: Optional[ClaseNodo]):
            if n:
                yield n.valor
                yield from _pre(n.izquierdo)
                yield from _pre(n.derecho)

        yield from _pre(self.raiz)

    def postorden(self) -> Generator[int, None, None]:
        """Genera los valores del árbol en postorden."""
        def _post(n: Optional[ClaseNodo]):
            if n:
                yield from _post(n.izquierdo)
                yield from _post(n.derecho)
                yield n.valor

        yield from _post(self.raiz)

    # -------------------- Aliases para compatibilidad --------------------
    # Mantienen tu API original con estilo no-PEP8.
    def contarNodos(self) -> int:  # noqa: N802  (nombre heredado)
        """Alias de `contar_nodos()` (compatibilidad con código existente)."""
        return self.contar_nodos()

    def isVacio(self) -> bool:  # noqa: N802
        """Alias de `is_vacio()` (compatibilidad con código existente)."""
        return self.is_vacio()


if __name__ == "__main__":
    arbol1 = ArbolBinario()
    for v in (100, 90, 120, 70, 75, 130, 200):
        arbol1.insertar(v)

    print("Cantidad de nodos:", arbol1.contar_nodos())
    print("Árbol vacío?:", arbol1.is_vacio())
    print("Buscar 75:", arbol1.buscar(75))
    print("Altura:", arbol1.altura())
    print("Mínimo:", arbol1.minimo())
    print("Máximo:", arbol1.maximo())
    print("Inorden:", list(arbol1.inorden()))
