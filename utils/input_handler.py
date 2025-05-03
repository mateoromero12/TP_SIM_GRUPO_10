from typing import List
from utils.random_generators import (
    generate_uniform_distribution,
    generate_exponential_distribution,
    generate_normal_distribution,
)


def get_number_of_classes() -> int:
    """
    Obtiene el número de clases del usuario.

    Returns:
        Número de clases seleccionado por el usuario.
    """
    class_options = {1: 10, 2: 15, 3: 20, 4: 25}

    print('Elige el número de clases:')
    for key, value in class_options.items():
        print(f'{key}: {value}')

    choice = int(input('Ingresa tu elección: '))
    while choice not in class_options.keys():
        print('Elección inválida. Por favor, elige nuevamente.')
        choice = int(input('Ingresa tu elección: '))

    return class_options[choice]


def get_random_variables(precision: int) -> List[float]:
    """
    Obtiene las variables aleatorias según la distribución seleccionada.

    Args:
        precision: Precisión decimal para redondear las variables generadas.

    Returns:
        Lista de variables aleatorias generadas.
    """
    max_sample_size = 1000000

    sample_size = int(input('Ingresa el tamaño de la muestra: '))
    while sample_size <= 0 or sample_size > max_sample_size:
        print(f'El tamaño de la muestra debe estar entre 1 y {max_sample_size}')
        sample_size = int(input('Ingresa el tamaño de la muestra: '))

    distribution_choice = int(input('Elige la distribución (1: Uniforme, 2: Exponencial, 3: Normal): '))
    while distribution_choice not in [1, 2, 3]:
        print('Elección de distribución inválida. Por favor, elige 1, 2 o 3.')
        distribution_choice = int(input('Elige la distribución (1: Uniforme, 2: Exponencial, 3: Normal): '))

    if distribution_choice == 1:
        return generate_uniform_distribution(sample_size, precision)
    elif distribution_choice == 2:
        return generate_exponential_distribution(sample_size, precision)
    elif distribution_choice == 3:
        return generate_normal_distribution(sample_size, precision)