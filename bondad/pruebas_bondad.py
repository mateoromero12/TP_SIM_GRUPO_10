from scipy.stats import chi2
from bondad.valores import ks_tabulado, chi_tabulado
import numpy as np
from bondad.display_resultados import (
    mostrar_tabla_chi_agrupado,
    mostrar_resultado_chi,
    mostrar_resultado_ks,
    mostrar_tabla_frecuencias,
)
from utils.validador_input import pedir_float

def valorAlfa(tipo_prueba):
    """
    Solicita al usuario el nivel de significancia (alfa) y lo valida.

    Returns:
        float: El nivel de significancia ingresado por el usuario.
    """
    alfa_por_prueba = {
        'chi2':   [0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],
        'ks':     [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20],
    }

    alfa_permitidos = alfa_por_prueba.get(tipo_prueba)
    if alfa_permitidos is None:
        raise ValueError(f"Tipo de prueba no soportado: {tipo_prueba}")

    alfa = pedir_float(
        'Ingrese el nivel de significancia (ej: 0.05): ',
        condicion=lambda x: x in alfa_permitidos,
        mensaje_error=f'El nivel de significancia debe estar entre los valores permitidos para la prueba "{tipo_prueba}":\n{alfa_permitidos}'
    )
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
    gl = k - 1 

    if gl <= 0:
        print("No hay suficientes grados de libertad para aplicar la prueba de Chi-cuadrado.")
        return False
    
    alfa = valorAlfa('chi2')
    valor_critico = chi_tabulado[gl][alfa]

    mostrar_resultado_chi(estadistico, valor_critico, gl, alfa)

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
    alfa = valorAlfa('ks')

    valor_critico = ks_tabulado[n][alfa]

    mostrar_resultado_ks(intervalos, fo, fe, n, estadistico, valor_critico, alfa)

    return estadistico <= valor_critico
