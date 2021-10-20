import pandas as pd
import matplotlib.pyplot as mplt
import numpy as np

data = pd.read_csv("disney_plus_titles.csv")
datatvg = []
for i in data.iloc:
    if i["type"] == "Movie":
        if i["rating"] == "TV-G":
            datatvg.append(i)

datatvpg = []
for i in data.iloc:
    if i["type"] == "Movie":
        if i["rating"] == "TV-PG":
            datatvpg.append(i)

duracionestvg = []
for i in datatvg:
    duracionestvg.append([i["duration"], i["release_year"]])

duracionestvpg = []
for i in datatvpg:
    duracionestvpg.append([i["duration"], i["release_year"]])

def sacar_espaciomin(list):
    list2 = []
    for i in list:
        list2.append([int(i[0][:-4]),int(i[1])])
    return list2

duracionestvg = sacar_espaciomin(duracionestvg)
duracionestvpg = sacar_espaciomin(duracionestvpg)

mayortvg = 182
mayortvpg = 148

def por_año_de_lanzamiento(list):
    return list[1]

duracionestvg.sort(key = por_año_de_lanzamiento)
duracionestvpg.sort(key = por_año_de_lanzamiento)

def solo_duracion(list):
    list2 = []
    for i in range(len(list)):
        list2.append(list[i][0])
    return list2

duracionestvg = solo_duracion(duracionestvg)
duracionestvpg = solo_duracion(duracionestvpg)

lista_indicestvg = []
for i in range(len(duracionestvg)):
    lista_indicestvg.append(i+1)

lista_indicestvpg = []
for i in range(len(duracionestvpg)):
    lista_indicestvpg.append(i+1)

fig, ax = mplt.subplots()
ax.scatter(lista_indicestvg, duracionestvg)
mplt.show()

fig, ax = mplt.subplots()
ax.scatter(lista_indicestvpg, duracionestvpg)
mplt.show()

print(f"Promedio tvg = {np.mean(duracionestvg)}")
print(f"Varianza tvg = {np.var(duracionestvg)}")
print(f"Mediana tvg = {np.median(duracionestvg)}")
print(f"Promedio tvpg = {np.mean(duracionestvpg)}")
print(f"Varianza tvpg = {np.var(duracionestvpg)}")
print(f"Mediana tvpg = {np.median(duracionestvpg)}")