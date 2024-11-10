# Función para calcular el costo de almacenamiento
def calcular_costo_almacenamiento(stock, costo_por_unidad):
    return stock * costo_por_unidad * 10

# Función para calcular el costo de pedido
def calcular_costo_pedido(cantidad_comprada, costo_pedido_1, costo_pedido_2, costo_pedido_3):
    if cantidad_comprada <= 100:
        return costo_pedido_1
    elif 101 <= cantidad_comprada <= 200:
        return costo_pedido_2
    else:
        return costo_pedido_3

# Función para calcular el costo de ruptura
def calcular_costo_ruptura(ruptura, costo_por_unidad):
    return ruptura * costo_por_unidad * 10 if ruptura > 0 else 0

# Función para calcular el costo acumulado
def calcular_costo_acumulado(costo_pedido, costo_almacenamiento, costo_ruptura):
    return costo_pedido + costo_almacenamiento + costo_ruptura

def calcular_costo_medio(costo_acumulado, costo_medio_anterior, dia):
    calculo = (1/dia) * (((dia-1)*costo_medio_anterior )+ costo_acumulado)
    return calculo
