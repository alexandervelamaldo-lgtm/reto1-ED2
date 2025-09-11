class Nodo:
    """
    Clase que representa un nodo de un árbol binario.

    Atributos:
        valor (int): valor almacenado en el nodo.
        hijo_izquierdo (Nodo | None): referencia al hijo izquierdo.
        hijo_derecho (Nodo | None): referencia al hijo derecho.
    """

    def __init__(self, valor: int) -> None:
        """
        Inicializa un nodo con un valor y sin hijos.
        
        Args:
            valor (int): Valor a almacenar en el nodo.
        """
        self.valor: int = valor
        self.hijo_izquierdo: Nodo | None = None
        self.hijo_derecho: Nodo | None = None

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del nodo.
        
        Returns:
            str: Representación del nodo.
        """
        return f"Nodo({self.valor})"


class ArbolBinario:
    """
    Implementación de un Árbol Binario de Búsqueda (ABB) sin balanceo.

    Métodos implementados en forma recursiva e iterativa:
    - Insertar / insertar_nodo_recursivo / insertar_nodo_iterativo
    - Buscar / buscar_recursivo / buscar_iterativo
    - EsHoja / es_hoja
    - Altura (en niveles)
    - Cantidad (número de nodos)
    - Amplitud (recorrido por niveles / BFS)
    - InOrden (rec/it), PreOrden (rec/it), PostOrden (rec/it)
    """

    def __init__(self) -> None:
        """Crea un árbol binario vacío."""
        self.raiz: Nodo | None = None

    # -------------------- Insertar --------------------
    def insertar(self, valor: int) -> None:
        """
        Inserta un valor en el árbol (versión simple).

        Args:
            valor (int): Valor a insertar en el árbol.
        """
        self.insertar_nodo_recursivo(valor)

    def Insertar(self, valor: int) -> None:
        """
        Inserta un valor en el árbol (alias con mayúscula).
        
        Args:
            valor (int): Valor a insertar en el árbol.
        """
        self.insertar(valor)

    def insertar_nodo_recursivo(self, valor: int) -> None:
        """
        Inserta un valor en el árbol de forma recursiva.
        
        Args:
            valor (int): Valor a insertar en el árbol.
        """
        def _insertar(raiz: Nodo | None, valor: int) -> Nodo:
            """
            Función auxiliar recursiva para insertar un nodo.
            Args:
                raiz (Nodo | None): Nodo raíz actual.
                valor (int): Valor a insertar.
            Returns:
                Nodo: Nodo raíz actualizado.
            """
            if raiz is None:
                return Nodo(valor)
            if valor < raiz.valor:
                raiz.hijo_izquierdo = _insertar(raiz.hijo_izquierdo, valor)
            else:
                raiz.hijo_derecho = _insertar(raiz.hijo_derecho, valor)
            return raiz

        self.raiz = _insertar(self.raiz, valor)

    def insertar_nodo_iterativo(self, valor: int) -> None:
        """
        Inserta un valor en el árbol de forma iterativa.
        
        Args:
            valor (int): Valor a insertar en el árbol.
        """
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
        """
        Verifica si el árbol está vacío.
        
        Returns:
            bool: True si el árbol está vacío, False en caso contrario.
        """
        return self.raiz is None

    def es_hoja(self, nodo: Nodo) -> bool:
        """
        Verifica si un nodo es hoja (no tiene hijos).
        
        Args:
            nodo (Nodo): Nodo a verificar.
        Returns:
            bool: True si es hoja, False en caso contrario.
        """
        return nodo.hijo_izquierdo is None and nodo.hijo_derecho is None

    def EsHoja(self, nodo: Nodo) -> bool:
        """
        Verifica si un nodo es hoja (alias con mayúscula).
        
        Args:
            nodo (Nodo): Nodo a verificar.
        Returns:
            bool: True si es hoja, False en caso contrario.
        """
        return self.es_hoja(nodo)

    # -------------------- Buscar --------------------
    def buscar(self, valor: int) -> bool:
        """
        Busca un valor en el árbol (versión simple, iterativa).
        
        Args:
            valor (int): Valor a buscar.
        Returns:
            bool: True si el valor está en el árbol, False en caso contrario.
        """
        return self.buscar_iterativo(valor)

    def Buscar(self, valor: int) -> bool:
        """
        Busca un valor en el árbol (alias con mayúscula).
        
        Args:
            valor (int): Valor a buscar.
        Returns:
            bool: True si el valor está en el árbol, False en caso contrario.
        """
        return self.buscar(valor)

    def buscar_recursivo(self, valor: int) -> bool:
        """
        Busca un valor en el árbol de forma recursiva.
        
        Args:
            valor (int): Valor a buscar.
        Returns:
            bool: True si el valor está en el árbol, False en caso contrario.
        """
        def _buscar(nodo: Nodo | None, valor: int) -> bool:
            """
            Función auxiliar recursiva para buscar un valor.
            Args:
                nodo (Nodo | None): Nodo actual.
                valor (int): Valor a buscar.
            Returns:
                bool: True si se encuentra, False en caso contrario.
            """
            if nodo is None:
                return False
            if valor == nodo.valor:
                return True
            if valor < nodo.valor:
                return _buscar(nodo.hijo_izquierdo, valor)
            return _buscar(nodo.hijo_derecho, valor)

        return _buscar(self.raiz, valor)

    def buscar_iterativo(self, valor: int) -> bool:
        """
        Busca un valor en el árbol de forma iterativa.
        
        Args:
            valor (int): Valor a buscar.
        Returns:
            bool: True si el valor está en el árbol, False en caso contrario.
        """
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            if valor < actual.valor:
                actual = actual.hijo_izquierdo
            else:
                actual = actual.hijo_derecho
        return False

    # -------------------- Altura (niveles) --------------------
    def altura(self) -> int:
        """
        Calcula la altura del árbol en **niveles**.
        
        Definición usada:
            - Árbol vacío: 0
            - Hoja: 1
            - General: 1 + máx(altura(izq), altura(der))
        
        Returns:
            int: Altura en niveles.
        """
        def _h(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + max(_h(nodo.hijo_izquierdo), _h(nodo.hijo_derecho))

        return _h(self.raiz)

    def Altura(self) -> int:
        """
        Calcula la altura en niveles (alias con mayúscula).
        
        Returns:
            int: Altura en niveles.
        """
        return self.altura()

    # -------------------- Cantidad (número de nodos) --------------------
    def cantidad(self) -> int:
        """
        Cuenta la cantidad total de nodos del árbol.
        
        Returns:
            int: Número de nodos.
        """
        def _contar(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + _contar(nodo.hijo_izquierdo) + _contar(nodo.hijo_derecho)

        return _contar(self.raiz)

    def Cantidad(self) -> int:
        """
        Cuenta la cantidad total de nodos (alias con mayúscula).
        
        Returns:
            int: Número de nodos.
        """
        return self.cantidad()

    # -------------------- Amplitud (BFS) --------------------
    def amplitud(self) -> list[int]:
        """
        Recorre el árbol por **amplitud** (niveles) y devuelve sus valores.

        Returns:
            list[int]: Valores visitados en orden por niveles (BFS).
        """
        if self.raiz is None:
            return []
        resultado: list[int] = []
        cola: list[Nodo] = [self.raiz]
        i = 0
        # Usamos una lista como cola; avanzamos con índice para O(1) amortizado
        while i < len(cola):
            actual = cola[i]
            i += 1
            resultado.append(actual.valor)
            if actual.hijo_izquierdo is not None:
                cola.append(actual.hijo_izquierdo)
            if actual.hijo_derecho is not None:
                cola.append(actual.hijo_derecho)
        return resultado

    def Amplitud(self) -> list[int]:
        """
        Recorre por amplitud (alias con mayúscula).

        Returns:
            list[int]: Valores visitados en orden por niveles (BFS).
        """
        return self.amplitud()

    # -------------------- Recorridos en profundidad --------------------
    def inorden_recursivo(self) -> list[int]:
        """
        Devuelve los valores en recorrido inorden de forma recursiva.
        
        Returns:
            list[int]: Lista de valores en orden.
        """
        def _in(nodo: Nodo | None, res: list[int]) -> None:
            if nodo:
                _in(nodo.hijo_izquierdo, res)
                res.append(nodo.valor)
                _in(nodo.hijo_derecho, res)

        resultado: list[int] = []
        _in(self.raiz, resultado)
        return resultado

    def inorden_iterativo(self) -> list[int]:
        """
        Devuelve los valores en recorrido inorden de forma iterativa.
        
        Returns:
            list[int]: Lista de valores en orden.
        """
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
        """
        Devuelve los valores en recorrido preorden de forma recursiva.
        
        Returns:
            list[int]: Lista de valores en preorden.
        """
        def _pre(nodo: Nodo | None, res: list[int]) -> None:
            if nodo:
                res.append(nodo.valor)
                _pre(nodo.hijo_izquierdo, res)
                _pre(nodo.hijo_derecho, res)

        resultado: list[int] = []
        _pre(self.raiz, resultado)
        return resultado

    def preorden_iterativo(self) -> list[int]:
        """
        Devuelve los valores en recorrido preorden de forma iterativa.
        
        Returns:
            list[int]: Lista de valores en preorden.
        """
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
        """
        Devuelve los valores en recorrido postorden de forma recursiva.
        
        Returns:
            list[int]: Lista de valores en postorden.
        """
        def _post(nodo: Nodo | None, res: list[int]) -> None:
            if nodo:
                _post(nodo.hijo_izquierdo, res)
                _post(nodo.hijo_derecho, res)
                res.append(nodo.valor)

        resultado: list[int] = []
        _post(self.raiz, resultado)
        return resultado

    def postorden_iterativo(self) -> list[int]:
        """
        Devuelve los valores en recorrido postorden de forma iterativa.
        
        Returns:
            list[int]: Lista de valores en postorden.
        """
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
        arbol.Insertar(v)  # alias con mayúscula

    print("¿Árbol vacío?:", arbol.es_vacio())
    print("Buscar(75):", arbol.Buscar(75))
    print("Buscar(500):", arbol.Buscar(500))
    print("Altura:", arbol.Altura(), "(niveles)")
    print("Cantidad de nodos:", arbol.Cantidad())
    print("Amplitud (BFS):", arbol.Amplitud())
    print("InOrden recursivo:", arbol.inorden_recursivo())
    print("InOrden iterativo:", arbol.inorden_iterativo())
    print("PreOrden recursivo:", arbol.preorden_recursivo())
    print("PreOrden iterativo:", arbol.preorden_iterativo())
    print("PostOrden recursivo:", arbol.postorden_recursivo())
    print("PostOrden iterativo:", arbol.postorden_iterativo())