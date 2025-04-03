import sys
import os

# Agregar la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.gui.interfaz import iniciar_interfaz

# Función principal que invoca la interfaz gráfica
def main():
    iniciar_interfaz()

# Ejecutar el programa
if __name__ == "__main__":
    main()
