from __future__ import annotations
from typing import Optional, Generator, List


class NodoAVL:
    """
    Nodo de un Árbol AVL.

    Atributos:
        valor (int): valor almacenado.
        izquierdo (NodoAVL | None): hijo izquierdo.
        derecho (NodoAVL | None): hijo derecho.
        altura (int): altura del nodo (hoja = 1).
    """

    def __init__(self, valor: int) -> None:
        self.valor: int = valor
        self.izquierdo: Optional[NodoAVL] = None
        self.derecho: Optional[NodoAVL] = None
        self.altura: int = 1  # nodo nuevo se considera hoja

    def factor_equilibrio(self) -> int:
        """Retorna FE = altura(izq) - altura(der)."""
        alt_izq = self.izquierdo.altura if self.izquierdo else 0
        alt_der = self.derecho.altura if self.derecho else 0
        return alt_izq - alt_der

    def __repr__(self) -> str:
        return f"NodoAVL(valor={self.valor}, altura={self.altura})"


class ArbolAVL:
    """
    Árbol AVL (Árbol Binario de Búsqueda auto-balanceado).

    Operaciones principales:
        - insertar(valor): O(log n) amortizado
        - buscar(valor):   O(log n)
        - recorridos:      O(n)

    Definiciones:
        - Altura de hoja = 1
        - Factor de equilibrio (FE) en {-1, 0, 1}
    """

    def __init__(self) -> None:
        self.raiz: Optional[NodoAVL] = None

    # ----------------- Utilidades internas -----------------
    def _altura(self, nodo: Optional[NodoAVL]) -> int:
        """Altura segura (0 si nodo es None)."""
        return nodo.altura if nodo else 0

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        """Actualiza la altura de un nodo a partir de sus hijos."""
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    # Rotación simple a la derecha (caso LL)
    def _rotar_derecha(self, y: NodoAVL) -> NodoAVL:
        """
        Rotación a la derecha:

              y                      x
             / \                    / \
            x   T3   ->            T1  y
           / \                        / \
          T1  T2                     T2  T3
        """
        x = y.izquierdo
        assert x is not None  # por tipo
        T2 = x.derecho

        # rotar
        x.derecho = y
        y.izquierdo = T2

        # actualizar alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    # Rotación simple a la izquierda (caso RR)
    def _rotar_izquierda(self, x: NodoAVL) -> NodoAVL:
        """
        Rotación a la izquierda:

            x                         y
           / \                       / \
          T1  y        ->           x  T3
             / \                   / \
            T2 T3                 T1 T2
        """
        y = x.derecho
        assert y is not None
        T2 = y.izquierdo

        # rotar
        y.izquierdo = x
        x.derecho = T2

        # actualizar alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    def _balancear(self, nodo: NodoAVL) -> NodoAVL:
        """
        Restaura el balance del nodo si su FE está fuera de {-1, 0, 1}.
        Casos:
            LL: FE(nodo) > 1 y FE(izq) >= 0   -> rotar_derecha(nodo)
            LR: FE(nodo) > 1 y FE(izq) <  0   -> rotar_izquierda(izq) y luego rotar_derecha(nodo)
            RR: FE(nodo) < -1 y FE(der) <= 0  -> rotar_izquierda(nodo)
            RL: FE(nodo) < -1 y FE(der) >  0  -> rotar_derecha(der) y luego rotar_izquierda(nodo)
        """
        fe = nodo.factor_equilibrio()

        # Caso LL
        if fe > 1 and nodo.izquierdo and nodo.izquierdo.factor_equilibrio() >= 0:
            return self._rotar_derecha(nodo)

        # Caso LR
        if fe > 1 and nodo.izquierdo and nodo.izquierdo.factor_equilibrio() < 0:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        # Caso RR
        if fe < -1 and nodo.derecho and nodo.derecho.factor_equilibrio() <= 0:
            return self._rotar_izquierda(nodo)

        # Caso RL
        if fe < -1 and nodo.derecho and nodo.derecho.factor_equilibrio() > 0:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        # Ya balanceado
        return nodo

    # ----------------- Insertar (público y auxiliar) -----------------
    def insertar(self, valor: int) -> None:
        """Inserta un valor y re-balancea el camino hasta la raíz."""
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo: Optional[NodoAVL], valor: int) -> NodoAVL:
        """Inserción BST y rebalanceo AVL."""
        if nodo is None:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        else:
            nodo.derecho = self._insertar(nodo.derecho, valor)

        # Actualizar altura y balancear
        self._actualizar_altura(nodo)
        return self._balancear(nodo)

    # ----------------- Buscar -----------------
    def buscar(self, valor: int) -> bool:
        """Retorna True si el valor está en el árbol; False si no."""
        n = self.raiz
        while n:
            if valor == n.valor:
                return True
            n = n.izquierdo if valor < n.valor else n.derecho
        return False

    # ----------------- Altura del árbol -----------------
    def altura(self) -> int:
        """Altura de la raíz (hoja = 1; árbol vacío = 0)."""
        return self.raiz.altura if self.raiz else 0

    # ----------------- Recorridos -----------------
    def inorden(self) -> List[int]:
        """Retorna los valores en recorrido inorden."""
        res: List[int] = []

        def _in(n: Optional[NodoAVL]) -> None:
            if n:
                _in(n.izquierdo)
                res.append(n.valor)
                _in(n.derecho)

        _in(self.raiz)
        return res

    def preorden(self) -> List[int]:
        """Retorna los valores en recorrido preorden."""
        res: List[int] = []

        def _pre(n: Optional[NodoAVL]) -> None:
            if n:
                res.append(n.valor)
                _pre(n.izquierdo)
                _pre(n.derecho)

        _pre(self.raiz)
        return res

    def postorden(self) -> List[int]:
        """Retorna los valores en recorrido postorden."""
        res: List[int] = []

        def _post(n: Optional[NodoAVL]) -> None:
            if n:
                _post(n.izquierdo)
                _post(n.derecho)
                res.append(n.valor)

        _post(self.raiz)
        return res


if __name__ == "__main__":
    avl = ArbolAVL()
    # Secuencia que provoca varios rebalanceos
    for v in (30, 20, 40, 10, 25, 22, 50, 5, 35, 45, 42):
        avl.insertar(v)

    print("Altura:", avl.altura())                 # e.g., 4 o similar según inserciones
    print("Inorden (asc):", avl.inorden())         # ordenada
    print("Preorden:", avl.preorden())
    print("Postorden:", avl.postorden())
    print("Buscar 22:", avl.buscar(22))
    print("Buscar 99:", avl.buscar(99))
