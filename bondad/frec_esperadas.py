import math

def frecuencia_esperada(distrib, n_muestra, intervalos, parametros):

    #if distrib == 1:
    if distrib == "Uniforme":
        return fe_uniforme(n_muestra, len(intervalos))
    #elif distrib == 2:
    elif distrib == "Exponencial":
        return fe_exponencial(n_muestra,intervalos, parametros)
    else:
        return fe_normal(n_muestra, intervalos, parametros)
    
    
# Devuelve una lista con las frecuencias esperadas para una distr uniforme
def fe_uniforme(n, cant_intervalos):
    return [round(n/cant_intervalos, ndigits=4)] * cant_intervalos


# Devuelve una lista con las frecuencias esperadas para una distr normal
def fe_normal(n, intervalos, parametros):
    
    media, desviacion = parametros
    frecuencias = []

    for intervalo in intervalos:
        marca_clase = round((intervalo[0]+intervalo[1])/2, ndigits=4)
        densidad = (math.e ** (-0.5 * ((marca_clase - media) / desviacion) ** 2)) / (desviacion * math.sqrt(2 * math.pi)) 
        densidad = densidad * (intervalo[1]-intervalo[0])
        
        f_esperada = densidad * n
        frecuencias.append(round(f_esperada, 4))
        
    return frecuencias


# Devuelve una lista con las frecuencias esperadas para una distr exponencial
def fe_exponencial(n, intervalos, parametros):
    lam_da = parametros
    frecuencias = []
    
    for intervalo in intervalos:
        marca_clase = round((intervalo[0]+intervalo[1])/2, ndigits=4)
        # densidad =  (1/media) * math.e ** (-(1/media) * marca_clase) *  (intervalo[1]-intervalo[0])
        acumulacion = (1 - math.e ** (- (lam_da) * intervalo[1])) - (1 - math.e ** (- (lam_da) * intervalo[0]))
        
        f_esperada = acumulacion * n
        frecuencias.append(round(f_esperada, 4))
        
    return frecuencias
    
