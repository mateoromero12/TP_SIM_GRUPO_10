from typing import List, Tuple
import matplotlib.pyplot as plt


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