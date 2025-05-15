from typing import List, Tuple
from utils.generadores import (
    generar_uniforme,
    generar_exponencial,
    generar_normal,
)

def obtener_cantidad_clases() -> int:
    opciones_clases = {1: 10, 2: 15, 3: 20, 4: 25}

    print('Elige el número de intervalos:')
    for clave, valor in opciones_clases.items():
        print(f'{clave}: {valor}')

    eleccion = int(input('Ingresa tu elección: '))
    while eleccion not in opciones_clases.keys():
        print('Elección inválida. Por favor, elige nuevamente.')
        eleccion = int(input('Ingresa tu elección: '))

    return opciones_clases[eleccion]

def obtener_variables_aleatorias(precision: int) -> Tuple[List[float], int, Tuple[float, float]]:
    max_tamanio_muestra = 1000000

    tamanio_muestra = int(input('Ingresa el tamaño de la muestra: '))
    while tamanio_muestra <= 0 or tamanio_muestra > max_tamanio_muestra:
        print(f'El tamaño de la muestra debe estar entre 1 y {max_tamanio_muestra}')
        tamanio_muestra = int(input('Ingresa el tamaño de la muestra: '))

    eleccion_distribucion = int(input('Elige la distribución (1: Uniforme, 2: Exponencial, 3: Normal): '))
    while eleccion_distribucion not in [1, 2, 3]:
        print('Elección de distribución inválida. Por favor, elige 1, 2 o 3.')
        eleccion_distribucion = int(input('Elige la distribución (1: Uniforme, 2: Exponencial, 3: Normal): '))

    if eleccion_distribucion == 1:
        a = float(input('Ingresa el límite inferior (a): '))
        b = float(input('Ingresa el límite superior (b): '))
        while a >= b:
            print('Límites inválidos. El límite inferior debe ser menor que el límite superior.')
            a = float(input('Ingresa el límite inferior (a): '))
            b = float(input('Ingresa el límite superior (b): '))
        muestra = generar_uniforme(tamanio_muestra, precision, a, b)
        return muestra, 1, (a, b)

    elif eleccion_distribucion == 2:
        lambda_val = float(input('Ingresa lambda (λ): '))
        while lambda_val <= 0:
            print('Lambda inválido. Lambda debe ser mayor que 0.')
            lambda_val = float(input('Ingresa lambda (λ): '))
        muestra = generar_exponencial(tamanio_muestra, precision, lambda_val)
        return muestra, 2, (lambda_val)

    elif eleccion_distribucion == 3:
        media = float(input('Ingresa la media (μ): '))
        desviacion = float(input('Ingresa la desviación estándar (σ): '))
        while desviacion <= 0:
            print('Desviación estándar inválida. Debe ser mayor que 0.')
            desviacion = float(input('Ingresa la desviación estándar (σ): '))
        muestra = generar_normal(tamanio_muestra, precision, media, desviacion)
        return muestra, 3, (media, desviacion)
