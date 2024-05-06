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
print("Arreglo de smartphones:", smartphones_array)
print()
print("Arreglo de marcas:", brands_array)
print()
print("Arreglo de precios finales:", final_prices_array)
print()