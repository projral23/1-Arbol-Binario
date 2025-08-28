class NodoBinario:
    def __init__(self, dato=None):
        self.dato = dato
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getHijoIzquierdo(self):
        return self.hijoIzquierdo

    def setHijoIzquierdo(self, hijoIzquierdo):
        self.hijoIzquierdo = hijoIzquierdo

    def getHijoDerecho(self):
        return self.hijoDerecho

    def setHijoDerecho(self, hijoDerecho):
        self.hijoDerecho = hijoDerecho

    def esVacioHijoIzquierdo(self):
        return NodoBinario.esNodoVacio(self.hijoIzquierdo)

    def esVacioHijoDerecho(self):
        return NodoBinario.esNodoVacio(self.hijoDerecho)

    def esHoja(self):
        return self.esVacioHijoIzquierdo() and self.esVacioHijoDerecho()

    @staticmethod
    def esNodoVacio(nodo):
        return nodo is None

    @staticmethod
    def nodoVacio():
        return None