'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 07/01/2024 
ProblemaB: Chicharronera
'''
#captura los valores para resolver la ecuación cuadrantica
valores = input()
#guardar los datos obtenidos en su variable correspondiente
a, b, c = map(int, valores.split())

#operacion de la formula general para las ecuaciones cuadranticas
z = (b**2-4*a*c)**0.5

x1 = (-b+z)/(2*a)
x2 = (-b-z)/(2*a)

#salida de los resultados calculados anteriormente
print(x1," ", x2)
