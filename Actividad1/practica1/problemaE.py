'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 07/01/2024 
ProblemaC: Dólares
'''
#capturar la cantidad de dolares y almacenarla en una variable
dolares = int(input())

#capturar el valor del dolar en pesos y almacenarla en un variable
valor_dolar = int(input())

#Restricciones para que no se realice la operacion si los valores capturados son negativos
if dolares >= 0 & valor_dolar >= 0:
    #Calculo de conversion de dólares a pesos
    total = dolares * valor_dolar
    #imprimir el resultado calculado
    print(total)



