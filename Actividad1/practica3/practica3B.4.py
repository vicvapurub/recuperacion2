'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 08/01/2024 
ProblemaD: Ayuda a una tienda

'''
#capturar el monto de la compra y almacenarla en una variable
monto_compra = float(input())

#Comprobar en que rango se encuentra el monto de compra y calcular el descuento
if monto_compra > 15000:
    total = monto_compra-(monto_compra*0.25)
    print(total)
elif monto_compra <= 15000 and monto_compra >= 7001:
    total = monto_compra-(monto_compra*0.18)
    print(total)
elif monto_compra <= 7000 and monto_compra >= 1001:
    total = monto_compra-(monto_compra*0.11)
    print(total)
elif monto_compra <= 1000 and monto_compra >= 500:
    total = monto_compra-(monto_compra*0.05)
    print(total)
else:
    print(monto_compra)
