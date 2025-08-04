#  Tema: Análisis de datos climatológicos de Precipitación y Temperatura, región de América Central en el periodo de 1950-2023.   
## Estudiantes: Silvia María Cerdas Mora y Ana Isabel Valverde Gardela  

## *Preguntas para responder*  

1. ¿Existe una modificación en las precipitaciones mensuales, de América Central, para el periodo seleccionado? 

2. ¿Existe una modificación considerada de la temperatura sobre la región seleccionada, en el periodo de 1950 a la de 2023? 

3. ¿Se evidencia una tendencia de aumento de la temperatura mínima en relación con la máxima?, se puede asociar al Cambio Climático? 

4. ¿Cuál año presenta mayor modificación de las variables, se debió a la influencia de algún fenómeno meteorológico asociado, para la región de América Central?
5. 


## *Hipótesis iniciales*
Cambio marcado entre los valores de las precipitaciones sobre la región seleccionada debido a los cambios climatológicos de la región. 
  
Mayor impacto sobre la región a durante la presencia de eventos extremos del ENOS, tanto en su fase fría como cálida, afectando se distinta forma la vertiente del Caribe centroamericana, como la vertiente del Pacífico de América Central.  
Presencia de una correlación positiva entre el ENOS y las variables de estudio.  

Presencia de anomalías de las precipitaciones y temperaturas. 

## *Visualizaciones planteadas* 

Mapa de la región seleccionada implementado cartography  

Gráfico lineal con el fin de visualizar la tendencia de la temperatura promedio anual de los 7 países en el periodo seleccionado.  

Gráfico lineal con el fin de visualizar la tendencia de la precipitación anual de los 7 países en el periodo seleccionado. 

Histograma de la variable de precipitación. 

Gráficos de correlación entre variables y el índice  

Gráfico para la visualización de los valores de las Anomalías de las variables. 

Dinámica de época lluviosa y seca  

## *Metodología* 
*Datos Utilizados: URL: https://climateknowledgeportal.worldbank.org/. de:*

1. Precipitación (mm) 
2. Temperatura máxima (°C) 
3. Temperatura mínima (°C)

*Datos utilizados de: URL: https://psl.noaa.gov/enso/mei/*

1. Índice del MEI (ENOS) 

Mediante el uso de los datos del ERA5 de las variables de precipitación (mm), temperatura máxima (°C) y mínima (°C) para la serie de tiempo de 1950 a 2023, y de los datos de la NOAA del Índice Multivariado de El Niño Oscilación del Sur (MEI) los caules van de 1979 al 2023, se lleva a cabo un análisis de estas variables en relación con los cambios evidenciados de los valores.  

Los archivos descargados del ERA5 son en formato excel y además las columnas corresponden a las fechas, por lo cual se transpusieron los datos mediante un código de python y se convirtió a csv (se agregará a anexos), se crearon dos archivos, uno que contiene las temperaturas máximas y mínimas y otro con los datos de precipitación. Entonces ahora el archivo va contener las siguientes columnas:
1. code: código de la estación
2. name: nombre del lugar
3. year: año del dato
4. month: mes del dato
5. temp_min, temp_max / precip

Por medio de la creación de un código en Python y usando Visual Studio Code, se va a crear un código para la visualización y graficación de los datos. Las visualizaciones serán claves para poder responder las preguntas planteadas, sin embargo, es de manera clave la búsqueda y lectura de distintos artículos científicos, con el fin de clarificar y relacionar eventos ENOS con los posibles cambios de los valores y con esto el análisis de la dinámica de América Central de las precipitaciones y temperaturas, como estas se encuentran relacionado a los agentes externos (fenómenos meteorológicos). 
