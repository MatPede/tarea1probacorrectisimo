import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as mplt

data = pd.read_csv("disney_plus_titles.csv")
dataComedy= []
for i in data.iloc:
    if i["type"] == "Movie":
        if "Comedy" in i["listed_in"]:
            dataComedy.append(i)

dataFamily= []
for i in data.iloc:
    if i["type"] == "Movie":
        if "Family" in i["listed_in"]:
            dataFamily.append(i)

duracionesComedy = []
for i in dataComedy:
    duracionesComedy.append(i["duration"])

duracionesFamily = []
for i in dataFamily:
    duracionesFamily.append(i["duration"])

def sacar_espaciomin(list):
    list2 = []
    for i in list:
        list2.append(int(i[:-4]))
    return list2

duracionesComedy = sacar_espaciomin(duracionesComedy)
duracionesFamily = sacar_espaciomin(duracionesFamily)

duracionesComedy.sort()
duracionesFamily.sort()

mayorComedy = duracionesComedy[-1]
mayorFamily = duracionesFamily[-1]

cantidad_intervalos_Comedy = int(1+3.22*math.log(mayorComedy, 10)) + 1
cantidad_intervalos_Family = int(1+3.22*math.log(mayorFamily, 10)) + 1

intervalos_Comedy = []
for i in range(1,1 + cantidad_intervalos_Comedy):
    intervalos_Comedy.append(i * (int(mayorComedy/cantidad_intervalos_Comedy) + 1))

intervalos_Family = []
for i in range(1,1 + cantidad_intervalos_Family):
    intervalos_Family.append(i * (int(mayorFamily/cantidad_intervalos_Family) + 1))


intervalos_Comedy_0 = [0]
intervalos_Family_0 = [0]
for i in intervalos_Comedy:
    intervalos_Comedy_0.append(i)
for i in intervalos_Family:
    intervalos_Family_0.append(i)
datosComedy = [] 
datosFamily = [] 
for i in range(len(intervalos_Comedy)):
    datosComedy.append(0)

for i in range(len(intervalos_Family)):
    datosFamily.append(0)

for i in range(1, cantidad_intervalos_Comedy + 1):
    for j in duracionesComedy:
        if intervalos_Comedy_0[i - 1] <= j < intervalos_Comedy_0[i]:
            datosComedy[i - 1] += 1
for i in range(1, cantidad_intervalos_Family + 1):
    for j in duracionesFamily:
        if intervalos_Family_0[i - 1] <= j < intervalos_Family_0[i]:
            datosFamily[i - 1] += 1

print("intervalo / Duracion")
for i in range(5):
    print(f"{intervalos_Comedy[i]}          {datosComedy[i]} ")
for i in range(3):
    print(f"{intervalos_Comedy[5 + i]}         {datosComedy[5 + i]} ")
for i in range(5):
    print(" ")
print("intervalo / Duracion")
for i in range(5):
    print(f"{intervalos_Family[i]}          {datosFamily[i]} ")
for i in range(3):
    print(f"{intervalos_Family[5 + i]}         {datosFamily[5 + i]} ")


print(datosComedy)

barras = np.arange(len(intervalos_Comedy))
anchura = 0.3

mplt.bar(barras, datosComedy,width=anchura)
mplt.xticks(barras + anchura,intervalos_Comedy)
mplt.ylabel("Cantidad en este intervalo de tiempo")
mplt.show()



