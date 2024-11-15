#Analisis de datos con panda (analisis descriptivo)
#1. para anallzar datos con pandas necesitamso instalar he importar la herramienta

import pandas as pd

#2 se obtiene la fuente de datos 
# esto en python se llama lista de datos
datos=[
    {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22},
        {'Nombre': 'estanislao gallego', 'Ciudad': 'Medellín', 'Edad': 26},
    {'Nombre': 'santiago perez', 'Ciudad': 'bogota', 'Edad': 25},
    {'Nombre': 'Patricia esponja', 'Ciudad': 'cali', 'Edad': 24},
    {'Nombre': 'Sara Perez', 'Ciudad': 'Pereira', 'Edad': 23},
    {'Nombre': 'Mariaza arango', 'Ciudad': 'Medellín', 'Edad': 22}
]

#3 Se capturan los datos:
#Pandas utiliza una tabla tabulada que se llama dataframe

datosOrdenados=pd.DataFrame(datos)

#print(datosOrdenados)

#Utilizando el head() los primero 5 registros:
#print(datosOrdenados.head(10))

#utilizabdo el tail() los ultimos 5:
#print(datosOrdenados.tail())

#utilizando el info() te sale los tipos de datos
#print(datosOrdenados.info())

#utilizando el describe() te sale las estadisticas de los datos
#print(datosOrdenados.describe())

#utilizando corchetes [] muestra lo que le especifiques
#print(datosOrdenados['Nombre'])
#print(datosOrdenados['Edad']+5)

#datosOrdenados.drop(0) eliminando registro
#print(datosOrdenados)

#Agrupa los datos
#print(datosOrdenados.groupby('Ciudad').size())