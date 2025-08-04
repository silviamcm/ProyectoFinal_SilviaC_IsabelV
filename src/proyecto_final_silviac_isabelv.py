import pandas as pd
#import matplotlib as plt

# 1. Se realiza la carga de los datos con el uso el URL datos cargados 
# en el GitHub

precip = ('https://raw.githubusercontent.com/silviamcm/'
          'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/precip.csv')

temp =('https://raw.githubusercontent.com/silviamcm/'
       'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/temp.csv')

mei = ('https://raw.githubusercontent.com/silviamcm/'
       'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/indicemei.csv')

#Se crean los dataframe de datos de las variables 
#establecidas para el respectivas modificaciones y analisis correspondiente
df_precip = pd.read_csv(precip)
df_temp = pd.read_csv(temp)
df_mei = pd.read_csv(mei)

# 2. Información básica del dataset 
#Se implementa la aplicación de la función df.describe, el cual visualiza 
# valores estadisticos de los datos del dataframe 
print(f'\n Realiza la visualización de la función .describe() de '
      'los valores estadisticos de los datos de precipitación')
print(f'{df_precip["precip"].describe().round(2)}')

print(f'\n Realiza la visualización de la función .describe() de '
      'los valores estadisticos de los datos de temperatura')
print(f'{df_temp["temp_max"].describe().round(2)}')
print(f'\n {df_temp["temp_min"].describe().round(2)}')

print(f'\n Realiza la visualización de la función .describe() de '
      'los valores estadisticos de los datos de índice del MEI')
print(f'{df_mei[[str(i) for i in range(1,13)]].describe().round(2)}')

#Se implementa la aplicación de la función df.tail el cual visualiza
#los ultimos registros, en este caso los ultimos 10
print(f'\n Realiza la visualización de la función .tail() '
      'de las últimas 10 filas del dataframe de precipitacion')
print(df_precip.tail(10))

print(f'\n Realiza la visualización de la función .tail() '
      'de las últimas 10 filas del dataframe de temperatura')
print(df_temp.tail(10))

print(f'\n Realiza la visualización de la función .tail() '
      'de las últimas 10 filas del dataframe del indice del MEI')
print(df_mei.tail(10))

#Se implementa la aplicación de la función df.info el cual visualiza
print(f'\n Realiza la visualización de la función .info() de precipitacion')
print(f'{df_precip.info()}')

print(f'\n Realiza la visualización de la función .info() de temperatura')
print(f'{df_temp.info()}')

print(f'\n Realiza la visualización de la función .info() del indice del MEI')
print(f'{df_mei.info()}')

#3. Identificación de valores nulos en los dataframes 

# Se utiliza la función .insull() para ontención de  la existencia de valores 
# nulos, y .sum() para sumar la cantidad de estos, 0: indica no valores nulos
print(f'\n Cantidad de valores nulos de las columnas de df precipitacion:')
print(f"{df_precip.isnull().sum()}")

print(f'\n Cantidad de valores nulos de las columnas de df temperatura:')
print(f"{df_temp.isnull().sum()}")

print(f'\n Cantidad de valores nulos de las columnas de df mei:')
print(f"{df_mei.isnull().sum()}")




