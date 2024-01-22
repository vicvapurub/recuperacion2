'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 15/01/2024 
Problema A: Future Squads en Fornais Fácil

'''
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def calcular_squads_distintas(n):
    return factorial(n) // (factorial(4) * factorial(n - 4))

def generar_permutaciones(nombres, r):
    if r == 0:
        yield []
    else:
        for i, nombre in enumerate(nombres):
            for perm in generar_permutaciones(nombres[i + 1:], r - 1):
                yield [nombre] + perm

def imprimir_squads_posibles(nombres):
    # Ignorar el nombre "Ricardo"
    nombres = [nombre for nombre in nombres if nombre not in ["Ricardo", "Mirón"]]
    # Obtener el número de miembros después de ignorar "Ricardo"
    num_miembros = len(nombres)

    # Verificar si hay exactamente cuatro miembros
    if num_miembros == 4:
        print("Como simplemente hay 4 personas, sólo hay una manera de organizar el squad.")
    else:
        # Generar y mostrar los squads posibles de forma iterativa
        squads_posibles = generar_permutaciones(nombres, 4)
        for i, squad in enumerate(squads_posibles, 1):
            print(f"{i}.- {' '.join(squad)}")

# Capturar la serie de nombres
nombres = input().split()

# Imprimir todas las combinaciones posibles
imprimir_squads_posibles(nombres)


