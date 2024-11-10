import tkinter as tk
from tkinter import ttk
from validaciones import validar_entradas
from fila import crear_fila_cola, crear_fila_tabla_refrigerio
from utilidades import calcular_random_uniforme, generar_random_probabilidad, generar_random_uniforme

salto_ultima_fila = 0
tk.Tk.report_callback_exception = lambda *args: print("Error en Tkinter:", args)

# Array que define los anchos para cada columna
anchos_columnas = [
    5,   # Fila
    10,  # Reloj
    20,  # Evento
    25,  # Próximo Evento
    15,  # Random Llegada
    20,  # Tiempo entre Llegadas
    20,  # Próxima Llegada
    18,  # Random Necesidad
    20,  # Necesidad Cliente
    15,  # Random Venta
    20,  # Tiempo Atención
    20,  # Fin Atención
    18,  # Random Reparación
    20,  # Tiempo Reparación
    20,  # Fin Reparación
    15,  # Random refrigerio
    15,  # Toma refrigerio
    20,  # Random Tipo refrigerio
    15,  # Tipo refrigerio
    15,  # Tiempo refrigerio
    20,  # Fin refrigerio
    20,  # Ayudante Estado
    15,  # Cola Ayudante
    20,  # Relojero Estado
    20,  # Cola Relojes Reparar
    20,  # Cola Relojes Reparados
    15,  # Clientes Atendidos
    20,  # Clientes No Reparados
    25,  # Tiempo Ocupado Ayudante
    25,  # Tiempo Ocupado Relojero
    10   # Ancho de una celda para un cliente
]

