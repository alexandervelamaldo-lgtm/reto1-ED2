from flask import Flask, render_template, request, jsonify
import json
from arboles.abb import ArbolBinario
from arboles.avl import ArbolAVL

app = Flask(__name__)

# Instancias globales de los árboles
arbol_abb = ArbolBinario()
arbol_avl = ArbolAVL()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertar', methods=['POST'])
def insertar():
    data = request.json
    valor = int(data['valor'])
    tipo_arbol = data['tipo_arbol']
    
    if tipo_arbol == 'abb':
        arbol_abb.insertar(valor)
        return jsonify({'mensaje': f'Valor {valor} insertado en ABB'})
    else:
        arbol_avl.insertar(valor)
        return jsonify({'mensaje': f'Valor {valor} insertado en AVL'})

@app.route('/eliminar', methods=['POST'])
def eliminar():
    data = request.json
    valor = int(data['valor'])
    tipo_arbol = data['tipo_arbol']
    
    if tipo_arbol == 'abb':
        # Implementar eliminación para ABB si es necesario
        return jsonify({'mensaje': 'Eliminación no implementada para ABB'})
    else:
        arbol_avl.eliminar(valor)
        return jsonify({'mensaje': f'Valor {valor} eliminado de AVL'})

@app.route('/recorrido/<tipo>', methods=['GET'])
def obtener_recorrido(tipo):
    tipo_arbol = request.args.get('tipo_arbol', 'abb')
    
    if tipo_arbol == 'abb':
        arbol = arbol_abb
    else:
        arbol = arbol_avl
    
    if tipo == 'inorden':
        resultado = arbol.inorden_recursivo() if hasattr(arbol, 'inorden_recursivo') else arbol.inorden()
    elif tipo == 'preorden':
        resultado = arbol.preorden_recursivo() if hasattr(arbol, 'preorden_recursivo') else arbol.preorden()
    elif tipo == 'postorden':
        resultado = arbol.postorden_recursivo() if hasattr(arbol, 'postorden_recursivo') else arbol.postorden()
    elif tipo == 'amplitud':
        resultado = arbol.amplitud() if hasattr(arbol, 'amplitud') else []
    else:
        resultado = []
    
    return jsonify({'recorrido': resultado})

@app.route('/estructura', methods=['GET'])
def obtener_estructura():
    tipo_arbol = request.args.get('tipo_arbol', 'abb')
    
    if tipo_arbol == 'abb':
        arbol = arbol_abb
    else:
        arbol = arbol_avl
    
    # Convertir el árbol a una estructura JSON para visualización
    def nodo_a_dict(nodo):
        if nodo is None:
            return None
        return {
            'valor': nodo.valor,
            'izquierdo': nodo_a_dict(nodo.hijo_izquierdo if hasattr(nodo, 'hijo_izquierdo') else nodo.izquierdo),
            'derecho': nodo_a_dict(nodo.hijo_derecho if hasattr(nodo, 'hijo_derecho') else nodo.derecho)
        }
    
    raiz_dict = nodo_a_dict(arbol.raiz)
    return jsonify({'arbol': raiz_dict})

@app.route('/limpiar', methods=['POST'])
def limpiar_arbol():
    data = request.json
    tipo_arbol = data['tipo_arbol']
    
    if tipo_arbol == 'abb':
        arbol_abb.raiz = None
        return jsonify({'mensaje': 'ABB limpiado'})
    else:
        arbol_avl.raiz = None
        return jsonify({'mensaje': 'AVL limpiado'})

if __name__ == '__main__':
    app.run(debug=True)