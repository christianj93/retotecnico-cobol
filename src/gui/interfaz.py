import tkinter as tk
from tkinter import filedialog, messagebox
from src.logic.logica import calcular_balance, transaccion_mayor_monto, contar_transacciones, leer_csv

def cargar_archivo(text_area):
    """
    Abre un cuadro de diálogo para seleccionar un archivo CSV, lee el archivo,
    calcula el balance final, la transacción de mayor monto y el conteo de transacciones.
    Luego, muestra estos resultados en la interfaz gráfica en un área de texto.
    """
    # Seleccionar el archivo CSV
    file_path = filedialog.askopenfilename(title="Selecciona el archivo CSV", filetypes=[("CSV files", "*.csv")])

    # Si no se selecciona un archivo, se termina la ejecución
    if not file_path:
        return

    # Leer el archivo CSV
    transacciones = leer_csv(file_path)

    # Calcular los resultados
    balance = calcular_balance(transacciones)
    transaccion_id, transaccion_monto = transaccion_mayor_monto(transacciones)
    conteo = contar_transacciones(transacciones)

    # Limpiar el área de texto antes de mostrar los resultados
    text_area.delete(1.0, tk.END)

    # Mostrar los resultados en el área de texto
    resultados = (
        f"Reporte de Transacciones\n"
        f"---------------------------------------------\n"
        f"Balance Final: {balance:.2f}\n"
        f"Transacción de Mayor Monto: ID {transaccion_id} - {transaccion_monto}\n"
        f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']} \n"
    )
    text_area.insert(tk.END, resultados)

def salir():
    """Cerrar la aplicación"""
    confirmacion = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
    if confirmacion:
        root.quit()

def iniciar_interfaz():
    """
    Crea y ejecuta la interfaz gráfica utilizando tkinter.
    """
    global root
    root = tk.Tk()
    root.title("Procesador de Transacciones Bancarias")

    # Frame para los resultados
    frame_resultados = tk.Frame(root)
    frame_resultados.pack(pady=10)

    # Botón para cargar el archivo
    boton_cargar = tk.Button(root, text="Cargar CSV", command=lambda: cargar_archivo(text_area))
    boton_cargar.pack(pady=10)    

    # Frame para el área de texto donde se mostrarán los resultados
    frame_texto = tk.Frame(root)
    frame_texto.pack(pady=10)

    # Área de texto para mostrar los resultados
    text_area = tk.Text(frame_texto, width=50, height=10, wrap=tk.WORD)
    text_area.pack()

    # Botón para salir de la aplicación
    boton_salir = tk.Button(root, text="Salir", command=salir)
    boton_salir.pack(pady=5)

    # Ejecutar la interfaz gráfica
    root.mainloop()
