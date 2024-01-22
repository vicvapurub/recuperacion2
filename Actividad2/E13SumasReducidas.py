'''
| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 19/01/2024
| Ejercicio13: Las sumas resucidas

'''
# funcion para calcular el sumando reducido
def sumando_reducido(num):
    if num < 10:
        return num - 1
    else:
        producto_digitos = 1
        while num > 0:
            producto_digitos *= num % 10
            num //= 10
        return producto_digitos

# entrada de datos
precios = list(map(int, input().split()))

# verificacion de limites y cálculo del descuento total
if 1 <= len(precios) <= 1000 and all(1 <= precio <= 1000 for precio in precios):
    descuento_total = sum(sumando_reducido(precio) for precio in precios)
    print(descuento_total)



