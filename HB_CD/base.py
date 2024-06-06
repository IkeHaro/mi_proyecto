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
    
    """
    Agrupa los datos por nivel de experiencia y calcula el salario promedio en USD.
    Luego crea un gráfico de barras para visualizar el salario promedio por nivel de experiencia.
    
    """
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

def mapa_poblacion_junior_salarios():
    
    """
    Filtra los datos para personas de nivel entry-level (junior) que trabajan en Estados Unidos.
    Luego crea una gráfica de puntos para visualizar los salarios de nivel junior en Estados Unidos.
    
    """
    
    # Filtrar los datos para personas de nivel entry-level (junior)
    junior_df = df[df['experience_level'] == 'EN']

    # Filtrar los datos para personas de nivel entry-level (junior) que trabajan en Estados Unidos
    us_junior_df = junior_df[junior_df['employee_residence'] == 'US']

    # Crear una gráfica de puntos para visualizar los salarios de nivel junior en Estados Unidos
    plt.figure(figsize=(10, 6))
    plt.scatter(us_junior_df['work_year'], us_junior_df['salary_in_usd'], alpha=0.6, edgecolors='w', linewidth=0.5)

    # Agregar etiquetas y título
    plt.title('Salarios de Personas de Nivel Junior en Ciencia de Datos en Estados Unidos (Entry-level)')
    plt.xlabel('Año de Trabajo')
    plt.ylabel('Salario en USD')
    plt.grid(True)
    plt.show()

    # Calcular el salario máximo, mínimo y promedio para personas de nivel entry-level en Estados Unidos
    max_salary_us = us_junior_df['salary_in_usd'].max()
    min_salary_us = us_junior_df['salary_in_usd'].min()
    mean_salary_us = us_junior_df['salary_in_usd'].mean()

    max_salary_us, min_salary_us, mean_salary_us

def iqr_poblacion_junior():
    
    """
    Filtra los datos para personas de nivel entry-level (junior) que trabajan en Estados Unidos.
    Ajusta los límites superiores e inferiores de los salarios para reducir los valores atípicos.
    Luego crea diagramas de caja y de violín para visualizar la distribución de salarios por año.
    
    """
    
    # Filtrar los datos para personas de nivel entry-level (junior)
    junior_df = df[df['experience_level'] == 'EN']

    # Filtrar los datos para personas de nivel entry-level (junior) que trabajan en Estados Unidos
    us_junior_df = junior_df[junior_df['employee_residence'] == 'US']

    # Ajustar el límite superior manualmente para reducir los valores atípicos
    upper_bound_adjusted = 125000

    # Filtrar los datos para eliminar los valores atípicos con el nuevo límite superior
    adjusted_us_junior_df = us_junior_df[us_junior_df['salary_in_usd'] <= upper_bound_adjusted]

    # Ajustar el límite inferior para excluir valores por debajo de $50,000
    lower_bound_adjusted = 50000

    # Filtrar los datos para eliminar los valores atípicos con el nuevo límite inferior
    adjusted_us_junior_df = adjusted_us_junior_df[adjusted_us_junior_df['salary_in_usd'] >= lower_bound_adjusted]

    # Box plot de salarios por año
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='work_year', y='salary_in_usd', data=adjusted_us_junior_df)
    plt.title('Diagrama de Caja de Salarios de Nivel Junior en Ciencia de Datos en EE.UU. por Año')
    plt.xlabel('Año de Trabajo')
    plt.ylabel('Salario en USD')
    plt.grid(True)
    plt.show()
    
    # Gráfico de violín de salarios por año
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='work_year', y='salary_in_usd', data=adjusted_us_junior_df, inner='quartile')
    plt.title('Distribución de Salarios de Nivel Junior en Ciencia de Datos en EE.UU. por Año')
    plt.xlabel('Año de Trabajo')
    plt.ylabel('Salario en USD')
    plt.grid(True)
    plt.show()

