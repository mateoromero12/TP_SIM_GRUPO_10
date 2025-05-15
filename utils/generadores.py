import random
import numpy as np
from math import pi
from typing import List, Tuple


def generar_uniforme(tamanio_muestra: int, precision: int, a: float, b: float) -> List[float]:
    """
    Genera variables aleatorias con distribución uniforme en el intervalo [a, b).
    """
    return [round(a + random.random() * (b - a), precision) for _ in range(tamanio_muestra)]


def generar_exponencial(tamanio_muestra: int, precision: int, lambda_val: float) -> List[float]:
    """
    Genera números aleatorios con distribución exponencial usando lambda.
    """
    return [round(-np.log(1 - random.random()) / lambda_val, precision) for _ in range(tamanio_muestra)]


def generar_normal(tamanio_muestra: int, precision: int, media: float, desviacion: float) -> List[float]:
    """
    Genera números aleatorios con distribución normal (media y desviación estándar).
    Usa el método de Box-Muller.
    """
    numeros_aleatorios = []
    for _ in range((tamanio_muestra + 1) // 2):
        n1, n2 = generar_normal_box_muller(media, desviacion)
        numeros_aleatorios.extend([round(n1, precision), round(n2, precision)])
        if len(numeros_aleatorios) >= tamanio_muestra:
            break
    return numeros_aleatorios[:tamanio_muestra]


def generar_normal_box_muller(media: float, desviacion: float) -> Tuple[float, float]:
    """
    Genera dos números aleatorios con distribución normal usando el método Box-Muller.
    """
    u1 = random.random()
    u2 = random.random()
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * pi * u2)
    z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * pi * u2)
    return media + z1 * desviacion, media + z2 * desviacion
