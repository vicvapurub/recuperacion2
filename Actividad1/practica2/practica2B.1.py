'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 08/01/2024 
ProblemaA: Bubu y las edades cluberas

'''
#Capturar los edades y guardaralas en una lista 
lista_edades = list(map(str, input().split()))

#Convertir la lista a conjunto para que se ordene y no se repita alguna edad
lista_edades = set(lista_edades)

#Volver a convertir de conjunto a lista
lista_conjunto = list(lista_edades)

#Ordenar la lista de mayor a menor
lista_resultado = sorted(lista_conjunto, reverse=True)

#Imprimir toda lista ordenada de mayor a menor
print(lista_resultado)










