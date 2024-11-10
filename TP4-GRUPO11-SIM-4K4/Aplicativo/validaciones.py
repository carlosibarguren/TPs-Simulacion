import tkinter as tk
from tkinter import messagebox

def validar_float(entry, nombre_campo):
    """Función para validar si una entrada es un float y no está vacía"""
    try:
        valor = float(entry.get())
        return valor
    except ValueError:
        if entry.get() == "":
            messagebox.showerror("Error de validación", f"El campo '{nombre_campo}' no puede estar vacío.")
        else:
            messagebox.showerror("Error de validación", f"El valor en el campo '{nombre_campo}' debe ser un número decimal válido (float).")
        return None  # Devolver None si hay un error para que el flujo se controle adecuadamente
    
def validar_int(entry, nombre_campo):
    """Función para validar si una entrada es un integer y no está vacía"""
    try:
        valor = int(entry.get())
        return valor
    except ValueError:
        if entry.get() == "":
            messagebox.showerror("Error de validación", f"El campo '{nombre_campo}' no puede estar vacío.")
        else:
            messagebox.showerror("Error de validación", f"El valor en el campo '{nombre_campo}' debe ser un número entero (int).")
        return None  # Devolver None si hay un error para que el flujo se controle adecuadamente


def validar_entradas(entry_prob_compra, entry_prob_repara, entry_prob_retira,
                     entry_cliente_desde, entry_cliente_hasta,
                     entry_venta_desde, entry_venta_hasta,
                     entry_reparar_desde, entry_reparar_hasta,
                     entry_prob_cafe, entry_demora_cafe,
                     entry_tiempo_simular, entry_a, entry_b):
    
    try:
        # Validar que cada campo es un float y no está vacío
        prob_compra = validar_float(entry_prob_compra, "Probabilidad de Compra")
        prob_repara = validar_float(entry_prob_repara, "Probabilidad de Reparación")
        prob_retira = validar_float(entry_prob_retira, "Probabilidad de Retiro")
        cliente_desde = validar_float(entry_cliente_desde, "Cliente Desde")
        cliente_hasta = validar_float(entry_cliente_hasta, "Cliente Hasta")
        venta_desde = validar_float(entry_venta_desde, "Venta Desde")
        venta_hasta = validar_float(entry_venta_hasta, "Venta Hasta")
        reparar_desde = validar_float(entry_reparar_desde, "Reparar Desde")
        reparar_hasta = validar_float(entry_reparar_hasta, "Reparar Hasta")
        prob_cafe = validar_float(entry_prob_cafe, "Probabilidad de Café")
        demora_cafe = validar_float(entry_demora_cafe, "Demora de Café")
        tiempo_simular = validar_float(entry_tiempo_simular, "Tiempo a Simular")
        valor_a = validar_float(entry_a, "Valor A")
        valor_b = validar_int(entry_b, "Valor B")

        # Si algún campo no es válido, retornar False
        if None in [prob_compra, prob_repara, prob_retira, cliente_desde, cliente_hasta,
                    venta_desde, venta_hasta, reparar_desde, reparar_hasta, prob_cafe,
                    demora_cafe, tiempo_simular, valor_a, valor_b]:
            return False

        # Validar que las probabilidades sumen 1 y que no sean negativas
        if prob_compra + prob_repara + prob_retira != 1:
            raise ValueError("La suma de las probabilidades de compra, reparación y retiro debe ser exactamente 1.")
        if prob_compra < 0:
            raise ValueError("La probabilidad de compra no puede ser negativa.")
        if prob_repara < 0:
            raise ValueError("La probabilidad de reparación no puede ser negativa.")
        if prob_retira < 0:
            raise ValueError("La probabilidad de retiro no puede ser negativa.")

        # Validar cliente desde y hasta
        if cliente_desde < 0:
            raise ValueError("'Cliente Desde' no puede ser menor a 0.")
        if cliente_desde >= cliente_hasta:
            raise ValueError("'Cliente Desde' debe ser menor que 'Cliente Hasta'.")

        # Validar venta desde y hasta
        if venta_desde < 0:
            raise ValueError("'Venta Desde' no puede ser menor a 0.")
        if venta_desde >= venta_hasta:
            raise ValueError("'Venta Desde' debe ser menor que 'Venta Hasta'.")

        # Validar reparar desde y hasta
        if reparar_desde < 0:
            raise ValueError("'Reparar Desde' no puede ser menor a 0.")
        if reparar_desde >= reparar_hasta:
            raise ValueError("'Reparar Desde' debe ser menor que 'Reparar Hasta'.")

        # Validar probabilidad de café
        if not (0 <= prob_cafe <= 1):
            raise ValueError("La probabilidad de café debe estar entre 0 y 1.")

        # Validar demora del café
        if demora_cafe < 0:
            raise ValueError("La demora del café no puede ser menor a 0.")

        # Validar tiempo a simular
        if tiempo_simular < 0:
            raise ValueError("El tiempo a simular no puede ser menor a 0.")

        # Validar a y b
        if valor_a < 0:
            raise ValueError("'Mostrar Desde' no puede ser menor a 0.")
        if valor_a > tiempo_simular:
            raise ValueError("'Mostrar Desde' no puede ser mayor que el tiempo a simular.")

        return True  # Si todo está bien, devolver True

    except ValueError as e:
        # Mostrar un mensaje de error con Tkinter si alguna validación falla
        messagebox.showerror("Error de validación", str(e))
        return False
