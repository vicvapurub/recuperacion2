'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 15/01/2024 
Problema B: Los números de Zaido

'''
def factorizar(n):
    factores = []
    # Encontrar factores primos
    while n % 2 == 0:
        factores.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n = n // i
    if n > 2:
        factores.append(n)
    return factores

def suma_factores_potencias(n):
    factores = factorizar(n)
    suma = 0
    for factor in set(factores):
        exponente = factores.count(factor)
        suma += factor**exponente
    return suma

def verificar_wilson_zaido(n):
    suma = suma_factores_potencias(n)
    if n % suma == 0:
        print("A wilson Zaido")
    else:
        print("Chaaale")

# Capturar el número n
numero_n = int(input())

# Verificar y mostrar el resultado
verificar_wilson_zaido(numero_n)











