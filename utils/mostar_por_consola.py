from typing import List, Tuple
import matplotlib.pyplot as plt
from tabulate import tabulate

def mostrar_variables_generadas(variables_aleatorias: List[float], precision: int) -> None:
    """
    Muestra las variables aleatorias generadas en la consola.

    Args:
        variables_aleatorias: Lista de variables generadas.
        precision: Precisión decimal para mostrar las variables.
    """
    print('\nVariables aleatorias generadas:')
    print(', '.join(f'{numero:.{precision}f}' for numero in variables_aleatorias))

def mostrar_intervalos_y_frecuencias(intervalos: List[Tuple[float, float]], frecuencias: List[int], precision: int) -> None:
    """
    Muestra los intervalos y las frecuencias en formato tabular usando tabulate.
    """
    tabla = [
        [f"[{lim_inf:.{precision}f}, {lim_sup:.{precision}f})", frecuencia]
        for (lim_inf, lim_sup), frecuencia in zip(intervalos, frecuencias)
    ]
    print("\nIntervalos y frecuencias:")
    print(tabulate(tabla, headers=["Intervalo", "Frecuencia Observada"], tablefmt="github"))

def graficar_histograma(intervalos: List[Tuple[float, float]], frecuencias: List[int], precision: int) -> None:
    """
    Genera un histograma a partir de los intervalos y frecuencias.

    Args:
        intervalos: Lista de tuplas que representan los límites de cada intervalo.
        frecuencias: Lista de frecuencias para cada intervalo.
        precision: Precisión decimal para mostrar los límites de los intervalos en las etiquetas.
    """
    plt.bar(
        range(len(intervalos)),
        frecuencias,
        tick_label=[f'[{lim_inf:.{precision}f}, {lim_sup:.{precision}f})' for lim_inf, lim_sup in intervalos]
    )
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Variables Aleatorias')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=False)

    # Esperar entrada del usuario para cerrar la ventana (opcional)
    input("\n--- Presiona Enter para continuar ---")