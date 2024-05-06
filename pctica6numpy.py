import numpy as np
import csv

# Paso 1: Cargar datos desde el archivo CSV
phones_store = []
with open('smartphones.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        phones_store.append(float(row['Final Price']))

# Convertir la lista de ventas mensuales a un arreglo NumPy
phones_store = np.array(phones_store)

print("Datos de ventas de smartphones:")
print(phones_store)

