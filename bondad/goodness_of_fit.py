    
chi_tabulado = (3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067, 15.507, 16.919, 18.307,
                19.675, 21.026, 22.362, 23.685, 24.996, 26.296, 27.587, 28.869, 30.144, 31.410,
                32.671, 33.924, 35.172, 36.415, 37.652, 38.885, 40.113, 41.337, 42.557, 43.773)

ks_tabulado = (0.9750, 0.8419, 0.7076, 0.6239, 0.5633, 0.5193, 0.4834, 0.4543, 0.4300, 0.4093,
               0.3912, 0.3754, 0.3614, 0.3489, 0.3376, 0.3273, 0.3180, 0.3094, 0.3014, 0.2941,
               0.2872, 0.2809, 0.2749, 0.2693, 0.2640, 0.2591, 0.2544, 0.2499, 0.2457, 0.2417,
               0.2379, 0.2342, 0.2308, 0.2274, 0.2243, 0.2212, 0.2183, 0.2154, 0.2127, 0.2101)

def chi_squared_test(intervalos, fo, fe, distr) -> None:
    i = 0
    v = []
    ace = 0
    aco = 0

    z = 0
    lim_inferior = intervalos[0][0]
    lim_superior = None
    while i < len(intervalos):
        if fe[i] < 5:
            lim_inferior = intervalos[i][0]
            while i < len(intervalos):
                ace = fe[i] + ace
                aco = fo[i] + aco
                if ace >= 5:
                    lim_superior = intervalos[i][1]
                    break
                else:
                    if i < len(intervalos):
                        z = i
                        pass
                i = i + 1

            if ace >= 5:
                v.append([[lim_inferior, lim_superior], aco, ace, None, None])
                lim_inferior = intervalos[i][1]

            else:
                v[len(v) - 1][0] = [lim_inferior, intervalos[len(intervalos) - 1][1]]
                v[len(v) - 1][1] = round(v[len(v) - 1][1] + aco, 4)
                v[len(v) - 1][2] = round(v[len(v) - 1][2] + ace, 4)

        else:
            v.append([intervalos[i], fo[i], round(fe[i], 4), None, None])
            lim_inferior = intervalos[i][1]

        i = i + 1
        aco = 0
        ace = 0

    j = 0
    print("Intervalos  ", "Frecuencia Ob.  ", "Frecuencia Esp.  ", "C          ", "C(AC)       ")
    while j < len(v):
        fe = v[j][2]
        fo = v[j][1]
        v[j][3] = round(((fe - fo)**2)/fe, 4)
        if j == 0:
            v[j][4] = v[j][3]
        else:
            v[j][4] = round(v[j][3] + v[j - 1][4], 4)
        print("-"*40)
        print(v[j])
        j = j + 1

    calculado = v[len(v) - 1][4]
    tabulado = chi_tabulado[len(v)-1-distr]

    print("/" * 100)
    print("Valor del estadístico de prueba:", calculado)
    print("Valor tabulado para un alfa de 0,05:", tabulado)
    return tabulado >= calculado 

def kolmogorov_smirnov_test(intervalos, fo, fe, N) -> None:
    i = 0
    v = []
    while i < len(intervalos):
        v.append([intervalos[i], fo[i], round(fe[i], 4), round(fo[i]/N, 4), round(fe[i]/N, 4), None, None, None, None])
        i += 1
    j = 0
    print("Intervalos  ", "frecuencia ob. ", "frecuencia esp. ", "Probabilidad ob.  ", "Probabilidad esp. ", "Po(AC)    ", "Pe(AC)     ", "|Pe(AC) - Po(AC)|", "MAX(|Pe(AC) - Po(AC)|)")
    while j < len(v):
        if j == 0:
            v[j][5] = round(v[j][3], 4)
            v[j][6] = round(v[j][4], 4)
            v[j][7] = round(abs(v[j][5] - v[j][6]), 4)
            v[j][8] = round(v[j][7], 4)
        else:

            v[j][5] = round(v[j-1][5] + v[j][3], 4)
            v[j][6] = round(v[j-1][5] + v[j][4], 4)
            v[j][7] = round(abs(v[j][5] - v[j][6]), 4)
            if v[j][7] >= v[j - 1][8]:
                v[j][8] = round(v[j][7], 4)
            else:
                v[j][8] = round(v[j - 1][8], 4)

        print(v[j])
        print("-"*40)
        j += 1
    
    calculado = v[len(v) - 1][8]
    tabulado = ks_tabulado[N-1] if N <= 40 else round(1.36 / N ** 0.5, 4)

    print("/" * 100)
    print("Valor del estadístico de prueba:", calculado)
    print("Valor tabulado para un alfa de 0,05:", tabulado)
    return tabulado >= calculado
