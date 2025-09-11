let arbolData = null;

function mostrarMensaje(mensaje, esError = false) {
    const elemento = document.getElementById('mensaje');
    elemento.textContent = mensaje;
    elemento.style.color = esError ? 'red' : 'green';
}

function mostrarRecorrido(recorrido, tipo) {
    const elemento = document.getElementById('recorridoResultado');
    elemento.innerHTML = `<strong>${tipo}:</strong> [${recorrido.join(', ')}]`;
}

async function insertarValor() {
    const valorInput = document.getElementById('valorInput');
    const tipoArbol = document.getElementById('tipoArbol').value;
    const valor = parseInt(valorInput.value);
    
    if (isNaN(valor)) {
        mostrarMensaje('Por favor ingrese un valor numérico válido', true);
        return;
    }
    
    try {
        const response = await fetch('/insertar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ valor, tipo_arbol: tipoArbol })
        });
        
        const data = await response.json();
        mostrarMensaje(data.mensaje);
        valorInput.value = '';
        await actualizarVisualizacion();
    } catch (error) {
        mostrarMensaje('Error al insertar valor: ' + error.message, true);
    }
}

async function eliminarValor() {
    const valorInput = document.getElementById('valorInput');
    const tipoArbol = document.getElementById('tipoArbol').value;
    const valor = parseInt(valorInput.value);
    
    if (isNaN(valor)) {
        mostrarMensaje('Por favor ingrese un valor numérico válido', true);
        return;
    }
    
    try {
        const response = await fetch('/eliminar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ valor, tipo_arbol: tipoArbol })
        });
        
        const data = await response.json();
        mostrarMensaje(data.mensaje);
        valorInput.value = '';
        await actualizarVisualizacion();
    } catch (error) {
        mostrarMensaje('Error al eliminar valor: ' + error.message, true);
    }
}

async function realizarRecorrido(tipo) {
    const tipoArbol = document.getElementById('tipoArbol').value;
    
    try {
        const response = await fetch(`/recorrido/${tipo}?tipo_arbol=${tipoArbol}`);
        const data = await response.json();
        mostrarRecorrido(data.recorrido, tipo);
    } catch (error) {
        mostrarMensaje('Error al realizar recorrido: ' + error.message, true);
    }
}

async function limpiarArbol() {
    const tipoArbol = document.getElementById('tipoArbol').value;
    
    try {
        const response = await fetch('/limpiar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tipo_arbol: tipoArbol })
        });
        
        const data = await response.json();
        mostrarMensaje(data.mensaje);
        await actualizarVisualizacion();
    } catch (error) {
        mostrarMensaje('Error al limpiar árbol: ' + error.message, true);
    }
}

async function actualizarVisualizacion() {
    const tipoArbol = document.getElementById('tipoArbol').value;
    
    try {
        const response = await fetch(`/estructura?tipo_arbol=${tipoArbol}`);
        const data = await response.json();
        arbolData = data.arbol;
        dibujarArbol();
    } catch (error) {
        console.error('Error al obtener estructura del árbol:', error);
    }
}

function dibujarArbol() {
    const canvas = document.getElementById('treeCanvas');
    const ctx = canvas.getContext('2d');
    
    // Limpiar canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    if (!arbolData) {
        // Mostrar mensaje cuando el árbol está vacío
        ctx.font = '20px Arial';
        ctx.fillStyle = '#999';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('Árbol vacío', canvas.width / 2, canvas.height / 2);
        return;
    }
    
    // Configuración de dibujo
    const radio = 20;
    const verticalEspacio = 80;
    const horizontalEspacio = 40;
    
    // Calcular dimensiones del árbol
    const anchoArbol = calcularAnchoArbol(arbolData) * horizontalEspacio;
    
    // Calcular posiciones de todos los nodos (centrados)
    const posiciones = {};
    const xInicial = canvas.width / 2; // Centrar horizontalmente
    calcularPosiciones(arbolData, 0, xInicial, posiciones, horizontalEspacio, verticalEspacio);
    
    // Dibujar conexiones primero (para que queden detrás de los nodos)
    dibujarConexiones(ctx, arbolData, posiciones, radio);
    
    // Dibujar nodos
    for (const [id, pos] of Object.entries(posiciones)) {
        dibujarNodo(ctx, pos.x, pos.y, radio, id);
    }
}

