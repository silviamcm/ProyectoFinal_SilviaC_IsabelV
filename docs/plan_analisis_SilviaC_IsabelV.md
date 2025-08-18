#  Tema: Análisis de datos climatológicos de Precipitación y Temperatura, región de América Central en el periodo de 1950-2023.   
## Estudiantes: Silvia María Cerdas Mora y Ana Isabel Valverde Gardela  

## *Preguntas para responder*  

1. ¿Existe una modificación en las precipitaciones, de América Central, para el periodo seleccionado? 

2. ¿Cuál es el comportamiento de los promedios de la temperatura, en cada país para el periodo de 1950-2023? 

3. ¿Se evidencia una tendencia de aumento de la temperatura mínima  con respecto a la máxima?, se puede asociar al Cambio Climático? 

4. ¿Cuál año presenta mayor modificación de las variables, se debió a la influencia de algún fenómeno meteorológico asociado, para la región de América Central?

## *Hipótesis iniciales*
Cambio marcado entre los valores de las precipitaciones sobre la región seleccionada debido a los cambios climatológicos de la región. 
  
Mayor impacto sobre la región a durante la presencia de eventos extremos del ENOS, tanto en su fase fría como cálida, afectando se distinta forma la vertiente del Caribe centroamericana, como la vertiente del Pacífico de América Central.  
Presencia de una correlación positiva entre el ENOS y las variables de estudio.  

Presencia de anomalías de las precipitaciones y temperaturas. 

## *Visualizaciones planteadas*   

1. Gráfico lineal con el fin de visualizar la tendencia de la temperatura promedio anual de los 7 países en el periodo seleccionado.  

2. Gráfico lineal con el fin de visualizar la tendencia de la precipitación anual de los 7 países en el periodo seleccionado. 

3. Histograma de la variable de precipitación. 

4. Gráfico de barras para la visualización de las anomalías de precipitación. 

5. Gráfico lineal para la dinámica de época lluviosa y seca en cada país.

6. Gráfico circular para comparar la precipitación en cada país.

## *Metodología* 
*Datos Utilizados: URL: https://climateknowledgeportal.worldbank.org/. de:*

1. Precipitación (mm) 
2. Temperatura máxima (°C) 
3. Temperatura mínima (°C)

Los archivos descargados del ERA5 son en formato excel y además las columnas corresponden a las fechas, por lo cual se transpusieron los datos mediante un código de python y se convirtió a csv (se agregará a anexos), se crearon dos archivos, uno que contiene las temperaturas máximas y mínimas y otro con los datos de precipitación. Entonces ahora el archivo va contener las siguientes columnas:
1. code: código de la estación
2. name: nombre del lugar
3. year: año del dato
4. month: mes del dato
5. temp_min, temp_max / precip

Por medio de la creación de un código en Python y usando Visual Studio Code, se va a crear un código para la visualización y graficación de los datos. Las visualizaciones serán claves para poder responder las preguntas planteadas, sin embargo, es de manera clave la búsqueda y lectura de distintos artículos científicos, con el fin de clarificar y relacionar eventos ENOS con los posibles cambios de los valores y con esto el análisis de la dinámica de América Central de las precipitaciones y temperaturas, como estas se encuentran relacionado a los agentes externos (fenómenos meteorológicos). 

## *Resultados y Análisis*

## *Ejemplos*
### Caso 1: 2010 (Fenómeno de La niña)


(Instituto Meteorológico Nacional, s.f.)
(NOAA, s.f.)

### Caso 2: 2019 (Fenómeno de El Niño)
Otro ejemplo es el caso 2,  para este año se da la presencia del Fenómeno de El Niño sobre América Central, afectando directamente las precipitaciones de los paises de la región. Presentando una disminución marcada en los valores promedios, como es el caso de dos dos paises: Belice y Costa Rica.

Belice, preecenta afectaciones marcadas dentro de su sector agro, se de la presenia por parte del Ministerio de agricultura sobre dicho tema mediente comunicados de prensa sobre la sequia. 
El servicio Meteorologíco  establece a el Niño como un impulsador climatologico, como se estableció para el año 2019, evidenciando una disminución de las precipitaciones en relacion con los valores normales (Ministerio de Agricultura de Belice, s.f.).

Para el 2019, en el caso de Costa Rica, se establece la disminución de las precipitaciones, de acuerdo con el informe 10 del Boletín del ENOS del IMN.
En el cual evidencia que desde noviembre del año 2018 tanto para la región centroamericana, como para la región del Mar Caribe se dan valores positivos de la anomalia, de acuerdo con el estudio de stacione y estimadores de lluvia las zonas con mayor afectación son: la Vertiente del Caribe, como la Zona Norte (donde se presentó una sequía meterologíca). Estableciendo porcentajes de lluvia menores al 55% en todo el pais de los valores normales (Instituto Meteorológico Nacional, 2019).

De acuerdo con información del portal "Ojo del Clima", el porcentaje  de disminución alcanzó un 20% del total de lluvias para el año del 2019. De acuerdo con información suminstrada por el dirctor interino del IMN, el señor Werner Stolz: región del Valle Central y Pacífico el porcentaje es de 15-20% y Caribe un superavir de 15-20%.
(Ojo al Clima, s.f.).

## *Referencia*
1. Instituto Meteorológico Nacional. (s.f.). La Niña se disipó (Boletín del ENOS, n.º 46). https://www.imn.ac.cr/documents/10179/28154/%23%2046
2. Instituto Meteorológico Nacional. (2019). Informe 10 (Boletín del ENOS). https://www.imn.ac.cr/documents/10179/470467/%23119
3. Ministerio de Agricultura de Belice. (s.f.). Comunicado de prensa sobre la sequía. https://www.agriculture.gov.bz/drought-press-release/
4. NOAA. (s.f.). Eventos climáticos de 2010 relacionados con El Niño o La Niña. NOAA Clima.gov. https://www.climate.gov/news-features/features/2010-climate-events-connected-el-ni%C3%B1o-or-la-ni%C3%B1a
5. Ojo al Clima. (s.f.). Lluvias se redujeron 20% en 2019 con El Niño moderado. Recuperado el 16 de agosto de 2025, de https://ojoalclima.com/articles/lluvias-se-redujeron-20-en-2019-con-el-nino-moderado


