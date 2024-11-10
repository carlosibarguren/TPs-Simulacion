# Función para crear la tabla con las mismas columnas para ambas políticas
def crear_fila_tabla(dia, random_demanda, demanda, stock, ruptura, compra, cantidad_comprada, random_demora, demora, disponible, costo_almacenamiento, costo_pedido, costo_ruptura, costo_acumulado, costo_medio):
    fila = {
        "Día": dia,
        "Random Demanda": random_demanda,
        "Demanda": demanda,
        "Ventas": min(stock, demanda),
        "Stock Inicial": stock,  # Stock al inicio del día
        "Ruptura": ruptura,
        "Compra": compra,
        "Cantidad Comprada": cantidad_comprada,
        "Random Demora": random_demora,
        "Demora": demora,
        "Disponible": disponible,
        "Costo Almacenamiento": costo_almacenamiento,
        "Costo Pedido": costo_pedido,
        "Costo Ruptura": costo_ruptura,
        "Costo Acumulado": costo_acumulado,  # Nueva columna de costo acumulado
        "Costo Medio": costo_medio  # Costo medio con 4 decimales
    }
    return fila
