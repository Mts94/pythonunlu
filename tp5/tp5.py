"""Cree una función que reciba dos números como parámetro, y muestre en
pantalla la suma aritmética de ambos. Invoque a la función con dos números
leídos desde teclado."""

def aritmetica(n1,n2):
    n1 = int(input('Ingrese el primer valor: '))
    n2 = int(input('Ingrese segundo valor: '))
    resultado = n1 + n2
    print(resultado)

z = aritmetica(0,0)

"""Modifique el script del ejercicio anterior para que la función retorne el resultado
en vez de mostrarlo. El programa debe seguir mostrando el resultado en
pantalla.
"""
def aritmetica(n1,n2):
    n1 = int(input('Ingrese el primer valor: '))
    n2 = int(input('Ingrese segundo valor: '))
    resultado = n1 + n2
    return resultado

z = aritmetica(0,0)
print(z)


"""
Cree una función que reciba un string como parámetro, y retorne la cantidad de
letras que posee. Luego, utilice la función para escribir un programa que solicite
ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
ese nombre."""

print('Bienvenido!')
print('**********************************')
def cantidad_letras (palabra):
    palabra = input('ingrese una palabra o frase : ')
    cantidad = len(palabra)
    return cantidad
 
c = cantidad_letras(0) 

print(f'La cantidad de letras que hay en tu palabra o frase es {c}')


"""Cree una función que reciba dos números como parámetro (base y exponente),
y retorne el resultado de elevar base a la potencia exponente.
"""

def potencia(base,exponente):
    base = int(input('Ingrese número base: '))
    exponente = int(input('Ingrese número exponente: '))
    resultado = base ** exponente
    print(resultado)
    return resultado

p = potencia(0,0)

"""
Cree una función que reciba un string como parámetro, y retorne el mismo
string, pero con todas las letras convertidas a mayúsculas."""

def trans_letras(palabra):
    palabra = input('Escriba texto en minuscula a transformar:')
    transformation = palabra.upper()
    return transformation

lts = trans_letras(0)

print(lts)
    
    
"""
 Modifique 
 la función del ejercicio anterior para que retorne dos versiones del
 string recibido como parámetro: primero la versión en minúsculas, y luego la
versión en mayúsculas.
 """   
 
def trans_letras2(palabra1,palabra2):
    palabra = input('Escriba texto :')
    transformation_upper = palabra.upper()
    tranformation_lower = palabra.lower()
    return transformation_upper, tranformation_lower


lts2 = trans_letras2(0,0)

print(lts2)

"""
Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
y retorne True si nombre1 tiene más letras que nombre2, o False en caso
contrario.
"""

def cantidad(nombre1, nombre2):
    nombre1 = input('Ingrese primer nombre: ')
    nombre2 = input('Ingrese segundo nombre: ')
    comparacion = len(nombre1) > len(nombre2)
    print(comparacion)
    return comparacion

l = cantidad(0,0)

 
 
"""
 Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
programa_principal.py, que ejecute el programa haciendo uso de la función
creada en el otro archivo.
"""

