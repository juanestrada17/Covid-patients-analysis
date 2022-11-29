import pandas
from statistics import mean

data = pandas.read_csv("COVCOL.csv")

original_edad = data["Edad"].tolist()
lista_sexo = data["Sexo"].tolist()
lista_edad = data["Edad"].tolist()
lista_agnos = data["Unidad de medida de edad"].tolist()
lista_estado = data["Estado"].tolist()


estados = []
for index, unidad_edad in enumerate(lista_agnos):
    if unidad_edad == 1 and original_edad[index] > 18:
        estados.append(lista_estado[index])

sobrevivientes = [original_edad[i] for i, estado in enumerate(estados) if estado == "Leve"]


for index, unidad_edad in enumerate(lista_agnos):
    if unidad_edad == 2 and lista_edad[index] < 13:
        lista_edad[index] = 0
    elif unidad_edad == 3:
        lista_edad[index] = 0
    elif unidad_edad == 2 and lista_edad[index] < 13:
        lista_edad[index] = 1

categoria_edad = []

for x in lista_edad:
    if x <= 5:
        categoria_edad.append("Primera infancia")
    elif 6 <= x <= 11:
        categoria_edad.append("Infante")
    elif 12 <= x <= 17:
        categoria_edad.append("Adolescente")
    elif 18 <= x <= 59:
        categoria_edad.append("Adulto")
    else:
        categoria_edad.append("Persona mayor")

all_data = dict({"Sexo": lista_sexo, "Edad en agnos": lista_edad, "Concepto": categoria_edad})

all_info = pandas.DataFrame(all_data)
all_info.to_csv("analisis_covcol.csv", sep=";", index= False)

# from test import tester
# import csv

# """Inicio espacio para programar funciones propias"""
# # En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)


# """Fin espacio para programar funciones propias"""



def solucion():
    if 3 in lista_agnos:
        days = [i for i, unidad_edad in enumerate(lista_agnos) if unidad_edad == 3]
        menor_dias = min(days)
        age_youngest = original_edad[menor_dias]
        unit_youngest = 3
    elif 2 in lista_agnos:
        months = [i for i, unidad_edad in enumerate(lista_agnos) if unidad_edad == 2 and lista_edad[i] < 13]
        menor_meses = min(months)
        age_youngest = original_edad[menor_meses]
        unit_youngest = 2
    elif 1 in lista_agnos:
        years = [i for i, unidad_edad in enumerate(lista_agnos) if unidad_edad == 1]
        menor_agnos = min(years)
        age_youngest = original_edad[menor_agnos]
        unit_youngest = 1

    mean_alive_g = mean(sobrevivientes)

    return age_youngest, unit_youngest, mean_alive_g


"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED DESARROLLE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
print(solucion())
