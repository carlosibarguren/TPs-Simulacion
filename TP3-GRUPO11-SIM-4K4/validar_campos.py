import tkinter as tk
from tkinter import messagebox

def validar_campos(dias, probabilidades_demanda, probabilidades_demora, costos_pedido, intervalo_inicio, intervalo_fin, politica_seleccionada, productos_cada_7_dias=None):
    try:
        # Validar que la cantidad de días a simular no esté vacía y sea un entero positivo mayor a 0
        if not dias:
            raise ValueError("El campo 'Cantidad de días a simular' no puede estar vacío.")
        try:
            dias = int(dias)
        except ValueError:
            raise ValueError("El campo 'Cantidad de días a simular' debe ser un número entero.")
        if dias <= 0:
            raise ValueError("El campo 'Cantidad de días a simular' debe ser un número entero positivo mayor a cero.")

        # Validar probabilidades de demanda
        suma_prob_demanda = 0
        for i, prob in enumerate(probabilidades_demanda):
            if not prob:
                raise ValueError(f"La probabilidad de demanda {i*10} decenas no puede estar vacía.")
            try:
                prob_float = float(prob)
            except ValueError:
                raise ValueError(f"La probabilidad de demanda {i*10} decenas debe ser un número racional.")
            if prob_float < 0 or prob_float > 1:
                raise ValueError(f"La probabilidad de demanda {i*10} decenas debe estar entre 0 y 1.")
            suma_prob_demanda += prob_float

        if round(suma_prob_demanda, 4) != 1:
            raise ValueError("La suma de las probabilidades de demanda debe ser igual a 1.")

        # Validar probabilidades de demora
        suma_prob_demora = 0
        for i, prob in enumerate(probabilidades_demora):
            if not prob:
                raise ValueError(f"La probabilidad de demora de {i+1} día(s) no puede estar vacía.")
            try:
                prob_float = float(prob)
            except ValueError:
                raise ValueError(f"La probabilidad de demora de {i+1} día(s) debe ser un número racional.")
            if prob_float < 0 or prob_float > 1:
                raise ValueError(f"La probabilidad de demora de {i+1} día(s) debe estar entre 0 y 1.")
            suma_prob_demora += prob_float

        if round(suma_prob_demora, 4) != 1:
            raise ValueError("La suma de las probabilidades de demora debe ser igual a 1.")

        # Validar costos de pedido
        for i, costo in enumerate(costos_pedido):
            rango = None
            if i == 0:
                rango = '0 - 100 decenas'
            elif i == 1:
                rango = '101 - 200 decenas'
            else:
                rango = '200+ decenas'
            if not costo:
                raise ValueError(f"El costo de pedido para el rango '{rango}' no puede estar vacío.")
            try:
                costo_float = float(costo)
            except ValueError:
                raise ValueError(f"El costo de pedido para el rango '{rango}' debe ser un número racional.")
            if costo_float <= 0:
                raise ValueError(f"El costo de pedido para el rango '{rango}' debe ser un número racional positivo.")

        # Validar intervalo de filas
        if not intervalo_inicio:
            raise ValueError("El campo 'Intervalo de inicio' no puede estar vacío.")
        if not intervalo_fin:
            raise ValueError("El campo 'Intervalo de fin' no puede estar vacío.")

        try:
            intervalo_inicio = int(intervalo_inicio)
            intervalo_fin = int(intervalo_fin)
        except ValueError:
            raise ValueError("El 'Intervalo de inicio' y 'Intervalo de fin' deben ser números enteros.")

        if intervalo_inicio <= 0:
            raise ValueError("El intervalo de inicio debe ser un número entero positivo mayor a cero.")
        if intervalo_fin <= intervalo_inicio:
            raise ValueError("El intervalo de fin debe ser mayor que el intervalo de inicio.")
        if intervalo_fin > dias:
            raise ValueError(f"El intervalo de fin no puede ser mayor que la cantidad de días generados ({dias}).")

        # Validar campo de productos cada 7 días si se selecciona la política A
        if politica_seleccionada == "A":
            if not productos_cada_7_dias:
                raise ValueError("El campo 'Decenas a comprar cada 7 días' es obligatorio en la Política A.")
            try:
                productos_cada_7_dias = int(productos_cada_7_dias)
            except ValueError:
                raise ValueError("El campo 'Decenas a comprar cada 7 días' debe ser un número entero.")
            if productos_cada_7_dias <= 0:
                raise ValueError("El campo 'Decenas a comprar cada 7 días' debe ser un número entero positivo mayor a cero.")

        # Si todas las validaciones son correctas, retornar True
        return True

    except ValueError as e:
        # Mostrar el mensaje de error en caso de cualquier error de validación
        messagebox.showerror("Error de validación", str(e))
        return False
