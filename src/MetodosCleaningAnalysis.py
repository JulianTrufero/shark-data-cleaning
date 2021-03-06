#FUNCIONES PARA LIMPIAR DATOS:

import re 

def keep_columns(x, y):
    """
    Toma como argumento la lista de las columnas que quiero conservar y el nombre del data frame.
    Recorre el indice de columnas del data frame correspondiente y elimina las
    columnas que no quiero conservar
    """
    relevant = x
    for i in y.columns:
        if i not in relevant:
            y.drop(columns=[i], inplace=True)

def filtracion(x):
    """
    Toma como argumento un string, detecta con el re.findall de Regex si tiene la estructura numerica de fecha 'aaaa.mm.dd'. Genera una lista de 
    un elemento, y si la posición correspondiente al mes 'mm' coincide con el index del mes en el diccionario de meses,
    devuelve el valor correspondiente, o sea, el nombre del mes.
    """
    months = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    m = re.findall('\d{4}.\d{2}.\d{2}', x)
    if m and m[0][5:7] != '00':
        for k, v in months.items():
            if k == m[0][5:7]:
                return v     

def filtracion_especies(x):
    """
    Toma como argumento un string, detecta con el re.findall de Regex los string que poseen la palabra shark. Genera una lista de 
    un elemento, y devuelve el valor correspondiente convertido a minúsculas.
    """
    m = re.findall('\w+. shark', x)
    if m:
        return (m[0].lower())

def filtracion_actividades(x):

    """
    Toma como argumento un string, detecta con el re.findall de Regex los string que poseen terminan en 'ing'. Genera una lista de 
    un elemento que corresponde a la palabra encontrada, y la devuelve convertida a minúsculas.
    """

    m = re.findall('\w+.ing', str(x))
    if m:
        return (m[0].lower())