# Cree un script que le solicite al usuario ingresar un número por teclado, y
# luego le informe en pantalla si su número es mayor que 10; antes de finalizar
# e independientemente de lo que haya sucedido antes, el script mostrará un
# mensaje de despedida. Ejemplos de cómo debería verse la salida del script:
# Número mayor que 10:
# Tu número (N) es mayor que 10!
# Saludos!
# Número menor o igual que 10:
# Modifique el script anterior para que mantenga el funcionamiento, pero
# ahora, cuando el número no es mayor que 10, también se muestre un
# mensaje “Tu número (N) es menor o igual que 10!”.

print('Bienvenid@!')

num1 = int(input('Ingrese un número: '))
saludo = 'Saludos!'

def mayor_que(num1):
    if (num1 > 10):
        return f'Tu número {num1} es mayor 10 \n {saludo} '
        
    elif (num1 < 10):
        return f'Tu número {num1} es menor 10 \n {saludo}'
        
    elif (num1 == 10):
        return f'Tu número {num1} es igual a 10 \n {saludo}'
    else:
        return f'{saludo}'

    
print(mayor_que(num1))


#     Cree un script que le solicite al usuario ingresar dos números por teclado, y
# luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
# de que los números sean iguales, y muestre un mensaje acorde.



ingreso1 = int(input('Ingrese primer número entero: '))
ingreso2 = int(input('Ingrese un segndo número entero: '))

def comparar(ing1, ing2):
    if (ing1 > ing2):
        return f'El número {ing1} es mayor que {ing2}'
    elif (ing1 == ing2):
        return f'Los números ingresados son iguales: {ing1}'
    else:
        return f'El número {ing1} es menor que {ing2}'


print(comparar(ingreso1,ingreso2))

# Cree un script que le solicite al usuario ingresar un número por teclado, y le
# informe con un mensaje si su número es positivo, negativo, o 0.


numero_int = int(input('Ingrese número: '))

def pos_neg(numero):
    if (numero > 0):
        return f'El número {numero} es positivo.'
    elif (numero == 0):
        return f'El número {numero} es 0.'
    else:
        return f'El número {numero} es negativo.'


print(pos_neg(numero_int))

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

def dias_de_la_semana(dia):

    if (dia == 1):
        return 'Domingo'
    elif (dia == 2):
        return 'Lunes'
    elif (dia == 3):
        return 'Martes'
    elif (dia == 4):
        return 'Miercoles'
    elif (dia == 5):
        return 'Jueves'
    elif (dia == 6):
        return 'Viernes'
    elif (dia == 7):
        return 'Sabado'
    else:
        return 'Numero e dia no válido.'

print(dias_de_la_semana(dia))
# Cree un script que le solicite a un alumno de la asignatura Introducción a la
# Programación que ingrese las notas de sus dos parciales. Como resultado, se
# le debe informar al alumno su situación, junto con la nota promedio. Las
# reglas para saber la situación de un alumno son las siguientes:
# ● Para estar promovido (es decir, cursada aprobada y no requiere
# rendir final), el alumno debe haber aprobado ambos parciales y
# tener un promedio mayor o igual a 8.
# ● Para estar regular (cursada aprobada, pero debe rendir final), el
# alumno debe haber aprobado ambos parciales (nota mayor o igual
# a 4).
# ● Si el alumno no ha aprobado ambos parciales (es decir, tiene nota
# menor que 4 en alguno de ellos), entonces queda en condición de
# libre (es decir, puede rendir un final extendido o recursar).
print('Binvenidos a introducción a la programación.')
parcial1 = float(input('Ingrese la nota de su primer parcial: '))
parcial2 = float(input('Ingrese la nota de su segundo parcial: '))
promedio = (parcial1 + parcial2) / 2


def intro_prog(promedio, parcial1, parcial2):

    if (promedio >= 8):
        return f'Tu promedio es {promedio}, estas promovido no necesitas rendir un final.'
    
    elif (parcial1 >= 4 and parcial2 >= 4 and promedio < 8):
        return f'Tu promedio es {promedio}, debes presentar un final integrador.'
    else:(promedio <= 4)
    return f'Tu promedio es {promedio}, puedes presentar un final extendido o recursar la materia'


print(intro_prog(promedio, parcial1, parcial2))



# Cree un script que determine si un triángulo es isósceles, equilátero, o
# escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
# números, correspondientes a los tres lados del triángulo.
# equilátero = todos los lados iguales
# isósceles = dos lados iguales
# escaleno = todos los lados diferentes


lado1 = float(input('Ingrese primer lado de triangulo a evaluar: '))
lado2 = float(input('Ingrese segundo lado de triangulo a evaluar: '))
lado3 = float(input('Ingrese tercer lado de triangulo a evaluar: '))

def determinar_triangulo(a,b,c):
    if(a == b and b == c):
         return 'Tu triangulo es equilatero'
    elif(a != b and a != c and b != c):
        return 'Tu triagulo es escaleno.'
    else:
        return 'Tu triagulo es isoceles'
    
    
print(determinar_triangulo(lado1,lado2,lado3))



# Las estructuras alternativas pueden utilizarse para validar datos. Por
# ejemplo, si se intenta crear una función que tome dos enteros como
# parámetro y muestre el resultado de su división, puede ocurrir un error si el
# denominador es cero. Utilice la estructura alternativa para validar que el
# denominador no sea cero; en caso de serlo, la función deberá mostrar el
# mensaje “No se puede dividir por 0!” en lugar de intentar mostrar el
# resultado.
        
def division(f,denominador):
    if (denominador == 0):
        return 'El denominador no puede ser 0.'
    else:
        return f / denominador
    
    
print(division(45,5))
print(division(45,0))
    
    
#     Python ofrece algunas funciones built-in para facilitar la implementación de
# validaciones. A continuación se listan algunas de las más comunes:
# valor.isdigit()
# Retorna True si todos los caracteres de valor son numéricos, False en caso
# contrario.
# valor.isalpha()
# Retorna True si todos los caracteres de valor son alfabéticos (no
# numéricos), False en caso contrario.
# valor.isalnum()
# Retorna True si valor es una combinación alfanumérica (caracteres y
# números), False en caso contrario.
# Codifique una función que reciba un parámetro cualquiera proveniente del
# usuario del programa (que puede contener letras, números, o una combinación
# de ambas), e indique si el mismo es un número, una palabra, o un valor
# alfanumérico. Compruebe que su función resuelve el problema enviándole
# valores correspondientes a las tres posibilidades.


valor_cadena = str(input('Ingrese una cadena de tecto a evaluar: '))

def cadena_cualquiera(valor_cadena):
    if(valor_cadena.isdigit() == True):
        return f'Todos tus caracteres son númericos.'
    elif(valor_cadena.isalpha() == True):
        return f'Todos tus caracteres son alfabeticos.'
    elif(valor_cadena.isalnum() == True):
        return f'Tus caracteres son alfanumericos.'
       
print(cadena_cualquiera(valor_cadena))
      
        
     
x = int(input("Ingrese un número entre -10 y 10: "))

if (x>= -10 or x <=10):

    print("Número válido")

else:

    print("Número inválido")
