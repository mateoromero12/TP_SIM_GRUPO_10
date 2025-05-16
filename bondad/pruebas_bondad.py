from scipy.stats import chi2
from bondad.valores import ks_tabulado
import numpy as np
from bondad.display_resultados import (
    mostrar_tabla_chi_agrupado,
    mostrar_resultado_chi,
    mostrar_resultado_ks,
    mostrar_tabla_frecuencias,
)

def valorAlfa():
    """
    Solicita al usuario el nivel de significancia (alfa) y lo valida.

    Returns:
        float: El nivel de significancia ingresado por el usuario.
    """
    alfa = float(input("Ingrese el nivel de significancia: "))
    while alfa <= 0 or alfa >= 1:
        print("El nivel de significancia debe estar entre 0 y 1.")
        alfa = float(input("Ingrese el nivel de significancia: "))
    return alfa

def chi_cuadrado(intervalos, fo, fe, distribucion: str) -> bool:
    """
    Implementa la prueba de bondad de ajuste Chi-cuadrado siguiendo el enfoque teórico del material,
    incluyendo la agrupación de clases con frecuencia esperada < 5.

    Args:
        intervalos: lista de tuplas con los extremos de cada clase.
        fo: lista de frecuencias observadas.
        fe: lista de frecuencias esperadas.
        distribucion: nombre de la distribución ("Uniforme", "Exponencial", "Normal").

    Returns:
        True si no se rechaza H0 (estadístico <= valor crítico), False si se rechaza.
    """
    # Mostrar tabla sin agrupar
    mostrar_tabla_frecuencias(intervalos, fo, fe)

    # Agrupar clases con fe < 5
    grupos = []
    acumulado_fo = 0
    acumulado_fe = 0
    nuevo_intervalo = None

    for i in range(len(fe)):
        if fe[i] < 5:
            if nuevo_intervalo is None:
                nuevo_intervalo = list(intervalos[i])
            else:
                nuevo_intervalo[1] = intervalos[i][1]
            acumulado_fo += fo[i]
            acumulado_fe += fe[i]

            if acumulado_fe >= 5:
                grupos.append((tuple(nuevo_intervalo), acumulado_fo, acumulado_fe))
                nuevo_intervalo = None
                acumulado_fo = 0
                acumulado_fe = 0
        else:
            if acumulado_fe > 0:
                if nuevo_intervalo is None:
                    nuevo_intervalo = list(intervalos[i])
                else:
                    nuevo_intervalo[1] = intervalos[i][1]
                acumulado_fo += fo[i]
                acumulado_fe += fe[i]
                grupos.append((tuple(nuevo_intervalo), acumulado_fo, acumulado_fe))
                nuevo_intervalo = None
                acumulado_fo = 0
                acumulado_fe = 0
            else:
                grupos.append((intervalos[i], fo[i], fe[i]))

    if acumulado_fe > 0:
        grupos[-1] = (
            (grupos[-1][0][0], intervalos[-1][1]),
            grupos[-1][1] + acumulado_fo,
            round(grupos[-1][2] + acumulado_fe, 4)
        )

    estadistico = mostrar_tabla_chi_agrupado(grupos)

    k = len(grupos)
    m = {"Uniforme": 0, "Exponencial": 1, "Normal": 2}[distribucion]
    gl = k - 1 - m

    if gl <= 0:
        print("No hay suficientes grados de libertad para aplicar la prueba de Chi-cuadrado.")
        return False
    
    alfa = valorAlfa()
    valor_critico = chi2.ppf(alfa, gl)
    mostrar_resultado_chi(estadistico, valor_critico, gl)

    return estadistico <= valor_critico


def kolmogorov_smirnov(intervalos, fo, fe, n: int) -> bool:
    """
    Implementa la prueba de Kolmogorov-Smirnov con datos agrupados según el enfoque del material teórico.

    Args:
        intervalos: lista de tuplas (limite inferior, superior).
        fo: lista de frecuencias observadas.
        fe: lista de frecuencias esperadas.
        n: tamaño total de la muestra.

    Returns:
        True si no se rechaza H0 (estadístico <= valor crítico), False si se rechaza.
    """

    k = len(intervalos)
    po = [round(f / n, 4) for f in fo]
    pe = [round(f / n, 4) for f in fe]

    po_ac = np.cumsum(po)
    pe_ac = np.cumsum(pe)

    diferencias = [round(abs(po_ac[i] - pe_ac[i]), 4) for i in range(k)]
    estadistico = max(diferencias)
    alfa = valorAlfa()

    if n <= 30:
        valor_critico = ks_tabulado[n - 1]
    else:
        valor_critico = round(1.36 / (n ** alfa), 4)

    mostrar_resultado_ks(intervalos, fo, fe, n, estadistico, valor_critico)

    return estadistico <= valor_critico
