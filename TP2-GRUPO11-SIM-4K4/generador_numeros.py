import random

# Función para generar números aleatorios en [0, 1) asegurando que nunca sea 1
def generar_aleatorios_uniformes(n):
    serie = [random.uniform(0, 1 - 1e-4) for _ in range(n)]
    return serie