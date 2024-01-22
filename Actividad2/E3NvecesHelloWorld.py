'''

| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 16/01/2024
| Ejercicio3: N veces Hello world repetidos

'''
#funcion que imprime los "Hello World"
def imprimir_hello_world(n):
    for i in range(1, n + 1):
        print(f"{i} {'hello world ' * i}")
#Captura el numero entero lo guarda en una variable 
n = int(input())
#Verifica si el número capturado es un unmero entero mayor a 0
if n > 0:
    imprimir_hello_world(n)

