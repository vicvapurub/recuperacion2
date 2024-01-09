'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 08/01/2024 
ProblemaE: Intersección de intervalos

'''
#capturar los numeros y almcenarlos en una variable
a1, a2, b1, b2 = map(int, input().split())

#verificar los un número pertenece a ambos intervalo y imprimir una respuesta de 1 o 0
if a2 >= b1 and a1 <= b2:
    print(1)
else:
    print(0)