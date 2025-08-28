class Nodo:
    """
    Clase que representa un nodo de un árbol binario.

    Atributos:
        valor (int): valor almacenado en el nodo.
        hijo_izquierdo (Nodo | None): referencia al hijo izquierdo.
        hijo_derecho (Nodo | None): referencia al hijo derecho.
    """

    def __init__(self, valor: int) -> None:
        """Inicializa un nodo con un valor y sin hijos."""
        self.valor: int = valor
        self.hijo_izquierdo: Nodo | None = None
        self.hijo_derecho: Nodo | None = None

    def __repr__(self) -> str:
        """Devuelve una representación en cadena del nodo."""
        return f"Nodo({self.valor})"


class ArbolBinario:
    """
    Implementación de un Árbol Binario de Búsqueda (ABB) sin balanceo.

    Métodos implementados en forma recursiva e iterativa:
    - InsertarNodo(x)
    - EsVacio()
    - EsHoja()
    - BuscarX()
    - InOrden()
    - PostOrden()
    - PreOrden()
    """

    def __init__(self) -> None:
        """Crea un árbol vacío."""
        self.raiz: Nodo | None = None

    # -------------------- Insertar --------------------
    def insertar_nodo_recursivo(self, valor: int) -> None:
        """Inserta un valor en el árbol de forma recursiva."""

        def _insertar(raiz: Nodo | None, valor: int) -> Nodo:
            if raiz is None:
                return Nodo(valor)
            if valor < raiz.valor:
                raiz.hijo_izquierdo = _insertar(raiz.hijo_izquierdo, valor)
            else:
                raiz.hijo_derecho = _insertar(raiz.hijo_derecho, valor)
            return raiz

        self.raiz = _insertar(self.raiz, valor)

    def insertar_nodo_iterativo(self, valor: int) -> None:
        """Inserta un valor en el árbol de forma iterativa."""
        nuevo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if valor < actual.valor:
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
    def es_vacio(self) -> bool:
        """Verifica si el árbol está vacío."""
        return self.raiz is None

    def es_hoja(self, nodo: Nodo) -> bool:
        """Verifica si un nodo es hoja."""
        return nodo.hijo_izquierdo is None and nodo.hijo_derecho is None

    # -------------------- Buscar --------------------
    def buscar_recursivo(self, valor: int) -> bool:
        """Busca un valor en el árbol de forma recursiva."""

        def _buscar(nodo: Nodo | None, valor: int) -> bool:
            if nodo is None:
                return False
            if valor == nodo.valor:
                return True
            if valor < nodo.valor:
                return _buscar(nodo.hijo_izquierdo, valor)
            return _buscar(nodo.hijo_derecho, valor)

        return _buscar(self.raiz, valor)

    def buscar_iterativo(self, valor: int) -> bool:
        """Busca un valor en el árbol de forma iterativa."""
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            if valor < actual.valor:
                actual = actual.hijo_izquierdo
            else:
                actual = actual.hijo_derecho
        return False

    # -------------------- Recorridos --------------------
    def inorden_recursivo(self) -> list[int]:
        """Devuelve los valores en recorrido inorden de forma recursiva."""
        def _in(nodo: Nodo | None, res: list[int]) -> None:
            if nodo:
                _in(nodo.hijo_izquierdo, res)
                res.append(nodo.valor)
                _in(nodo.hijo_derecho, res)
        resultado: list[int] = []
        _in(self.raiz, resultado)
        return resultado

    def inorden_iterativo(self) -> list[int]:
        """Devuelve los valores en recorrido inorden de forma iterativa."""
        resultado: list[int] = []
        pila: list[Nodo] = []
        actual = self.raiz
        while pila or actual:
            while actual:
                pila.append(actual)
                actual = actual.hijo_izquierdo
            actual = pila.pop()
            resultado.append(actual.valor)
            actual = actual.hijo_derecho
        return resultado

    def preorden_recursivo(self) -> list[int]:
        """Devuelve los valores en recorrido preorden de forma recursiva."""
        def _pre(nodo: Nodo | None, res: list[int]) -> None:
            if nodo:
                res.append(nodo.valor)
                _pre(nodo.hijo_izquierdo, res)
                _pre(nodo.hijo_derecho, res)
        resultado: list[int] = []
        _pre(self.raiz, resultado)
        return resultado

    def preorden_iterativo(self) -> list[int]:
        """Devuelve los valores en recorrido preorden de forma iterativa."""
        if not self.raiz:
            return []
        resultado: list[int] = []
        pila: list[Nodo] = [self.raiz]
        while pila:
            nodo = pila.pop()
            resultado.append(nodo.valor)
            if nodo.hijo_derecho:
                pila.append(nodo.hijo_derecho)
            if nodo.hijo_izquierdo:
                pila.append(nodo.hijo_izquierdo)
        return resultado

    def postorden_recursivo(self) -> list[int]:
        """Devuelve los valores en recorrido postorden de forma recursiva."""
        def _post(nodo: Nodo | None, res: list[int]) -> None:
            if nodo:
                _post(nodo.hijo_izquierdo, res)
                _post(nodo.hijo_derecho, res)
                res.append(nodo.valor)
        resultado: list[int] = []
        _post(self.raiz, resultado)
        return resultado

    def postorden_iterativo(self) -> list[int]:
        """Devuelve los valores en recorrido postorden de forma iterativa."""
        if not self.raiz:
            return []
        resultado: list[int] = []
        pila1: list[Nodo] = [self.raiz]
        pila2: list[Nodo] = []
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


if __name__ == "__main__":
    arbol = ArbolBinario()
    for v in (100, 90, 120, 70, 75, 130, 200):
        arbol.insertar_nodo_recursivo(v)

    print("¿Árbol vacío?:", arbol.es_vacio())
    print("Buscar recursivo 75:", arbol.buscar_recursivo(75))
    print("Buscar iterativo 500:", arbol.buscar_iterativo(500))
    print("InOrden recursivo:", arbol.inorden_recursivo())
    print("InOrden iterativo:", arbol.inorden_iterativo())
    print("PreOrden recursivo:", arbol.preorden_recursivo())
    print("PreOrden iterativo:", arbol.preorden_iterativo())
    print("PostOrden recursivo:", arbol.postorden_recursivo())
    print("PostOrden iterativo:", arbol.postorden_iterativo())
