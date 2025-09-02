from NodoBinario import NodoBinario
from collections import deque

class ArbolBinario:

    def __init__(self):
        self.raiz = None
    
    def getraiz(self):
        return self.raiz
    
    def setraiz(self, nodo):
        self.raiz = nodo

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoBinario(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.dato:
            if nodo_actual.hijoIzquierdo is None:
                nodo_actual.hijoIzquierdo = NodoBinario(valor)
            else:
                self._insertar_recursivo(nodo_actual.hijoIzquierdo, valor)
        elif valor > nodo_actual.dato:
            if nodo_actual.hijoDerecho is None:
                nodo_actual.hijoDerecho = NodoBinario(valor)
            else:
                self._insertar_recursivo(nodo_actual.hijoDerecho, valor)

    def es_hoja(self, valor):
        nodo = self._buscar_recursivo(self.raiz, valor)
        if nodo is None:
            return False
        return nodo.hijoIzquierdo is None and nodo.hijoDerecho is None

    def altura(self):
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo_actual):
        if nodo_actual is None:
            return -1
        altura_izquierda = self._altura_recursiva(nodo_actual.hijoIzquierdo)
        altura_derecha = self._altura_recursiva(nodo_actual.hijoDerecho)
        return 1 + max(altura_izquierda, altura_derecha)
    
    def cantidad(self):
        return self._cantidad_recursiva(self.raiz)

    def _cantidad_recursiva(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self._cantidad_recursiva(nodo_actual.hijoIzquierdo) + self._cantidad_recursiva(nodo_actual.hijoDerecho)
    
    def amplitud(self):
        if self.raiz is None:
            return []

        valores = []
        cola = deque([self.raiz])
        while cola:
            nodo_actual = cola.popleft()
            valores.append(nodo_actual.dato)

            if nodo_actual.hijoIzquierdo:
                cola.append(nodo_actual.hijoIzquierdo)
            if nodo_actual.hijoDerecho:
                cola.append(nodo_actual.hijoDerecho)
        return valores

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor) is not None
        
    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None or nodo_actual.dato == valor:
            return nodo_actual
        if valor < nodo_actual.dato:
            return self._buscar_recursivo(nodo_actual.hijoIzquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.hijoDerecho, valor)

    #Metodos de Recorrido 
    
    def inorden(self):

        return self._inorden_recursivo(self.raiz, [])
    
    def _inorden_recursivo(self, nodo_actual, lista_valores):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.hijoIzquierdo, lista_valores)
            lista_valores.append(nodo_actual.dato)
            self._inorden_recursivo(nodo_actual.hijoDerecho, lista_valores)
        return lista_valores
        
    def preorden(self):
        return self._preorden_recursivo(self.raiz, [])

    def _preorden_recursivo(self, nodo_actual, lista_valores):
        if nodo_actual:
            lista_valores.append(nodo_actual.dato)
            self._preorden_recursivo(nodo_actual.hijoIzquierdo, lista_valores)
            self._preorden_recursivo(nodo_actual.hijoDerecho, lista_valores)
        return lista_valores
    
    def postorden(self):
        return self._postorden_recursivo(self.raiz, [])

    def _postorden_recursivo(self, nodo_actual, lista_valores):
        if nodo_actual:
            self._postorden_recursivo(nodo_actual.hijoIzquierdo, lista_valores)
            self._postorden_recursivo(nodo_actual.hijoDerecho, lista_valores)
            lista_valores.append(nodo_actual.dato)
        return lista_valores
