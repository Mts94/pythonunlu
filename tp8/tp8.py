""" 1. Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
para detenerse, debe mostrar el mensaje “--- TERMINADO ---”. """

# def ingreso_palabras():
#     #funcion que pide al usuario ingresar paralabrass para mostrar en
#     # pantalla hasta que ingrese la pabara 'parar para detener la ejecucion
#     palabra = ""
#     while(palabra != 'parar'):
#         palabra = input('Bienvenido, ingrese palabras: ')
#         print(palabra)
#         print(" ")
#         print('Para deterse ingrese la palabra: parar')
#         print('   ')

#         if(palabra == 'parar' or palabra == 'PARAR'):
#               print('---TERMINADO---')

#     return palabra

# ingreso_palabras()


""" 2. Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
cargar. Una vez ingresadas las notas, el programa debe informar la nota
promedio (tenga cuidado de no incluir al -1 dentro del promedio). """


def promedio_parciales():
    suma_notas = 0
    cantidad_notas = 0
    # Pedimos que se ingresen las notas
    nota = float(input('Ingrese la nota del parcial: '))
    while nota != -1:
        suma_notas += nota

        cantidad_notas += 1

        nota = float(input('Ingrese nota de parcial: '))

        # se calculan prmedio de las notas

    if cantidad_notas > 0:
        promedio_notas = suma_notas / cantidad_notas
        print(f'El promedio de las notas es {promedio_notas:.2f}')

    else:
        print('No se ingresaron notas de parciales.')


promedio_parciales()

""" Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
programa debe ser capaz de solicitarle al usuario que reingrese el número
cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
vez que detecte un error de validación, informele al usuario cuál fue el error, con
los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”. """


def leer_numeros():
    numero = input('Ingresee un dato: ')
    while (numero.isalpha()):
        print('El dato ingresado no es númerico')
        numero = input('Ingrese un dato: ')

    numero = int(numero)

    if (numero < 0 or numero > 100):
        print('El valor ingresado esta fuera del rango perimitido.')
    else:
        print(f'{numero}, es válido. Gracias!')

    return numero


print(leer_numeros())
