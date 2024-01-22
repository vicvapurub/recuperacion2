'''

| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 17/01/2024
| Ejercicio8: Producto punto sin arreglos

'''
def producto_punto(n, vector_a, vector_b):
    
    resultado = sum(a * b for a, b in zip(vector_a, vector_b))
    return resultado

# Entrada de datos
n = int(input())

# solicitar componentes de manera alternada
componentes = []
for i in range(n):
    componente_a = float(input())
    componente_b = float(input())
    componentes.extend([componente_a, componente_b])

# Dividir componentes en vectores a y b
vector_a = componentes[::2]
vector_b = componentes[1::2]

# calculo y salida del resultado
resultado = int(producto_punto(n, vector_a, vector_b))
    
print(resultado)









