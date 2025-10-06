import time
# Lista de alumnos (cada alumno es un diccionario)
alumnos = [
    {"nombre": "Ana", "matricula": 202310, "materias": 38, "promedio": 8.5},
    {"nombre": "Luis", "matricula": 202104, "materias": 40, "promedio": 9.0},
    {"nombre": "María", "matricula": 202256, "materias": 25, "promedio": 7.4},
    {"nombre": "Jorge", "matricula": 202199, "materias": 45, "promedio": 8.8},
    {"nombre": "Carla", "matricula": 202412, "materias": 29, "promedio": 8.1},
    {"nombre": "Pedro", "matricula": 202300, "materias": 33, "promedio": 7.9},
    {"nombre": "Lucía", "matricula": 202155, "materias": 41, "promedio": 9.3}
]

# a) Selección directa por nombre
def seleccion_directa(lista, campo):
    datos = lista.copy()
    n = len(datos)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if datos[j][campo].lower() < datos[min_index][campo].lower():
                min_index = j
        datos[i], datos[min_index] = datos[min_index], datos[i]
    return datos


# b) Quicksort por materias aprobadas
def quicksort(lista, campo):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2][campo]
    menores = [x for x in lista if x[campo] < pivote]
    iguales = [x for x in lista if x[campo] == pivote]
    mayores = [x for x in lista if x[campo] > pivote]
    return quicksort(menores, campo) + iguales + quicksort(mayores, campo)

# Main
print("=== Datos originales ===")
for a in alumnos:
    print(a)
print("-" * 50)

# Ordenar por nombre (selección directa)
inicio = time.time()
orden_nombre = seleccion_directa(alumnos, "nombre")
t1 = time.time() - inicio

print("=== Ordenado por Nombre (Selección directa) ===")
for a in orden_nombre:
    print(a)
print(f"Tiempo: {t1:.8f} segundos\n")

# Ordenar por materias aprobadas (quicksort)
inicio = time.time()
orden_materias = quicksort(alumnos, "materias")
t2 = time.time() - inicio

print("=== Ordenado por Materias Aprobadas (Quicksort) ===")
for a in orden_materias:
    print(a)
print(f"Tiempo: {t2:.8f} segundos\n")

print("-" * 50)
print("Comparación de tiempos:")
print(f"Selección directa: {t1:.8f} s")
print(f"Quicksort:         {t2:.8f} s")