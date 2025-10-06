import time

# 1. Inserción Directa (por matrícula)
def insercion_directa_paralelo(matriculas, nombres, materias):
    n = len(matriculas)
    # Copias locales para no alterar los originales
    mat = matriculas.copy()
    nom = nombres.copy()
    mat_apr = materias.copy()

    for i in range(1, n):
        clave_mat = mat[i]
        clave_nom = nom[i]
        clave_apr = mat_apr[i]
        j = i - 1
        # Mueve todos los registros mayores una posición adelante
        while j >= 0 and mat[j] > clave_mat:
            mat[j + 1] = mat[j]
            nom[j + 1] = nom[j]
            mat_apr[j + 1] = mat_apr[j]
            j -= 1
        # Inserta los valores en la posición correcta
        mat[j + 1] = clave_mat
        nom[j + 1] = clave_nom
        mat_apr[j + 1] = clave_apr

    return mat, nom, mat_apr


# 2. Quicksort (por materias aprobadas)
def quicksort_paralelo(matriculas, nombres, materias):
    if len(materias) <= 1:
        return matriculas, nombres, materias

    pivote = materias[len(materias) // 2]
    menores_mat, iguales_mat, mayores_mat = [], [], []
    menores_nom, iguales_nom, mayores_nom = [], [], []
    menores_apr, iguales_apr, mayores_apr = [], [], []

    for m, n, a in zip(matriculas, nombres, materias):
        if a < pivote:
            menores_mat.append(m)
            menores_nom.append(n)
            menores_apr.append(a)
        elif a == pivote:
            iguales_mat.append(m)
            iguales_nom.append(n)
            iguales_apr.append(a)
        else:
            mayores_mat.append(m)
            mayores_nom.append(n)
            mayores_apr.append(a)

    # Llamadas recursivas
    m1, n1, a1 = quicksort_paralelo(menores_mat, menores_nom, menores_apr)
    m2, n2, a2 = quicksort_paralelo(mayores_mat, mayores_nom, mayores_apr)

    return (
        m1 + iguales_mat + m2,
        n1 + iguales_nom + n2,
        a1 + iguales_apr + a2
    )


# Main
# Listas paralelas
matriculas = [202310, 202104, 202256, 202199, 202412, 202300, 202155]
nombres = ["Ana", "Luis", "María", "Jorge", "Carla", "Pedro", "Lucía"]
materias_aprobadas = [38, 40, 25, 45, 29, 33, 41]

print("=== Datos originales ===")
for m, n, a in zip(matriculas, nombres, materias_aprobadas):
    print(f"Matrícula: {m} | Nombre: {n:<6} | Materias aprobadas: {a}")
print("-" * 50)

#   Ordenamiento por matrícula (inserción directa)
inicio = time.time()
mat1, nom1, apr1 = insercion_directa_paralelo(matriculas, nombres, materias_aprobadas)
tiempo_insercion = time.time() - inicio

print("=== Ordenado por Matrícula (Inserción Directa) ===")
for m, n, a in zip(mat1, nom1, apr1):
    print(f"Matrícula: {m} | Nombre: {n:<6} | Materias aprobadas: {a}")
print(f"Tiempo: {tiempo_insercion:.8f} segundos\n")

#   Ordenamiento por materias aprobadas (Quicksort)
inicio = time.time()
mat2, nom2, apr2 = quicksort_paralelo(matriculas, nombres, materias_aprobadas)
tiempo_quick = time.time() - inicio

print("=== Ordenado por Materias Aprobadas (Quicksort) ===")
for m, n, a in zip(mat2, nom2, apr2):
    print(f"Matrícula: {m} | Nombre: {n:<6} | Materias aprobadas: {a}")
print(f"Tiempo: {tiempo_quick:.8f} segundos\n")

# Tiempos

print("-" * 50)
print("Comparación de tiempos:")
print(f"Inserción Directa: {tiempo_insercion:.8f} s")
print(f"Quicksort:         {tiempo_quick:.8f} s")