'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 15/01/2024 
Problema B: Velocidad Horizontal de un avión

'''
import math

def calcular_velocidad_promedio(velocidad_viento, angulo_ataque, direccion_avion):
    # Si la dirección del avión es 0 (izquierda), ajustar el ángulo
    if not direccion_avion:
        angulo_ataque = 180 - angulo_ataque

    # Convertir el ángulo a radianes
    angulo_radianes = math.radians(angulo_ataque)

    # Calcular la velocidad promedio considerando el ángulo
    velocidad = velocidad_viento * math.cos(angulo_radianes)

    return velocidad

def main():
    sets = input().strip().split()

    velocidades = []

    for set_parametros in sets:
        parametros = list(map(float, set_parametros.split(',')))

        velocidad = calcular_velocidad_promedio(*parametros)

        velocidades.append(velocidad)

    # Calcular la velocidad promedio y redondear hacia abajo
    velocidad_promedio = math.floor(math.fsum(velocidades) / len(velocidades))

    print(velocidad_promedio)

if __name__ == "__main__":
    main()
