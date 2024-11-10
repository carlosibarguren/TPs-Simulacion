import tkinter as tk
from tkinter import ttk, messagebox
from generador_numeros import generar_aleatorios_uniformes
from transformador_distribuciones import transformar_uniforme, transformar_exponencial, transformar_normal
from gestor_txt import exportar_a_txt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from validar_campos import validar_campos

# Campos que varían según la distribución elegida
entry_uniforme_a = entry_uniforme_b = entry_exponencial = entry_normal_media = entry_normal_desv = None

# Crear la interfaz gráfica principal
def crear_interfaz():

    global root, boton_generar_histograma, boton_generar_tabla, frame_graficos, distribucion_seleccionada, entry_n, intervalos_seleccionados
    
    root = tk.Tk()
    root.title("Trabajo Práctico Nro 2 - Grupo 11")
    root.geometry("1200x800")

    # Título principal centrado en azul oscuro, negrita y fuente Arial
    titulo_label = tk.Label(root, text="Trabajo Práctico Nro 2 - Grupo 11", font=("Arial", 20, "bold"), fg="#111111")
    titulo_label.pack(pady=20)

    # Crear frame principal para inputs y gráfico
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame para los inputs a la izquierda
    frame_inputs = tk.Frame(main_frame)
    frame_inputs.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=(50, 0))

    # Selección de distribución
    ttk.Label(frame_inputs, text="Seleccione la distribución:", font=("Arial", 10)).grid(column=0, row=1, padx=5, pady=5)
    distribucion_seleccionada = ttk.Combobox(frame_inputs, values=['Uniforme', 'Exponencial', 'Normal'], font=("Arial", 10))
    distribucion_seleccionada.grid(column=0, row=2, padx=5, pady=5)
    distribucion_seleccionada.config(state="readonly")
    distribucion_seleccionada.bind("<<ComboboxSelected>>", lambda e: actualizar_campos(distribucion_seleccionada.get(), frame_campos))

    # Tamaño de la muestra
    ttk.Label(frame_inputs, text="Tamaño de la muestra:", font=("Arial", 10)).grid(column=0, row=3, padx=5, pady=5)
    entry_n = ttk.Entry(frame_inputs, font=("Arial", 10))
    entry_n.grid(column=0, row=4, padx=5, pady=5)

    # Frame para campos adicionales (Uniforme, Exponencial, Normal)
    frame_campos = ttk.Frame(frame_inputs)
    frame_campos.grid(column=0, row=5, padx=5, pady=5)

    # Botón para generar números aleatorios
    boton_generar_numeros = tk.Button(frame_inputs, text="Generar Números Aleatorios", command=generar_numeros_aleatorios, bg="#111111", fg="white", font=("Arial", 10))
    boton_generar_numeros.grid(column=0, row=6, padx=5, pady=5)

    # Crear frame para botones
    frame_botones = tk.Frame(frame_inputs)
    frame_botones.grid(column=0, row=7, padx=5, pady=10)

    # Selección del número de intervalos
    ttk.Label(frame_botones, text="Intervalos:", font=("Arial", 10)).grid(column=0, row=1, padx=5, pady=5)
    intervalos_seleccionados = ttk.Combobox(frame_botones, values=['5', '10', '15', '20'], font=("Arial", 10))
    intervalos_seleccionados.grid(column=1, row=1, padx=5, pady=5)
    intervalos_seleccionados.current(0)
    intervalos_seleccionados.config(state="readonly")

    # Botón para generar el histograma (Inicialmente deshabilitado)
    boton_generar_histograma = tk.Button(frame_botones, text="Histograma", command=mostrar_histograma, bg="#CBCBCB", fg="black", font=("Arial", 10), state=tk.DISABLED)
    boton_generar_histograma.grid(column=0, row=2, padx=5, pady=5)

    # Botón para generar la tabla de frecuencias (Inicialmente deshabilitado)
    boton_generar_tabla = tk.Button(frame_botones, text="Tabla de Frecuencias", command=mostrar_tabla, bg="#CBCBCB", fg="black", font=("Arial", 10), state=tk.DISABLED)
    boton_generar_tabla.grid(column=1, row=2, padx=5, pady=5)

    # Botón para cerrar la aplicación (debajo de los botones de la izquierda)
    cerrar_button = tk.Button(frame_inputs, text="Cerrar", command=root.quit, bg="#B21E1E", fg="white", font=("Arial", 10))
    cerrar_button.grid(column=0, row=10, padx=5, pady=10)

    # Frame para los gráficos a la derecha de los inputs
    frame_graficos = tk.Frame(main_frame)
    frame_graficos.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=175, pady=20)

    root.mainloop()


