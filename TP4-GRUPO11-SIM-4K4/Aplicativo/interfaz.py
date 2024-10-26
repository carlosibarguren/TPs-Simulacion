import tkinter as tk
from tkinter import ttk
from validaciones import validar_entradas
from fila import crear_fila
import random
from utilidades import calcular_random_uniforme, generar_random_probabilidad, generar_random_uniforme

def crear_interfaz():

    global root, frame_resultados, entry_prob_compra, entry_prob_repara, entry_prob_retira, entry_cliente_desde, entry_cliente_hasta, entry_venta_desde, entry_venta_hasta, entry_reparar_desde, entry_reparar_hasta, entry_prob_cafe, entry_demora_cafe, entry_tiempo_simular, entry_a, entry_b
    root = tk.Tk()
    root.title("Simulación de Colas - Relojería B")
    
    # Obtener el tamaño de la pantalla y ajustar la ventana a ese tamaño
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto = root.winfo_screenheight()
    root.geometry(f"{pantalla_ancho}x{pantalla_alto}")

    tk.Label(root, text="Trabajo Práctico N°4 - Grupo 11", font=("Arial", 16, "bold")).place(x=500, y=10)

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
    entry_reparar_desde.insert(0, "6")
    entry_reparar_desde.place(x=680, y=110)

    tk.Label(root, text="Tiempo Hasta:").place(x=580, y=140)
    entry_reparar_hasta = tk.Entry(root, width=5, justify='center')
    entry_reparar_hasta.insert(0, "10")
    entry_reparar_hasta.place(x=680, y=140)

    tk.Label(root, text="Tomar Café", font=("Arial", 11, "bold")).place(x=750, y=70)

    tk.Label(root, text="Probabilidad:").place(x=740, y=110)
    entry_prob_cafe = tk.Entry(root, width=5, justify='center')
    entry_prob_cafe.insert(0, "0.1")
    entry_prob_cafe.place(x=820, y=110)

    tk.Label(root, text="Demora:").place(x=765, y=140)
    entry_demora_cafe = tk.Entry(root, width=5, justify='center')
    entry_demora_cafe.insert(0, "5")
    entry_demora_cafe.place(x=820, y=140)

    tk.Label(root, text="Tiempo a Simular (min):").place(x=890, y=75)
    entry_tiempo_simular = tk.Entry(root, width=10, justify='center')
    entry_tiempo_simular.place(x=1030, y=75)

    tk.Label(root, text="Mostrar desde:").place(x=920, y=120)
    entry_a = tk.Entry(root, width=10, justify='center')
    entry_a.place(x=1030, y=120)

    tk.Label(root, text="Mostrar hasta:").place(x=920, y=150)
    entry_b = tk.Entry(root, width=10, justify='center')
    entry_b.place(x=1030, y=150)

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

    # Ejecutar la ventana
    root.mainloop()

