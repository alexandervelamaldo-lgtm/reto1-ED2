from __future__ import annotations
from typing import Optional, List


class NodoAVL:
    """Nodo de un Árbol AVL."""
    def __init__(self, valor: int) -> None:
        self.valor: int = valor
        self.izquierdo: Optional[NodoAVL] = None
        self.derecho: Optional[NodoAVL] = None
        self.altura: int = 1  # hoja = 1

    def factor_equilibrio(self) -> int:
        """FE = altura(izq) - altura(der)."""
        alt_izq = self.izquierdo.altura if self.izquierdo else 0
        alt_der = self.derecho.altura if self.derecho else 0
        return alt_izq - alt_der

    def __repr__(self) -> str:
        return f"NodoAVL(valor={self.valor}, altura={self.altura})"


class ArbolAVL:
    """Árbol AVL (ABB auto-balanceado) con insertar y eliminar balanceados."""
    def __init__(self) -> None:
        self.raiz: Optional[NodoAVL] = None

    # ---------- utilidades ----------
    def _altura(self, nodo: Optional[NodoAVL]) -> int:
        return nodo.altura if nodo else 0

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    def _rotar_derecha(self, y: NodoAVL) -> NodoAVL:
        x = y.izquierdo
        assert x is not None
        T2 = x.derecho
        x.derecho = y
        y.izquierdo = T2
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    def _rotar_izquierda(self, x: NodoAVL) -> NodoAVL:
        y = x.derecho
        assert y is not None
        T2 = y.izquierdo
        y.izquierdo = x
        x.derecho = T2
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    def _balancear(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica la rotación necesaria según el FE del nodo."""
        fe = nodo.factor_equilibrio()

        # LL
        if fe > 1 and nodo.izquierdo and nodo.izquierdo.factor_equilibrio() >= 0:
            return self._rotar_derecha(nodo)
        # LR
        if fe > 1 and nodo.izquierdo and nodo.izquierdo.factor_equilibrio() < 0:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)
        # RR
        if fe < -1 and nodo.derecho and nodo.derecho.factor_equilibrio() <= 0:
            return self._rotar_izquierda(nodo)
        # RL
        if fe < -1 and nodo.derecho and nodo.derecho.factor_equilibrio() > 0:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo  # ya balanceado

    # ---------- insertar ----------
    def insertar(self, valor: int) -> None:
        """Inserta un valor y rebalancea el camino a la raíz."""
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo: Optional[NodoAVL], valor: int) -> NodoAVL:
        if nodo is None:
            return NodoAVL(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        else:
            # Nota: los duplicados se envían a la derecha.
            nodo.derecho = self._insertar(nodo.derecho, valor)

        self._actualizar_altura(nodo)
        return self._balancear(nodo)

    # ---------- eliminar ----------
    def eliminar(self, valor: int) -> None:
        """Elimina un valor (si existe) y mantiene el balance AVL."""
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo: Optional[NodoAVL], valor: int) -> Optional[NodoAVL]:
        if nodo is None:
            return None

        # 1) Búsqueda BST estándar
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar(nodo.derecho, valor)
        else:
            # 2) Encontrado: aplicar casos
            # Caso A: 0 hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            # Caso B: 1 hijo (izquierdo o derecho)
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            # Caso C: 2 hijos -> reemplazar por sucesor (mínimo en subárbol derecho)
            sucesor = self._min_nodo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.valor)

        # 3) Actualizar altura y re-balancear al volver de la recursión
        self._actualizar_altura(nodo)
        return self._balancear(nodo)

    def _min_nodo(self, nodo: NodoAVL) -> NodoAVL:
        """Retorna el nodo con el valor mínimo del subárbol dado."""
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    # ---------- otras operaciones ----------
    def buscar(self, valor: int) -> bool:
        n = self.raiz
        while n:
            if valor == n.valor:
                return True
            n = n.izquierdo if valor < n.valor else n.derecho
        return False

    def altura(self) -> int:
        return self.raiz.altura if self.raiz else 0

    def inorden(self) -> List[int]:
        res: List[int] = []
        def _in(n: Optional[NodoAVL]) -> None:
            if n:
                _in(n.izquierdo)
                res.append(n.valor)
                _in(n.derecho)
        _in(self.raiz)
        return res

    def preorden(self) -> List[int]:
        res: List[int] = []
        def _pre(n: Optional[NodoAVL]) -> None:
            if n:
                res.append(n.valor)
                _pre(n.izquierdo)
                _pre(n.derecho)
        _pre(self.raiz)
        return res

    def postorden(self) -> List[int]:
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

    # Construcción
    for v in (30, 20, 40, 10, 25, 22, 50, 5, 35, 45, 42):
        avl.insertar(v)

    print("Inorden (antes):", avl.inorden())
    print("Altura (antes):", avl.altura())

    # Eliminaciones que fuerzan diferentes rebalanceos
    for eliminar in (10, 40, 30):  # 10(hoja), 40(1 hijo), 30(2 hijos)
        print(f"\nEliminar {eliminar}:")
        avl.eliminar(eliminar)
        print("Inorden:", avl.inorden())
        print("Preorden:", avl.preorden())
        print("Altura:", avl.altura())
        # Comprobación de búsqueda
        print(f"Buscar {eliminar}:", avl.buscar(eliminar))
