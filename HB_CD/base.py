import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
file_path = 'C:/Users/danny/OneDrive/Documents/mi_proyecto/HB_CD/ds_salaries.csv'
df = pd.read_csv(file_path)

#print(df.head())
#print(df.info())

def ingresos_exp():
    # Mapeo para renombrar los niveles de experiencia
    experience_levels = {
        'EN': 'Entry Level',
        'MI': 'Mid Level',
        'SE': 'Senior Level',
        'EX': 'Executive'
    }

    # Agrupar los datos por nivel de experiencia y calcular el salario promedio en USD
    salary_by_experience = df.groupby('experience_level')['salary_in_usd'].mean().rename(index=experience_levels)

    # Crear un gráfico de barras para visualizar el salario promedio por nivel de experiencia
    plt.figure(figsize=(10, 6))
    salary_by_experience.plot(kind='bar', color='skyblue')
    plt.title('Salario Promedio por Nivel de Experiencia')
    plt.xlabel('Nivel de Experiencia')
    plt.ylabel('Salario Promedio en USD')
    plt.xticks(rotation=0)  # Mantener los nombres de los niveles de experiencia horizontales
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def ingresos_ubi():
    
    # Agrupar los datos por ubicación de la compañía y calcular el salario promedio en USD
    salary_by_location = df.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False)
    
    # Filtrar para obtener los diez países con los mayores ingresos promedio
    top_10_salary_locations = salary_by_location.head(10)
    
    # Mapeo de códigos de países a nombres completos para una mejor visualización
    country_names = {
        'IL': 'Israel',
        'PR': 'Puerto Rico',
        'US': 'United States',
        'RU': 'Russia',
        'CA': 'Canada',
        'JP': 'Japan',
        'AU': 'Australia',
        'DE': 'Germany',
        'GB': 'United Kingdom',
        'NZ': 'New Zealand'
    }
    
    # Renombrar los índices usando el mapeo
    top_10_salary_locations = top_10_salary_locations.rename(index=country_names)
    
    # Crear un gráfico de barras para visualizar el salario promedio en los diez países con mayores ingresos
    plt.figure(figsize=(12, 8))
    top_10_salary_locations.plot(kind='bar', color='teal')
    plt.title('Top 10 Países con Mayores Ingresos Promedio en Ciencia de Datos')
    plt.xlabel('Ubicación de la Compañía')
    plt.ylabel('Salario Promedio en USD')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        
    # Filtrar para obtener los diez países con los menores ingresos promedio
    bottom_10_salary_locations = salary_by_location.tail(10)

    # Mapeo de códigos de países a nombres completos para una mejor visualización
    country_names_low = {
        'MK': 'Macedonia del Norte',
        'BO': 'Bolivia',
        'MA': 'Marruecos',
        'AL': 'Albania',
        'VN': 'Vietnam',
    }

    # Renombrar los índices usando el mapeo para los países con menores ingresos
    bottom_10_salary_locations = bottom_10_salary_locations.rename(index=country_names_low)

    # Crear un gráfico de barras para visualizar el salario promedio en los diez países con menores ingresos
    plt.figure(figsize=(12, 8))
    bottom_10_salary_locations.plot(kind='bar', color='lightcoral')
    plt.title('Top 10 Países con Menores Ingresos Promedio en Ciencia de Datos')
    plt.xlabel('Ubicación de la Compañía')
    plt.ylabel('Salario Promedio en USD')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def trabajo_remoto():

    # Agrupar los datos por el ratio de trabajo remoto y calcular el porcentaje de empleados en cada categoría
    remote_work_distribution = df['remote_ratio'].value_counts(normalize=True) * 100
    
    # Renombrar los índices para mejorar la legibilidad
    remote_index_names = {
        0: 'No Remote Work',
        100: 'Fully Remote',
        50: 'Partially Remote'
    }
    remote_work_distribution = remote_work_distribution.rename(index=remote_index_names)
    
    # Crear un gráfico de barras para visualizar los porcentajes
    plt.figure(figsize=(10, 6))
    remote_work_distribution.plot(kind='bar', color='cadetblue')
    plt.title('Distribution of Remote Work')
    plt.xlabel('Type of Remote Work')
    plt.ylabel('Percentage of Employees')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def tendencia_trabajo_remoto():

    # Agrupar los datos por año y ratio de trabajo remoto y calcular el porcentaje de empleados en cada categoría para cada año
    remote_growth = df.groupby(['work_year', 'remote_ratio']).size().unstack(fill_value=0)
    
    # Calcular porcentajes por año
    remote_growth_percent = remote_growth.div(remote_growth.sum(axis=1), axis=0) * 100
    
    # Extraer las columnas para empleados completamente remotos y sin trabajo remoto
    fully_remote_and_no_remote_trend = remote_growth_percent[[100, 0]]
    
    # Crear un gráfico de línea para visualizar las tendencias de ambos grupos
    plt.figure(figsize=(12, 7))
    fully_remote_and_no_remote_trend.plot(kind='line', marker='o', linestyle='-')
    plt.title('Tendencia de Trabajo Remoto y Sin Trabajo Remoto por Año')
    plt.xlabel('Año')
    plt.ylabel('Porcentaje de Empleados (%)')
    plt.grid(True)
    plt.xticks(fully_remote_and_no_remote_trend.index)  # Asegurar que todos los años estén etiquetados correctamente
    plt.legend(['Fully Remote', 'No Remote Work'], loc='best')
    plt.show()
    
    
ingresos_exp()
ingresos_ubi()
trabajo_remoto()
tendencia_trabajo_remoto()