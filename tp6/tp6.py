# Cree un script que le solicite al usuario ingresar un número por teclado, y
# luego le informe en pantalla si su número es mayor que 10; antes de finalizar
# e independientemente de lo que haya sucedido antes, el script mostrará un
# mensaje de despedida. Ejemplos de cómo debería verse la salida del script:
# Número mayor que 10:
# Tu número (N) es mayor que 10!
# Saludos!
# Número menor o igual que 10:
print('Bienvenid@!')
num = float(input('Ingrese un número: '))
saludo = 'Saludos!'

# if (num >= 10):
#     print(f'Tu número {num} es mayor que 10')

#     print(saludo)
# else:
#     print(saludo)


# Modifique el script anterior para que mantenga el funcionamiento, pero
# ahora, cuando el número no es mayor que 10, también se muestre un
# mensaje “Tu número (N) es menor o igual que 10!”.

if (num >= 10):
    print(f'Tu número {num} es mayor o igual a 10')
    print(saludo)
elif (num <= 10):
    print(f'Tu número {num} es menor o igual a 10')
else:
    print(saludo)
    
#     Cree un script que le solicite al usuario ingresar dos números por teclado, y
# luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
# de que los números sean iguales, y muestre un mensaje acorde.


ingreso1 = int(input('Ingrese primer número entero: '))
ingreso2 = int(input('Ingrese un segndo número entero: '))

if(ingreso1 > ingreso2):
    print(f'El número {ingreso1} es mayor que {ingreso2}')
elif(ingreso1 == ingreso2):
    print(f'Los números ingresados son iguales: {ingreso1}')
else:
    print(f'El número {ingreso1} es menor que {ingreso2}')


# Cree un script que le solicite al usuario ingresar un número por teclado, y le
# informe con un mensaje si su número es positivo, negativo, o 0.

numero_int = int(input('Ingrese número: '))

if(numero_int>0):
    print(f'El número {numero_int} es positivo.')
elif(numero_int == 0):
    print(f'El número {numero_int} es 0.')
else:
    print(f'El número {numero_int} es negativo.')
    
#     Cree un script que, dado un número de día de la semana ingresado por
# teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
# números y días de la semana es la siguiente:
# 1 = Domingo.
# 2 = Lunes.
# 3 = Martes.
# 4 = Miércoles.
# 5 = Jueves.
# 6 = Viernes.
# 7 = Sábado.

dia = int(input('Ingrese un dia de la semana del 1 al 7: '))

if(dia == 1):
    print('Domingo')
elif(dia == 2):
    print('Lunes')
elif(dia == 3):
    print('Martes')
elif(dia == 4):
    print('Miercoles')
elif(dia == 5):
    print('Jueves')
elif(dia == 6):
    print('Viernes')
elif(dia == 7):
    print('Sabado')
else:
    print('Numero de dia no válido.')