def crear_interfaz():

    global root, frame_resultados, entry_prob_compra, entry_prob_repara, entry_prob_retira 
    global entry_cliente_desde, entry_cliente_hasta, entry_venta_desde, entry_venta_hasta, entry_reparar_desde
    global entry_reparar_hasta, entry_prob_refrigerio, entry_tiempo_simular, entry_a, entry_b, scrollbar_x
    global entry_a_refrigerio, entry_paso_refrigerio

    root = tk.Tk()
    root.title("Simulación de Colas - Relojería B")
    
    # Obtener el tamaño de la pantalla y ajustar la ventana a ese tamaño
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto = root.winfo_screenheight()
    root.geometry(f"{pantalla_ancho}x{pantalla_alto}")

    tk.Label(root, text="Trabajo Práctico N°5 - Grupo 11", font=("Arial", 16, "bold")).place(x=500, y=10)

    tk.Label(root, text="Llegada del Cliente", font=("Arial", 11, "bold")).place(x=20, y=70)

    tk.Label(root, text="Tiempo Desde:").place(x=20, y=110)
    entry_cliente_desde = tk.Entry(root, width=5, justify='center')
    entry_cliente_desde.insert(0, "13")
    entry_cliente_desde.place(x=120, y=110)

    tk.Label(root, text="Tiempo Hasta:").place(x=20, y=140)
    entry_cliente_hasta = tk.Entry(root, width=5, justify='center')
    entry_cliente_hasta.insert(0, "17")
    entry_cliente_hasta.place(x=120, y=140)

    tk.Label(root, text="Necesidad del Cliente", font=("Arial", 11, "bold")).place(x=210, y=60)

    tk.Label(root, text="Probabilidad Compra:").place(x=218, y=90)
    entry_prob_compra = tk.Entry(root, width=5, justify='center')
    entry_prob_compra.insert(0, "0.45")
    entry_prob_compra.place(x=350, y=90)

    tk.Label(root, text="Probabilidad Reparación:").place(x=200, y=120)
    entry_prob_repara = tk.Entry(root, width=5, justify='center')
    entry_prob_repara.insert(0, "0.25")
    entry_prob_repara.place(x=350, y=120)

    tk.Label(root, text="Probabilidad Retirar:").place(x=225, y=150)
    entry_prob_retira = tk.Entry(root, width=5, justify='center')
    entry_prob_retira.insert(0, "0.30")
    entry_prob_retira.place(x=350, y=150)

    tk.Label(root, text="Demora Venta", font=("Arial", 11, "bold")).place(x=435, y=70)

    tk.Label(root, text="Tiempo Desde:").place(x=420, y=110)
    entry_venta_desde = tk.Entry(root, width=5, justify='center')
    entry_venta_desde.insert(0, "6")
    entry_venta_desde.place(x=520, y=110)

    tk.Label(root, text="Tiempo Hasta:").place(x=420, y=140)
    entry_venta_hasta = tk.Entry(root, width=5, justify='center')
    entry_venta_hasta.insert(0, "10")
    entry_venta_hasta.place(x=520, y=140)

    tk.Label(root, text="Demora Reparacion", font=("Arial", 11, "bold")).place(x=580, y=70)

    tk.Label(root, text="Tiempo Desde:").place(x=580, y=110)
    entry_reparar_desde = tk.Entry(root, width=5, justify='center')
    entry_reparar_desde.insert(0, "18")
    entry_reparar_desde.place(x=680, y=110)

    tk.Label(root, text="Tiempo Hasta:").place(x=580, y=140)
    entry_reparar_hasta = tk.Entry(root, width=5, justify='center')
    entry_reparar_hasta.insert(0, "22")
    entry_reparar_hasta.place(x=680, y=140)

    tk.Label(root, text="Refrigerio", font=("Arial", 11, "bold")).place(x=790, y=60)

    tk.Label(root, text="Probabilidad:").place(x=770, y=90)
    entry_prob_refrigerio = tk.Entry(root, width=5, justify='center')
    entry_prob_refrigerio.insert(0, "0.1")
    entry_prob_refrigerio.place(x=850, y=90)

    tk.Label(root, text="Paso Euler:").place(x=780, y=120)
    entry_paso_refrigerio = tk.Entry(root, width=5, justify='center')
    entry_paso_refrigerio.place(x=850, y=120)

    tk.Label(root, text="Constante A:").place(x=770, y=150)
    entry_a_refrigerio = tk.Entry(root, width=5, justify='center')
    entry_a_refrigerio.place(x=850, y=150)

    tk.Label(root, text="Tiempo a Simular (min):").place(x=920, y=75)
    entry_tiempo_simular = tk.Entry(root, width=10, justify='center')
    entry_tiempo_simular.place(x=1060, y=75)

    tk.Label(root, text="Mostrar desde:").place(x=970, y=110)
    entry_a = tk.Entry(root, width=10, justify='center')
    entry_a.place(x=1060, y=110)

    tk.Label(root, text="Cantidad Filas:").place(x=970, y=140)
    entry_b = tk.Entry(root, width=10, justify='center')
    entry_b.place(x=1060, y=140)

    boton_simular = tk.Button(root, text="Simular", command=lambda: simular(), bg="#1B2F45", fg="white", font=("Arial", 10, "bold"), width=10, height=2)
    boton_simular.place(x=1170, y=60)

    boton_cerrar = tk.Button(root, text="Cerrar", command=root.quit, bg="#800000", fg="white", font=("Arial", 10, "bold"), width=10, height=2)
    boton_cerrar.place(x=1170, y=120)

    # Tabla con scrollbars
    global canvas, frame_tabla

    canvas = tk.Canvas(root)
    canvas.place(x=20, y=200, width=1300, height=400)  # Ajustar la posición y el tamaño de la tabla

    scrollbar_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar_y.place(x=1320, y=200, height=400)

    scrollbar_x = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    scrollbar_x.place(x=20, y=600, width=1300)

    canvas.config(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

    frame_tabla = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_tabla, anchor="nw")

    #Crear Frame Resultados
    frame_resultados = tk.Frame(root)
    frame_resultados.place(x=180, y=630, width=1300, height=50)  # Ajusta la posición y tamaño del frame

    global frame_contenido, canvas_refrigerio

    # Crear una ventana secundaria para las tablas
    ventana_refrigerio = tk.Toplevel()
    ventana_refrigerio.title("Tablas de Integración Euler")
    ventana_refrigerio.geometry("1400x600")

    # Título centrado en la ventana
    tk.Label(ventana_refrigerio, text="Tablas de Integración Euler", font=("Arial", 18, "bold")).pack(pady=10)

    # Canvas para el área de tablas con scrollbars
    canvas_refrigerio = tk.Canvas(ventana_refrigerio)
    canvas_refrigerio.place(x=20, y=100, width=1300, height=400)  # Ajusta posición y tamaño

    scrollbar_x_refrigerio = tk.Scrollbar(ventana_refrigerio, orient="horizontal", command=canvas_refrigerio.xview)
    scrollbar_x_refrigerio.place(x=20, y=500, width=1300)  # Posiciona el scrollbar horizontal

    frame_contenido = tk.Frame(canvas_refrigerio)
    canvas_refrigerio.create_window((0, 0), window=frame_contenido, anchor="nw")
    canvas_refrigerio.configure(xscrollcommand=scrollbar_x_refrigerio.set)

    # Actualizar el área de scroll después de añadir contenido
    frame_contenido.update_idletasks()
    canvas_refrigerio.config(scrollregion=canvas_refrigerio.bbox("all"))

    # Ejecutar la ventana principal
    root.mainloop()

