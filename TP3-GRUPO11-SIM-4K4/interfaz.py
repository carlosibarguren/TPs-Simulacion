import tkinter as tk
from tkinter import ttk
from simulacion import simular_politica_a, simular_politica_b
from validar_campos import validar_campos

def cerrar_app():
    root.destroy()  # Cierra la aplicación

def ejecutar_simulacion():
    # Obtener los valores de los campos
    dias = entry_dias.get()
    
    intervalo_inicio = entry_intervalo_inicio.get()
    intervalo_fin = entry_intervalo_fin.get()

    probabilidades_demanda = [
        entry_prob_0.get(),
        entry_prob_10.get(),
        entry_prob_20.get(),
        entry_prob_30.get(),
        entry_prob_40.get(),
        entry_prob_50.get()
    ]

    probabilidades_demora = [
        entry_prob_1d.get(),
        entry_prob_2d.get(),
        entry_prob_3d.get(),
        entry_prob_4d.get()
    ]

    costos_pedido = [
        entry_costo_0_100.get(),
        entry_costo_101_200.get(),
        entry_costo_200_mas.get()
    ]

    politica_seleccionada = politica_var.get()

    if politica_seleccionada == "A":
        productos_cada_7_dias = entry_productos_cada_7_dias.get()
    else:
        productos_cada_7_dias = None

    # Validar los campos
    if validar_campos(dias, probabilidades_demanda, probabilidades_demora, costos_pedido, intervalo_inicio, intervalo_fin, politica_seleccionada, productos_cada_7_dias):
        # Continuar con la simulación si la validación es exitosa
        
        # Convertir a enteros
        dias = int(dias)
        intervalo_inicio = int(intervalo_inicio)
        intervalo_fin = int(intervalo_fin)

        # Validacion para no mostrar la ultima fila dos veces
        if dias == intervalo_fin:
            intervalo_fin -= 1

        # Probabilidades de demanda
        probabilidades_demanda = [
            float(entry_prob_0.get()),
            float(entry_prob_10.get()),
            float(entry_prob_20.get()),
            float(entry_prob_30.get()),
            float(entry_prob_40.get()),
            float(entry_prob_50.get())
        ]
        
        # Probabilidades de demora
        probabilidades_demora = [
            float(entry_prob_1d.get()),
            float(entry_prob_2d.get()),
            float(entry_prob_3d.get()),
            float(entry_prob_4d.get())
        ]
        
        # Costos de pedido
        costos_pedido = [
            float(entry_costo_0_100.get()),
            float(entry_costo_101_200.get()),
            float(entry_costo_200_mas.get())
        ]

        if politica_seleccionada == "A":
            productos_cada_7_dias = int(productos_cada_7_dias)  # Convertir a entero
            resultado = simular_politica_a(dias, 20, probabilidades_demanda, probabilidades_demora, costos_pedido[0], costos_pedido[1], costos_pedido[2], productos_cada_7_dias)
        else:
            resultado = simular_politica_b(dias, 20, probabilidades_demanda, probabilidades_demora, costos_pedido[0], costos_pedido[1], costos_pedido[2])

        # Mostrar los resultados en la tabla
        tree.delete(*tree.get_children())  # Aquí usamos la tabla 'tree'
        for fila in resultado[intervalo_inicio-1:intervalo_fin] + [resultado[-1]]:
            tree.insert("", tk.END, values=(
                fila['Día'], fila['Random Demanda'], fila['Demanda'], fila['Ventas'], fila['Stock Inicial'], fila['Ruptura'],
                fila['Compra'], fila['Cantidad Comprada'], fila['Random Demora'], fila['Demora'], 
                fila['Disponible'], fila['Costo Almacenamiento'], fila['Costo Pedido'], fila['Costo Ruptura'], fila['Costo Acumulado'], fila['Costo Medio']
            ))

def mostrar_campo_productos():
    # Mostrar o esconder el campo de productos según la política seleccionada
    if politica_var.get() == "A":
        label_productos_cada_7_dias.grid(row=0, column=7, padx=10)
        entry_productos_cada_7_dias.grid(row=0, column=8)
    else:
        label_productos_cada_7_dias.grid_remove()  # Esconder el campo si no es política A
        entry_productos_cada_7_dias.grid_remove()


