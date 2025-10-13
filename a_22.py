import pandas as pd


def bubble_sort(df, column):
    """Ordena un DataFrame usando Bubble Sort según la columna dada."""
    data = df.to_dict("records")
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][column] > data[j + 1][column]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return pd.DataFrame(data)

def merge_sorted(df1, df2, column):
    """Intercala dos DataFrames ya ordenados según 'column'."""
    merged = []
    i = j = 0
    while i < len(df1) and j < len(df2):
        if df1.iloc[i][column] <= df2.iloc[j][column]:
            merged.append(df1.iloc[i])
            i += 1
        else:
            merged.append(df2.iloc[j])
            j += 1
    # Añadir los elementos restantes
    while i < len(df1):
        merged.append(df1.iloc[i])
        i += 1
    while j < len(df2):
        merged.append(df2.iloc[j])
        j += 1
    return pd.DataFrame(merged)

#  LECTURA DE ARCHIVOS
A1 = pd.read_excel("A1.xlsx")
A2 = pd.read_excel("A2.xlsx")
A3 = pd.read_excel("A3.xlsx")

# Si los archivos no están ordenados, aplicamos bubble sort
A1 = bubble_sort(A1, "Nombre")
A2 = bubble_sort(A2, "Nombre")
A3 = bubble_sort(A3, "Nombre")

#  INTERCALACIÓN DE ARCHIVOS
intercalado1 = merge_sorted(A1, A2, "Nombre")
RECITALES = merge_sorted(intercalado1, A3, "Nombre")

#  GUARDAR RESULTADO FINAL
RECITALES.to_excel("RECITALES.xlsx", index=False)

print("Archivo RECITALES.xlsx generado")
