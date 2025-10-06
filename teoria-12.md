# Se tiene un arreglo de N números enteros
a) ¿Cuántas comparaciones y cuántos intercambios se deben realizar si se ordena el arreglo con método de la burbuja?
## Comparaciones
- En cada ronda se comparan elementos adyacentes
- R1: (n-1) comparaciones
- R2: (n-2) comparaciones
- Rn: (n-1): 1 comparación
- Total: (n-1)+(n-2)+....+1 = n(n-1)/2 = O(n^2)

## Intercambios
- Mejor caso: ya esta ordenado = 0 intercambios
- Caso promedio: n(n-1)/4 intercambios
- Peor caso: Arreglo en orden inverso n(n-1)/2 intercambios

b) ¿Cuántas comparaciones y cuántos intercambios se deben realizar si se ordena el arreglo con el método de selección directa?
## Comparaciones
- Encontrar el minimo en cada posición
- Posicion 0: (n-1) comparaciones
- P1: (n-2) comparaciones
- P(n-2): 1 comparación
- Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n^2)

## Intercambios
- Se realiza un intercambio por cada posición (excepto la ultima)
- Total intercambios = (n-1) = O(n)
