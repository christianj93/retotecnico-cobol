import csv
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class ProcesadorTransacciones:
    def __init__(self):
        self.balance = 0.0
        self.transaccion_mayor = {"id": None, "monto": float('-inf')}
        self.conteo = {"Crédito": 0, "Débito": 0}
    
    def procesar_csv(self, archivo_csv):
        try:
            with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
                lector = csv.DictReader(csvfile)
                for fila in lector:
                    tipo = fila['tipo']
                    monto = float(fila['monto'])
                    transaccion_id = fila['id']
                    
                    if tipo == "Crédito":
                        self.balance += monto
                        self.conteo["Crédito"] += 1
                    elif tipo == "Débito":
                        self.balance -= monto
                        self.conteo["Débito"] += 1
                    
                    if monto > self.transaccion_mayor["monto"]:
                        self.transaccion_mayor = {"id": transaccion_id, "monto": monto}
            return True
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo no encontrado.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
            return False
    
    def obtener_reporte(self):
        return (
            f"Balance Final: {self.balance:.2f}\n"
            f"Transacción de Mayor Monto: ID {self.transaccion_mayor['id']} - {self.transaccion_mayor['monto']:.2f}\n"
            f"Conteo de Créditos: {self.conteo['Crédito']}\n"
            f"Conteo de Débitos: {self.conteo['Débito']}"
        )

class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Transacciones")
        self.root.geometry("500x400")
        
        self.procesador = ProcesadorTransacciones()
        
        self.label = tk.Label(root, text="Seleccione un archivo CSV:")
        self.label.pack(pady=10)
        
        self.boton_cargar = tk.Button(root, text="Cargar CSV", command=self.cargar_csv)
        self.boton_cargar.pack(pady=5)
        
        self.texto_resultado = tk.Text(root, height=10, width=50, wrap=tk.WORD)
        self.texto_resultado.pack(pady=10)
        
        self.boton_salir = tk.Button(root, text="Salir", command=root.quit)
        self.boton_salir.pack(pady=5)
    
    def cargar_csv(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if archivo:
            if self.procesador.procesar_csv(archivo):
                reporte = self.procesador.obtener_reporte()
                self.texto_resultado.delete("1.0", tk.END)
                self.texto_resultado.insert(tk.END, reporte)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()
