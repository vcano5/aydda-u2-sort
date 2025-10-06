from quicksort_7a import quicksort
# DATOS = [
#     {
#         "nombre": "Nombre1",
#         "ciudad": "Ciudad1",
#         "num_estrellas": "NumEstrellas1",
#         "num_cuartos": "NumCuartos1"
#     },
#     {
#         "nombre": "Nombre2",
#         "ciudad": "Ciudad2",
#         "num_estrellas": "NumEstrellas2",
#         "num_cuartos": "NumCuartos2"
#     },
#     {
#         "nombre": "Nombre3",
#         "ciudad": "Ciudad3",
#         "num_estrellas": "NumEstrellas3",
#         "num_cuartos": "NumCuartos3"
#     },
#     {
#         "nombre": "Nombre4",
#         "ciudad": "Ciudad4",
#         "num_estrellas": "NumEstrellas4",
#         "num_cuartos": "NumCuartos4"
#     },
#     {
#         "nombre": "Nombre5",
#         "ciudad": "Ciudad5",
#         "num_estrellas": "NumEstrellas5",
#         "num_cuartos": "NumCuartos5"
#     }
# ]

DATOS = [
    {
        "nombre": "Hotel Xcaret México",
        "ciudad": "Playa del Carmen",
        "num_estrellas": 5,
        "num_cuartos": 900
    },
    {
        "nombre": "Four Seasons Hotel Mexico City",
        "ciudad": "Ciudad de México",
        "num_estrellas": 5,
        "num_cuartos": 240
    },
    {
        "nombre": "Camino Real Polanco",
        "ciudad": "Ciudad de México",
        "num_estrellas": 5,
        "num_cuartos": 712
    },
    {
        "nombre": "Hotel Riu Plaza Guadalajara",
        "ciudad": "Guadalajara",
        "num_estrellas": 5,
        "num_cuartos": 550
    },
    {
        "nombre": "Hotel Emporio Acapulco",
        "ciudad": "Acapulco",
        "num_estrellas": 4,
        "num_cuartos": 422
    }
]


if __name__ == "__main__":
    # Primero ordenar por nombre (criterio secundario)
    sorted_data = quicksort(DATOS, key="nombre")
    # Luego ordenar por ciudad (criterio principal) - debe mantener el orden por nombre
    sorted_data = quicksort(sorted_data, key="ciudad")
    
    for item in sorted_data:    
        print(item)