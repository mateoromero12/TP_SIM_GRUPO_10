from utils.input_handler import get_random_variables, get_number_of_classes
from utils.intervals import calculate_intervals_and_frequencies
from utils.display import display_generated_variables, display_intervals_and_frequencies, plot_histogram
from bondad.frec_esperadas import frecuencia_esperada
from bondad.pruebas_bondad import chi_cuadrado, kolmogorov_smirnov

def main() -> None:
    """
    Función principal que coordina la generación de variables aleatorias,
    el cálculo de intervalos y frecuencias, y la visualización de resultados.
    """
    dist_map = {1: "Uniforme", 2: "Exponencial", 3: "Normal"}

    while True:
        print("\n--- Generador de variables aleatorias ---")
        print("1. Generar nueva distribución")
        print("2. Salir")

        option = input("Elige una opción (1 o 2): ")
        if option == '1':
            precision: int = 4
            random_variables, dist_code, params = get_random_variables(precision)
            dist_name = dist_map[dist_code]

            num_classes = get_number_of_classes()

            intervals, frequency_counts = calculate_intervals_and_frequencies(random_variables, num_classes)

            display_generated_variables(random_variables, precision)
            display_intervals_and_frequencies(intervals, frequency_counts, precision)
            plot_histogram(intervals, frequency_counts, precision)

            if len(random_variables) > 30:
                print("\n--- Prueba de Bondad Chi-Cuadrado ---")
                frec_esperadas = frecuencia_esperada(dist_name, len(random_variables), intervals, params)
                passed = chi_cuadrado(intervals, frequency_counts, frec_esperadas, dist_name)
                print("Resultado:", "No se rechaza H0" if passed else "Se rechaza H0")

            else:
                print("\n--- Prueba de Bondad Kolmogorov-Smirnov ---")
                frec_esperadas = frecuencia_esperada(dist_name, len(random_variables), intervals, params)
                passed = kolmogorov_smirnov(intervals, frequency_counts, frec_esperadas, len(random_variables))
                print("Resultado:", "No se rechaza H0" if passed else "Se rechaza H0")


        elif option == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige 1 o 2.")


if __name__ == '__main__':
    main()
