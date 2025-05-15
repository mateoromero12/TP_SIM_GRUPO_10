from typing import List, Tuple
import matplotlib.pyplot as plt
<<<<<<< HEAD
=======
from tabulate import tabulate
>>>>>>> origin/mateo


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
<<<<<<< HEAD
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
=======
    Muestra los intervalos y las frecuencias en formato tabular usando tabulate.
    """
    tabla = [
        [f"[{lower:.{precision}f}, {upper:.{precision}f})", count]
        for (lower, upper), count in zip(intervals, frequency_counts)
    ]
    print("\nIntervalos y frecuencias:")
    print(tabulate(tabla, headers=["Intervalo", "Frecuencia Observada"], tablefmt="github"))
>>>>>>> origin/mateo


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
<<<<<<< HEAD
    plt.show()
=======
    plt.show(block=False)

    # Esperar entrada del usuario para cerrar la ventana (opcional)
    input("\n--- Presiona Enter para continuar ---")
>>>>>>> origin/mateo