# Función de simulación
def simular():

    global muestro_fila, cliente_inicial_fila1, tiene_refrigerio

    # Variable global para almacenar el número del primer cliente en la simulación
    cliente_inicial_fila1 = None
    
    # Crear ventana de carga
    ventana_carga = tk.Toplevel(root)
    ventana_carga.title("Cargando...")
    ventana_carga.geometry("300x115")
    ventana_carga.configure(bg="#546682")  
    ventana_carga.overrideredirect(True)  # Eliminar barra de título
    ventana_carga.geometry("+500+320")

     # Etiqueta con texto blanco
    tk.Label(ventana_carga, text="Cargando...", font=("Arial", 12), fg="white", bg="#546682").pack(expand=True)
    
    # Forzar la actualización de la interfaz gráfica para mostrar la ventana de carga
    ventana_carga.update()

    try:
        tiene_refrigerio = False

        # Validar las entradas
        if validar_entradas(entry_prob_compra, entry_prob_repara, entry_prob_retira, 
                        entry_cliente_desde, entry_cliente_hasta,
                        entry_venta_desde, entry_venta_hasta,
                        entry_reparar_desde, entry_reparar_hasta,
                        entry_prob_refrigerio, entry_paso_refrigerio,
                        entry_a_refrigerio, entry_tiempo_simular, 
                        entry_a, entry_b):

            # Obtener los valores de los parámetros desde la interfaz
            prob_compra = float(entry_prob_compra.get())
            prob_repara = float(entry_prob_repara.get())
            tiempo_llegada_desde = float(entry_cliente_desde.get())
            tiempo_llegada_hasta = float(entry_cliente_hasta.get())
            tiempo_venta_desde = float(entry_venta_desde.get())
            tiempo_venta_hasta = float(entry_venta_hasta.get())
            tiempo_reparar_desde = float(entry_reparar_desde.get())
            tiempo_reparar_hasta = float(entry_reparar_hasta.get())
            prob_refrigerio = float(entry_prob_refrigerio.get())
            paso_refrigerio = float(entry_paso_refrigerio.get())
            a_refrigerio = float(entry_a_refrigerio.get())
            tiempo_simulacion = float(entry_tiempo_simular.get())
            tiempo_tabla_desde = float(entry_a.get())
            cantidad_filas_mostrar = int(entry_b.get())

            # Limpiar la tabla anterior
            for widget in frame_tabla.winfo_children():
                widget.destroy()

            # Limpiar frame_resultados antes de agregar nuevos valores
            for widget in frame_resultados.winfo_children():
                widget.destroy()

            # Limpiar frame_contenido antes de agregar nuevos valores
            for widget in frame_contenido.winfo_children():
                widget.destroy()

            # Crear los encabezados de las columnas
            columnas_fijas = ["Fila", "Reloj", "Evento", "Próximo Evento", "Random Llegada", "Tiempo entre Llegadas", "Próxima Llegada",
                            "Random Necesidad", "Necesidad Cliente", "Random Venta", "Tiempo Atención", "Fin Atención",
                            "Random Reparación", "Tiempo Reparación", "Fin Reparación", "Random refrigerio", "Toma refrigerio", 
                            "Random Tipo refrigerio", "Tipo refrigerio", "Tiempo refrigerio","Fin refrigerio",
                            "Ayudante Estado", "Cola Ayudante", "Relojero Estado", "Cola Relojes Reparar", "Cola Relojes Reparados",
                            "Clientes Atendidos", "Clientes No Reparados", "Tiempo Ocupado Ayudante", "Tiempo Ocupado Relojero"]

            # Crear widgets para los encabezados
            for i, col_name in enumerate(columnas_fijas):
                header = tk.Label(frame_tabla, text=col_name, borderwidth=1, relief="solid", bg="lightgray")
                header.grid(row=0, column=i, sticky="nsew")

            # Valores Primera Fila
            reloj = 0
            evento = "Inicio"
            proximo_evento = "Llegada Cliente"
            random_llegada = generar_random_uniforme()
            tiempo_entre_llegadas = calcular_random_uniforme(random_llegada, tiempo_llegada_desde, tiempo_llegada_hasta)
            proxima_llegada = 0 + tiempo_entre_llegadas
            random_necesidad = ""
            necesidad_cliente = ""
            random_venta = ""
            tiempo_atencion = ""
            fin_atencion = ""
            random_reparacion = ""
            tiempo_reparacion = ""
            fin_reparacion = ""
            random_refrigerio = ""
            toma_refrigerio = ""
            random_tipo_refrigerio = ""
            tipo_refrigerio = ""
            tiempo_refrigerio = ""
            fin_refrigerio = ""
            ayudante_estado = "Libre"
            cola_ayudante = 0
            relojero_estado = "Libre"
            cola_relojes_reparar = 0 
            cola_relojes_reparados = 3
            clientes_atendidos = 0
            clientes_no_reparados = 0
            tiempo_ocupado_ayudante = 0
            tiempo_ocupado_relojero = 0
            clientes = [1]

            cliente_sa = 0
            contador = 1
            muestro_fila = False

            # Generar el primer random de llegada al inicio
            if tiempo_tabla_desde == 0:
                # Fila inicial con los valores iniciales
                fila_inicial = crear_fila_cola(reloj, evento, proximo_evento, random_llegada, tiempo_entre_llegadas, proxima_llegada,
                            random_necesidad, necesidad_cliente, random_venta, tiempo_atencion, fin_atencion, 
                            random_reparacion, tiempo_reparacion, fin_reparacion, random_refrigerio, toma_refrigerio, random_tipo_refrigerio,
                            tipo_refrigerio, tiempo_refrigerio, fin_refrigerio, ayudante_estado, cola_ayudante, relojero_estado, 
                            cola_relojes_reparar, cola_relojes_reparados, clientes_atendidos, clientes_no_reparados, tiempo_ocupado_ayudante, 
                            tiempo_ocupado_relojero, clientes)
                crear_fila_en_tabla(fila_inicial)

                contador += 1

            # Inicializar valores de anteriores
            anterior_reloj = 0
            proximo_tiempo = proxima_llegada
            anterior_proxima_llegada = proxima_llegada
            anterior_fin_atencion = fin_atencion
            anterior_fin_reparacion = fin_reparacion
            anterior_fin_refrigerio = fin_refrigerio
            anterior_proximo_evento = proximo_evento
            anterior_necesidad_cliente = necesidad_cliente
            anterior_cola_relojes_reparados = cola_relojes_reparados
            anterior_fin_atencion = fin_atencion
            anterior_fin_reparacion = fin_reparacion

            while proximo_tiempo < tiempo_simulacion:
                # Actualizar el reloj al tiempo del próximo evento
                reloj = proximo_tiempo
                evento = anterior_proximo_evento

                # Solo generar el random_llegada si el evento actual es "Llegada Cliente"
                if evento == "Llegada Cliente":
                    random_llegada = generar_random_uniforme()
                    tiempo_entre_llegadas = calcular_random_uniforme(random_llegada, tiempo_llegada_desde, tiempo_llegada_hasta)
                    proxima_llegada = reloj + tiempo_entre_llegadas
                    cola_ayudante += 1
                    clientes.append("EA")  # Se agrega un nuevo cliente esperando atención

                else: 
                    random_llegada = ""
                    tiempo_entre_llegadas = ""
                    proxima_llegada = anterior_proxima_llegada

                if evento == "Fin Atencion":
                    # Eliminar cliente atendido
                    clientes_atendidos += 1
                    clientes.pop(1)
                    clientes[0] += 1  # Incrementa el índice del primer cliente en el array
                    if anterior_necesidad_cliente == "Retira":
                        if anterior_cola_relojes_reparados == 0:
                            clientes_no_reparados += 1
                        else:
                            cola_relojes_reparados -= 1
                    elif anterior_necesidad_cliente == "Repara":
                        cola_relojes_reparar += 1

                if (evento == "Llegada Cliente" and len(clientes) == 2) or (evento == "Fin Atencion" and len(clientes) > 1):
                    random_necesidad = generar_random_probabilidad()
                    if random_necesidad < prob_compra:
                        necesidad_cliente = "Compra"
                    elif random_necesidad < prob_compra + prob_repara:
                        necesidad_cliente = "Repara"
                    else:
                        necesidad_cliente = "Retira"
                    if necesidad_cliente == "Compra":
                        random_venta = generar_random_uniforme()
                        tiempo_atencion = calcular_random_uniforme(random_venta, tiempo_venta_desde, tiempo_venta_hasta)
                    else:
                        random_venta = ""
                        tiempo_atencion = 3
                    fin_atencion = reloj + tiempo_atencion
                    ayudante_estado = "Ocupado"
                    cola_ayudante -= 1
                    clientes[cliente_sa + 1] = "SA"  # Marcar que el cliente está siendo atendido
                    
                elif evento == "Fin Atencion":
                    random_necesidad = ""
                    necesidad_cliente = ""
                    random_venta = ""
                    tiempo_atencion = ""
                    fin_atencion = ""             
                    ayudante_estado = "Libre"
                else:
                    random_necesidad = ""
                    necesidad_cliente = anterior_necesidad_cliente
                    random_venta = ""
                    tiempo_atencion = ""
                    fin_atencion = anterior_fin_atencion

                if evento == "Fin Reparacion":
                    cola_relojes_reparados += 1

                    random_refrigerio = generar_random_probabilidad()

                    if random_refrigerio < prob_refrigerio:
                        toma_refrigerio = "Si"
                        random_tipo_refrigerio = generar_random_probabilidad()
                        if random_tipo_refrigerio < 0.5:
                            tipo_refrigerio = "Refresco"
                            valor_refrigerio = 50
                        else:
                            tipo_refrigerio = "Cafe"
                            valor_refrigerio = 80

                        tiempo_actual = 0
                        demora_actual = 0
                        demora_posterior = 0
                        if tiempo_tabla_desde <= reloj and contador <= cantidad_filas_mostrar:
                            tabla_refrigerio = crear_tabla_en_pantalla(round(reloj, 4))

                            while demora_posterior <= valor_refrigerio:
                                primer_derivada = round(0.4 * valor_refrigerio + tiempo_actual + a_refrigerio*cola_relojes_reparar,4)
                                demora_posterior = round(demora_actual + paso_refrigerio * primer_derivada, 4)
                                fila_tabla = crear_fila_tabla_refrigerio(
                                    tiempo_actual=tiempo_actual,
                                    valor_actual=demora_actual,
                                    primer_derivada=primer_derivada,
                                    valor_proximo=demora_posterior)
                                agregar_fila_a_tabla(tabla_refrigerio, fila_tabla)
                                demora_actual = demora_posterior
                                tiempo_actual = round(tiempo_actual + paso_refrigerio,4)

                            fila_tabla = crear_fila_tabla_refrigerio(
                                    tiempo_actual=tiempo_actual,
                                    valor_actual=demora_actual,
                                    primer_derivada="",
                                    valor_proximo="")
                            agregar_fila_a_tabla(tabla_refrigerio, fila_tabla)
                        else:
                            while demora_posterior <= valor_refrigerio:
                                primer_derivada = round(0.4 * valor_refrigerio + tiempo_actual + a_refrigerio*cola_relojes_reparar,4)
                                demora_posterior = round(demora_actual + paso_refrigerio * primer_derivada, 4)
                                demora_actual = demora_posterior
                                tiempo_actual += paso_refrigerio

                        tiempo_refrigerio = tiempo_actual
                        fin_refrigerio = tiempo_refrigerio + reloj
                        relojero_estado = "TR"
                        random_reparacion = ""  # No se puede reparar durante el refrigerio
                        tiempo_reparacion = ""
                        fin_reparacion = ""
                    else:
                        toma_refrigerio = "No"
                        random_tipo_refrigerio = ""
                        tipo_refrigerio = ""
                        tiempo_refrigerio = ""
                        fin_refrigerio = ""

                        if cola_relojes_reparar > 0:  # Si hay relojes en cola, empieza la reparación
                            random_reparacion = generar_random_uniforme()
                            tiempo_reparacion = calcular_random_uniforme(random_reparacion, tiempo_reparar_desde, tiempo_reparar_hasta)
                            fin_reparacion = reloj + tiempo_reparacion
                            relojero_estado = "Ocupado"
                            cola_relojes_reparar -= 1
                        else:  # Si no hay relojes en cola, el relojero queda libre
                            random_reparacion = ""
                            tiempo_reparacion = ""
                            fin_reparacion = ""
                            relojero_estado = "Libre"

                elif evento == "Fin refrigerio":
                    random_refrigerio = ""
                    toma_refrigerio = ""
                    random_tipo_refrigerio = ""
                    tipo_refrigerio = ""
                    tiempo_refrigerio = ""
                    fin_refrigerio = ""
                    
                    if cola_relojes_reparar > 0:  # Si hay relojes en cola, comienza una nueva reparación
                        random_reparacion = generar_random_uniforme()
                        tiempo_reparacion = calcular_random_uniforme(random_reparacion, tiempo_reparar_desde, tiempo_reparar_hasta)
                        fin_reparacion = reloj + tiempo_reparacion
                        relojero_estado = "Ocupado"
                        cola_relojes_reparar -= 1
                    else:  # Si no hay relojes en cola, el relojero queda libre
                        random_reparacion = ""
                        tiempo_reparacion = ""
                        fin_reparacion = ""
                        relojero_estado = "Libre"
                else:
                    # Mantener los valores de la fila anterior si no se trata de un evento relacionado con el relojero
                    if cola_relojes_reparar > 0 and anterior_fin_reparacion == "" and anterior_fin_refrigerio == "":
                        random_reparacion = generar_random_uniforme()
                        tiempo_reparacion = calcular_random_uniforme(random_reparacion, tiempo_reparar_desde, tiempo_reparar_hasta)
                        fin_reparacion = reloj + tiempo_reparacion
                        relojero_estado = "Ocupado"
                        cola_relojes_reparar -= 1
                    else:
                        random_refrigerio = ""
                        toma_refrigerio = ""
                        random_tipo_refrigerio = ""
                        tipo_refrigerio = ""
                        tiempo_refrigerio = ""
                        fin_refrigerio = anterior_fin_refrigerio
                        random_reparacion = ""
                        tiempo_reparacion = ""
                        fin_reparacion = anterior_fin_reparacion
                if evento == "Fin Atencion":
                    tiempo_ocupado_ayudante += reloj - anterior_reloj
                elif fin_atencion != "" and random_necesidad == "":
                    tiempo_ocupado_ayudante += reloj - anterior_reloj

                if evento == "Fin Reparacion" or evento == "Fin refrigerio":
                    tiempo_ocupado_relojero += reloj - anterior_reloj
                elif (fin_reparacion != "" and random_reparacion == "") or (fin_refrigerio != "" and random_refrigerio == ""):
                    tiempo_ocupado_relojero += reloj - anterior_reloj

                # Inicializar los tiempos a infinito si son ""
                tiempo_llegada_cliente = proxima_llegada if proxima_llegada != "" else float('inf')
                tiempo_fin_atencion = fin_atencion if fin_atencion != "" else float('inf')
                tiempo_fin_reparacion = fin_reparacion if fin_reparacion != "" else float('inf')
                tiempo_fin_refrigerio = fin_refrigerio if fin_refrigerio != "" else float('inf')

                # Encontrar el próximo evento y aplicar prioridad en caso de empate
                if tiempo_fin_atencion <= min(tiempo_fin_reparacion, tiempo_fin_refrigerio, tiempo_llegada_cliente):
                    proximo_evento = "Fin Atencion"
                    proximo_tiempo = tiempo_fin_atencion
                elif tiempo_fin_reparacion <= min(tiempo_fin_refrigerio, tiempo_llegada_cliente):
                    proximo_evento = "Fin Reparacion"
                    proximo_tiempo = tiempo_fin_reparacion
                elif tiempo_fin_refrigerio <= tiempo_llegada_cliente:
                    proximo_evento = "Fin refrigerio"
                    proximo_tiempo = tiempo_fin_refrigerio
                else:
                    proximo_evento = "Llegada Cliente"
                    proximo_tiempo = tiempo_llegada_cliente

                # Actualizar los tiempos anteriores
                anterior_reloj = reloj
                anterior_proxima_llegada = proxima_llegada
                anterior_fin_atencion = fin_atencion
                anterior_fin_reparacion = fin_reparacion
                anterior_fin_refrigerio = fin_refrigerio
                anterior_proximo_evento = proximo_evento
                anterior_necesidad_cliente = necesidad_cliente
                anterior_cola_relojes_reparados = cola_relojes_reparados

                if tiempo_tabla_desde <= reloj and contador <= cantidad_filas_mostrar:
                    # Crear la nueva fila y agregarla a la simulación
                    fila = crear_fila_cola(reloj, evento, proximo_evento, random_llegada, tiempo_entre_llegadas, proxima_llegada,
                            random_necesidad, necesidad_cliente, random_venta, tiempo_atencion, fin_atencion, 
                            random_reparacion, tiempo_reparacion, fin_reparacion, random_refrigerio, toma_refrigerio, random_tipo_refrigerio,
                            tipo_refrigerio, tiempo_refrigerio, fin_refrigerio, ayudante_estado, cola_ayudante, relojero_estado, 
                            cola_relojes_reparar, cola_relojes_reparados, clientes_atendidos, clientes_no_reparados, tiempo_ocupado_ayudante, 
                            tiempo_ocupado_relojero, clientes)
                    crear_fila_en_tabla(fila)
                    contador += 1
                elif contador > cantidad_filas_mostrar and not muestro_fila:
                    muestro_fila = True

            print("Simulado correctamente")
        
            if muestro_fila:
                fila = crear_fila_cola(reloj, evento, proximo_evento, random_llegada, tiempo_entre_llegadas, proxima_llegada,
                            random_necesidad, necesidad_cliente, random_venta, tiempo_atencion, fin_atencion, 
                            random_reparacion, tiempo_reparacion, fin_reparacion, random_refrigerio, toma_refrigerio, random_tipo_refrigerio,
                            tipo_refrigerio, tiempo_refrigerio, fin_refrigerio, ayudante_estado, cola_ayudante, relojero_estado, 
                            cola_relojes_reparar, cola_relojes_reparados, clientes_atendidos, clientes_no_reparados, tiempo_ocupado_ayudante, 
                            tiempo_ocupado_relojero, clientes)
                crear_fila_en_tabla(fila)

            resultado_probabilidad = round((clientes_no_reparados/clientes_atendidos), 4)

            # Mostrar el resultado en frame_resultados
            tk.Label(frame_resultados, text="Probabilidad del Cliente de Reloj No Reparado:", font=("Arial", 11)).grid(row=0, column=0, sticky="w")
            tk.Label(frame_resultados, text=str(resultado_probabilidad), font=("Arial", 11, "bold")).grid(row=0, column=1, sticky="w")

            resultado_ayudante = round((tiempo_ocupado_ayudante*100)/reloj,4)
            tk.Label(frame_resultados, text="                 Porcentaje Ayudante Ocupado:", font=("Arial", 11)).grid(row=0, column=2, sticky="w")
            tk.Label(frame_resultados, text=str(resultado_ayudante)+" %", font=("Arial", 11, "bold")).grid(row=0, column=3, sticky="w")

            resultado_relojero = round((tiempo_ocupado_relojero*100)/reloj,4)
            tk.Label(frame_resultados, text="                 Porcentaje Relojero Ocupado", font=("Arial", 11)).grid(row=0, column=4, sticky="w")
            tk.Label(frame_resultados, text=str(resultado_relojero)+" %", font=("Arial", 11, "bold")).grid(row=0, column=5, sticky="w")

            crear_encabezado_superior()

            if not tiene_refrigerio:
                tk.Label(frame_contenido, text="No se tomó un refrigerio en el intervalo seleccionado", font=("Arial", 13)).pack(padx=400, pady=200)
    
    finally:
        # Cerrar la ventana de carga una vez que la simulación haya terminado
        ventana_carga.destroy()

