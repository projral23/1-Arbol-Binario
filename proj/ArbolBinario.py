from NodoBinario import NodoBinario

class ArbolBinario:

    def es_arbol_vacio(self):
        self.raiz = None

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