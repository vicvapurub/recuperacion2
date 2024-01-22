'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 15/01/2024 
Problema D: Los Números de Missa (Fácil)

'''
def es_numero_missa(numero, potencia):
    suma_digitos_potencia = sum(int(digito) ** potencia for digito in str(numero))
    return suma_digitos_potencia == numero
    
entrada = input()
n, k = map(int, entrada.split())

if es_numero_missa(n, k):
    print("Simón Missa")
else:
    print("Nelpas mijo")




