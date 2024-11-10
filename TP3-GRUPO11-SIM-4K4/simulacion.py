from aleatorios import generar_aleatorios_uniformes
from costos import calcular_costo_medio, calcular_costo_almacenamiento, calcular_costo_pedido, calcular_costo_ruptura, calcular_costo_acumulado
from calculos import calcular_demanda, calcular_demora
from tabla import crear_fila_tabla  # Importamos la función de creación de la tabla

def simular_politica_a(dias, stock_inicial, probabilidades_demanda, probabilidades_demora, costo_pedido_1, costo_pedido_2, costo_pedido_3, productos_cada_7_dias=180):
    stock = stock_inicial
    acumulado_costos = 0
    tabla_resultados = []
    demora_anterior = 0
    disponible = 0
    stock_comprado = 0

    # Generar números aleatorios para la demanda
    aleatorios_demanda = generar_aleatorios_uniformes(dias)

    # Definir costo medio anterior como cero inicialmente
    costo_medio_anterior = 0

    for dia in range(1, dias + 1):
        # Obtener randoms para la demanda con 4 decimales
        random_demanda = round(aleatorios_demanda[dia - 1], 4)
        
        # Calcular la demanda usando las funciones importadas
        demanda = calcular_demanda(random_demanda, probabilidades_demanda)

        # Si la demora anterior era 1, sumar el stock del pedido al stock existente
        if demora_anterior == 1:
            stock += stock_comprado  # Sumar el pedido al stock
            disponible = stock_comprado  # Mostrar en la columna "Disponible"
            stock_comprado = 0  # Reiniciar después de añadir al stock
        else:
            disponible = 0

        # Calcular la ruptura (si demanda > stock) o dejar en blanco si no hay ruptura
        if demanda > stock:
            ruptura = demanda - stock
        else:
            ruptura = 0

        # Calcular costos
        costo_almacenamiento = calcular_costo_almacenamiento(stock, 30)  # Ejemplo: costo por unidad es 30
        costo_ruptura = calcular_costo_ruptura(ruptura, 40)  # Ejemplo: costo por ruptura es 40
        # Calcular el costo de pedido solo cuando "Compra" es "Sí"
        if dia % 7 == 1 or dia == 1:
            costo_pedido = calcular_costo_pedido(productos_cada_7_dias, costo_pedido_1, costo_pedido_2, costo_pedido_3)
        else:
            costo_pedido = 0
        
        costo_acumulado = calcular_costo_acumulado(costo_pedido, costo_almacenamiento, costo_ruptura)
        
         # Costo medio con 4 decimales
        costo_medio = round(calcular_costo_medio(costo_acumulado, costo_medio_anterior, dia),4)

        # Reaprovisionar según política A: Pedido el primer día y luego cada 7 días
        if dia % 7 == 1 or dia == 1:
            cantidad_comprada = productos_cada_7_dias
            compra = "Sí"
            
            random_demora = round(generar_aleatorios_uniformes(1)[0], 4)  # Corregido: Acceder al número en la lista

            demora = calcular_demora(random_demora, probabilidades_demora)
            stock_comprado = cantidad_comprada  # Guardar la cantidad comprada para añadir cuando la demora llegue a 1
        else:
            cantidad_comprada = 0
            compra = "No"
            random_demora = ""
            # Simulación de la demora del pedido (restar 1 si hay un valor mayor a 1 en la fila anterior)
            if demora_anterior > 1:
                demora = demora_anterior - 1
            else:
                demora = ""

        
        # Generar la fila de la tabla usando la función de creación de tabla
        fila = crear_fila_tabla(dia, random_demanda, demanda, stock, ruptura, compra, cantidad_comprada, random_demora, demora, disponible, costo_almacenamiento, costo_pedido, costo_ruptura, costo_acumulado, costo_medio)
        tabla_resultados.append(fila)

        # Actualizar la demora anterior para la siguiente iteración
        demora_anterior = demora if demora != "" else 0

        # Restar las ventas al final del día, después de calcular la ruptura
        stock -= min(stock, demanda)

        costo_medio_anterior = costo_medio


    return tabla_resultados