# Función para actualizar los campos según la distribución seleccionada
def actualizar_campos(distribucion, frame_campos):
    
    # Limpiar los campos adicionales existentes
    for widget in frame_campos.winfo_children():
        widget.destroy()

    global entry_uniforme_a, entry_uniforme_b, entry_exponencial, entry_normal_media, entry_normal_desv

    #Crear los campos según la distribución elegida
    if distribucion == 'Uniforme':
        ttk.Label(frame_campos, text="Valor de a:", font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5)
        entry_uniforme_a = ttk.Entry(frame_campos)
        entry_uniforme_a.grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(frame_campos, text="Valor de b:", font=("Arial", 10)).grid(column=0, row=1, padx=5, pady=5)
        entry_uniforme_b = ttk.Entry(frame_campos)
        entry_uniforme_b.grid(column=1, row=1, padx=5, pady=5)

    elif distribucion == 'Exponencial':
        ttk.Label(frame_campos, text="Lambda (escala):", font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5)
        entry_exponencial = ttk.Entry(frame_campos)
        entry_exponencial.grid(column=1, row=0, padx=5, pady=5)

    elif distribucion == 'Normal':
        ttk.Label(frame_campos, text="Media:", font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5)
        entry_normal_media = ttk.Entry(frame_campos)
        entry_normal_media.grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(frame_campos, text="Desviación Estándar:", font=("Arial", 10)).grid(column=0, row=1, padx=5, pady=5)
        entry_normal_desv = ttk.Entry(frame_campos)
        entry_normal_desv.grid(column=1, row=1, padx=5, pady=5)


# Función para generar números aleatorios
def generar_numeros_aleatorios():
    
    global serie_generada

    # Limpiar cualquier gráfico o tabla anterior
    for widget in frame_graficos.winfo_children():
        widget.destroy()

    # Validar los campos antes de continuar
    if not validar_campos(distribucion_seleccionada, entry_n, entry_uniforme_a, entry_uniforme_b, entry_exponencial, entry_normal_media, entry_normal_desv):
        return

    n = int(entry_n.get())
    
    # Generar los números aleatorios entre 0 y 1
    serie_inicial = generar_aleatorios_uniformes(n)

    if distribucion_seleccionada.get() == 'Uniforme':
        a = float(entry_uniforme_a.get())
        b = float(entry_uniforme_b.get())
        serie_generada = transformar_uniforme(serie_inicial, a, b)
    elif distribucion_seleccionada.get() == 'Exponencial':
        lambd = float(entry_exponencial.get())
        serie_generada = transformar_exponencial(serie_inicial, lambd)
    elif distribucion_seleccionada.get() == 'Normal':
        media = float(entry_normal_media.get())
        desv = float(entry_normal_desv.get())
        serie_generada = transformar_normal(serie_inicial, media, desv)

    # Habilitar botones después de generar los números
    boton_generar_histograma.config(state=tk.NORMAL, bg="#494949", fg="white")
    boton_generar_tabla.config(state=tk.NORMAL, bg="#494949", fg="white")

    # Exportar Números Aleatorios al TXT
    exportar_a_txt(serie_inicial) 

    # Mensaje de Éxito
    messagebox.showinfo("Éxito", "Los números aleatorios se han generado correctamente.")


# Función para mostrar el histograma a partir de los números generados
def mostrar_histograma():

    global serie_generada
    
    intervalos = int(intervalos_seleccionados.get())
    fig, ax = plt.subplots(figsize=(8, 5))

    counts, bins, patches = ax.hist(serie_generada, bins=intervalos, edgecolor='black')
    ax.set_ylim(0, max(counts) * 1.15)

    for count, bin_edge in zip(counts, bins):
        label = f'{int(count)}'
        ax.text(bin_edge + (bins[1] - bins[0]) / 2, count + max(counts) * 0.01, label, ha='center', va='bottom', rotation=90)

    ax.set_xticks(bins)
    ax.set_xticklabels([f'{tick:.2f}' for tick in bins], rotation=90)
    ax.set_title(f'Histograma de la Distribución con {intervalos} Intervalos', pad=20)
    ax.set_xlabel('Valores', labelpad=20)
    ax.set_ylabel('Frecuencia')

    plt.subplots_adjust(bottom=0.2)
    ax.grid(True)

    # Se actualiza el gráfico en el área correcta
    for widget in frame_graficos.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame_graficos)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Función para calcular la tabla de frecuencias
