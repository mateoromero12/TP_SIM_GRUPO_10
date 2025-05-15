from typing import List, Tuple

<<<<<<< HEAD

=======
>>>>>>> origin/mateo
def calculate_intervals_and_frequencies(random_variables: List[float], num_classes: int) -> Tuple[List[Tuple[float, float]], List[int]]:
    """
    Calcula los intervalos y las frecuencias de las variables aleatorias generadas.

    Args:
        random_variables: Lista de variables aleatorias generadas.
        num_classes: Número de clases o intervalos.

    Returns:
        Una tupla que contiene:
<<<<<<< HEAD
        - intervals: Lista de tuplas que representan los límites de cada intervalo.
=======
        - intervals: Lista de tuplas que representan los límites de cada intervalo (con 4 decimales).
>>>>>>> origin/mateo
        - frequency_counts: Lista de frecuencias para cada intervalo.
    """
    min_value = min(random_variables)
    max_value = max(random_variables)
    interval_size = (max_value - min_value) / num_classes

<<<<<<< HEAD
    # Crear los intervalos
    intervals = [
        (min_value + i * interval_size, min_value + (i + 1) * interval_size)
=======
    # Crear los intervalos redondeando a 4 decimales
    intervals = [
        (
            round(min_value + i * interval_size, 4),
            round(min_value + (i + 1) * interval_size, 4)
        )
>>>>>>> origin/mateo
        for i in range(num_classes)
    ]

    # Inicializar las frecuencias
    frequency_counts = [0] * num_classes

    # Asignar cada variable al intervalo correspondiente
    for number in random_variables:
        index = int((number - min_value) / interval_size)
        if index == num_classes: 
            index -= 1
        frequency_counts[index] += 1

<<<<<<< HEAD
    return intervals, frequency_counts
=======
    return intervals, frequency_counts
>>>>>>> origin/mateo
