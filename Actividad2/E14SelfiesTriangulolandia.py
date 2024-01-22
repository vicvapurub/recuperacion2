'''
| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 20/04/2024
| Ejercicio14: Selfies en Triangulolandia

'''
import math

def calcular_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def mejor_altura(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        area = calcular_area(a, b, c)
        altura_a = 2 * area / a
        altura_b = 2 * area / b
        altura_c = 2 * area / c
        return max(altura_a, altura_b, altura_c)
    else:
        return None

a, b, c = map(float, input().split())
resultado = mejor_altura(a, b, c)
if resultado is not None:
    print(round(resultado, 5))
else:
    print("ERROR")

