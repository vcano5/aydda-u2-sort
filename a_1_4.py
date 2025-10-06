import time

# 1. Burbuja simple
def burbuja_simple(arr):
    n = len(arr)
    lista = arr.copy()
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# 2. Burbuja con señal
def burbuja_con_senal(arr):
    n = len(arr)
    lista = arr.copy()
    for i in range(n - 1):
        intercambiado = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista

# 3. ShakerSort 
def shaker_sort(arr):
    lista = arr.copy()
    inicio = 0
    fin = len(lista) - 1
    while inicio < fin:
        # recorrido hacia adelante
        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        fin -= 1

        # recorrido hacia atrás
        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
        inicio += 1
    return lista

#  Main
apellidos = [
    "Ramírez", "López", "Zapata", "García", "Fernández", "Martínez", "Hernández", "Ruiz",
    "González", "Pérez", "Sánchez", "Torres", "Díaz", "Vargas", "Morales", "Jiménez",
    "Castro", "Ortiz", "Rojas", "Mendoza", "Guerrero", "Silva", "Cortés", "Delgado",
    "Aguilar", "Medina", "Reyes", "Chávez", "Cruz", "Vega", "Romero", "Navarro",
    "Flores", "Ramos", "Ibarra", "León", "Cabrera", "Molina", "Carrillo", "Peña",
    "Acosta", "Herrera", "Salazar", "Fuentes", "Miranda", "Valenzuela", "Luna", "Padilla",
    "Rosales", "Montoya", "Bravo", "Escobar", "Mejía", "Solís", "Ponce", "Varela",
    "Álvarez", "Domínguez", "Camacho", "Bautista", "Castañeda", "Arroyo", "Benítez", "Osorio",
    "Treviño", "Gallegos", "Beltrán", "Orozco", "Zamora", "Estrada", "Rivera", "Núñez",
    "Correa", "Valdez", "Soto", "Palacios", "Sandoval", "Esquivel", "Pacheco", "Cervantes",
    "Godoy", "Montes", "Méndez", "Lozano", "Barajas", "Quiroz", "Arellano", "Sepúlveda",
    "Tapia", "Villegas", "Olivares", "Tovar", "Mora", "Figueroa", "Calderón", "Saavedra"
]


print("Arreglo original de apellidos:")
print(apellidos)
print("-" * 40)

# --- 1. Burbuja simple ---
inicio = time.time()
resultado1 = burbuja_simple(apellidos)
tiempo1 = time.time() - inicio

# --- 2. Burbuja con señal ---
inicio = time.time()
resultado2 = burbuja_con_senal(apellidos)
tiempo2 = time.time() - inicio

# --- 3. ShakerSort ---
inicio = time.time()
resultado3 = shaker_sort(apellidos)
tiempo3 = time.time() - inicio

#  Resultados
print("Resultado Burbuja simple:")
print(resultado1)
print(f"Tiempo: {tiempo1:.8f} segundos\n")

print("Resultado Burbuja con señal:")
print(resultado2)
print(f"Tiempo: {tiempo2:.8f} segundos\n")

print("Resultado ShakerSort:")
print(resultado3)
print(f"Tiempo: {tiempo3:.8f} segundos\n")

print("-" * 40)
print("Comparación de tiempos:")
print(f"Burbuja simple:     {tiempo1:.8f} s")
print(f"Burbuja con señal:  {tiempo2:.8f} s")
print(f"ShakerSort:         {tiempo3:.8f} s")
