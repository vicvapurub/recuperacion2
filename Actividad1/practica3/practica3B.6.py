'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 08/01/2024 
ProblemaF: Multiplos dentro de un intervalo

'''
#capturar los dos datos y almacenarlos en una variable
a, b = map(int, input().split())

#imprimir los numeros entre "a" y "b" que sean multiplos de "a"
for i in range(a, b+1, a):
    print(i, end=" ")