from utils.gestor_parametros import obtener_variables_aleatorias, obtener_cantidad_clases
from utils.intervalos_de_frecuencia import calcular_intervalos_y_frecuencias
from utils.mostar_por_consola import mostrar_variables_generadas, mostrar_intervalos_y_frecuencias, graficar_histograma
from bondad.frec_esperadas import frecuencia_esperada
from bondad.pruebas_bondad import chi_cuadrado, kolmogorov_smirnov


def main() -> None:
    """
    Función principal que coordina la generación de variables aleatorias,
    el cálculo de intervalos y frecuencias, y la visualización de resultados.
    """
    mapa_distribuciones = {1: "Uniforme", 2: "Exponencial", 3: "Normal"}

    while True:
        print("\n--- Generador de variables aleatorias ---")
        print("1. Generar nueva distribución")
        print("2. Salir")

        opcion = input("Elige una opción (1 o 2): ")
        if opcion == '1':
            precision: int = 4
            lista_aleatoria, codigo_dist, parametros = obtener_variables_aleatorias(precision)
            nombre_distribucion = mapa_distribuciones[codigo_dist]

            cantidad_intervalos = obtener_cantidad_clases()

            intervalos, frecuencias = calcular_intervalos_y_frecuencias(
                lista_aleatoria, cantidad_intervalos
            )

            mostrar_variables_generadas(lista_aleatoria, precision)
            mostrar_intervalos_y_frecuencias(intervalos, frecuencias, precision)
            graficar_histograma(intervalos, frecuencias, precision)

            if len(lista_aleatoria) > 30:
                print("\n--- Prueba de Bondad Chi-Cuadrado ---")
                frecuencias_esperadas = frecuencia_esperada(
                    nombre_distribucion, len(lista_aleatoria), intervalos, parametros
                )
                passed = chi_cuadrado(
                    intervalos, frecuencias, frecuencias_esperadas, nombre_distribucion
                )
                # print("Resultado:", "No se rechaza H0" if passed else "Se rechaza H0")

            else:
                print("\n--- Prueba de Bondad Kolmogorov-Smirnov ---")
                frecuencias_esperadas = frecuencia_esperada(
                    nombre_distribucion, len(lista_aleatoria), intervalos, parametros
                )
                passed = kolmogorov_smirnov(
                    intervalos, frecuencias, frecuencias_esperadas, len(lista_aleatoria)
                )
                # print("Resultado:", "No se rechaza H0" if passed else "Se rechaza H0")

        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige 1 o 2.")


if __name__ == '__main__':
    main()
