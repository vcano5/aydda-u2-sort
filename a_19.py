import pandas as pd

# Leer el archivo existente
df = pd.read_excel("huespedes.xlsx")

print("=== Datos originales ===")
print(df)
print("-" * 50)

# Método de Mezcla Directa
def merge_sort_dataframe(df, campo):
    # Caso base: un solo registro o ninguno
    if len(df) <= 1:
        return df

    mitad = len(df) // 2
    izquierda = df.iloc[:mitad]
    derecha = df.iloc[mitad:]

    # Llamadas recursivas para cada mitad
    izquierda_ordenada = merge_sort_dataframe(izquierda, campo)
    derecha_ordenada = merge_sort_dataframe(derecha, campo)

    # Mezclar ambas mitades ordenadas
    resultado = pd.DataFrame(columns=df.columns)
    i = j = 0

    while i < len(izquierda_ordenada) and j < len(derecha_ordenada):
        if izquierda_ordenada.iloc[i][campo] <= derecha_ordenada.iloc[j][campo]:
            resultado = pd.concat([resultado, izquierda_ordenada.iloc[[i]]], ignore_index=True)
            i += 1
        else:
            resultado = pd.concat([resultado, derecha_ordenada.iloc[[j]]], ignore_index=True)
            j += 1

    # Agregar los elementos restantes
    resultado = pd.concat([resultado, izquierda_ordenada.iloc[i:]], ignore_index=True)
    resultado = pd.concat([resultado, derecha_ordenada.iloc[j:]], ignore_index=True)

    return resultado


# a) Ordenar por número de habitación
orden_habitacion = merge_sort_dataframe(df, "NumeroHabitacion")

# b) Ordenar por nombre de huésped
orden_nombre = merge_sort_dataframe(df, "NombreHuesped")

print("=== Ordenado por número de habitación (Mezcla directa) ===")
print(orden_habitacion)
print("-" * 50)

print("=== Ordenado por nombre del huésped (Mezcla directa) ===")
print(orden_nombre)
print("-" * 50)

