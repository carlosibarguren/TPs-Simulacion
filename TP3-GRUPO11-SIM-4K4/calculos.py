# Función para calcular la demanda en base a las probabilidades acumuladas
def calcular_demanda(random_value, probabilidades_demanda):
    acumulada = 0
    demanda_valores = [0, 10, 20, 30, 40, 50]
    
    for i, prob in enumerate(probabilidades_demanda):
        limite_superior = acumulada + prob
        if acumulada <= random_value < limite_superior:
            return demanda_valores[i]
        acumulada = limite_superior
    
    return None  # En caso de que algo no calce (no debería ocurrir)

# Función para calcular la demora en base a las probabilidades acumuladas
def calcular_demora(random_value, probabilidades_demora):
    acumulada = 0
    demora_valores = [1, 2, 3, 4]
    
    for i, prob in enumerate(probabilidades_demora):
        limite_superior = acumulada + prob
        if acumulada <= random_value < limite_superior:
            return demora_valores[i]
        acumulada = limite_superior
    
    return None  # En caso de que algo no calce (no debería ocurrir)
