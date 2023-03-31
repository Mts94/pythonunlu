"""Cree un script para mostrar los primeros 100 números enteros positivos,
 comenzando desde el 1. """


def mostrar_positivos():
    for n in range(1, 101):
        print(n)


mostrar_positivos()

print("****************************************************************")
""" 
Modifique el script del ejercicio anterior para que se muestren sólo los números
pares. Para saber si un número es par, utilice el operador de módulo (%). """


def mostrar_pares():
    for n in range(1, 101):
        if (n % 2 == 0):
            print(n)


mostrar_pares()

print("**********************************************")

""" 
Cree un script para calcular el resultado de sumar los números desde el 75 al
150. """


def sumar_valores():
    suma = 0

    for i in range(75, 150+1):
        suma = suma+i
        print(suma)


sumar_valores()


print('****************************************')

"""      
Cree un script que le solicite al usuario ingresar un número entero, y muestre
en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
este ejercicio, pero recuerde que la función range no incluye al valor máximo
enviado como parámetro.
factorial de n = n! = 1 * 2 * 3 * ... * (n - 1) * n """


def factorial():
    n = int(input('Hola, ingrese un número entero: '))
    for i in range(1, n):
        n = n * i

    print(f'El factorial es {n}.')


factorial()


""" Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
uno, informarle si el mismo es positivo, negativo, o cero. """


def pos_neg():
    entero = 1
    if (entero > 0):
        return f'El número {entero}, es positivo'
    elif (entero == 0):
        return f'El número {entero}, es igual a 0.'
    else:
        return f'El número {entero}, es negativo'


def bucle_pregunta():
    for i in range(10):
        print(pos_neg())


bucle_pregunta()

print('************************************')


""" Cree un script que le solicite al usuario ingresar 10 números, y una vez
ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1. """

# con listas


def crear_lista():
    # se crea lisa vacia y se solicitan e ingresan datos para la creacion de la lista
    numeros = []
    for i in range(10):
        numeros.append(int(input('Ingrese un numero entero: ')))

    return numeros


m = crear_lista()

print(m)


def maximo_mum(m):
    # se obtiene valor maximo ingresado por usuario con la fun bull-it max
    return max(m)


maxi = maximo_mum(m)

print(f'El valor maximo ingresado es {maxi}')


def minimo(m):
    # se obtiene valor minio ingresado por usuario con funcion bull-it min
    return min(m)


minimo = minimo(m)
print(f'El valor minimo ingresado es {minimo}')


# sin listas
def maximo_numer():
    maximo = None
    posicion = None
    for i in range(1, 11):
        numero = int(input(f"Ingrese el número {i}: "))
        if maximo is None or numero > maximo:
            maximo = numero
        posicion = i

    return f'El mayor número ingresado es {maximo}, y lo ingresaste en la posición {posicion}.'


print(maximo_numer())


print('*****************************************')

""" Un cliente ha solicitado un programa que le permita ingresar los mililitros de
lluvia caídos diariamente en una semana, para que el programa le informe en
pantalla el promedio de precipitación de esa semana. El cliente también desea
saber cuál fue el día en que más llovió en la semana.
A modo ilustrativo, un reporte generado por el programa debería verse como
sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
El promedio de precipitaciones fue de XX mls. diarios.
El día de más precipitaciones fue el xxxxxx (nombre del día).
Tenga en cuenta que la numeración de los días de la semana comienza con el 1
para el día domingo.
Codifique el programa para dar solución a lo solicitado por el cliente. """


def dias_precipitaciones():
    # Pedimos al usuario que ingrese los mililitros de lluvia caídos diariamente durante una semana
    print("Ingrese los mililitros de lluvia caídos diariamente durante una semana:")


# Inicializamos las variables necesarias para realizar los cálculos
    suma_precipitaciones = 0
    dia_mas_lluvioso = 1
    mayor_precipitacion = 0

# Leemos los mililitros de lluvia caídos para cada día de la semana
    for dia in range(1, 8):
        precipitacion = int(input(f"Día {dia}: "))
        suma_precipitaciones += precipitacion
        if precipitacion > mayor_precipitacion:
            mayor_precipitacion = precipitacion
            dia_mas_lluvioso = dia

# Calculamos el promedio de precipitaciones y mostramos el resultado
    promedio_precipitaciones = suma_precipitaciones / 7
    
# Mostramos el día con mayor precipitación
    if dia_mas_lluvioso == 1:
        nombre_dia_mas_lluvioso = "Domingo"
    elif dia_mas_lluvioso == 2:
        nombre_dia_mas_lluvioso = "Lunes"
    elif dia_mas_lluvioso == 3:
        nombre_dia_mas_lluvioso = "Martes"
    elif dia_mas_lluvioso == 4:
        nombre_dia_mas_lluvioso = "Miércoles"
    elif dia_mas_lluvioso == 5:
        nombre_dia_mas_lluvioso = "Jueves"
    elif dia_mas_lluvioso == 6:
        nombre_dia_mas_lluvioso = "Viernes"
    else:
        nombre_dia_mas_lluvioso = "Sábado"

    return f'El promedio de precipitaciones fue de {promedio_precipitaciones:.2f} mls. diarios.El día de más precipitaciones fue el {nombre_dia_mas_lluvioso} .'
    
    
print(dias_precipitaciones())