def simular_politica_b(dias, stock_inicial, probabilidades_demanda, probabilidades_demora, costo_pedido_1, costo_pedido_2, costo_pedido_3):
    stock = stock_inicial
    acumulado_costos = 0
    tabla_resultados = []
    demora_anterior = 0
    disponible = 0
    stock_comprado = 0
    acumulador_demanda = 0  # Acumulador de demanda para "Cantidad A Comprar"

    # Generar números aleatorios para la demanda
    aleatorios_demanda = generar_aleatorios_uniformes(dias)

    # Definir costo medio anterior como cero inicialmente
    costo_medio_anterior = 0

    for dia in range(1, dias + 1):
        # Obtener randoms para la demanda con 4 decimales
        random_demanda = round(aleatorios_demanda[dia - 1], 4)

        # Calcular la demanda usando las funciones importadas
        demanda = calcular_demanda(random_demanda, probabilidades_demanda)

        # Acumular la demanda en "Cantidad A Comprar"
        acumulador_demanda += demanda

        # Si la demora anterior era 1, sumar el stock del pedido al stock existente
        if demora_anterior == 1:
            stock += stock_comprado  # Sumar el pedido al stock
            disponible = stock_comprado  # Mostrar en la columna "Disponible"
            stock_comprado = 0  # Reiniciar después de añadir al stock
        else:
            disponible = 0

        # Calcular la ruptura (si demanda > stock) o dejar en blanco si no hay ruptura
        if demanda > stock:
            ruptura = demanda - stock
        else:
            ruptura = 0

        # Calcular costos
        costo_almacenamiento = calcular_costo_almacenamiento(stock, 30)  # Ejemplo: costo por unidad es 30
        costo_ruptura = calcular_costo_ruptura(ruptura, 40)  # Ejemplo: costo por ruptura es 40
        costo_pedido = calcular_costo_pedido(acumulador_demanda, costo_pedido_1, costo_pedido_2, costo_pedido_3) if dia % 10 == 1 else 0
        costo_acumulado = calcular_costo_acumulado(costo_pedido, costo_almacenamiento, costo_ruptura)
        
        # Costo medio con 4 decimales
        costo_medio = round(calcular_costo_medio(costo_acumulado, costo_medio_anterior, dia),4)

        # Reaprovisionar según política B: Pedido basado en demanda acumulada cada 10 días
        if dia % 10 == 1:
            cantidad_comprada = acumulador_demanda  # Pedido basado en demanda acumulada hasta la fila actual
            compra = "Sí"          
            random_demora = round(generar_aleatorios_uniformes(1)[0], 4)
            demora = calcular_demora(random_demora, probabilidades_demora)
            stock_comprado = cantidad_comprada  # Guardar la cantidad comprada para añadir cuando la demora llegue a 1
            acumulador_demanda = 0  # Reiniciar el acumulador después de realizar la compra
        else:
            cantidad_comprada = acumulador_demanda  # Mostrar la acumulación de demanda en esta fila
            compra = "No"
            random_demora = ""
            # Simulación de la demora del pedido (restar 1 si hay un valor mayor a 1 en la fila anterior)
            if demora_anterior > 1:
                demora = demora_anterior - 1
            else:
                demora = ""

        # Generar la fila de la tabla usando la función de creación de tabla
        fila = crear_fila_tabla(dia, random_demanda, demanda, stock, ruptura, compra, cantidad_comprada, random_demora, demora, disponible, costo_almacenamiento, costo_pedido, costo_ruptura, costo_acumulado, costo_medio)
        tabla_resultados.append(fila)

        # Actualizar la demora anterior para la siguiente iteración
        demora_anterior = demora if demora != "" else 0

        # Restar las ventas al final del día, después de calcular la ruptura
        stock -= min(stock, demanda)

        costo_medio_anterior = costo_medio

    return tabla_resultados

