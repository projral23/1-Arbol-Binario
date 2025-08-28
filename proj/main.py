from ArbolBinario import ArbolBinario

# Crear una instancia del arbol
mi_arbol = ArbolBinario()
print("Árbol binario creado.")
print("Raíz inicial:", mi_arbol.raiz)
print("-" * 20)

# Insertar valores en el arbol
print("Insertando valores: 50, 30, 70, 20, 40, 60, 80")
mi_arbol.insertar(50)
mi_arbol.insertar(30)
mi_arbol.insertar(70)
mi_arbol.insertar(20)
mi_arbol.insertar(40)
mi_arbol.insertar(60)
mi_arbol.insertar(80)
print("-" * 20)

# Demostrar los recorridos del arbol
print("Recorridos del árbol:")
# Inorden: izquierda -> raíz -> derecha (valores ordenados)
inorden_lista = mi_arbol.inorden()
print(f"Recorrido Inorden: {inorden_lista}")

# Preorden: raíz -> izquierda -> derecha
preorden_lista = mi_arbol.preorden()
print(f"Recorrido Preorden: {preorden_lista}")

# Postorden: izquierda -> derecha -> raíz
postorden_lista = mi_arbol.postorden()
print(f"Recorrido Postorden: {postorden_lista}")
print("-" * 20)

# Demostrar la función de búsqueda
print("Buscando valores:")
valor_buscar_1 = 40
resultado_1 = mi_arbol.buscar(valor_buscar_1)
print(f"¿El valor {valor_buscar_1} se encuentra en el árbol? {resultado_1}")

valor_buscar_2 = 99
resultado_2 = mi_arbol.buscar(valor_buscar_2)
print(f"¿El valor {valor_buscar_2} se encuentra en el árbol? {resultado_2}")