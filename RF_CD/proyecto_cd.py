import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
file_path = 'C:/Users/danny/OneDrive/Documents/mi_proyecto/RF_CD/Drug_overdose.csv'
data = pd.read_csv(file_path)

# Filtrar los datos para incluir solo 'All drug overdose deaths' y 'Total' para todas las edades
filtered_data = data[(data['AGE'] == 'All ages') & 
                     (data['PANEL'] == 'All drug overdose deaths') & 
                     (data['STUB_NAME'] == 'Total')]

# Ordenar los datos por año en orden ascendente
filtered_data_sorted = filtered_data.sort_values(by='YEAR')

# Extraer las columnas relevantes para la visualización
years = filtered_data_sorted['YEAR']
death_rates = filtered_data_sorted['ESTIMATE']

# Generar la gráfica Tasas de Muerte por Sobredosis
plt.figure(figsize=(10, 6))
plt.plot(years, death_rates, marker='o', linestyle='-', color='b')
plt.title('Tasas de Muerte por Sobredosis de Drogas a lo Largo de los Años (Todas las Edades, Total)')
plt.xlabel('Año')
plt.ylabel('Muertes por cada 100,000 habitantes')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar grafica Tasas de Muerte por Sobredosis
plt.show()