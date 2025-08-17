#Avance 3 - SilviaC e IsabelV

#Se importan las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Se realiza la carga de los datos con el uso el URL datos cargados 
# en el GitHub
precip = ('https://raw.githubusercontent.com/silviamcm/'
          'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/precip.csv')

temp =('https://raw.githubusercontent.com/silviamcm/'
       'ProyectoFinal_SilviaC_IsabelV/refs/heads/main/data/temp.csv')



#Se crean los dataframe de datos de las variables 
#establecidas para el respectivas modificaciones y análisis correspondiente
df_precip = pd.read_csv(precip)
df_temp = pd.read_csv(temp)

#Agrugamiento de los valores por país
#Precipitación
df_bel =df_precip[df_precip['code'].str.contains(r'BLZ',case=False, na=False)]
df_guat= df_precip[df_precip['code'].str.contains(r'GTM',case=False, na=False)]
df_hon= df_precip[df_precip['code'].str.contains(r'HND',case=False, na=False)]
df_sal= df_precip[df_precip['code'].str.contains(r'SLV',case=False, na=False)]
df_nic= df_precip[ df_precip['code'].str.contains(r'NIC',case=False, na=False)]
df_cri= df_precip[df_precip['code'].str.contains(r'CRI',case=False, na=False)]
df_pan= df_precip[df_precip['code'].str.contains(r'PAN',case=False, na=False)]


#Temperatura
df_bel_temp =df_temp[df_precip['code'].str.contains(r'BLZ',case=False, 
                                                    na=False)]
df_guat_temp= df_precip[df_precip['code'].str.contains(r'GTM',case=False,
                                                       na=False)]
df_hon_temp= df_precip[df_precip['code'].str.contains(r'HND',case=False, 
                                                      na=False)]
df_sal_temp= df_precip[df_precip['code'].str.contains(r'SLV',case=False, 
                                                      na=False)]
df_nic_temp= df_precip[ df_precip['code'].str.contains(r'NIC',case=False,
                                                       na=False)]
df_cri_temp= df_precip[df_precip['code'].str.contains(r'CRI',case=False, 
                                                      na=False)]
df_pan_temp= df_precip[df_precip['code'].str.contains(r'PAN',case=False, 
                                                      na=False)]

#Creación de definiciones de funciones utilizadas dentro del codigo
#Definción de funciones para opción 1 y menu secundario

def menu_secundario():
    print(f'\n------ Menú Secundario -------')
    print(f'a: Valores Estadísticos de datos utilizados'
          'y uso de función df.info().')
    print(f'b: Primeras y últimas filas de sets de datos.')
    print(f'c: Comprobación valores nulos')
    print(f'd: identificación de los tipos de datos de las columnas')
    print(f'e: Salir ')
    print(f'--------------------------------\n')


def valores_estadisticos():
    #Se implementa función df.describe(), visualiza 
    # valores estadísticos de los datos del dataframe 
    print(f'\n Visualización de la función .describe() de precipitación')
    print(f'{df_precip["precip"].describe().round(2)}')
    #Información de temperaturas de la función df.describe()
    print(f'\n Visualización de la función .describe() de temperatura')
    print(f'{df_temp["temp_max"].describe().round(2)}')
    print(f'\n {df_temp["temp_min"].describe().round(2)}')
    

    #Se implementa la aplicación de la función df.info el cual visualiza
    print(f'\n Visualización de la función .info() de precipitación')
    print(f'{df_precip.info()}')
    #Información de temperaturas de la función df.info
    print(f'\n Visualización de la función .info() de temperatura')
    print(f'{df_temp.info()}')
    # Información del MEI de la función df.info
    print(f'\n Visualización de la función .info() del índice del MEI')

    
def filas_extremas():
    #Mostrar las primeras 10 filas de cada dataset, se coloca 11 para que tome 
    #en cuenta el nombre de las columnas
    print('\n Filas de Precipitación:\n')
    print(df_precip.head(11))

    print(f'\n-Filas de Temperatura:\n')
    print(df_temp.head(11))

    print(f'\n-Filas de Índice MEI:\n')
    

    #Aplicación de la función df.tail el cual visualiza
    #los últimos registros, en este caso los últimos 10
    print(f'\n Visualización de la función .tail() de precipitación')
    print(df_precip.tail(10))

    print(f'\n Visualización de la función .tail() de temperatura')
    print(df_temp.tail(10))

    print(f'\n Visualización de la función .tail() del índice del MEI')
    
    
