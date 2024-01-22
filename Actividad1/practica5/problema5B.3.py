'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 15/01/2024 
Problema C: Bubu y los panas capicúas

'''
#función para regresar el número inverso
def capicua(n):
    str_numero = str(n)
    return str_numero == str_numero[::-1]

#verificar si el numero es capucua sino sumarle su inverso
def hacer_capicua(n):
    while not capicua(n):
        reverso = int(str(n)[::-1])
        n += reverso
    return n

#capturar número entero positivo
n = int(input())

#guardar el dato anteriormente capturado en una variable e inicializar la función hacer_capicua
capicua = hacer_capicua(n)
#imprimir numero capicua
print(capicua)



