import os

# Función para generar un archivo de texto con los números aleatorios
def exportar_a_txt(series):
    # Definir la ruta del archivo donde se guardará el archivo de texto
    filepath = os.path.join(os.getcwd(), "numeros_aleatorios.txt")

    # Abrir el archivo en modo escritura ('w') y escribir los valores
    with open(filepath, 'w') as f:
        for valor in series:
            # Reemplazar puntos por comas y escribir cada valor en una nueva línea
            f.write(f"{valor:.4f}".replace(".", ",") + "\n")
    