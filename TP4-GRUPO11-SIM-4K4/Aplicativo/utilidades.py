import random

def calcular_random_uniforme(random, a, b):
    return round(a + random * (b - a), 4)

def generar_random_probabilidad():
    return round(random.uniform(0, 0.9999), 4)

def generar_random_uniforme():
    return round(random.uniform(0, 1), 4)