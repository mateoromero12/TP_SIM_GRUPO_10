<<<<<<< HEAD
from typing import List
=======
from typing import List, Tuple
>>>>>>> origin/mateo
from utils.random_generators import (
    generate_uniform_distribution,
    generate_exponential_distribution,
    generate_normal_distribution,
)


def get_number_of_classes() -> int:
<<<<<<< HEAD
    """
    Obtiene el número de clases del usuario.

    Returns:
        Número de clases seleccionado por el usuario.
    """
    class_options = {1: 10, 2: 15, 3: 20, 4: 25}

    print('Elige el número de clases:')
=======
    class_options = {1: 10, 2: 15, 3: 20, 4: 25}

    print('Elige el número de intervalos:')
>>>>>>> origin/mateo
    for key, value in class_options.items():
        print(f'{key}: {value}')

    choice = int(input('Ingresa tu elección: '))
    while choice not in class_options.keys():
        print('Elección inválida. Por favor, elige nuevamente.')
        choice = int(input('Ingresa tu elección: '))

    return class_options[choice]


<<<<<<< HEAD
def get_random_variables(precision: int) -> List[float]:
    """
    Obtiene las variables aleatorias según la distribución seleccionada.

    Args:
        precision: Precisión decimal para redondear las variables generadas.

    Returns:
        Lista de variables aleatorias generadas.
    """
=======
def get_random_variables(precision: int) -> Tuple[List[float], int, Tuple[float, float]]:
>>>>>>> origin/mateo
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
<<<<<<< HEAD
        return generate_uniform_distribution(sample_size, precision)
    elif distribution_choice == 2:
        return generate_exponential_distribution(sample_size, precision)
    elif distribution_choice == 3:
        return generate_normal_distribution(sample_size, precision)
=======
        a = float(input('Ingresa el límite inferior (a): '))
        b = float(input('Ingresa el límite superior (b): '))
        while a >= b:
            print('Límites inválidos. El límite inferior debe ser menor que el límite superior.')
            a = float(input('Ingresa el límite inferior (a): '))
            b = float(input('Ingresa el límite superior (b): '))
        sample = generate_uniform_distribution(sample_size, precision, a, b)
        return sample, 1, (a, b)

    elif distribution_choice == 2:
        lambda_val = float(input('Ingresa lambda (λ): '))
        while lambda_val <= 0:
            print('Lambda inválido. Lambda debe ser mayor que 0.')
            lambda_val = float(input('Ingresa lambda (λ): '))
        sample = generate_exponential_distribution(sample_size, precision, lambda_val)
        return sample, 2, (lambda_val)

    elif distribution_choice == 3:
        mean = float(input('Ingresa la media (μ): '))
        std_dev = float(input('Ingresa la desviación estándar (σ): '))
        while std_dev <= 0:
            print('Desviación estándar inválida. Debe ser mayor que 0.')
            std_dev = float(input('Ingresa la desviación estándar (σ): '))
        sample = generate_normal_distribution(sample_size, precision, mean, std_dev)
        return sample, 3, (mean, std_dev)
>>>>>>> origin/mateo
