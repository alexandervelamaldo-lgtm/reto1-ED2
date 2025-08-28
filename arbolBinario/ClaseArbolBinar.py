from __future__ import annotations
from typing import Optional, List

from ClaseNodo import ClaseNodo


class ArbolBinario:
    """
    Representa un Árbol Binario de Búsqueda (ABB).

    Permite insertar valores, buscar nodos y recorrer el árbol
    en diferentes órdenes (inorden, preorden, postorden).
    Incluye implementaciones recursivas e iterativas.
    """

    def __init__(self) -> None:
        """Inicializa un árbol vacío."""
        self.raiz: Optional[ClaseNodo] = None

    # -------------------- Insertar --------------------
    def InsertarNodo(self, x: int) -> None:
        """
        Inserta un valor en el árbol de forma recursiva.

        Args:
            x (int): Valor a insertar.
        """
        self.raiz = self._insertar_recursivo(self.raiz, x)

    def _insertar_recursivo(
        self,
        nodo: Optional[ClaseNodo],
        x: int
    ) -> ClaseNodo:
        """
        Inserta un valor en el subárbol recursivamente.

        Args:
            nodo (ClaseNodo | None): Nodo actual.
            x (int): Valor a insertar.

        Returns:
            ClaseNodo: Nodo actualizado.
        """
        if nodo is None:
            return ClaseNodo(x)
        if x < nodo.valor:
            nodo.hijo_izquierdo = self._insertar_recursivo(
                nodo.hijo_izquierdo, x
            )
        else:
            nodo.hijo_derecho = self._insertar_recursivo(
                nodo.hijo_derecho, x
            )
        return nodo

    def InsertarNodoIterativo(self, x: int) -> None:
        """
        Inserta un valor en el árbol de forma iterativa.

        Args:
            x (int): Valor a insertar.
        """
        nuevo = ClaseNodo(x)
        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if x < actual.valor:
                if actual.hijo_izquierdo is None:
                    actual.hijo_izquierdo = nuevo
                    break
                actual = actual.hijo_izquierdo
            else:
                if actual.hijo_derecho is None:
                    actual.hijo_derecho = nuevo
                    break
                actual = actual.hijo_derecho

    # -------------------- Estado --------------------
    def EsVacio(self) -> bool:
        """
        Verifica si el árbol está vacío.

        Returns:
            bool: True si el árbol no tiene nodos.
        """
        return self.raiz is None

    def EsHoja(self, nodo: ClaseNodo) -> bool:
        """
        Verifica si un nodo es hoja.

        Args:
            nodo (ClaseNodo): Nodo a verificar.

        Returns:
            bool: True si el nodo no tiene hijos.
        """
        return nodo.hijo_izquierdo is None and nodo.hijo_derecho is None

    # -------------------- Búsqueda --------------------
    def BuscarX(self, x: int) -> bool:
        """
        Busca un valor en el árbol de forma recursiva.

        Args:
            x (int): Valor a buscar.

        Returns:
            bool: True si el valor está en el árbol.
        """
        return self._buscar_recursivo(self.raiz, x)

    def _buscar_recursivo(
        self,
        nodo: Optional[ClaseNodo],
        x: int
    ) -> bool:
        """
        Busca un valor en un subárbol recursivamente.

        Args:
            nodo (ClaseNodo | None): Nodo actual.
            x (int): Valor a buscar.

        Returns:
            bool: True si el valor está en el subárbol.
        """
        if nodo is None:
            return False
        if nodo.valor == x:
            return True
        if x < nodo.valor:
            return self._buscar_recursivo(nodo.hijo_izquierdo, x)
        return self._buscar_recursivo(nodo.hijo_derecho, x)

    def BuscarXIterativo(self, x: int) -> bool:
        """
        Busca un valor en el árbol de forma iterativa.

        Args:
            x (int): Valor a buscar.

        Returns:
            bool: True si el valor está en el árbol.
        """
        actual = self.raiz
        while actual:
            if actual.valor == x:
                return True
            actual = (
                actual.hijo_izquierdo
                if x < actual.valor
                else actual.hijo_derecho
            )
        return False

    # -------------------- Recorridos --------------------
    def InOrden(self) -> List[int]:
        """
        Recorre el árbol en inorden de forma recursiva.

        Returns:
            List[int]: Valores en orden ascendente.
        """
        resultado: List[int] = []

        def _in(nodo: Optional[ClaseNodo]) -> None:
            if nodo:
                _in(nodo.hijo_izquierdo)
                resultado.append(nodo.valor)
                _in(nodo.hijo_derecho)

        _in(self.raiz)
        return resultado

    def InOrdenIterativo(self) -> List[int]:
        """
        Recorre el árbol en inorden de forma iterativa.

        Returns:
            List[int]: Valores en orden ascendente.
        """
        resultado: List[int] = []
        pila: List[ClaseNodo] = []
        actual = self.raiz

        while pila or actual:
            while actual:
                pila.append(actual)
                actual = actual.hijo_izquierdo
            actual = pila.pop()
            resultado.append(actual.valor)
            actual = actual.hijo_derecho

        return resultado

    def PreOrden(self) -> List[int]:
        """
        Recorre el árbol en preorden de forma recursiva.

        Returns:
            List[int]: Valores visitados en preorden.
        """
        resultado: List[int] = []

        def _pre(nodo: Optional[ClaseNodo]) -> None:
            if nodo:
                resultado.append(nodo.valor)
                _pre(nodo.hijo_izquierdo)
                _pre(nodo.hijo_derecho)

        _pre(self.raiz)
        return resultado

    def PreOrdenIterativo(self) -> List[int]:
        """
        Recorre el árbol en preorden de forma iterativa.

        Returns:
            List[int]: Valores visitados en preorden.
        """
        if self.raiz is None:
            return []

        resultado: List[int] = []
        pila: List[ClaseNodo] = [self.raiz]

        while pila:
            nodo = pila.pop()
            resultado.append(nodo.valor)
            if nodo.hijo_derecho:
                pila.append(nodo.hijo_derecho)
            if nodo.hijo_izquierdo:
                pila.append(nodo.hijo_izquierdo)

        return resultado

    def PostOrden(self) -> List[int]:
        """
        Recorre el árbol en postorden de forma recursiva.

        Returns:
            List[int]: Valores visitados en postorden.
        """
        resultado: List[int] = []

        def _post(nodo: Optional[ClaseNodo]) -> None:
            if nodo:
                _post(nodo.hijo_izquierdo)
                _post(nodo.hijo_derecho)
                resultado.append(nodo.valor)

        _post(self.raiz)
        return resultado

    def PostOrdenIterativo(self) -> List[int]:
        """
        Recorre el árbol en postorden de forma iterativa.

        Returns:
            List[int]: Valores visitados en postorden.
        """
        if self.raiz is None:
            return []

        resultado: List[int] = []
        pila1: List[ClaseNodo] = [self.raiz]
        pila2: List[ClaseNodo] = []

        while pila1:
            nodo = pila1.pop()
            pila2.append(nodo)
            if nodo.hijo_izquierdo:
                pila1.append(nodo.hijo_izquierdo)
            if nodo.hijo_derecho:
                pila1.append(nodo.hijo_derecho)

        while pila2:
            resultado.append(pila2.pop().valor)

        return resultado


# -------------------- Prueba rápida --------------------
if __name__ == "__main__":
    arbol = ArbolBinario()
    for v in (100, 90, 120, 70, 75, 130, 200):
        arbol.InsertarNodo(v)

    print("¿Árbol vacío?:", arbol.EsVacio())
    print("Buscar 75 (rec):", arbol.BuscarX(75))
    print("Buscar 500 (iter):", arbol.BuscarXIterativo(500))
    print("InOrden rec:", arbol.InOrden())
    print("InOrden iter:", arbol.InOrdenIterativo())
    print("PreOrden rec:", arbol.PreOrden())
    print("PreOrden iter:", arbol.PreOrdenIterativo())
    print("PostOrden rec:", arbol.PostOrden())
    print("PostOrden iter:", arbol.PostOrdenIterativo())