def mostrar_valores_nulos():
    # Se utiliza la función .insull() para obtención de existencia de valores 
    # nulos, y .sum() para la suma de estos, 0: indica no valores nulos
    print(f'\n Cantidad de valores nulos en columnas de df precipitación:')
    print(f"{df_precip.isnull().sum()}")

    print(f'\n Cantidad de valores nulos en columnas de df temperatura:')
    print(f"{df_temp.isnull().sum()}")

    print(f'\n Cantidad de valores nulos en columnas de df MEI:')
   
    
def mostrar_tipos_datos():
    # Identificar los tipos de datos en cada columna
    print(f'\n-Tipos de datos en Precipitación:\n')
    print(df_precip.dtypes)

    print(f'\n-Tipos de datos en Temperatura:\n')
    print(df_temp.dtypes)

    print(f'\n-Tipos de datos en Índice MEI:\n')
   

def sub_menu():
    while True:
        menu_secundario()
        seg_opcion = input('Por favor escriba la opcion deseada:')
        
        if seg_opcion.casefold() =="a".casefold():
            valores_estadisticos()
        
        elif seg_opcion.casefold() =="b".casefold():
            filas_extremas()
            
        elif seg_opcion.casefold() =="c".casefold():
            mostrar_valores_nulos()
            
        elif seg_opcion.casefold() =="d".casefold():
            mostrar_tipos_datos()
            
        elif seg_opcion.casefold() =="e".casefold():
            print('Regresa al Menú Principal')
            break
        else:
            print('Seleccione opción válida.')  
  

#Definción de funciones para opción 2

def mostar_graficas_precipi():
    #Gráfica de América Central y la tendencia del valor promedio anual 
    # de las precipitaciones del periodo de datos  seleccionado
    prom_anual_bel = df_bel.groupby(df_bel['year'])['precip'].mean()
    prom_anual_gua = df_guat.groupby(df_guat['year'])['precip'].mean()
    prom_anual_hon = df_hon.groupby(df_hon['year'])['precip'].mean()
    prom_anual_sal = df_sal.groupby(df_sal['year'])['precip'].mean()
    prom_anual_nic = df_nic.groupby(df_nic['year'])['precip'].mean()
    prom_anual_cri = df_cri.groupby(df_cri['year'])['precip'].mean()
    prom_anual_pan = df_pan.groupby(df_pan['year'])['precip'].mean()

    plt.figure(figsize=(12, 5))

    plt.plot(prom_anual_bel,color="m")
    plt.plot(prom_anual_gua,color="g")
    plt.plot(prom_anual_hon,color="y")
    plt.plot(prom_anual_sal,color="b")
    plt.plot(prom_anual_nic,color="c")
    plt.plot(prom_anual_cri,color="r")
    plt.plot(prom_anual_pan,color="k")

    plt.title('Precipitación promedio anual América Central\n'
    'periodo de 1950-2023, datos del ')
    plt.xlabel('Año')
    plt.ylabel('Precipitación promedio [mm]')
    plt.legend(['Belice','Guatemala','Honduras','El Salvador','Nicaragua'
    ,'Costa Rica','Panamá'])
    plt.grid(True)
    plt.show()
#Tambien utilizado en la opción 2
    
#Definción de funciones para opción 3
def opcion_3():
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
    
 
#Definción de funcion para Menú Principal   
def opcion_menu():
    print(f'\n    Menú Principal    ')
    print(f'1. Información Básica de los DataFrame.')
    print(f'2. Visualización de Gráficas Básicas.')
    print(f'3. visualizaciones más Complejas.')
    print(f'4. Salir ')
    print(f'------------------------\n')
    

while True:
    opcion_menu()
    print('Bienvenido, selección del 1 al 4')
    opcion =int(input('Por favor escriba la opcion deseada:'))

    if opcion == 1:
        sub_menu()   
    elif opcion == 2:
        #Visualización de gráfica lineal de precipitación promedio en A.C. 
        print(f'Se observa la tendencia de la precipitación en A.C.')
        mostar_graficas_precipi()
        #Visualización de gráfica lineal de temperatura media en A.C. 
        print(f'Se observa la tendencia de la precipitación en A.C.')
        
    elif opcion == 3:
        opcion_3() 
    elif opcion == 4:
        break
    else:
        print('Por favor, Seleccione una opción válida del menú')

