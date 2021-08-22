#FUNCIONES PARA LIMPIAR DATOS: HIPOTESIS I

def drop():
    """
    Por cada elemento perteneciente al index de columnas, si este no pertenece a la lista de columnas
    relevantes, lo elimina del data frame
    """
    relevant = ['Case Number', 'Type', 'Case Number.1', 'Case Number.2']
    for i in sdf.columns:
        if i not in relevant:
            sdf.drop(columns=[i], inplace=True)

def filtracion(x):
    """
    Por cada valor de X, detecta con el re.findall de Regex si tiene la estructura 'aaaa.mm.dd'. Genera una lista de 
    un elemento, y si la posición correspondiente a 'mm' coincide con el index del mes en el diccionario de meses,
    devuelve el valor correspondiente, o sea, el nombre del mes.
    """
    months = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    m = re.findall('\d{4}.\d{2}.\d{2}', x)
    if m and m[0][5:7] != '00':
        for k, v in months.items():
            if k == m[0][5:7]:
                return v
#FUNCIONES PARA LIMPIAR DATOS: HIPOTESIS II       

def drop2():
    """
    Por cada elemento perteneciente al index de columnas, si este no pertenece a la lista de columnas
    relevantes, lo elimina del data frame
    """
    relevant = ['Injury', 'Fatal (Y/N)', 'Species ']
    for i in sdf2.columns:
        if i not in relevant:
            sdf2.drop(columns=[i], inplace=True)

def filtracion_especies(x):
    """

    """
    m = re.findall('\w+. shark', x)
    if m:
        return (m[0].lower())
