"""
Árbol Binario de Búsqueda (ABB) simple, sin balanceo.

Características:
- Inserción: O(h)
- Búsqueda: O(h)
- Recorridos (inorden, preorden, postorden): O(n)
- Conteo de nodos: O(n)

Donde h es la altura; en el peor caso (árbol desbalanceado) h ≈ n.
"""

from __future__ import annotations
from typing import Generator, Optional

from ClaseNodo import ClaseNodo


class ArbolBinario:
    """Implementación de un Árbol Binario de Búsqueda (ABB).

    Invariante:
        Para cualquier nodo:
        todos los valores del subárbol izquierdo < nodo.valor < subárbol derecho.
    """

    def __init__(self) -> None:
        """Crea un árbol vacío."""
        self.raiz: Optional[ClaseNodo] = None

    # -------------------- Inserción --------------------
    def insertar(self, valor: int) -> None:
        """Inserta un valor en el árbol."""
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
        """Verifica si un valor existe en el árbol."""
        nodo = self.raiz
        while nodo:
            if valor == nodo.valor:
                return True
            nodo = nodo.izquierdo if valor < nodo.valor else nodo.derecho
        return False

    # -------------------- Conteo --------------------
    def contar_nodos(self) -> int:
        """Cuenta la cantidad de nodos en el árbol."""
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
        """Verifica si el árbol está vacío."""
        return self.raiz is None

    def altura(self) -> int:
        """Calcula la altura del árbol."""
        def _h(n: Optional[ClaseNodo]) -> int:
            if n is None:
                return -1
            return 1 + max(_h(n.izquierdo), _h(n.derecho))

        return _h(self.raiz)

    def minimo(self) -> Optional[int]:
        """Obtiene el valor mínimo almacenado en el árbol."""
        n = self.raiz
        if n is None:
            return None
        while n.izquierdo:
            n = n.izquierdo
        return n.valor

    def maximo(self) -> Optional[int]:
        """Obtiene el valor máximo almacenado en el árbol."""
        n = self.raiz
        if n is None:
            return None
        while n.derecho:
            n = n.derecho
        return n.valor

    # -------------------- Recorridos --------------------
    def inorden(self) -> Generator[int, None, None]:
        """Genera los valores del árbol en recorrido inorden (ascendente)."""
        def _in(n: Optional[ClaseNodo]):
            if n:
                yield from _in(n.izquierdo)
                yield n.valor
                yield from _in(n.derecho)

        yield from _in(self.raiz)

    def preorden(self) -> Generator[int, None, None]:
        """Genera los valores del árbol en recorrido preorden."""
        def _pre(n: Optional[ClaseNodo]):
            if n:
                yield n.valor
                yield from _pre(n.izquierdo)
                yield from _pre(n.derecho)

        yield from _pre(self.raiz)

    def postorden(self) -> Generator[int, None, None]:
        """Genera los valores del árbol en recorrido postorden."""
        def _post(n: Optional[ClaseNodo]):
            if n:
                yield from _post(n.izquierdo)
                yield from _post(n.derecho)
                yield n.valor

        yield from _post(self.raiz)

    # -------------------- Aliases para compatibilidad --------------------
    def contarNodos(self) -> int:  # noqa: N802
        """Alias de `contar_nodos()` (compatibilidad con código existente)."""
        return self.contar_nodos()

    def isVacio(self) -> bool:  # noqa: N802
        """Alias de `is_vacio()` (compatibilidad con código existente)."""
        return self.is_vacio()


if __name__ == "__main__":
    arbol1 = ArbolBinario()
    for v in (100, 90, 120, 70, 75, 130, 200):
        arbol1.insertar(v)

    print("¿El árbol está vacío?:", arbol1.is_vacio())
    print("Cantidad de nodos:", arbol1.contar_nodos())
    print("Altura del árbol:", arbol1.altura())
    print("Valor mínimo:", arbol1.minimo())
    print("Valor máximo:", arbol1.maximo())
    print("Recorrido inorden (ascendente):", list(arbol1.inorden()))
    print("Recorrido preorden:", list(arbol1.preorden()))
    print("Recorrido postorden:", list(arbol1.postorden()))
    print("Buscar 75:", arbol1.buscar(75))
    print("Buscar 500:", arbol1.buscar(500))
