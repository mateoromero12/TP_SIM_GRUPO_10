import random
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from typing import List, Tuple


def main() -> None:
    """
    Función principal que coordina la generación de variables aleatorias,
    el cálculo de intervalos y frecuencias, y la visualización de resultados.
    """
    precision: int = 4
    random_variables: List[float] = get_random_variables(precision)
    num_classes: int = get_number_of_classes()

    intervals, frequency_counts = calculate_intervals_and_frequencies(random_variables, num_classes)

    display_generated_variables(random_variables, precision)
    display_intervals_and_frequencies(intervals, frequency_counts, precision)

    plot_histogram(intervals, frequency_counts, precision)


def calculate_intervals_and_frequencies(random_variables: List[float], num_classes: int) -> Tuple[List[Tuple[float, float]], List[int]]:
    """
    Calcula los intervalos y las frecuencias de las variables aleatorias generadas.

    Args:
        random_variables: Lista de variables aleatorias generadas.
        num_classes: Número de clases o intervalos.

    Returns:
        Una tupla que contiene:
        - intervals: Lista de tuplas que representan los límites de cada intervalo.
        - frequency_counts: Lista de frecuencias para cada intervalo.
    """
    min_value = min(random_variables)
    max_value = max(random_variables)
    interval_size = (max_value - min_value) / num_classes

    # Crear los intervalos
    intervals = [
        (min_value + i * interval_size, min_value + (i + 1) * interval_size)
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

    return intervals, frequency_counts


def display_generated_variables(random_variables: List[float], precision: int) -> None:
    """
    Muestra las variables aleatorias generadas en la consola.

    Args:
        random_variables: Lista de variables generadas.
        precision: Precisión decimal para mostrar las variables.
    """
    print('\nVariables aleatorias generadas:')
    print(', '.join(f'{number:.{precision}f}' for number in random_variables))


def display_intervals_and_frequencies(intervals: List[Tuple[float, float]], frequency_counts: List[int], precision: int) -> None:
    """
    Muestra los intervalos y las frecuencias en la consola.

    Args:
        intervals: Lista de tuplas que representan los límites de cada intervalo.
        frequency_counts: Lista de frecuencias para cada intervalo.
        precision: Precisión decimal para mostrar los límites de los intervalos.
    """
    print('\nIntervalos y frecuencias:')
    print(f'{"Intervalo":<25} {"Frecuencia":<10}')
    print('-' * 35)
    for i, (lower_bound, upper_bound) in enumerate(intervals):
        interval_str = f'[{lower_bound:.{precision}f}, {upper_bound:.{precision}f})'
        print(f'{interval_str:<25} {frequency_counts[i]:<10}')


def plot_histogram(intervals: List[Tuple[float, float]], frequency_counts: List[int], precision: int) -> None:
    """
    Genera un histograma a partir de los intervalos y frecuencias.

    Args:
        intervals: Lista de tuplas que representan los límites de cada intervalo.
        frequency_counts: Lista de frecuencias para cada intervalo.
        precision: Precisión decimal para mostrar los límites de los intervalos en las etiquetas.
    """
    plt.bar(
        range(len(intervals)),
        frequency_counts,
        tick_label=[f'[{lower:.{precision}f}, {upper:.{precision}f})' for lower, upper in intervals]
    )
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Variables Aleatorias')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


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


def generate_uniform_distribution(sample_size: int, precision: int) -> List[float]:
    """
    Genera variables aleatorias con distribución uniforme.

    Args:
        sample_size: Tamaño de la muestra.
        precision: Precisión decimal para redondear

    Returns:
        Lista de números generados con distribución uniforme.
    """
    lower_bound = float(input('Ingresa el límite inferior (a): '))
    upper_bound = float(input('Ingresa el límite superior (b): '))
    while lower_bound >= upper_bound:
        print('Límites inválidos. El límite inferior debe ser menor que el límite superior.')
        lower_bound = float(input('Ingresa el límite inferior (a): '))
        upper_bound = float(input('Ingresa el límite superior (b): '))
    return [round(float(generate_uniform_random(lower_bound, upper_bound)), precision) for _ in range(sample_size)]


def generate_exponential_distribution(sample_size: int, precision: int) -> List[float]:
    """
    Genera números aleatorios con distribución exponencial.

    Args:
        sample_size: Tamaño de la muestra.
        precision: Precisión decimal para redondear los números generados.

    Returns:
        Lista de números generados con distribución exponencial.
    """
    lambda_value = float(input('Ingresa lambda (λ): '))
    while lambda_value <= 0:
        print('Lambda inválido. Lambda debe ser mayor que 0.')
        lambda_value = float(input('Ingresa lambda (λ): '))
    return [round(float(generate_exponential_random(lambda_value)), precision) for _ in range(sample_size)]


def generate_normal_distribution(sample_size: int, precision: int) -> List[float]:
    """
    Genera números aleatorios con distribución normal.

    Args:
        sample_size: Tamaño de la muestra.
        precision: Precisión decimal para redondear los números generados.

    Returns:
        Lista de números generados con distribución normal.
    """
    mean = float(input('Ingresa la media (μ): '))
    std_dev = float(input('Ingresa la desviación estándar (σ): '))
    while std_dev <= 0:
        print('Desviación estándar inválida. Debe ser mayor que 0.')
        std_dev = float(input('Ingresa la desviación estándar (σ): '))

    random_numbers = []
    for _ in range((sample_size + 1) // 2):
        n1, n2 = generate_normal_random(mean, std_dev)
        random_numbers.extend([
            round(float(n1), precision),
            round(float(n2), precision)
        ][:max(0, sample_size - len(random_numbers))]) 

    return random_numbers


def generate_uniform_random(lower_bound: float, upper_bound: float) -> float:
    """
    Genera un número aleatorio con distribución uniforme.

    Args:
        lower_bound: Límite inferior del rango.
        upper_bound: Límite superior del rango.

    Returns:
        Número aleatorio generado.
    """
    return lower_bound + random.random() * (upper_bound - lower_bound)


def generate_exponential_random(lambda_value: float) -> float:
    """
    Genera un número aleatorio con distribución exponencial.

    Args:
        lambda_value: Parámetro lambda de la distribución exponencial.

    Returns:
        Número aleatorio generado.
    """
    return -np.log(1 - random.random()) / lambda_value


def generate_normal_random(mean: float, std_dev: float) -> Tuple[float, float]:
    """
    Genera dos números aleatorios con distribución normal usando el método Box-Muller.

    Args:
        mean: Media de la distribución.
        std_dev: Desviación estándar de la distribución.

    Returns:
        Dos números aleatorios generados.
    """
    random1 = random.random()
    random2 = random.random()
    n1 = (np.sqrt(-2 * np.log(random1)) * np.cos(2 * pi * random2)) * std_dev + mean
    n2 = (np.sqrt(-2 * np.log(random1)) * np.sin(2 * pi * random2)) * std_dev + mean
    return n1, n2


if __name__ == '__main__':
    main()