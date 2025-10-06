DATOS = [
    {
        "clave": "1424",
        "nombre": "Paleta Payaso",
        "precio": 20.00
    },
    {
        "clave": "1465",
        "nombre": "Gansito",
        "precio": 15.00
    },
    {
        "clave": "4126",
        "nombre": "Pan de muerto",
        "precio": 30.00
    }
]

def quicksort(data, key='clave'):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][key]
    left = [x for x in data if x[key] < pivot]
    middle = [x for x in data if x[key] == pivot]
    right = [x for x in data if x[key] > pivot]
    return quicksort(left, key) + middle + quicksort(right, key)



if __name__ == "__main__":
    sorted_data = quicksort(DATOS)
    print("Sorted data by 'clave':")
    for item in sorted_data:
        print(item)