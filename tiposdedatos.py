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

#Escribe un programa que muestre los numero enteros desde 1 hasta n

n = int(input('Ingrese un numero entero'))
suma = n*(n + 1) / 2

print('Los números enteros entre 1 y n son ', suma)


#Escriba un programa que caule su imc pidiendole al usuario su peso y altura en mts
print('Bienvenido!')
nombre = input('Ingresa tu nombre: ')
peso = float(input('Ingresa tu peso corporal en Kg: ' ))

altura = float(input('Ingresa tu altura en mts: '))

imc = peso / altura**2

resultado = f"Hola , {nombre} , tu indice de masa corporal es ,{(round(imc, 2))}"
print(resultado)