def crear_interfaz():
    global root, tree  # Declarar tree como global para usarla en otras funciones
    root = tk.Tk()
    root.state('zoomed')
    root.title("Trabajo Práctico Nº3 - Grupo 11")
    
    # Título
    label_titulo = tk.Label(root, text="Trabajo Práctico Nº3 - Grupo 11", font=("Arial", 16))
    label_titulo.pack(pady=10)
    
    # Crear un frame para la fila con los campos de política, días a simular y el intervalo
    frame_campos = tk.Frame(root)
    frame_campos.pack(pady=10)

    # Selector de política, días, productos a comprar e intervalo en la primera fila (arriba de todo)
    global politica_var
    politica_var = tk.StringVar()
    label_politica = tk.Label(frame_campos, text="Seleccione la Política:")
    label_politica.grid(row=0, column=0, padx=10)
    
    combo_politica = ttk.Combobox(frame_campos, textvariable=politica_var, state="readonly")
    combo_politica['values'] = ("A", "B")  
    combo_politica.grid(row=0, column=1)
    combo_politica.current(0)  # Seleccionar el valor "A" como predeterminado
    combo_politica.bind("<<ComboboxSelected>>", lambda event: mostrar_campo_productos())


    # Campo para días a simular
    label_dias = tk.Label(frame_campos, text="Días a Simular:")
    label_dias.grid(row=0, column=2, padx=10)
    global entry_dias
    entry_dias = tk.Entry(frame_campos, width=10)
    entry_dias.grid(row=0, column=3)

    # Intervalo de filas a mostrar
    label_intervalo = tk.Label(frame_campos, text="Filas a Mostrar (Inicio - Fin):")
    label_intervalo.grid(row=0, column=4, padx=10)
    global entry_intervalo_inicio, entry_intervalo_fin
    entry_intervalo_inicio = tk.Entry(frame_campos, width=10)
    entry_intervalo_inicio.grid(row=0, column=5)
    entry_intervalo_fin = tk.Entry(frame_campos, width=10)
    entry_intervalo_fin.grid(row=0, column=6)

    # Campo para productos a comprar (solo para política A)
    global label_productos_cada_7_dias, entry_productos_cada_7_dias
    label_productos_cada_7_dias = tk.Label(frame_campos, text="Cantidad a Comprar:")
    entry_productos_cada_7_dias = tk.Entry(frame_campos, width=10)
    entry_productos_cada_7_dias.insert(0, "180")
    label_productos_cada_7_dias.grid(row=0, column=7, padx=10)
    entry_productos_cada_7_dias.grid(row=0, column=8)

    # Crear un frame para las tablas de probabilidades y costos
    frame_tablas = tk.Frame(root)
    frame_tablas.pack(pady=10)

    # Tabla de Probabilidades de Demanda
    frame_probabilidades = tk.Frame(frame_tablas)
    frame_probabilidades.grid(row=0, column=0, padx=20)
    label_probabilidades = tk.Label(frame_probabilidades, text="Probabilidades Demanda")
    label_probabilidades.grid(row=0, column=0, columnspan=2)

    global entry_prob_0, entry_prob_10, entry_prob_20, entry_prob_30, entry_prob_40, entry_prob_50
    entry_prob_0 = tk.Entry(frame_probabilidades, width=5)
    entry_prob_0.grid(row=1, column=1)
    entry_prob_0.insert(0, "0.05")
    label_0 = tk.Label(frame_probabilidades, text="0 decenas")
    label_0.grid(row=1, column=0)

    entry_prob_10 = tk.Entry(frame_probabilidades, width=5)
    entry_prob_10.grid(row=2, column=1)
    entry_prob_10.insert(0, "0.12")
    label_10 = tk.Label(frame_probabilidades, text="10 decenas")
    label_10.grid(row=2, column=0)

    entry_prob_20 = tk.Entry(frame_probabilidades, width=5)
    entry_prob_20.grid(row=3, column=1)
    entry_prob_20.insert(0, "0.18")
    label_20 = tk.Label(frame_probabilidades, text="20 decenas")
    label_20.grid(row=3, column=0)

    entry_prob_30 = tk.Entry(frame_probabilidades, width=5)
    entry_prob_30.grid(row=4, column=1)
    entry_prob_30.insert(0, "0.25")
    label_30 = tk.Label(frame_probabilidades, text="30 decenas")
    label_30.grid(row=4, column=0)

    entry_prob_40 = tk.Entry(frame_probabilidades, width=5)
    entry_prob_40.grid(row=5, column=1)
    entry_prob_40.insert(0, "0.22")
    label_40 = tk.Label(frame_probabilidades, text="40 decenas")
    label_40.grid(row=5, column=0)

    entry_prob_50 = tk.Entry(frame_probabilidades, width=5)
    entry_prob_50.grid(row=6, column=1)
    entry_prob_50.insert(0, "0.18")
    label_50 = tk.Label(frame_probabilidades, text="50 decenas")
    label_50.grid(row=6, column=0)

    # Tabla de Probabilidades de Demora
    frame_demora = tk.Frame(frame_tablas)
    frame_demora.grid(row=0, column=1, padx=20)
    label_demora = tk.Label(frame_demora, text="Probabilidades Demora")
    label_demora.grid(row=0, column=0, columnspan=2)

    global entry_prob_1d, entry_prob_2d, entry_prob_3d, entry_prob_4d
    entry_prob_1d = tk.Entry(frame_demora, width=5)
    entry_prob_1d.grid(row=1, column=1)
    entry_prob_1d.insert(0, "0.15")
    label_1d = tk.Label(frame_demora, text="1 día")
    label_1d.grid(row=1, column=0)

    entry_prob_2d = tk.Entry(frame_demora, width=5)
    entry_prob_2d.grid(row=2, column=1)
    entry_prob_2d.insert(0, "0.20")
    label_2d = tk.Label(frame_demora, text="2 días")
    label_2d.grid(row=2, column=0)

    entry_prob_3d = tk.Entry(frame_demora, width=5)
    entry_prob_3d.grid(row=3, column=1)
    entry_prob_3d.insert(0, "0.40")
    label_3d = tk.Label(frame_demora, text="3 días")
    label_3d.grid(row=3, column=0)

    entry_prob_4d = tk.Entry(frame_demora, width=5)
    entry_prob_4d.grid(row=4, column=1)
    entry_prob_4d.insert(0, "0.25")
    label_4d = tk.Label(frame_demora, text="4 días")
    label_4d.grid(row=4, column=0)

    # Tabla de Costos Pedido
    frame_costos = tk.Frame(frame_tablas)
    frame_costos.grid(row=0, column=2, padx=20)
    label_costos = tk.Label(frame_costos, text="Costos Pedido")
    label_costos.grid(row=0, column=0, columnspan=2)

    global entry_costo_0_100, entry_costo_101_200, entry_costo_200_mas
    
    label_costo_0_100 = tk.Label(frame_costos, text="0 - 100 decenas")
    label_costo_0_100.grid(row=1, column=0)
    entry_costo_0_100 = tk.Entry(frame_costos, width=8)
    entry_costo_0_100.grid(row=1, column=1)
    entry_costo_0_100.insert(0, "2000")

    
    label_costo_101_200 = tk.Label(frame_costos, text="101 - 200 decenas")
    label_costo_101_200.grid(row=2, column=0)
    entry_costo_101_200 = tk.Entry(frame_costos, width=8)
    entry_costo_101_200.grid(row=2, column=1)
    entry_costo_101_200.insert(0, "2800")

    
    label_costo_200_mas = tk.Label(frame_costos, text="200+ decenas")
    label_costo_200_mas.grid(row=3, column=0)
    entry_costo_200_mas = tk.Entry(frame_costos, width=8)
    entry_costo_200_mas.grid(row=3, column=1)
    entry_costo_200_mas.insert(0, "3000")

    # Botones
    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=10)
    
    btn_simular = tk.Button(frame_botones, text="Ejecutar Simulación", command=ejecutar_simulacion, fg='white', bg='#383838')
    btn_simular.pack(side="left", padx=5)

    btn_cerrar = tk.Button(frame_botones, text="Cerrar", command=cerrar_app, fg="white", bg="red")
    btn_cerrar.pack(side="right", padx=5)

    # Crear una tabla para mostrar los resultados con scrollbars
    frame_tabla = tk.Frame(root)
    frame_tabla.pack(pady=10, fill=tk.BOTH, expand=True)

    scrollbar_y = tk.Scrollbar(frame_tabla, orient=tk.VERTICAL)
    scrollbar_x = tk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL)

    tree = ttk.Treeview(frame_tabla, columns=(
        "Día", "Random Demanda", "Demanda", "Ventas", "Stock Inicial", "Ruptura", "Compra", 
        "Cantidad a Comprar", "Random Demora", "Demora", "Disponible", 
        "Costo Almacenamiento", "Costo Pedido", "Costo Ruptura", "Costo Acumulado", "Costo Medio"
    ), show="headings", yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    
    scrollbar_y.config(command=tree.yview)
    scrollbar_x.config(command=tree.xview)

    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    tree.pack(fill=tk.BOTH, expand=True)

    # Definir encabezados y tamaños de las columnas
    for col in tree["columns"] :
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)


    root.mainloop()
