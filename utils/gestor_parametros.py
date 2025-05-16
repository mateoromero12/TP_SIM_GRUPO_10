from typing import List, Tuple
from utils.generadores import (
    generar_uniforme,
    generar_exponencial,
    generar_normal,
)
from utils.validador_input import pedir_float, pedir_int


def obtener_cantidad_clases() -> int:
    """
    Permite al usuario seleccionar la cantidad de intervalos (clases) para un histograma.

    Returns:
        int: Cantidad de clases seleccionada por el usuario.
    """
    opciones_clases = {1: 10, 2: 15, 3: 20, 4: 25}
    print('Elige el número de intervalos:')
    for clave, valor in opciones_clases.items():
        print(f'{clave}: {valor}')
    eleccion = pedir_int(
        'Ingresa tu elección: ',
        condicion=lambda x: x in opciones_clases,
        mensaje_error='Elección inválida. Por favor, elige nuevamente.'
    )
    return opciones_clases[eleccion]


def obtener_variables_aleatorias(
    precision: int
) -> Tuple[List[float], int, Tuple[float, float]]:
    """
    Solicita al usuario los parámetros para generar una muestra de variables aleatorias
    según una distribución seleccionada (Uniforme, Exponencial o Normal).

    Args:
        precision (int): Cantidad de decimales para los números generados.

    Returns:
        Tuple[List[float], int, Tuple[float, float]]:
            - Lista de variables aleatorias generadas.
            - Código de la distribución seleccionada (1: Uniforme, 2: Exponencial, 3: Normal).
            - Tupla con los parámetros usados para la generación.
    """
    max_tamanio_muestra = 1000000
    tamanio_muestra = pedir_int(
        'Ingresa el tamaño de la muestra: ',
        condicion=lambda x: 0 < x <= max_tamanio_muestra,
        mensaje_error=(
            f'El tamaño de la muestra debe estar entre 1 y {max_tamanio_muestra}'
        )
    )
    print('Elige la distribución (1: Uniforme, 2: Exponencial, 3: Normal): ')
    eleccion_distribucion = pedir_int(
        '',
        condicion=lambda x: x in [1, 2, 3],
        mensaje_error='Elección de distribución inválida. Por favor, elige 1, 2 o 3.'
    )

    if eleccion_distribucion == 1:
        a = pedir_float('Ingresa el límite inferior (a): ')
        b = pedir_float(
            'Ingresa el límite superior (b): ',
            condicion=lambda x: x > a,
            mensaje_error='El límite superior debe ser mayor que el inferior.'
        )
        muestra = generar_uniforme(tamanio_muestra, precision, a, b)
        return muestra, 1, (a, b)
    elif eleccion_distribucion == 2:
        lambda_val = pedir_float(
            'Ingresa lambda (λ): ',
            condicion=lambda x: x > 0,
            mensaje_error='Lambda debe ser mayor que 0.'
        )
        muestra = generar_exponencial(tamanio_muestra, precision, lambda_val)
        return muestra, 2, (lambda_val,)
    elif eleccion_distribucion == 3:
        media = pedir_float('Ingresa la media (μ): ')
        desviacion = pedir_float(
            'Ingresa la desviación estándar (σ): ',
            condicion=lambda x: x > 0,
            mensaje_error='Desviación estándar debe ser mayor que 0.'
        )
        muestra = generar_normal(tamanio_muestra, precision, media, desviacion)
        return muestra, 3, (media, desviacion)
