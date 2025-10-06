class Articulo:
    def __init__(self, clave, nombre, precio):
        self.clave = clave
        self.nombre = nombre
        self.precio = precio
    def imprimir_datos(self):
        print(self.clave, self.nombre, self.precio) 

payaso = Articulo("1424", "Paleta Payaso", 20.00)
gansito = Articulo("1465", "Gansito", 15.00)
pandemuerto = Articulo("4126", "Pan de muerto", 30.00)

DATOS = [
    payaso,
    gansito,
    pandemuerto
]

def crear_heap(data, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left].precio < data[smallest].precio:
        smallest = left

    if right < n and data[right].precio < data[smallest].precio:
        smallest = right

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        crear_heap(data, n, smallest)

def heapsort(data):

    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        crear_heap(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        crear_heap(data, i, 0)

    return data

if __name__ == "__main__":
    # Ordenar DATOS con heapsort de manera descendente segun "precio"
    sorted_data = heapsort(DATOS)
    for item in sorted_data:
        item.imprimir_datos()