def ingresos_ubi():
    
    """
    Agrupa los datos por ubicación de la compañía y calcula el salario promedio en USD.
    Luego crea un gráfico de barras para visualizar el salario promedio por ubicación.

    """
    
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
    
    """
    Agrupa los datos por tipo de trabajo remoto y calcula el salario promedio en USD.
    Luego crea un gráfico de barras para visualizar el salario promedio por tipo de trabajo remoto.

    """

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
    
    """
    Muestra la tendencia del trabajo remoto a lo largo de los años.
    Luego crea un gráfico de líneas para visualizar la tendencia del trabajo remoto en Ciencia de Datos.

    """

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
    
def salarios_junior(df, experience_level, country):
    
    """
    Filtra los datos para personas de nivel junior (entry-level) en el país especificado.
    Luego crea un gráfico de líneas para visualizar los promedios de salarios de nivel junior a lo largo del tiempo.
    
    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos de salarios.
        experience_level (str): El nivel de experiencia para filtrar (por defecto 'EN' para Entry Level).
        country (str): El país para filtrar (por defecto 'US').

    """
   
    # Filtrar por nivel de experiencia y país
    filtered_data = df[(df['experience_level'] == experience_level) & (df['company_location'] == country)]

    # Identificar y descartar el dato atípico en el año 2020 si es Estados Unidos y nivel junior
    if country == 'US' and experience_level == 'EN':
        filtered_data_2020 = filtered_data[(filtered_data['work_year'] == 2020) & (filtered_data['salary_in_usd'] < filtered_data[filtered_data['work_year'] == 2020]['salary_in_usd'].max())]
        filtered_data = pd.concat([
            filtered_data[filtered_data['work_year'] != 2020],
            filtered_data_2020
        ])

    # Calcular el promedio de salarios por año
    average_salaries_by_year = filtered_data.groupby('work_year')['salary_in_usd'].mean()

    # Crear gráfico de los promedios de salarios a lo largo del tiempo
    plt.figure(figsize=(10, 6))
    plt.plot(average_salaries_by_year.index, average_salaries_by_year.values, marker='o', linestyle='-', color='green')
    plt.title(f'Promedio de Salarios de Nivel {experience_level} en {country} por Año')
    plt.xlabel('Año')
    plt.ylabel('Promedio de Salario en USD')
    plt.grid(True)
    plt.xticks(average_salaries_by_year.index)  # Mostrar solo los años presentes en los datos
    plt.show()

def tipos_empleos(data, country='US'):
    
    """
    Filtra los datos para empleados en el país especificado trabajando tiempo completo o medio tiempo.
    Luego crea un gráfico de líneas para visualizar la cantidad de personas en empleos a tiempo completo y medio tiempo a lo largo del tiempo.
    
    Args:
        data (pd.DataFrame): El DataFrame que contiene los datos de salarios.
        country (str): El país para filtrar (por defecto 'US').
    
    """
    
    # Filtrar los datos para empleados en el país especificado trabajando tiempo completo o medio tiempo
    filtered_data = data[(data['employment_type'].isin(['FT', 'PT'])) & (data['company_location'] == country)]
    
    # Agrupar los datos por año y tipo de empleo, y contar las ocurrencias
    employment_counts = filtered_data.groupby(['work_year', 'employment_type']).size().unstack(fill_value=0)
    
    # Configurar la figura
    plt.figure(figsize=(10, 6))
    
    # Graficar los datos para tiempo completo y medio tiempo
    plt.plot(employment_counts.index, employment_counts['FT'], marker='o', linestyle='-', color='b', label='Tiempo Completo (FT)')
    plt.plot(employment_counts.index, employment_counts['PT'], marker='o', linestyle='-', color='r', label='Medio Tiempo (PT)')
    
    # Añadiendo título y etiquetas
    plt.title(f'Cantidad de Personas en Empleos a Tiempo Completo y Medio Tiempo en Ciencia de Datos en {country} (2020-2023)')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de Empleados')
    
    # Añadiendo leyenda y rejilla
    plt.legend()
    plt.grid(True)
    
    # Ajustando los ticks del eje x
    plt.xticks(employment_counts.index)
    
    # Mostrar la gráfica
    plt.show()
    
ingresos_exp()
ingresos_ubi()
trabajo_remoto()
tendencia_trabajo_remoto()
salarios_junior(df, 'EN', 'US')
tipos_empleos(df, 'US')
mapa_poblacion_junior_salarios()
iqr_poblacion_junior()