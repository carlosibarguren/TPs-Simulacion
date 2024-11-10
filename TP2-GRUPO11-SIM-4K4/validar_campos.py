from tkinter import messagebox

# Función para validar que los campos ingresados sean correctos (números, etc.)
def validar_campos(distribucion_seleccionada, entry_n, entry_uniforme_a, entry_uniforme_b, entry_exponencial, entry_normal_media, entry_normal_desv):
    try:
        # Verificar que se haya seleccionado una distribución
        if not distribucion_seleccionada.get():
            raise ValueError("Debe seleccionar una distribución.")
        
        # Validar que n sea un entero
        n = entry_n.get()
        if not n.isdigit():
            raise ValueError("El tamaño de la muestra debe ser un número entero positivo.")
        n = int(n)
        if n <= 0:
            raise ValueError("El tamaño de la muestra debe ser positivo.")
        
        
        # Validar que a y b sean floats en Uniforme
        if distribucion_seleccionada.get() == 'Uniforme':
            a = entry_uniforme_a.get()
            b = entry_uniforme_b.get()
            if not is_float(a) or not is_float(b):
                raise ValueError("Los valores de 'a' y 'b' deben ser números.")
            a = float(a)
            b = float(b)
            if a >= b:
                raise ValueError("El valor de 'b' debe ser mayor que 'a'.")
        
        # Validar que lambda sea float en Exponencial
        elif distribucion_seleccionada.get() == 'Exponencial':
            lambd = entry_exponencial.get()
            if not is_float(lambd):
                raise ValueError("Lambda debe ser un número.")
            lambd = float(lambd)
            if lambd <= 0:
                raise ValueError("Lambda debe ser mayor que cero.")
        
        # Validar que media y desviación sean floats en Normal
        elif distribucion_seleccionada.get() == 'Normal':
            media = entry_normal_media.get()
            desv = entry_normal_desv.get()
            if not is_float(media) or not is_float(desv):
                raise ValueError("Los valores de media y desviación estándar deben ser números.")
            media = float(media)
            desv = float(desv)
            if desv <= 0:
                raise ValueError("La desviación estándar debe ser mayor que cero.")
        
        return True
    except ValueError as e:
        messagebox.showerror("Error de Validación", str(e))
        return False

# Función auxiliar para verificar si una cadena puede ser convertida a float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
