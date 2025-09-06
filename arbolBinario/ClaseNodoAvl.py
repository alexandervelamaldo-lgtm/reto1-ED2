class NodoAVL:
    """
    Clase que representa un nodo de un Árbol AVL.

    Atributos:
        valor (int): Valor almacenado en el nodo.
        izquierdo (NodoAVL | None): Referencia al hijo izquierdo.
        derecho (NodoAVL | None): Referencia al hijo derecho.
        altura (int): Altura del nodo dentro del árbol.
    """

    def __init__(self, valor: int) -> None:
        """
        Inicializa un nodo AVL con un valor y sin hijos.

        Args:
            valor (int): Valor a almacenar en el nodo.
        """
        self.valor: int = valor
        self.izquierdo: NodoAVL | None = None
        self.derecho: NodoAVL | None = None
        self.altura: int = 1  # un nodo nuevo tiene altura 1

    def factor_equilibrio(self) -> int:
        """
        Calcula el factor de equilibrio (FE) del nodo.

        Returns:
            int: Diferencia entre la altura del hijo izquierdo y derecho.
        """
        alt_izq = self.izquierdo.altura if self.izquierdo else 0
        alt_der = self.derecho.altura if self.derecho else 0
        return alt_izq - alt_der

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del nodo.

        Returns:
            str: Representación del nodo con valor y altura.
        """
        return f"NodoAVL(valor={self.valor}, altura={self.altura})"
