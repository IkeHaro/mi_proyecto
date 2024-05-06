import numpy as np
import pandas as pd
import csv

#Cargamos archivo csv de nuestra ruta correspondiente
ruta_csv = "C:/Users/danny/OneDrive/Documents/mi_proyecto/smartphones.csv"
data = pd.read_csv(ruta_csv)

#Cargamos las columnas que necesitaremos de nuetro data set como listas de python
smartphones = data['Smartphone'].tolist()
brands = data['Brand'].tolist()
final_prices = data['Final Price'].tolist()

#Convertiremos nuestras listas en erreglos NumPy
smartphones_array = np.array(smartphones)
brands_array = np.array(brands)
final_prices_array = np.array(final_prices)

#Imprimimos para corroborar que se han cargado como se tiene planeado
#print("Arreglo de smartphones:", smartphones_array)
#print("Arreglo de marcas:", brands_array)
#print("Arreglo de precios finales:", final_prices_array)


def buscar_smartphones_por_marca(smartphones, brands_array):
    
    brand = input("Ingrese la marca que desea buscar: ")
     
    # Busca la marca en el arreglo de marcas
    indices = np.where(brands_array == brand)[0]
    
    # Imprime los smartphones correspondientes a esa marca
    if len(indices) > 0:
        print()
        print("Smartphones de la marca", brand, ":")
        for idx in indices:
            print(smartphones[idx])
    else:
        print("No se encontraron smartphones de la marca", brand)

# Suponiendo que tienes los arreglos smartphones y brands_array disponibles
while True:
    buscar_smartphones_por_marca(smartphones, brands_array)
    opcion = input("¿Desea hacer otra consulta? (s/n): ")
    if opcion.lower() != 's':
        break
