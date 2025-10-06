# Dado un arreglo unidimensional de N números enteros que debe ser ordenado de forma ascendente, conteste las siguientes preguntas
## a) Cuántas comparaciones e intercambios se deben realizar, aplicando el metodo de inserción directa, siguientes
### El arreglo ya está ordenado
#### Comparaciones
n-1 (una comparación por cada elemento desde p0)
#### Intercambios
0, no se necesitan intercambios

### El arreglo está ordenado en forma descentente
#### Comparaciones
n(n-1)/2 (peor caso)
### Intercambios
n(n-1)/2 (cada elemento debe moverse a su posición correcta)

## b) Conteste la pregunta del inciso anterior, para el método quicksort
### El arreglo ya está ordenado
#### Comparaciones
O(n^2) en el peor caso si se elige el primer o último elemento como pivote
#### Intercambios
0 o muy pocos (depende de la implementación)
### El arreglo está ordenado en forma descentente
#### Comparaciones
O(n^2) en el peor caso 
#### Intercambios
O(n^2) intercambios para reordenar completamente
## c) Conteste la pregunta del inciso anterior, para el método del monticulo (heapsort). 
### El arreglo ya está ordenado ó esta ordenado en forma descendente
#### Comparaciones
o(n log n) siempre construye el heap y extrae elementos
### Intercambios
o(n log n) debe reorganizar el heap en cada extracción.