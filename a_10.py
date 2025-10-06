import time

SUR = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Paraguay", "Perú", "Uruguay", "Venezuela"]
CENTRO = ["Belice", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panamá"]
NORTE = ["Canadá", "Estados Unidos", "México"]

# Fusión de los tres arreglos
AMERICA = SUR + CENTRO + NORTE
AMERICA.sort()

print("=== PROBLEMA 8 ===")
print("Países del continente ordenados alfabéticamente:")
print(AMERICA)
print("-" * 50)

# Ordenar SUR, CENTRO y NORTE
# usando inserción directa, inserción binaria y Shell sort
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
        pos = busqueda_binaria(lista, clave, 0, i)
        lista = lista[:pos] + [clave] + lista[pos:i] + lista[i + 1:]
    return lista


def shell_sort(arr):
    lista = arr.copy()
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


# Función para medir tiempos
def medir_tiempo(funcion, datos):
    inicio = time.time()
    resultado = funcion(datos)
    tiempo = time.time() - inicio
    return resultado, tiempo


# --- SUR ---
sur_ins, t1 = medir_tiempo(insercion_directa, SUR)
sur_bin, t2 = medir_tiempo(insercion_binaria, SUR)
sur_shell, t3 = medir_tiempo(shell_sort, SUR)

# --- CENTRO ---
cen_ins, t4 = medir_tiempo(insercion_directa, CENTRO)
cen_bin, t5 = medir_tiempo(insercion_binaria, CENTRO)
cen_shell, t6 = medir_tiempo(shell_sort, CENTRO)

# --- NORTE ---
nor_ins, t7 = medir_tiempo(insercion_directa, NORTE)
nor_bin, t8 = medir_tiempo(insercion_binaria, NORTE)
nor_shell, t9 = medir_tiempo(shell_sort, NORTE)


print("=== PROBLEMA 10 ===")
print("SUR:")
print("Inserción directa:", sur_ins)
print("Inserción binaria:", sur_bin)
print("Shell sort:       ", sur_shell, "\n")

print("CENTRO:")
print("Inserción directa:", cen_ins)
print("Inserción binaria:", cen_bin)
print("Shell sort:       ", cen_shell, "\n")

print("NORTE:")
print("Inserción directa:", nor_ins)
print("Inserción binaria:", nor_bin)
print("Shell sort:       ", nor_shell, "\n")

print("-" * 50)
print("Comparación de tiempos (segundos):\n")
print(f"SUR - Directa: {t1:.6f}, Binaria: {t2:.6f}, Shell: {t3:.6f}")
print(f"CENTRO - Directa: {t4:.6f}, Binaria: {t5:.6f}, Shell: {t6:.6f}")
print(f"NORTE - Directa: {t7:.6f}, Binaria: {t8:.6f}, Shell: {t9:.6f}")