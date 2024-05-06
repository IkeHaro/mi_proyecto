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
model = data['Model'].tolist()

#Convertiremos nuestras listas en erreglos NumPy
smartphones_array = np.array(smartphones)
brands_array = np.array(brands)
final_prices_array = np.array(final_prices)
model_array = np.array(model)

#Creamos un arrego el cual nos servira como un carrito de compras
carrito = np.full((3, 2), None)

def carrito_compras(smartphone, precio):

    # Crear el carrito como un arreglo de 3x2 lleno de None
    if 'carrito' not in globals():
        # Crear el carrito como un arreglo de 2x3 lleno de None
        globals()['carrito'] = np.full((3, 2), None)
    
    # Buscar la primera posición vacía en el carrito
    for i in range(carrito.shape[0]):
        for j in range(carrito.shape[1]):
            if carrito[i, j] is None:
                # Guardar el smartphone y su precio en el carrito
                carrito[i, j] = smartphone
                carrito[i, j + 1] = precio
                return
    
    print("El carrito está lleno, no se pueden agregar más elementos.")
    
def precio_final(carrito):
    # Inicializar el precio total como cero
    precio_total = 0
    
    # Sumar los precios de los smartphones en el carrito
    for i in range(carrito.shape[0]):
        if carrito[i, 1] is not None:
            precio_total += carrito[i, 1]
    
    return precio_total

def buscar_smartphones_por_marca(smartphones, brands_array, final_prices_array):
    
    brand = input("Ingrese la marca que desea buscar: ")
     
    # Busca la marca en el arreglo de marcas
    indices = np.where(brands_array == brand)[0]
    
    # Imprimir los smartphones y sus precios correspondientes
    if len(indices) > 0:
        print()
        print("Smartphones de la marca", brand, ":")
        for idx in indices:
            print(smartphones[idx], " - Precio:", final_prices_array[idx])
            
        # Pedir al usuario que seleccione un smartphone por su modelo
        modelo_seleccionado = input("Ingrese el modelo del smartphone que desea ver: ")
        
        # Buscar el modelo en el arreglo de modelos
        idx_modelo = np.where(model_array == modelo_seleccionado)[0]
        if len(idx_modelo) > 0:
            
            smartphone_seleccionado = smartphones[idx_modelo[0]]
            precio_seleccionado = final_prices_array[idx_modelo[0]]
            
            print()
            print("El smartphone seleccionado es:", smartphone_seleccionado)
            print("Precio:", precio_seleccionado)
            print()
            
            # Preguntar al usuario si desea agregar el smartphone al carrito de compras
            opcion = input("¿Desea agregar este smartphone al carrito de compras? (s/n): ")
            if opcion.lower() == 's':
                carrito_compras(smartphone_seleccionado, precio_seleccionado)
   
        else:
            print("No se encontró el modelo especificado.")              
    else:
        print("No se encontraron smartphones de la marca", brand)  
    
# Suponiendo que tienes los arreglos smartphones y brands_array disponibles
while True:
    buscar_smartphones_por_marca(smartphones, brands_array, final_prices_array)
    opcion = input("¿Desea hacer otra consulta? (s/n): ")
    if opcion.lower() != 's':
        break

def imprimir_carrito():
    if 'carrito' in globals():
        print("Carrito de compras:")
        print(carrito)
    else:
        print("El carrito de compras está vacío.")
        
imprimir_carrito()
precio_final_carrito = precio_final(carrito)
print("El precio final del carrito de compras es:", precio_final_carrito)