#Avance 6 - SilviaC e IsabelV

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


#Creación de definiciones de funciones utilizadas dentro del código
#Definción de funciones para opción 1 y menú secundario

def menu_secundario():
    print(f'\n------ Menú Secundario -------')
    print(f'a: Valores Estadísticos de datos utilizados'
          'y uso de función df.info().')
    print(f'b: Primeras y últimas filas de sets de datos.')
    print(f'c: Comprobación valores nulos')
    print(f'd: identificación de los tipos de datos de las columnas')
    print(f'e: Salir ')
    print(f'------------------------------\n')


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

    
def filas_extremas():
    #Mostrar las primeras 10 filas de cada dataset, se coloca 11 para que tome 
    #en cuenta el nombre de las columnas
    print('\n Filas de Precipitación:\n')
    print(df_precip.head(11))

    print(f'\n-Filas de Temperatura:\n')
    print(df_temp.head(11))


    #Aplicación de la función df.tail el cual visualiza
    #los últimos registros, en este caso los últimos 10
    print(f'\n Visualización de la función .tail() de precipitación')
    print(df_precip.tail(10))

    print(f'\n Visualización de la función .tail() de temperatura')
    print(df_temp.tail(10))
    
    
def mostrar_valores_nulos():
    # Se utiliza la función .insull() para obtención de existencia de valores 
    # nulos, y .sum() para la suma de estos, 0: indica no valores nulos
    print(f'\n Cantidad de valores nulos en columnas de df precipitación:')
    print(f"{df_precip.isnull().sum()}")

    print(f'\n Cantidad de valores nulos en columnas de df temperatura:')
    print(f"{df_temp.isnull().sum()}")
   
    
def mostrar_tipos_datos():
    # Identificar los tipos de datos en cada columna
    print(f'\n-Tipos de datos en Precipitación:\n')
    print(df_precip.dtypes)

    print(f'\n-Tipos de datos en Temperatura:\n')
    print(df_temp.dtypes)   


def sub_menu():
    while True:
        menu_secundario()
        seg_opcion = input('Por favor, escriba la opción deseada:')
        
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
            print('Seleccione una opción válida.')  
  

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

    plt.title('Precipitación prom anual A.C. periodo de 1950-2023')
    plt.xlabel('Año')
    plt.ylabel('Precipitación promedio [mm]')
    plt.legend(['Belice','Guatemala','Honduras','El Salvador','Nicaragua'
    ,'Costa Rica','Panamá'])
    plt.grid(True)
    plt.show()
    
#Realiza calculo de la precipitación promedio anual para América Central 
#agregando 
prom_anual_region = df_precip.groupby('year')['precip'].mean().reset_index()
prom_anual_region.rename(columns={'precip': 'precip_anual'}, inplace=True)

#Realiza el calculo del promedio historio de los datos, para tener un mejor
# control de estos 
promedio_historico = prom_anual_region['precip_anual'].mean()

# Se efectua el calculo de la anomalias en el periodo utilizado
prom_anual_region['anomalia_pct'] = (
    (prom_anual_region['precip_anual'] - promedio_historico)/promedio_historico
) * 100

# Se establece para el establecimiento de las anomalias positivas o negativas
positivas = prom_anual_region[prom_anual_region['anomalia_pct'] >= 0]
negativas = prom_anual_region[prom_anual_region['anomalia_pct'] < 0]

# crea el definimiento de la función para el manejo de esta dentro del código 
def mostrar_grafica_precip_anomalias():
	# codigo de graficación estableciendo el tamaño de la figura
	plt.figure(figsize=(12, 6))

	# Barras positivas (azul), se utiliza el tipo de grafica bar para la 
	# visualización de las anomalias positivas, edgecolor: el borde de la barra
	plt.bar(positivas['year'], positivas['anomalia_pct'],
      	 color='blue', edgecolor='black')

	# Barras negativas (rojo), se utiliza el tipo de grafica bar para la 
	# visualización de las anomalias negativas
	plt.bar(negativas['year'], negativas['anomalia_pct'],
        color='red', edgecolor='black')

	# Línea base en 0, se emplementa para colocar linea 
	#horizontal de color negro para tener una mejor observación
	plt.axhline(0, color='black', linestyle='--')

	# Se da la modificaciones de las ditintas etiquetas utilizadas
	# de los ejes x, y, título, 
	plt.title('Anomalía porcentual anual de precipitación en América Central\n'
           'Respecto al promedio histórico (1950–2023)')
	plt.xlabel('Años')
	plt.ylabel('Anomalía porcentual (%)')
	plt.xticks(rotation=45)
	#Utiliza un alpha  referente a la opacidad en el gráfico delos valores
	# representados 
	plt.grid(axis='y', linestyle='--', alpha=0.5)
	#Nos permite ajustar los distintos elementos de la gráfica 
	plt.tight_layout()
	#Permite mostrar el grafico, para su visualización 
	plt.show()

#De la columna code, se extraen los primeros 3 caracteres para crear la columna
#país, y se utiliza fuera de la función ya que se utiliza para otra gráfica más
#adelante
df_temp['country'] = df_temp['code'].str[:3]

