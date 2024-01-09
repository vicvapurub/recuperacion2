'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 08/01/2024 
ProblemaC: Palabra palindroma

'''
#Almacenar la palabra en un variable
p = input()

#usar el slicing para verificar si la palabra es palindroma
if p == p[::-1]:
    print("SI")
else:
    print("NO")