# Función de simulación
def simular():
    
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

    # Validar las entradas
    if validar_entradas(entry_prob_compra, entry_prob_repara, entry_prob_retira, 
                    entry_cliente_desde, entry_cliente_hasta,
                    entry_venta_desde, entry_venta_hasta,
                    entry_reparar_desde, entry_reparar_hasta,
                    entry_prob_cafe, entry_demora_cafe,
                    entry_tiempo_simular, entry_a, entry_b):

        # Obtener los valores de los parámetros desde la interfaz
        prob_compra = float(entry_prob_compra.get())
        prob_repara = float(entry_prob_repara.get())
        prob_retira = float(entry_prob_retira.get())
        tiempo_llegada_desde = float(entry_cliente_desde.get())
        tiempo_llegada_hasta = float(entry_cliente_hasta.get())
        tiempo_venta_desde = float(entry_venta_desde.get())
        tiempo_venta_hasta = float(entry_venta_hasta.get())
        tiempo_reparar_desde = float(entry_reparar_desde.get())
        tiempo_reparar_hasta = float(entry_reparar_hasta.get())
        prob_cafe = float(entry_prob_cafe.get())
        demora_cafe = float(entry_demora_cafe.get())
        tiempo_simulacion = float(entry_tiempo_simular.get())
        tiempo_tabla_desde = float(entry_a.get())
        tiempo_tabla_hasta = float(entry_b.get())

        # Limpiar la tabla anterior
        for widget in frame_tabla.winfo_children():
            widget.destroy()

        # Limpiar frame_resultados antes de agregar nuevos valores
        for widget in frame_resultados.winfo_children():
            widget.destroy()

        # Crear los encabezados de las columnas
        columnas_fijas = ["Reloj", "Evento", "Próximo Evento", "Random Llegada", "Tiempo entre Llegadas", "Próxima Llegada",
                          "Random Necesidad", "Necesidad Cliente", "Random Venta", "Tiempo Atención", "Fin Atención",
                          "Random Reparación", "Tiempo Reparación", "Fin Reparación", "Random Café", "Toma Café", "Fin Café",
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
        random_cafe = ""
        toma_cafe = ""
        fin_cafe = ""
        ayudante_estado = "Libre"
        cola_ayudante = 0
        relojero_estado = "Libre"
        cola_relojes_reparar = 0 
        cola_relojes_reparados = 3
        clientes_atendidos = 0
        clientes_no_reparados = 0
        tiempo_ocupado_ayudante = 0
        tiempo_ocupado_relojero = 0
        clientes = [0]

        # Generar el primer random de llegada al inicio
        if tiempo_tabla_desde == 0:
            # Fila inicial con los valores iniciales
            fila_inicial = crear_fila(reloj, evento, proximo_evento, random_llegada, tiempo_entre_llegadas, proxima_llegada,
                        random_necesidad, necesidad_cliente, random_venta, tiempo_atencion, fin_atencion, 
                        random_reparacion, tiempo_reparacion, fin_reparacion, random_cafe, toma_cafe, fin_cafe,
                        ayudante_estado, cola_ayudante, relojero_estado, cola_relojes_reparar, cola_relojes_reparados,
                        clientes_atendidos, clientes_no_reparados, tiempo_ocupado_ayudante, tiempo_ocupado_relojero, clientes)
            crear_fila_en_tabla(fila_inicial)

        # Inicializar valores de anteriores
        anterior_reloj = 0
        proximo_tiempo = proxima_llegada
        anterior_proxima_llegada = proxima_llegada
        anterior_fin_atencion = fin_atencion
        anterior_fin_reparacion = fin_reparacion
        anterior_fin_cafe = fin_cafe
        anterior_proximo_evento = proximo_evento
        anterior_necesidad_cliente = necesidad_cliente
        anterior_cola_relojes_reparados = cola_relojes_reparados
        anterior_fin_atencion = fin_atencion
        anterior_fin_reparacion = fin_reparacion
        anterior_random_reparacion = random_reparacion
        anterior_tiempo_reparacion = tiempo_reparacion

        contador = 0
        cliente_sa = 0

        while proximo_tiempo < tiempo_simulacion and  contador < 100000:
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

                random_cafe = generar_random_probabilidad()

                if random_cafe < prob_cafe:
                    toma_cafe = "Si"
                    fin_cafe = reloj + demora_cafe
                    relojero_estado = "TC"
                    random_reparacion = ""  # No se puede reparar durante el café
                    tiempo_reparacion = ""
                    fin_reparacion = ""
                else:
                    toma_cafe = "No"
                    fin_cafe = ""

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

            elif evento == "Fin Cafe":
                random_cafe = ""
                toma_cafe = ""
                fin_cafe = ""
                
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
                if cola_relojes_reparar > 0 and anterior_fin_reparacion == "" and anterior_fin_cafe == "":
                    random_reparacion = generar_random_uniforme()
                    tiempo_reparacion = calcular_random_uniforme(random_reparacion, tiempo_reparar_desde, tiempo_reparar_hasta)
                    fin_reparacion = reloj + tiempo_reparacion
                    relojero_estado = "Ocupado"
                    cola_relojes_reparar -= 1
                else:
                    random_cafe = ""
                    toma_cafe = ""
                    fin_cafe = anterior_fin_cafe
                    random_reparacion = ""
                    tiempo_reparacion = ""
                    fin_reparacion = anterior_fin_reparacion
            
            if evento == "Fin Atencion":
                tiempo_ocupado_ayudante += reloj - anterior_reloj
            elif fin_atencion != "" and random_necesidad == "":
                tiempo_ocupado_ayudante += reloj - anterior_reloj

            if evento == "Fin Reparacion" or evento == "Fin Cafe":
                tiempo_ocupado_relojero += reloj - anterior_reloj
            elif (fin_reparacion != "" and random_reparacion == "") or (fin_cafe != "" and random_cafe == ""):
                tiempo_ocupado_relojero += reloj - anterior_reloj

            # Inicializar los tiempos a infinito si son ""
            tiempo_llegada_cliente = proxima_llegada if proxima_llegada != "" else float('inf')
            tiempo_fin_atencion = fin_atencion if fin_atencion != "" else float('inf')
            tiempo_fin_reparacion = fin_reparacion if fin_reparacion != "" else float('inf')
            tiempo_fin_cafe = fin_cafe if fin_cafe != "" else float('inf')

            # Encontrar el próximo evento y aplicar prioridad en caso de empate
            if tiempo_fin_atencion <= min(tiempo_fin_reparacion, tiempo_fin_cafe, tiempo_llegada_cliente):
                proximo_evento = "Fin Atencion"
                proximo_tiempo = tiempo_fin_atencion
            elif tiempo_fin_reparacion <= min(tiempo_fin_cafe, tiempo_llegada_cliente):
                proximo_evento = "Fin Reparacion"
                proximo_tiempo = tiempo_fin_reparacion
            elif tiempo_fin_cafe <= tiempo_llegada_cliente:
                proximo_evento = "Fin Cafe"
                proximo_tiempo = tiempo_fin_cafe
            else:
                proximo_evento = "Llegada Cliente"
                proximo_tiempo = tiempo_llegada_cliente

            # Actualizar los tiempos anteriores
            anterior_reloj = reloj
            anterior_proxima_llegada = proxima_llegada
            anterior_fin_atencion = fin_atencion
            anterior_fin_reparacion = fin_reparacion
            anterior_fin_cafe = fin_cafe
            anterior_proximo_evento = proximo_evento
            anterior_necesidad_cliente = necesidad_cliente
            anterior_cola_relojes_reparados = cola_relojes_reparados

            if tiempo_tabla_desde <= reloj <= tiempo_tabla_hasta:
                # Crear la nueva fila y agregarla a la simulación
                fila = crear_fila(reloj, evento, proximo_evento, random_llegada, tiempo_entre_llegadas, proxima_llegada,
                        random_necesidad, necesidad_cliente, random_venta, tiempo_atencion, fin_atencion, 
                        random_reparacion, tiempo_reparacion, fin_reparacion, random_cafe, toma_cafe, fin_cafe,
                        ayudante_estado, cola_ayudante, relojero_estado, cola_relojes_reparar, cola_relojes_reparados,
                        clientes_atendidos, clientes_no_reparados, tiempo_ocupado_ayudante, tiempo_ocupado_relojero, clientes)
                crear_fila_en_tabla(fila)

            contador += 1

        print("Simulado correctamente")

        # Cerrar la ventana de carga una vez que la simulación haya terminado
        ventana_carga.destroy()

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


def crear_fila_en_tabla(fila):
    columnas_fijas = ["reloj", "evento", "proximo_evento", "random_llegada", "tiempo_entre_llegadas", "proxima_llegada",
                      "random_necesidad", "necesidad_cliente", "random_venta", "tiempo_atencion", "fin_atencion",
                      "random_reparacion", "tiempo_reparacion", "fin_reparacion", "random_cafe", "toma_cafe", "fin_cafe",
                      "ayudante_estado", "cola_ayudante", "relojero_estado", "cola_relojes_reparar", "cola_relojes_reparados",
                      "clientes_atendidos", "clientes_no_reparados", "tiempo_ocupado_ayudante", "tiempo_ocupado_relojero"]

    # Ajustar la altura de la fila del encabezado
    frame_tabla.grid_rowconfigure(0, minsize=40)  # Asegurar que la primera fila (encabezado) sea más alta

    # Crear los encabezados (solo en la primera fila)
    if len(frame_tabla.winfo_children()) == 0:  # Solo si es la primera fila
        for i, col_name in enumerate(columnas_fijas):
            header = tk.Label(frame_tabla, text=col_name, borderwidth=1, relief="solid")
            header.grid(row=0, column=i, sticky="ewns", ipadx=5, ipady=10)  # ipadx/ipady para ajustar el relleno interno

    # Determinar la fila actual en el frame_tabla
    row_count = (len(frame_tabla.winfo_children()) // len(columnas_fijas)) + 1

    # Crear las celdas de las columnas fijas
    for i, key in enumerate(columnas_fijas):
        valor = fila[key]
        if isinstance(valor, float):
            valor = round(valor, 4)
        label = tk.Label(frame_tabla, text=str(valor), borderwidth=1, relief="solid")
        label.grid(row=row_count, column=i, sticky="nsew")

    # Mostrar los estados de los clientes
    cliente_inicial = fila["clientes"][0]
    for i, cliente_estado in enumerate(fila["clientes"][1:], start=cliente_inicial + 1):
        texto_cliente = f"Cliente {i}: {cliente_estado}" if cliente_estado != "" else ""
        label = tk.Label(frame_tabla, text=texto_cliente, borderwidth=1, relief="solid")
        label.grid(row=row_count, column=len(columnas_fijas) + i - cliente_inicial - 1, sticky="nsew")

    # Ajustar el canvas
    frame_tabla.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
