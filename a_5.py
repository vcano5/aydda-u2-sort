import time
import random
# 1. Inserción Directa
def insercion_directa(arr):
    lista = arr.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# 2. Inserción Binaria
def insercion_binaria(arr):
    lista = arr.copy()

    def busqueda_binaria(sublista, elemento, inicio, fin):
        while inicio < fin:
            medio = (inicio + fin) // 2
            if sublista[medio] < elemento:
                inicio = medio + 1
            else:
                fin = medio
        return inicio

    for i in range(1, len(lista)):
        clave = lista[i]
        # Buscar la posición de inserción
        pos = busqueda_binaria(lista, clave, 0, i)
        # Desplazar los elementos a la derecha
        lista = lista[:pos] + [clave] + lista[pos:i] + lista[i + 1:]
    return lista


# 3. Selección Directa
def seleccion_directa(arr):
    lista = arr.copy()
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista


# Main

# Generar una lista de números enteros aleatorios
numeros = [random.randint(1, 999) for _ in range(30)]  # 30 números entre 1 y 999

print("Arreglo original de enteros:")
print(numeros)
print("-" * 40)

#Tiempos
# --- 1. Inserción Directa ---
inicio = time.time()
res1 = insercion_directa(numeros)
t1 = time.time() - inicio

# --- 2. Inserción Binaria ---
inicio = time.time()
res2 = insercion_binaria(numeros)
t2 = time.time() - inicio

# --- 3. Selección Directa ---
inicio = time.time()
res3 = seleccion_directa(numeros)
t3 = time.time() - inicio


#       Resultados finales
print("Resultado Inserción Directa:")
print(res1)
print(f"Tiempo: {t1:.8f} segundos\n")

print("Resultado Inserción Binaria:")
print(res2)
print(f"Tiempo: {t2:.8f} segundos\n")

print("Resultado Selección Directa:")
print(res3)
print(f"Tiempo: {t3:.8f} segundos\n")

print("-" * 40)
print("Comparación de tiempos:")
print(f"Inserción Directa:  {t1:.8f} s")
print(f"Inserción Binaria:  {t2:.8f} s")
print(f"Selección Directa:  {t3:.8f} s")