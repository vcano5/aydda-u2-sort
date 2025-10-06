from quicksort_7a import quicksort
import datetime

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

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j]['clave'] < data[min_idx]['clave']:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

if __name__ == "__main__":
    COPIA_MERGE = DATOS.copy()
    COPIA_SELECTION = DATOS.copy()
    
    selection_start = datetime.datetime.now()
    sorted_data = selection_sort(COPIA_SELECTION)
    selection_end = datetime.datetime.now()
    
    quicksort_start = datetime.datetime.now()
    sorted_data = quicksort(COPIA_MERGE)
    quicksort_end = datetime.datetime.now()

    print("Tiempo de ejecución de Selection Sort:", selection_end - selection_start)
    print("Tiempo de ejecución de Quick Sort:", quicksort_end - quicksort_start)
    