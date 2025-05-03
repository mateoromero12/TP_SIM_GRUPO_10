from utils.input_handler import get_random_variables, get_number_of_classes
from utils.intervals import calculate_intervals_and_frequencies
from utils.display import display_generated_variables, display_intervals_and_frequencies, plot_histogram


def main() -> None:
    """
    Función principal que coordina la generación de variables aleatorias,
    el cálculo de intervalos y frecuencias, y la visualización de resultados.
    """
    precision: int = 4
    random_variables = get_random_variables(precision)
    num_classes = get_number_of_classes()

    intervals, frequency_counts = calculate_intervals_and_frequencies(random_variables, num_classes)

    display_generated_variables(random_variables, precision)
    display_intervals_and_frequencies(intervals, frequency_counts, precision)

    plot_histogram(intervals, frequency_counts, precision)


if __name__ == '__main__':
    main()