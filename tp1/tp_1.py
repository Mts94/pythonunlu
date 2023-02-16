from datetime import date

def calcular_anios(fecha_nac):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nac.year
    
    return resultado

fecha = date(1994,10,27)
edad = calcular_anios(fecha)

print(f'la edad es: {edad}')