def calcular_tabla_frecuencias(series, intervalos):
    counts, bins = np.histogram(series, bins=intervalos)
    tabla_frecuencias = []
    for i in range(len(bins) - 1):
        lim_inferior = round(bins[i], 4)  # 4 decimales en límite inferior
        lim_superior = round(bins[i+1], 4)  # 4 decimales en límite superior
        frecuencia = int(counts[i])  # Convertir frecuencia a int
        tabla_frecuencias.append((lim_inferior, lim_superior, frecuencia))
    return tabla_frecuencias


# Función para mostrar la tabla de frecuencias a partir de los números generados
def mostrar_tabla():
    
    global serie_generada

    intervalos = int(intervalos_seleccionados.get())
    tabla_frecuencias = calcular_tabla_frecuencias(serie_generada, intervalos)
    
    # Limpiar cualquier widget anterior en el frame de gráficos
    for widget in frame_graficos.winfo_children():
        widget.destroy()

    # Crear un Treeview para mostrar la tabla con estilo
    tree = ttk.Treeview(frame_graficos, columns=("Corchete", "Límite Inferior", "Límite Superior", "Paréntesis", "Frecuencia"), show="headings", height=20)
    
    # Configurar encabezados de las columnas
    tree.heading("Corchete", text="")
    tree.heading("Límite Inferior", text="Límite Inferior")
    tree.heading("Límite Superior", text="Límite Superior")
    tree.heading("Paréntesis", text="")
    tree.heading("Frecuencia", text="Frecuencia")

    # Configurar las columnas para que los datos estén centrados
    tree.column("Corchete", anchor="center", width=20)
    tree.column("Límite Inferior", anchor="center", width=150)
    tree.column("Límite Superior", anchor="center", width=150)
    tree.column("Paréntesis", anchor="center", width=20)
    tree.column("Frecuencia", anchor="center", width=100)

    # Insertar los datos en la tabla
    for lim_inferior, lim_superior, frecuencia in tabla_frecuencias:
        tree.insert("", "end", values=("[", f"{lim_inferior:.4f}", f"{lim_superior:.4f}", ")", frecuencia))

    # Añadir líneas separadoras entre las filas
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"), anchor="center")
    style.configure("Treeview", rowheight=25, font=("Arial", 10), borderwidth=1, relief="solid")

    # Mostrar la tabla
    tree.grid(row=0, column=0, columnspan=5, sticky='nsew')

    # Botón para copiar la tabla a Excel
    boton_exportar_excel = tk.Button(frame_graficos, text="Copiar Tabla a Excel", command=lambda: exportar_tabla_frecuencias_a_excel(tabla_frecuencias), bg="#494949", fg="white", font=("Arial", 10))
    boton_exportar_excel.grid(row=1, column=0, columnspan=5, pady=10)


# Función para exportar la tabla de frecuencias a excel
def exportar_tabla_frecuencias_a_excel(tabla_frecuencias):
    tabla_texto = "Límite Inferior\tLímite Superior\tFrecuencia\n"
    for lim_inferior, lim_superior, frecuencia in tabla_frecuencias:
        # Reemplazar puntos por comas para que Excel lo reconozca como float
        lim_inferior_str = f"{lim_inferior:.4f}".replace(".", ",")
        lim_superior_str = f"{lim_superior:.4f}".replace(".", ",")
        tabla_texto += f"{lim_inferior_str}\t{lim_superior_str}\t{frecuencia}\n"
    
    # Copiar la tabla al portapapeles
    root.clipboard_clear()
    root.clipboard_append(tabla_texto)
    messagebox.showinfo("Tabla copiada", "La tabla de frecuencias ha sido copiada al portapapeles. Puedes pegarla en Excel.")

