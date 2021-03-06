import matplotlib.pyplot as mplt
import math

data1 = open("disney_plus_titles.csv", "r", encoding="utf8")
data = data1.read()
data1.close()

data1 = data.split("\n")
datos = data1.pop(0)
data = []

for i in data1:
    a = i.split(',')
    data.append(a)

data.pop(-1)

# funciones necesarias para crear la lista con todos los datos


def crear_listapop(lista, valor1, valor2):
    lista_pop = []
    for i in range(len(lista)):
        if valor1 <= i <= valor2:
            lista_pop.append(i + 1)
    return lista_pop


def crear_lista_datos_agrupados_en_comillas(lista, valor1, valor2):
    listax = []
    for i in range(len(lista)):
        if valor1 <= i <= valor2:
            a = lista[i]
            a = limpiar_comillas(a)
            listax.append(a)
    return listax


def popearx(lista, listapop):
    decontador = 0
    for i in listapop:
        lista.pop(i - decontador)
        decontador += 1


def limpiar_comillas(string):
    if string[0] == '\"':
        string = string[1:]
    if string[-1] == '\"':
        string = string[:-1]
    return(string)


def listar_comillas(lista):
    es_lista = False
    paso = False
    for i in range(len(lista)):
        if paso == False:
            if es_lista == False:
                contador_lista = 0
                contador_lista2 = 0

            if len(lista[i]) > 0:
                if lista[i][0] == '\"':
                    contador_lista = i
                    es_lista = True

                elif lista[i][-1] == '\"':
                    contador_lista2 = i
                    es_lista = False
                    listax = crear_lista_datos_agrupados_en_comillas(
                        lista, contador_lista, contador_lista2)
                    lista_pop = crear_listapop(
                        lista, contador_lista, contador_lista2)
                    lista.insert(contador_lista, listax)
                    popearx(lista, lista_pop)
                    paso = True


for j in range(len(data)):
    for i in range(11):
        listar_comillas(data[j])

datos = datos.split(",")

# hasta aca funciona y cree 2 listas, data es toda la informacion del dataset
# y datos dice a que se refiere cada dato de cada pelicula,
# ej: nombre, a??o de lanzamiento, etc...

peliculas = []
for i in data:
    if i[1] == 'Movie':
        peliculas.append(i)

a??os_agregados = []
a??os_agregados_i = []
for i in range(len(peliculas)):
    if len(peliculas[i][6]) > 0:
        a??o_agregado = peliculas[i][6][1]
        a??o_agregado = int(a??o_agregado[1:])
        a??os_agregados.append(a??o_agregado)
        a??os_agregados_i.append(i)

a??os_creados = []
for i in range(len(peliculas)):
    a??os_creado = int(peliculas[i][7])
    if i in a??os_agregados_i:
        a??os_creados.append(a??os_creado)

duracion_peliculas = []
for i in range(len(peliculas)):
    duracion = peliculas[i][9]
    duracion = int(duracion[:-4])
    if i in a??os_agregados_i:
        duracion_peliculas.append(duracion)

diferencia_a??os = []
for i in range(len(a??os_agregados)):
    diferencia_a??os.append(a??os_agregados[i] - a??os_creados[i])

diferencia_duracion = []
for i in range(len(diferencia_a??os)):
    diferencia_duracion.append([diferencia_a??os[i], duracion_peliculas[i]])


def por_a??os(list):
    return(list[0])


diferencia_duracion.sort(key=por_a??os)

cantidad_intervalos = 1+3.22*math.log(len(diferencia_a??os), 10)

intervalos = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
promedio_duracion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, 12):
    suma_intervalo = 0
    cantidad_intervalo = 0
    for j in diferencia_duracion:
        if intervalos[i - 1] <= j[0] < intervalos[i]:
            suma_intervalo += j[1]
            cantidad_intervalo += 1
    promedio_duracion[i - 1] = suma_intervalo/cantidad_intervalo

intervalos_a??os = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]


fig, ax = mplt.subplots()
ax.plot(intervalos_a??os, promedio_duracion)
mplt.show()