function calcularAnchoArbol(nodo) {
    if (!nodo) return 0;
    
    // Calcular el ancho como el máximo entre el subárbol izquierdo y derecho
    const anchoIzquierdo = calcularAnchoArbol(nodo.izquierdo || nodo.hijo_izquierdo);
    const anchoDerecho = calcularAnchoArbol(nodo.derecho || nodo.hijo_derecho);
    
    // El ancho total es la suma de los anchos de los subárboles más 1 para el nodo actual
    return anchoIzquierdo + anchoDerecho + 1;
}

function calcularPosiciones(nodo, nivel, x, posiciones, horizontalEspacio, verticalEspacio) {
    if (!nodo) return;
    
    // Calcular posición actual
    const y = nivel * verticalEspacio + 50;
    posiciones[nodo.valor] = { x, y };
    
    // Calcular espacio para subárboles
    const anchoIzquierdo = calcularAnchoArbol(nodo.izquierdo || nodo.hijo_izquierdo) * horizontalEspacio;
    const anchoDerecho = calcularAnchoArbol(nodo.derecho || nodo.hijo_derecho) * horizontalEspacio;
    
    // Posiciones para hijos
    if (nodo.izquierdo || nodo.hijo_izquierdo) {
        const hijoIzq = nodo.izquierdo || nodo.hijo_izquierdo;
        const xIzquierdo = x - anchoDerecho - horizontalEspacio;
        calcularPosiciones(
            hijoIzq, 
            nivel + 1, 
            xIzquierdo, 
            posiciones, 
            horizontalEspacio, 
            verticalEspacio
        );
    }
    
    if (nodo.derecho || nodo.hijo_derecho) {
        const hijoDer = nodo.derecho || nodo.hijo_derecho;
        const xDerecho = x + anchoIzquierdo + horizontalEspacio;
        calcularPosiciones(
            hijoDer, 
            nivel + 1, 
            xDerecho, 
            posiciones, 
            horizontalEspacio, 
            verticalEspacio
        );
    }
}

function dibujarConexiones(ctx, nodo, posiciones, radio) {
    if (!nodo) return;
    
    const posNodo = posiciones[nodo.valor];
    
    // Dibujar conexión con hijo izquierdo
    if (nodo.izquierdo || nodo.hijo_izquierdo) {
        const hijoIzq = nodo.izquierdo || nodo.hijo_izquierdo;
        const posHijoIzq = posiciones[hijoIzq.valor];
        
        ctx.beginPath();
        ctx.moveTo(posNodo.x, posNodo.y + radio);
        ctx.lineTo(posHijoIzq.x, posHijoIzq.y - radio);
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 2;
        ctx.stroke();
        
        dibujarConexiones(ctx, hijoIzq, posiciones, radio);
    }
    
    // Dibujar conexión con hijo derecho
    if (nodo.derecho || nodo.hijo_derecho) {
        const hijoDer = nodo.derecho || nodo.hijo_derecho;
        const posHijoDer = posiciones[hijoDer.valor];
        
        ctx.beginPath();
        ctx.moveTo(posNodo.x, posNodo.y + radio);
        ctx.lineTo(posHijoDer.x, posHijoDer.y - radio);
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 2;
        ctx.stroke();
        
        dibujarConexiones(ctx, hijoDer, posiciones, radio);
    }
}

function dibujarNodo(ctx, x, y, radio, valor) {
    // Círculo del nodo
    ctx.beginPath();
    ctx.arc(x, y, radio, 0, 2 * Math.PI);
    ctx.fillStyle = '#4CAF50';
    ctx.fill();
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Texto del valor
    ctx.fillStyle = 'white';
    ctx.font = 'bold 16px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(valor, x, y);
}

// Inicializar la visualización al cargar la página
document.addEventListener('DOMContentLoaded', actualizarVisualizacion);