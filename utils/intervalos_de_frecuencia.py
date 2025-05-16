from typing import List, Tuple


def calcular_intervalos_y_frecuencias(
    variables_aleatorias: List[float], cantidad_clases: int
) -> Tuple[List[Tuple[float, float]], List[int]]:
    """
    Calcula los intervalos y las frecuencias de las variables aleatorias generadas.

    Args:
        variables_aleatorias: Lista de variables aleatorias generadas.
        cantidad_clases: Número de clases o intervalos.

    Returns:
        Una tupla que contiene:
        - intervalos: Lista de tuplas que representan los límites de cada intervalo (con 4 decimales).
        - frecuencias: Lista de frecuencias para cada intervalo.
    """
    valor_min = min(variables_aleatorias)
    valor_max = max(variables_aleatorias)
    tamanio_intervalo = (valor_max - valor_min) / cantidad_clases

    # Crear los intervalos redondeando a 4 decimales
    intervalos = [
        (
            round(valor_min + i * tamanio_intervalo, 4),
            round(valor_min + (i + 1) * tamanio_intervalo, 4)
        )
        for i in range(cantidad_clases)
    ]

    # Inicializar las frecuencias
    frecuencias = [0] * cantidad_clases

    # Asignar cada variable al intervalo correspondiente
    for numero in variables_aleatorias:
        indice = int((numero - valor_min) / tamanio_intervalo)
        if indice == cantidad_clases:
            indice -= 1
        frecuencias[indice] += 1

    return intervalos, frecuencias
