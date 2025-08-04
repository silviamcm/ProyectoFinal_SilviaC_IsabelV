#Avance 1 - SilviaC e IsabelV

#Se importan las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# 1. Se realiza la carga de los datos con el uso el URL datos cargados 
# en el GitHub

precip = ('https://raw.githubusercontent.com/silviamcm/'
          'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/precip.csv')

temp =('https://raw.githubusercontent.com/silviamcm/'
       'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/temp.csv')

mei = ('https://raw.githubusercontent.com/silviamcm/'
       'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/indicemei.csv')

#Se crean los dataframe de datos de las variables 
#establecidas para el respectivas modificaciones y análisis correspondiente
df_precip = pd.read_csv(precip)
df_temp = pd.read_csv(temp)
df_mei = pd.read_csv(mei)

# 2. Información básica del dataset 
#Se implementa la aplicación de la función df.describe, el cual visualiza 
# valores estadísticos de los datos del dataframe 
print(f'\n Realiza la visualización de la función .describe() de '
      'los valores estadísticos de los datos de precipitación')
print(f'{df_precip["precip"].describe().round(2)}')

print(f'\n Realiza la visualización de la función .describe() de '
      'los valores estadísticos de los datos de temperatura')
print(f'{df_temp["temp_max"].describe().round(2)}')
print(f'\n {df_temp["temp_min"].describe().round(2)}')

print(f'\n Realiza la visualización de la función .describe() de '
      'los valores estadísticos de los datos de índice del MEI')
print(f'{df_mei[[str(i) for i in range(1,13)]].describe().round(2)}')

#Se implementa la aplicación de la función df.tail el cual visualiza
#los últimos registros, en este caso los últimos 10
print(f'\n Realiza la visualización de la función .tail() '
      'de las últimas 10 filas del dataframe de precipitación')
print(df_precip.tail(10))

print(f'\n Realiza la visualización de la función .tail() '
      'de las últimas 10 filas del dataframe de temperatura')
print(df_temp.tail(10))

print(f'\n Realiza la visualización de la función .tail() '
      'de las últimas 10 filas del dataframe del índice del MEI')
print(df_mei.tail(10))

#Se implementa la aplicación de la función df.info el cual visualiza
print(f'\n Realiza la visualización de la función .info() de precipitación')
print(f'{df_precip.info()}')

print(f'\n Realiza la visualización de la función .info() de temperatura')
print(f'{df_temp.info()}')

print(f'\n Realiza la visualización de la función .info() del índice del MEI')
print(f'{df_mei.info()}')

#3. Identificación de valores nulos en los dataframes 

# Se utiliza la función .insull() para la obtención de la existencia de valores 
# nulos, y .sum() para sumar la cantidad de estos, 0: indica no valores nulos
print(f'\n Cantidad de valores nulos de las columnas de df precipitación:')
print(f"{df_precip.isnull().sum()}")

print(f'\n Cantidad de valores nulos de las columnas de df temperatura:')
print(f"{df_temp.isnull().sum()}")

print(f'\n Cantidad de valores nulos de las columnas de df MEI:')
print(f"{df_mei.isnull().sum()}")

#4 Mostrar las primeras 10 filas de cada dataset, se coloca 11 para que tome 
#en cuenta el nombre de las columnas
print(f'\n-Filas de Precipitación:\n')
print(df_precip.head(11))

print(f'\n-Filas de Temperatura:\n')
print(df_temp.head(11))

print(f'\n-Filas de Índice MEI:\n')
print(df_mei.head(11))

#5 Identificar los tipos de datos en cada columna
print(f'\n-Tipos de datos en Precipitación:\n')
print(df_precip.dtypes)

print(f'\n-Tipos de datos en Temperatura:\n')
print(df_temp.dtypes)

print(f'\n-Tipos de datos en Índice MEI:\n')
print(df_mei.dtypes)

#6 Visualización exploratoria básica, se coloca una división de rangos de 50
plt.figure(figsize=(8, 9))  # Tamaño de la figura general

plt.suptitle('Distribuciones Climáticas en América Central '
             '(1950–2023)', fontsize=18)

# Histograma 1: Precipitación
plt.subplot(3, 1, 1)  # 3 filas, 1 columna, posición 1
df_precip['precip'].hist(bins=50, color='skyblue', edgecolor='black')
plt.title('Distribución de la precipitación')
plt.xlabel('Precipitación (mm)')
plt.ylabel('Frecuencia')

# Histograma 2: Temperatura máxima
plt.subplot(3, 1, 2)
df_temp['temp_max'].hist(bins=50, color='salmon', edgecolor='black')
plt.title('Distribución de la temperatura máxima')
plt.xlabel('Temperatura Máxima (°C)')
plt.ylabel('Frecuencia')

# Histograma 3: Temperatura mínima
plt.subplot(3, 1, 3)
df_temp['temp_min'].hist(bins=50, color='lightgreen', edgecolor='black')
plt.title('Distribución de la temperatura máxima')
plt.xlabel('Temperatura Mínima (°C)')
plt.ylabel('Frecuencia')

# Mostrar todo junto
plt.tight_layout()
plt.show()