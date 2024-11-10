def crear_fila_cola(reloj, evento, proximo_evento, random_llegada, tiempo_entre_llegadas, proxima_llegada,
                 random_necesidad, necesidad_cliente, random_venta, tiempo_atencion, fin_atencion, 
                 random_reparacion, tiempo_reparacion, fin_reparacion, random_refrigerio, toma_refrigerio, random_tipo_refrigerio, 
                 tipo_refrigerio, tiempo_refrigerio, fin_refrigerio,ayudante_estado, cola_ayudante, relojero_estado, 
                 cola_relojes_reparar, cola_relojes_reparados, clientes_atendidos, clientes_no_reparados, 
                 tiempo_ocupado_ayudante, tiempo_ocupado_relojero, clientes):
        
    fila = {
        "reloj": reloj,  # Columna 1: Reloj actual
        "evento": evento,  # Columna 2: Evento actual
        "proximo_evento": proximo_evento,  # Columna 3: Próximo evento
        "random_llegada": random_llegada,  # Columna 4: Número aleatorio para la llegada
        "tiempo_entre_llegadas": tiempo_entre_llegadas,  # Columna 5: Tiempo entre llegadas
        "proxima_llegada": proxima_llegada,  # Columna 6: Próxima llegada del cliente
        "random_necesidad": random_necesidad,  # Columna 7: Número aleatorio para la necesidad del cliente
        "necesidad_cliente": necesidad_cliente,  # Columna 8: Tipo de necesidad (Compra, Retira, Repara)
        "random_venta": random_venta,  # Columna 9: Número aleatorio para la venta
        "tiempo_atencion": tiempo_atencion,  # Columna 10: Tiempo de atención
        "fin_atencion": fin_atencion,  # Columna 11: Fin de atención
        "random_reparacion": random_reparacion,  # Columna 12: Número aleatorio para la reparación
        "tiempo_reparacion": tiempo_reparacion,  # Columna 13: Tiempo de reparación
        "fin_reparacion": fin_reparacion,  # Columna 14: Fin de reparación
        "random_refrigerio": random_refrigerio,  # Columna 15: Número aleatorio para el café
        "toma_refrigerio": toma_refrigerio,  # Columna 16: Si toma café o no
        "random_tipo_refrigerio": random_tipo_refrigerio, #Columna 17: Numero aleatorio para el tipo de refrigerio
        "tipo_refrigerio": tipo_refrigerio, # Columna 18: Tipo de refrigerio
        "tiempo_refrigerio": tiempo_refrigerio, #Columna 19: Tiempo de refrigerio 
        "fin_refrigerio": fin_refrigerio,  # Columna 20: Fin del café
        "ayudante_estado": ayudante_estado,  # Columna 21: Estado del ayudante (Libre, Ocupado)
        "cola_ayudante": cola_ayudante,  # Columna 22: Cola de clientes esperando atención
        "relojero_estado": relojero_estado,  # Columna 23: Estado del relojero (Libre, Ocupado, Café)
        "cola_relojes_reparar": cola_relojes_reparar,  # Columna 24: Cola de relojes para reparar
        "cola_relojes_reparados": cola_relojes_reparados,  # Columna 25: Cola de relojes reparados
        "clientes_atendidos": clientes_atendidos,  # Columna 26: Clientes atendidos
        "clientes_no_reparados": clientes_no_reparados,  # Columna 27: Clientes con relojes no reparados
        "tiempo_ocupado_ayudante": tiempo_ocupado_ayudante,  # Columna 28: Tiempo ocupado del ayudante
        "tiempo_ocupado_relojero": tiempo_ocupado_relojero,  # Columna 29: Tiempo ocupado del relojero
        "clientes": clientes  # Atributo adicional para los estados de los clientes (array)
    }

    return fila

def crear_fila_tabla_refrigerio(tiempo_actual, valor_actual, primer_derivada, valor_proximo):
    fila = {
        "tiempo_actual": tiempo_actual,
        "valor_actual": valor_actual,
        "primer_derivada": primer_derivada,
        "valor_proximo": valor_proximo
    }
    return fila