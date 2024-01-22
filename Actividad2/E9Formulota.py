'''
| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 17/01/2024
| Ejercicio9: Formulota

'''
#capturar los valores de tipo float x,y,z en una variable 
x = float(input())
y = float(input())
z = float(input())
#aplicar limites para las variables de -100<=x,y,x<=100
if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
    #Calcular la formulota 
    resultado = (((x+y)/(2*x))+(((x**3)+(y**3))/((x**2)+(y**2))))/((x**2)+(y**2)+(z**2))
    #cambiar el resultado con 6 digitos
    resultado = round(resultado, 6)
    #Imprimir el resultado
    print(resultado)

