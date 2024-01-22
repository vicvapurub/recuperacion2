'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 15/01/2024 
Problema E: Los números de Missa

'''
#Función para calcular el número de Missa
def grado_numero_missa(numero):
    n = 1
    while True:
        suma_digitos = sum(int(digit) ** n for digit in str(numero))
        if suma_digitos == numero:
            return n
        elif suma_digitos > numero:
            return -1
        n += 1
#Capturar el dato la almacenamos en un variable
numero = int(input())

#Mandamos a llamar la función con la variable creado previamente
resultado = grado_numero_missa(numero)
#Imprimimos el resultado
print(resultado)