# Variable global para mantener la referencia de la fila seleccionada
fila_seleccionada = None

def colorear_fila(row_count):
    global fila_seleccionada

    # Restaurar el color de la fila previamente seleccionada
    if fila_seleccionada is not None:
        for widget in frame_tabla.grid_slaves(row=fila_seleccionada):
            widget.config(bg="white")

    # Cambiar el color de la fila actualmente seleccionada
    for widget in frame_tabla.grid_slaves(row=row_count):
        widget.config(bg="lightblue")

    # Actualizar la fila seleccionada
    fila_seleccionada = row_count

def crear_fila_en_tabla(fila):
    global cliente_inicial_fila1, cantidad_clientes_mostrar, nro_ultimo_cliente, cliente_salto, salto_ultima_fila

    if cliente_inicial_fila1 is None:
        cliente_inicial_fila1 = fila["clientes"][0]  # Inicializar el cliente inicial con el primero que aparece

    columnas_fijas = ["fila", "reloj", "evento", "proximo_evento", "random_llegada", "tiempo_entre_llegadas",
                      "proxima_llegada", "random_necesidad", "necesidad_cliente", "random_venta", "tiempo_atencion",
                      "fin_atencion", "random_reparacion", "tiempo_reparacion", "fin_reparacion", "random_refrigerio",
                      "toma_refrigerio", "random_tipo_refrigerio", "tipo_refrigerio", "tiempo_refrigerio", "fin_refrigerio", 
                      "ayudante_estado", "cola_ayudante", "relojero_estado","cola_relojes_reparar", "cola_relojes_reparados", 
                      "clientes_atendidos", "clientes_no_reparados", "tiempo_ocupado_ayudante", "tiempo_ocupado_relojero"]

    # Determinar la fila actual
    row_count = len(frame_tabla.grid_slaves(column=0))  # Contar filas existentes

    # Asignar el número de fila al objeto `fila` si no lo tiene
    fila["fila"] = row_count

    # Crear celdas para las columnas fijas
    for i, key in enumerate(columnas_fijas):
        valor = fila[key] if key in fila else ""
        if isinstance(valor, float):
            valor = round(valor, 4)
        label = tk.Label(frame_tabla, text=str(valor), borderwidth=1, relief="solid", width=anchos_columnas[i])
        label.grid(row=row_count, column=i, sticky="nsew")
        label.bind("<Button-1>", lambda e, row=row_count: colorear_fila(row))  # Colorear fila al hacer clic

    # Gestión de las columnas dinámicas para los clientes
    cliente_inicial_actual = fila["clientes"][0]
    clientes_a_mostrar = fila["clientes"][1:]  # Ignorar el primer valor porque es el número base

    if muestro_fila:
        cliente_salto = nro_ultimo_cliente
        if cliente_inicial_actual > nro_ultimo_cliente:
            salto_ultima_fila = cliente_inicial_actual - nro_ultimo_cliente
            clientes_fuera = nro_ultimo_cliente - cliente_inicial_fila1
        else:
            clientes_fuera = cliente_inicial_actual - cliente_inicial_fila1
    else:
        clientes_fuera = cliente_inicial_actual - cliente_inicial_fila1
        cliente_salto = None

    # Crear columnas vacías para los clientes que ya salieron del sistema
    columna_actual = len(columnas_fijas)  # Índice inicial para las columnas dinámicas
    for _ in range(clientes_fuera):
        label_vacio = tk.Label(frame_tabla, text="", borderwidth=1, relief="solid", width=anchos_columnas[-1])
        label_vacio.grid(row=row_count, column=columna_actual, sticky="nsew")
        columna_actual += 1  # Avanzar al siguiente índice de columna
        label_vacio.bind("<Button-1>", lambda e, row=row_count: colorear_fila(row))  # Colorear fila al hacer clic

    cantidad_clientes_mostrar = len(clientes_a_mostrar)

    # Crear columnas para los clientes restantes en el sistema
    for i, estado_cliente in enumerate(clientes_a_mostrar):
        texto_cliente = f"Cliente {cliente_inicial_actual + i}: {estado_cliente}" if estado_cliente else ""
        label_cliente = tk.Label(frame_tabla, text=texto_cliente, borderwidth=1, relief="solid", width=anchos_columnas[-1])
        label_cliente.grid(row=row_count, column=columna_actual, sticky="nsew")
        columna_actual += 1  # Avanzar al siguiente índice de columna
        label_cliente.bind("<Button-1>", lambda e, row=row_count: colorear_fila(row))  # Colorear fila al hacer clic

    nro_ultimo_cliente = cantidad_clientes_mostrar + cliente_inicial_actual

    # Actualizar el canvas
    frame_tabla.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def crear_encabezado_superior():
    global frame_encabezado_superior, canvas_encabezado, cantidad_clientes_mostrar

    # Eliminar encabezado previo si existe
    if "canvas_encabezado" in globals():
        canvas_encabezado.destroy()

    # Crear un canvas para el encabezado superior
    canvas_encabezado = tk.Canvas(root, height=40, bg="#00264d", highlightthickness=0)
    canvas_encabezado.place(x=21, y=180, width=1299)

    # Asociar el scroll horizontal al encabezado
    canvas_encabezado.config(xscrollcommand=scrollbar_x.set)
    scrollbar_x.config(command=lambda *args: sincronizar_scroll(*args))

    # Frame para los títulos dentro del canvas
    frame_encabezado_superior = tk.Frame(canvas_encabezado, bg="#00264d")
    canvas_encabezado.create_window((0, 0), window=frame_encabezado_superior, anchor="nw")

    # Lista de nombres para las columnas fijas
    nombres_columnas = ["Fila", "Reloj", "Evento", "Próximo Evento", "Random Llegada", "Tiempo entre Llegadas", "Próxima Llegada",
                            "Random Necesidad", "Necesidad Cliente", "Random Venta", "Tiempo Atención", "Fin Atención",
                            "Random Reparación", "Tiempo Reparación", "Fin Reparación", "Random refrigerio", "Toma refrigerio", 
                            "Random Tipo refrigerio", "Tipo refrigerio", "Tiempo refrigerio","Fin refrigerio",
                            "Ayudante Estado", "Cola Ayudante", "Relojero Estado", "Cola Relojes Reparar", "Cola Relojes Reparados",
                            "Clientes Atendidos", "Clientes No Reparados", "Tiempo Ocupado Ayudante", "Tiempo Ocupado Relojero"]

    # Crear encabezados fijos
    for i, col_name in enumerate(nombres_columnas):
        label = tk.Label(frame_encabezado_superior, text=col_name, borderwidth=1, relief="solid",
                         bg="#00264d", fg="white", font=("Arial", 9), height=2, width=anchos_columnas[i])
        label.grid(row=0, column=i, sticky="nsew")

    total_clientes = nro_ultimo_cliente - cliente_inicial_fila1
    cantidad_clientes_mostrar, 

    # Crear un encabezado adicional para "Clientes"
    ancho_celda_cliente = anchos_columnas[-1] # Ancho de una celda para cliente
    for i in range(total_clientes):
        cliente_actual = cliente_inicial_fila1 + i
        if muestro_fila:
            if salto_ultima_fila == 0 and cliente_actual >= cliente_salto:
                return
            elif cliente_actual >= cliente_salto and cliente_actual < cliente_salto + salto_ultima_fila:
                pass
            else:
                label_cliente = tk.Label(frame_encabezado_superior, text=f"Cliente {cliente_actual}", borderwidth=1, relief="solid",
                                        bg="#00264d", fg="white", font=("Arial", 9), height=2, width=ancho_celda_cliente)
                label_cliente.grid(row=0, column=len(nombres_columnas) + i, sticky="nsew")
        else:
            label_cliente = tk.Label(frame_encabezado_superior, text=f"Cliente {cliente_actual}", borderwidth=1, relief="solid",
                                        bg="#00264d", fg="white", font=("Arial", 9), height=2, width=ancho_celda_cliente)
            label_cliente.grid(row=0, column=len(nombres_columnas) + i, sticky="nsew")

    # Ajustar el tamaño del canvas del encabezado
    frame_encabezado_superior.update_idletasks()
    canvas_encabezado.config(scrollregion=canvas_encabezado.bbox("all"))

