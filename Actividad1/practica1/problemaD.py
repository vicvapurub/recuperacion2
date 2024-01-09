'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 07/01/2024 
ProblemaC: Promedios
'''
#capturar las calificaciones de los alumnos
calificaciones = input()

#almacenar los valores obtenidos en una variable correspondiente
cal1, cal2, cal3, cal4, cal5 = map(int, calificaciones.split())

#calcular el promedio del alumno
promedio = (cal1 + cal2 + cal3 + cal4 + cal5)/5

#imprimir el resultado del promedio
print(int(promedio))