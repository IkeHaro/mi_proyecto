import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
df = pd.read_csv("Drug_overdose.csv")

# Filtrar los datos para todas las personas de todas las edades
all_persons_all_ages = df[(df['STUB_NAME'] == 'Total') & (df['AGE'] == 'All ages')]

# Generar la gráfica
plt.figure(figsize=(12, 6))
plt.plot(all_persons_all_ages['YEAR'], all_persons_all_ages['ESTIMATE'], marker='o')
plt.title('Tendencias de muertes por sobredosis a lo largo del tiempo (All persons, All ages)')
plt.xlabel('Año')
plt.ylabel('Tasa de mortalidad por sobredosis')
plt.grid(True)
plt.show()
