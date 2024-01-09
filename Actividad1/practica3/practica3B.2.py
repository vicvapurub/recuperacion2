'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 08/01/2024 
ProblemaB: Par, impar o nulo

'''
#capturar un numero entero y almacenarlo en una variable
numero = int(input())

#condicion para determinar de que tipo es el numero
if numero == 0:
    print("Nulo")
elif numero%2 == 0:
    print("Par")
else:
    print("Impar")


