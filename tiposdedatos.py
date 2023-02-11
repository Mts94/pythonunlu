# Escribir un programa que muestre un mensaje de bienvenida y imprima la suma de los cuadrados de dos numeros enteros


"""print('Bienvenid@')
nombre = input('Por favor ingrese su nombre')
n1 = int(input("Por favor ingrese un número"))
n2 = int(input("Por favor ingrese un segundo número"))
suma = 0
suma = n1*n1 + n2 * n2
suma = suma
print('Hola ' + nombre + 'la suma de los numeros es: ' + str(suma))
print('Fin de calculo') 

#Escribir un prgrama que muestre en pantalla el resulatado de la siguente operacion aritmetica
(3+2 / 2*5)*(3+2 / 2*5)

print('Hola ')
operacion = (3+2 / 2-5)*(3+2 / 2-5)
print('El resultado de la operacion es: ' + str(operacion) )
"""

# Escribir un programa que pregunte al usuario por el numero de horas trabajado y el coste por hora Despues debe mostrar por pantalla lo que corresponda

# horas = input('Cuantas horas trabajo hoy? ')
# costo_horas = input('Cual es el costo por hora? ')

# pago_diario = float(horas) * float(costo_horas)

# print('Usted hoy gano: ' , str(pago_diario))

# Escribir un programa que sume los caudrados de dos enteros

# print('Bienvenido')

# suma = 0
# n1 = int(input('Igrese primer valor'))
# n2 =int( input('ingrese segundo valor'))

# suma = suma + n1*n1
# suma = suma + n2*n2

# print(suma)


print('Bienvenidos al convertidos de unidades de longitud')
print('**************************************************')
millas = 0
pies = 0
pulgadas = 0
metros = 0

millas = float(input('Ingrese cantidad de millas: '))
pies = float(input('Ingrese cantidad de pies: '))
pulgadas = float(input('Ingrese cantidad de pulgadas: '))

metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas

print('La logitud es de ', metros, 'metros')
