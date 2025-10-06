from quicksort_7a import quicksort
from selection_8 import selection_sort


class Arreglo:
    tamano = 0 
    datos = []
    def lectura(self):
        # imrpirme el arreglo
        for item in self.datos:
            print(item)
    def escritura(self, nuevosDatos):
        self.datos = nuevosDatos
    def inserta(self, dato):
        self.datos.append(dato)
    def elimina(self, key):
        self.datos.remove(key)
    def busca(self, key):
        self.datos.index(key)   
    def ordenar_quick(self):
        return quicksort(self.datos)
    def ordenar_selectionU(self):
        return selection_sort(self.datos)