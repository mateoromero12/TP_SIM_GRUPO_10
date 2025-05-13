from utils.input_handler import get_random_variables, get_number_of_classes
from utils.intervals import calculate_intervals_and_frequencies
from utils.display import display_generated_variables, display_intervals_and_frequencies, plot_histogram
from bondad.goodness_of_fit import chi_squared_test, kolmogorov_smirnov_test
from bondad.frec_esperadas import frecuencia_esperada


def main() -> None:
    """
    Función principal que coordina la generación de variables aleatorias,
    el cálculo de intervalos y frecuencias, y la visualización de resultados.
    """
    while True:
        print("\n--- Generador de variables aleatorias ---")
        print("1. Generar nueva distribución")
        print("2. Salir")

        option = input("Elige una opción (1 o 2): ")
        if option == '1':
            precision: int = 4
            random_variables, distribution, params = get_random_variables(precision)

            num_classes = get_number_of_classes()

            intervals, frequency_counts = calculate_intervals_and_frequencies(random_variables, num_classes)

            display_generated_variables(random_variables, precision)
            display_intervals_and_frequencies(intervals, frequency_counts, precision)

            plot_histogram(intervals, frequency_counts, precision)
            
            #### Pruebas de Bondad:
            if len(random_variables) > 30:
                print("\n--- Prueba de Bondad Chi-Cuadrado ---")
                if distribution == 1:
                    frec_esperadas = frecuencia_esperada("Uniforme", len(random_variables), intervals, params)
                    chi_squared_test(intervals, frequency_counts, frec_esperadas, "Uniforme")
                elif distribution == 2:
                    frec_esperadas = frecuencia_esperada("Exponencial", len(random_variables), intervals, params)
                    chi_squared_test(intervals, frequency_counts, frec_esperadas, "Exponencial")
                elif distribution == 3:
                    frec_esperadas = frecuencia_esperada("Normal", len(random_variables), intervals, params)
                    chi_squared_test(intervals, frequency_counts, frec_esperadas, "Normal")
            else:
                print("\n--- Prueba de Bondad Kolmogorov-Smirnov ---")
                if distribution == 1:
                    #generar las frec esperadas
                    frec_esperadas = frecuencia_esperada("Uniforme", len(random_variables), intervals, params)
                    kolmogorov_smirnov_test(intervals, frequency_counts, frec_esperadas, len(random_variables))
                elif distribution == 2:
                    #generar las frec esperadas
                    frec_esperadas = frecuencia_esperada("Exponencial", len(random_variables), intervals, params)
                    kolmogorov_smirnov_test(intervals, frequency_counts, frec_esperadas, len(random_variables))
                elif distribution == 3:
                    #generar las frec esperadas
                    frec_esperadas = frecuencia_esperada("Normal", len(random_variables), intervals, params)
                    kolmogorov_smirnov_test(intervals, frequency_counts, frec_esperadas, len(random_variables))
         
        elif option == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige 1 o 2.")


if __name__ == '__main__':
    main()
