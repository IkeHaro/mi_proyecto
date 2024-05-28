import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Supongamos que ya tienes definidos estos DataFrames y listas
# Ejemplo de inicialización (deberías tener los datos reales)
years = [2000, 2001, 2002, 2003, 2004]
apples = [0.5, 0.6, 0.7, 0.8, 0.9]
oranges = [0.3, 0.35, 0.4, 0.45, 0.5]

# Cargar algunos datasets de ejemplo de Seaborn
flowers_df = sns.load_dataset('iris')
tips_df = sns.load_dataset('tips')
flights_df = sns.load_dataset('flights').pivot(index='month', columns='year', values='passengers')

# Dividir flowers_df en sub-dataframes
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

# Imagen de ejemplo (asegúrate de tener una imagen 'img' cargada)
img = np.random.rand(10, 10)  # Usar una imagen real

fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# Gráfico de líneas
axes[0, 0].plot(years, apples, 's-b')
axes[0, 0].plot(years, oranges, 'o--r')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Yield (tons per hectare)')
axes[0, 0].legend(['Apples', 'Oranges'])
axes[0, 0].set_title('Crop Yields in Kanto')

# Gráfico de dispersión con Seaborn
axes[0, 1].set_title('Sepal Length vs. Sepal Width')
sns.scatterplot(x=flowers_df.sepal_length,
                y=flowers_df.sepal_width,
                hue=flowers_df.species,
                s=100,
                ax=axes[0, 1])

# Histograma apilado
axes[0, 2].set_title('Distribution of Sepal Width')
axes[0, 2].hist([setosa_df.sepal_width,
                 versicolor_df.sepal_width, 
                 virginica_df.sepal_width],
                bins=np.arange(2, 5, 0.25),
                stacked=True)
axes[0, 2].legend(['Setosa', 'Versicolor', 'Virginica'])

# Gráfico de barras con Seaborn
axes[1, 0].set_title('Restaurant bills')
sns.barplot(x='day', y='total_bill', hue='sex',
            data=tips_df, ax=axes[1, 0])

# Heatmap con Seaborn
axes[1, 1].set_title('Flight traffic')
sns.heatmap(flights_df, cmap='Blues', ax=axes[1, 1])

# Mostrar una imagen
axes[1, 2].set_title('Data Science Meme')
axes[1, 2].imshow(img)
axes[1, 2].grid(False)
axes[1, 2].set_xticks([])
axes[1, 2].set_yticks([])

plt.tight_layout(pad=2)
plt.show()
