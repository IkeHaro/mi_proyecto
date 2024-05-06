import numpy as np
import pandas as pd
import csv

ruta_csv = "C:/Users/danny/OneDrive/Documents/mi_proyecto/smartphones.csv"
data = pd.read_csv(ruta_csv)

#print(data.head(10))

smartphones = data['Smartphone'].tolist()
brands = data['Brand'].tolist()
final_prices = data['Final Price'].tolist()

smartphones_array = np.array(smartphones)
brands_array = np.array(brands)
final_prices_array = np.array(final_prices)

print("Arreglo de smartphones:", smartphones_array)
print()
print("Arreglo de marcas:", brands_array)
print()
print("Arreglo de precios finales:", final_prices_array)
print()