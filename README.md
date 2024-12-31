# Web Scraper de Elementos de Transición

Este proyecto consiste en un web scraper que extrae información sobre los elementos de transición de la tabla periódica desde Wikipedia en español.

## Descripción

El script extrae los siguientes datos de cada elemento de transición:
- Nombre del elemento
- Número atómico
- Símbolo químico

Los datos se obtienen de la página de Wikipedia de la tabla periódica en español y se guardan en un archivo CSV.

## Requisitos

- Python 3.7 o superior
- Las dependencias listadas en `requirements.txt`

## Instalación

1. Clona este repositorio o descarga los archivos
2. Instala las dependencias:

## Uso

1. Ejecuta el script principal:

El script generará automáticamente un archivo CSV llamado `Metales_de_transicion.csv` con los datos extraídos.

## Estructura del Proyecto

## Salida

El archivo CSV generado contendrá las siguientes columnas:
- Nombre: Nombre del elemento químico
- Numero_Atomico: Número atómico del elemento
- Simbolo: Símbolo químico del elemento

## Manejo de Errores

El script incluye manejo de errores para:
- Problemas de conexión a la página web
- Errores en el parsing de datos
- Errores en la escritura del archivo CSV

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.

## Licencia

Este proyecto está bajo la Licencia MIT.