from scipy.stats import chi2
from bondad.valores import ks_tabulado
import numpy as np


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
                # unir lo acumulado con la clase actual si lo acumulado es insuficiente
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
        # agregar lo que quede
        grupos[-1] = (
            (grupos[-1][0][0], intervalos[-1][1]),
            grupos[-1][1] + acumulado_fo,
            round(grupos[-1][2] + acumulado_fe, 4)
        )

    print("\nIntervalo\tFo\tFe\tC\tC(AC)")
    estadistico = 0
    for i, (intv, fo_g, fe_g) in enumerate(grupos):
        c = round(((fe_g - fo_g)**2) / fe_g, 4)
        estadistico += c
        print(f"{intv}\t{fo_g}\t{fe_g:.4f}\t{c:.4f}\t{estadistico:.4f}")

    k = len(grupos)
    m = {"Uniforme": 0, "Exponencial": 1, "Normal": 2}[distribucion]
    gl = k - 1 - m
    

    if gl <= 0:
        print("No hay suficientes grados de libertad para aplicar la prueba de Chi-cuadrado.")
        return False

    valor_critico = chi2.ppf(0.95, gl)
    print("\nEstadístico Chi-cuadrado:", round(estadistico, 4))
    print("Valor crítico (alfa = 0.05):", round(valor_critico, 4))
    print("Grados de libertad:", gl)

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

    # Valor crítico aproximado (nivel de significancia 0.05)
    if n <= 40:
        valor_critico = ks_tabulado[n - 1]
    else:
        valor_critico = round(1.36 / (n ** 0.5), 4)

    print("\nIntervalo\tFo\tFe\tPoAC\tPeAC\t|PoAC - PeAC|")
    for i in range(k):
        print(f"{intervalos[i]}\t{fo[i]}\t{fe[i]}\t{po_ac[i]:.4f}\t{pe_ac[i]:.4f}\t{diferencias[i]:.4f}")

    print("\nEstadístico KS:", estadistico)
    print("Valor crítico (alfa = 0.05):", valor_critico)

    return estadistico <= valor_critico
