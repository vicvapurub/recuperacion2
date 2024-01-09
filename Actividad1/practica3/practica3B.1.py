'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 08/01/2024 
ProblemaA: Edades
'''
#capturar el numero de alumnos y guardarlo en una variable
numero_alumnos = int(input())

#con respecto al numero de alumnos verificar que se encuentren en el rango de (1 ,50)
if 1 <= numero_alumnos <=40:
    #captura las edades de los alumnos y los almacena en la lista si estan en el rango de (1 , 40)
    lista_edades = [int(x) for x in input().split() if 1 <= int(x) <=40]

    #crear un diccionario para poder hacer el conteo por edades
    contar_edades = {}

    #hace el conteo de las edades que se encuentran en la lista
    for edad in lista_edades:
        if edad in contar_edades:
            contar_edades[edad] += 1
        else:
            contar_edades[edad] = 1
    
    for edad, cantidad in sorted(contar_edades.items()):
        print(f"{edad} {cantidad}")





















