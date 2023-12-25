# Documentación RETO: Análisis Exploratorio de Datos (EDA). Prueba Tecnica.


##Abrir el archivo .ipynb en Google Colab o Jupyter notebook.


## Autor
[CARLOS IBAÑEZ]


## Objetivo del Código
El código tiene como objetivo realizar un EDA sobre un conjunto de datos de ventas y emplear modelos para predecir las cantidades en función de las características proporcionadas.

## Contenido del Código
El código se divide en varias secciones:

1. **Configuración Inicial:** Descarga de datos, lectura del archivo y visualización de las primeras filas del DataFrame.

2. **Limpieza de Datos:** Filtrado de datos, conversión de tipos, eliminación de valores nulos, y otras operaciones para asegurar la calidad de los datos.

3. **Análisis Exploratorio de Datos (EDA):**
   - **Descripción General:** Muestra información sobre el número de registros, tipos de datos y estadísticas descriptivas del conjunto de datos.
   - **Variables Categóricas:** Analiza la distribución de variables categóricas, mostrando visualizaciones y estadísticas descriptivas.
   - **Visualización Univariable TOP 15:** Muestra visualizaciones de las 15 principales categorías para variables categóricas.
   - **Artículos más vendidos por tienda:** Analiza y visualiza los artículos más vendidos por cada tienda.
   - **Artículo más vendido por cada año:** Analiza y visualiza el artículo más vendido por cada año.
   - **Ventas totales por color:** Analiza y visualiza las ventas totales por color.
   - **Material más vendido por cada año:** Analiza y visualiza el material más vendido por cada año.
   - **Producto más vendido por cada mes:** Analiza y visualiza el producto más vendido por cada mes.

4. **Predicción de Ventas Mensuales:**
   - Realiza una descomposición de la serie temporal para analizar tendencia, estacionalidad y residuos.
   - Ajusta un modelo SARIMA (Seasonal Autoregressive Integrated Moving Average) para realizar predicciones.
   - Visualiza las predicciones y el intervalo de confianza.

## Uso del Código## 
1. **Requisitos:**
   - Acceso a Google Colab Jupyter notebook.
   - Bibliotecas necesarias instaladas (pandas, matplotlib, seaborn, statsmodels, etc.).

2. **Ejecución del Código:**
   - Abre el archivo .ipynb en Google Colab o Jupyter notebook.
   - Ejecuta cada celda secuencialmente.
 
