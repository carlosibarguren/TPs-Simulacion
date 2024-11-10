def crear_fila(reloj, evento, proximo_evento, random_llegada, tiempo_entre_llegadas, proxima_llegada,
                 random_necesidad, necesidad_cliente, random_venta, tiempo_atencion, fin_atencion, 
                 random_reparacion, tiempo_reparacion, fin_reparacion, random_cafe, toma_cafe, fin_cafe,
                 ayudante_estado, cola_ayudante, relojero_estado, cola_relojes_reparar, cola_relojes_reparados,
                 clientes_atendidos, clientes_no_reparados, tiempo_ocupado_ayudante, tiempo_ocupado_relojero, clientes):
        
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
        "random_cafe": random_cafe,  # Columna 15: Número aleatorio para el café
        "toma_cafe": toma_cafe,  # Columna 16: Si toma café o no
        "fin_cafe": fin_cafe,  # Columna 17: Fin del café
        "ayudante_estado": ayudante_estado,  # Columna 18: Estado del ayudante (Libre, Ocupado)
        "cola_ayudante": cola_ayudante,  # Columna 19: Cola de clientes esperando atención
        "relojero_estado": relojero_estado,  # Columna 20: Estado del relojero (Libre, Ocupado, Café)
        "cola_relojes_reparar": cola_relojes_reparar,  # Columna 21: Cola de relojes para reparar
        "cola_relojes_reparados": cola_relojes_reparados,  # Columna 22: Cola de relojes reparados
        "clientes_atendidos": clientes_atendidos,  # Columna 23: Clientes atendidos
        "clientes_no_reparados": clientes_no_reparados,  # Columna 24: Clientes con relojes no reparados
        "tiempo_ocupado_ayudante": tiempo_ocupado_ayudante,  # Columna 25: Tiempo ocupado del ayudante
        "tiempo_ocupado_relojero": tiempo_ocupado_relojero,  # Columna 26: Tiempo ocupado del relojero
        "clientes": clientes  # Atributo adicional para los estados de los clientes (array)
    }

    return fila
