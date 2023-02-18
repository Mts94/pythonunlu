n_entero = int(input('Ingrese un numero entero: '))

print(f'El valor absoluto de {n_entero} es {abs(n_entero)}')


nombre = str(input('Ingrese su nombre: ' ))

print(f'El nombre {nombre}, tiene {len(nombre)} letras')


base =float(input('Ingrese un valor para base: '))
exp = float(input('Ingrese el valor exponente: '))
resultado = pow(base, exp)

print(f'El número {base} elevado al {exp} da como resultado {resultado}')


#Implemente un algoritmo en Python para calcular el perímetro de un
#rectángulo, conociendo su base y altura. Los datos se deben almacenar en
#variables, y el resultado se debe mostrar en pantalla.
#perímetro = 2 * (base + altura)

baseR = float(input('Ingrese medida de un lado del rectangulo: ') )

altura = float(input('Ingrese medida de otro lado del rectangulo: '))

perimetro = 2 * (baseR + altura)

print(f'El perimetro del rectangulo que tiene como base {baseR} y altura {altura} es de {perimetro}')
 
 
#Implemente un algoritmo en Python para calcular el área de un rectángulo,
#conociendo su base y altura. Los datos se deben almacenar en variables, y el
#resultado se debe mostrar en pantalla.
#área = base * altura

base_rect = float(input('Ingrese el valor de la base del rectangulo: ' ))
altura_h = float(input('Ingrese el valor de la altura del rectango: '))

area = base_rect * altura_h

print(f'El area del rectangulo ingresado es {area}')



#Implemente un algoritmo que intercambie los valores entre dos variables a y
#b cualesquiera. Por ejemplo, si a = 10 y b = 5, luego de ejecutar el algoritmo, la
#variable a debería ser igual 5, y la variable b debería ser igual a 10.

a = int(input('Ingrese un valor: '))
b = int(input('Ingrese segundo valor: '))
print(f'a:{a}')
print(f'b:{b}')

a, b = b, a 

print(f'Los nuevos valores son a: {a} y b: {b}.')


#Escriba un algoritmo que, conociendo las notas de los dos parciales de un
#alumno de la asignatura Introducción a la Programación, muestre en
#pantalla su promedio.

nombre_a = input('Ingrese nombre del alumno: ')

parc_1 = float(input('Cual es la calificación del primer parcial? : '))
parc_2 = float(input('Cual es la calificación del segundo parcial? : '))

promedio = (parc_1 + parc_2) / 2


print(f'El alumno {nombre_a} tiene un promedio de {promedio}')


#Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
#ahorrada en su cuenta (almacenando ese monto en una variable), muestre
#en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
#$14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
#formato:
#Usted tiene $XXX pesos argentinos, los cuales se convierten en:
#- U$XXX dólares.
#- R$XXX reales.
#- €XXX euros.#

pesos = float(input('que cantidad de pesos usted tiene ahorrados?: '))
dolares = pesos / 80.5
reales = pesos / 14.1
euros = pesos / 69.5

print(f'Usted tiene ${pesos} pesos argentinos, los cuales se convierten en: ')
print(f'-U${round(dolares, 2)} dólares.')
print(f'-R${round(reales,2)} reales')
print(f'-€{round(euros,2)} euros')