from typing import List, Tuple
from tabulate import tabulate


def mostrar_tabla_frecuencias(intervalos: List[Tuple[float, float]], fo: List[int], fe: List[float]) -> None:
    tabla = [[f"[{a:.4f}, {b:.4f})", o, round(e, 4)] for (a, b), o, e in zip(intervalos, fo, fe)]
    print("\nFrecuencias Observadas vs Esperadas (sin agrupar):")
    print(tabulate(tabla, headers=["Intervalo", "Fo", "Fe"], tablefmt="github"))


def mostrar_tabla_chi_agrupado(grupos: List[Tuple[Tuple[float, float], int, float]]) -> float:
    tabla = []
    estadistico = 0
    for (a, b), fo, fe in grupos:
        c = round(((fe - fo) ** 2) / fe, 4)
        estadistico += c
        tabla.append((f"[{a:.4f}, {b:.4f})", fo, round(fe, 4), c, round(estadistico, 4)))

    print("\nFrecuencias agrupadas para Chi-Cuadrado:")
    print(tabulate(tabla, headers=["Intervalo Agrupado", "Fo", "Fe", "C", "C(AC)"], tablefmt="github"))
    return estadistico


def mostrar_resultado_chi(estadistico: float, valor_critico: float, gl: int, alfa: float) -> None:
    tabla = [[
        round(estadistico, 4),
        round(valor_critico, 4),
        gl,
        alfa,
        "No se rechaza H0" if estadistico <= valor_critico else "Se rechaza H0"
    ]]
    print("\nResultado Chi-Cuadrado:")
    print(tabulate(tabla, headers=["Estadístico Chi", "Valor Crítico", "Grados Libertad", "α", "Conclusión"], tablefmt="github"))


def mostrar_resultado_ks(intervalos: List[Tuple[float, float]], fo: List[int], fe: List[float], n: int, estadistico: float, valor_critico: float, alfa: float) -> None:
    po = [round(f / n, 4) for f in fo]
    pe = [round(f / n, 4) for f in fe]

    po_ac = [round(sum(po[:i + 1]), 4) for i in range(len(po))]
    pe_ac = [round(sum(pe[:i + 1]), 4) for i in range(len(pe))]
    difs = [round(abs(po_ac[i] - pe_ac[i]), 4) for i in range(len(po))]

    tabla = [[f"[{a:.4f}, {b:.4f})", fo[i], fe[i], po_ac[i], pe_ac[i], difs[i]]
              for i, (a, b) in enumerate(intervalos)]

    print("\nResultado Kolmogorov-Smirnov:")
    print(tabulate(tabla, headers=["Intervalo", "Fo", "Fe", "PoAC", "PeAC", "|PoAC - PeAC|"], tablefmt="github"))

    resumen = [[round(estadistico, 4), round(valor_critico, 4), sum(fo), alfa,
                "No se rechaza H0" if estadistico <= valor_critico else "Se rechaza H0"]]
    print("\nResumen KS:")
    print(tabulate(resumen, headers=["Estadístico KS", "Valor Crítico", "Tamaño Muestra", "α", "Conclusión"], tablefmt="github"))
