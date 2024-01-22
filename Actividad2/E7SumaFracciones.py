'''

| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 17/01/2024
| Ejercicio7: Suma de fracciones simple

'''

# Obtener los numeradores y denominadores de las fracciones
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Verificar los límites
if 1 <= a <= 20 and 1 <= b <= 20 and 1 <= c <= 20 and 1 <= d <= 20:
    # Calcular la suma de las fracciones
    numerador_suma = a * d + c * b
    denominador_suma = b * d    

    # Mostrar el resultado en el formato especificado
    print(f"{a}/{b}+{c}/{d}={numerador_suma}/{denominador_suma}")