#Se crea la funcion para la gráfica de promedio de la temp media, máx y mín
def grafica_comparacion_maxmin():
    #Se agrupa por país, luego se calculan los promedios. Se usa el reset_index
    #debido a que country pasó a ser los índices del df entonces necesita
    #volver a ser una columna normal
    df_country_avg = (df_temp.groupby('country')
                      [['temp_max', 'temp_min']].mean().reset_index())

    #Aquí se va a calcular el promedio de la temp max y min y la temp media
    df_country_avg['temp_media'] = ((df_country_avg['temp_max'] + 
                                     df_country_avg['temp_min']) / 2)
    prom_general = df_country_avg['temp_media'].mean()

    #Se crea el gráfica de barras, la var x es paa la posición de los países en
    #el eje x, y el width para el ancho de la barra
    x = np.arange(len(df_country_avg['country']))
    width = 0.35 

    fig, ax = plt.subplots(figsize=(10, 6))

    #Aquí se crean las barras para cada temp, y la línea punteada del promedio 
    #general
    ax.bar(x - width/2, df_country_avg['temp_max'], 
           width, label='Temp Max', color='tomato')
    ax.bar(x + width/2, df_country_avg['temp_min'], 
           width, label='Temp Min', color='skyblue')
    ax.axhline(prom_general, color='black', linestyle='--', linewidth=2,
            label=f'Prom Temp Media ({prom_general:.2f}°C)')

    #Características del gráfico
    ax.set_ylabel('Temperatura (°C)')
    ax.set_title('Promedio de Temperatura Media, Máxima y Mínima por País de '
                 '1950 - 2023')
    ax.set_xticks(x)
    ax.set_xticklabels(df_country_avg['country'])
    ax.legend(loc='upper center',bbox_to_anchor=(0.5, -0.15), 
              ncol=3, frameon=False)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()


def grafica_tempmaxmin_pais():
    #Aquí agrupamos por país y año, y de una vez se calcula el promedio de las
    #temp max y min
    df_yearly = df_temp.groupby(['country', 'year'])[['temp_max', 
                                            'temp_min']].mean().reset_index()

    #Se grafican 9 subplots, auqnue son sólo 7 países, más adelante se borran
    #las subplots vacías
    fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))
    axs = axs.flatten()

    #Se usa .unique() ya que devuelve los valores únicos, en este caso los 
    #países sin duplicados
    paises = df_yearly['country'].unique()

    #Esta var es para ordenar las subplots a conveniencia
    posiciones = [0, 1, 2, 3, 4, 5, 7]

    #Se crea este for para que grafique cada país en las posiciones deseadas
    for idx_pais, pos_subplot in enumerate(posiciones):
        pais = paises[idx_pais]
        ax = axs[pos_subplot]

        data_pais = df_yearly[df_yearly['country'] == pais]

        ax.plot(data_pais['year'], data_pais['temp_max'], label='Temp Máxima', 
                color='darkgreen')
        ax.plot(data_pais['year'], data_pais['temp_min'], label='Temp Mínima', 
                color='orange')

        ax.set_title(f'País: {pais}')
        ax.set_xlabel('Año')
        ax.set_ylabel('Temperatura (°C)')
        ax.legend()
        ax.grid(True)

    #Este for es para eliminar las subplots vacías de las posiciones que no se 
    #usaron
    for i in range(len(axs)):
        if i not in posiciones:
            fig.delaxes(axs[i])

    fig.suptitle('Promedio Anual de la Temperatura Máxima y Mínima por País'
                 ' (1950-2023)', fontsize=16)
    
    #Aquí vamos a ajustar los espacios entre las subplots y el título
    plt.tight_layout(h_pad=5, w_pad=3, rect=[0, 0, 1, 0.95])
    plt.show()


#Definción de funciones para opción 3

def histogramas_preci_temp():
    #Visualización exploratoria básica, se coloca una división de rangos de 50
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
    
 
#Definción de función para Menú Principal   
def opcion_menu():
    print(f'\n------ Menú Principal ------')
    print(f'1. Información Básica de los DataFrame.')
    print(f'2. Visualización de Gráficas Básicas.')
    print(f'3. Visualizaciones más Complejas.')
    print(f'4. Salir ')
    print(f'----------------------------\n')
    
#Buble para el menú principal
while True:
    opcion_menu()
    print('Bienvenido, selección del 1 al 4')
    opcion =int(input('Por favor, escriba la opción deseada:'))

    if opcion == 1:
        sub_menu()   
    elif opcion == 2:
        #Visualización de gráfica lineal de precipitación promedio en A.C. 
        print(f'Se observa la tendencia de la precipitación en A.C.')
        mostar_graficas_precipi()
        #Visualización de gráfica lineal de temperatura media en A.C. 
        print(f'Se observa el comportamiento de la temperatura máxima y mínima'
              'respecto al promedio')
        grafica_comparacion_maxmin()
        #Visualización de gráfica de anomalías de los valores de la 
        #precipitación en A.C. 
        print(f'Se visualiza la gráfica de anomalías de la precipitación')
        mostrar_grafica_precip_anomalias()
    elif opcion == 3:
        #Visualización de los histogramas para la precipitación, temperatura
        #máxima y mínima
        print(f'Se observa la distribución del histograma de la precipitación'
              'y las temperaturas máximas y mínimas')
        histogramas_preci_temp()
        #Visualización de la gráfica lineal de temperaturas máximas y mínimas
        #por país
        print(f'Se observa la gráfica de la comparación del promedio de la'
              'temperatura máxima y mínima por país')
        grafica_tempmaxmin_pais() 
    elif opcion == 4:
        print('¡Gracias por utilizar el programa, vuelva pronto!')
        break
    else:
        print('Por favor, seleccione una opción válida del menú')