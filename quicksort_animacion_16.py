DATOS = [
    {"clave": 1424, "nombre": "Paleta Payaso", "precio": 20.00},
    {"clave": 1465, "nombre": "Gansito", "precio": 15.00},
    {"clave": 4126, "nombre": "Pan de muerto", "precio": 30.00}
]

def quicksort_visual(data, low, high, key="clave", depth=0):
    if low < high:
        p = particion(data, low, high, key, depth)
        quicksort_visual(data, low, p - 1, key, depth + 1)
        quicksort_visual(data, p + 1, high, key, depth + 1)

def particion(data, low, high, key, depth):
    pivot = data[high][key]
    i = low - 1
    print(f"{'  '*depth}Pivot = {pivot}")
    for j in range(low, high):
        if data[j][key] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            print(f"{'  '*depth}Swap {data[i][key]} <-> {data[j][key]} → {[x[key] for x in data]}")
    data[i+1], data[high] = data[high], data[i+1]
    print(f"{'  '*depth}Swap {data[i+1][key]} <-> {data[high][key]} → {[x[key] for x in data]}")
    print(f"{'  '*depth}Partición terminada → {[x[key] for x in data]}\n")
    return i + 1

if __name__ == "__main__":
    print("Arreglo inicial:", [x["clave"] for x in DATOS])
    quicksort_visual(DATOS, 0, len(DATOS) - 1)
    print("Arreglo final:", [x["clave"] for x in DATOS])