def sincronizar_scroll(*args):
    # Sincronizar el scroll del encabezado y la tabla
    canvas.xview(*args)
    canvas_encabezado.xview(*args)

# Crea una tabla específica para un instante del reloj
def crear_tabla_en_pantalla(reloj):

    global tiene_refrigerio

    if not tiene_refrigerio:
        tiene_refrigerio = True

    # Crear un marco para contener la tabla y su scrollbar
    frame_tabla_refrigerio = tk.Frame(frame_contenido, bd=2, relief="ridge", padx=10, pady=10)
    frame_tabla_refrigerio.pack(side="left", fill="both", expand=False, padx=10)

    # Título de la tabla
    tk.Label(frame_tabla_refrigerio, text=f"Tabla para el minuto: {reloj}", font=("Arial", 12, "bold")).pack(anchor="n")

    # Crear el Treeview (tabla)
    columnas = ["Tiempo Actual", "Valor Actual", "Primer Derivada", "Valor Próximo"]
    tabla = ttk.Treeview(frame_tabla_refrigerio, columns=columnas, show="headings", height=15)

    # Configurar encabezados y columnas
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=150)

    # Scrollbar vertical para la tabla
    scrollbar_y = tk.Scrollbar(frame_tabla_refrigerio, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar_y.set)

    # Empaquetar la tabla y su scrollbar
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")

    # Actualizar el área de scroll
    frame_contenido.update_idletasks()
    canvas_refrigerio.config(scrollregion=canvas_refrigerio.bbox("all"))

    return tabla

# Agrega una fila a la tabla especificada
def agregar_fila_a_tabla(tabla, fila):
    fila_data = {
        "Tiempo Actual": fila["tiempo_actual"],
        "Valor Actual": fila["valor_actual"],
        "Primer Derivada": fila["primer_derivada"],
        "Valor Próximo": fila["valor_proximo"]
    }
    tabla.insert("", "end", values=list(fila_data.values()))
