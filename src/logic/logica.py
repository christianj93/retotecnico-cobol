import csv
import tkinter as tk
from tkinter import messagebox

def calcular_balance(transacciones):
    """
    Calcula el balance final sumando los montos de las transacciones de tipo "Crédito" 
    y restando los de tipo "Débito".
    """
    balance = 0
    for transaccion in transacciones:
        if transaccion['tipo'] == 'Crédito':
            balance += float(transaccion['monto'])  # Se suman los créditos
        elif transaccion['tipo'] == 'Débito':
            balance -= float(transaccion['monto'])  # Se restan los débitos
    return balance

def transaccion_mayor_monto(transacciones):
    """
    Identifica la transacción de mayor monto.
    Retorna el ID de la transacción y el monto.
    """
    max_transaccion = max(transacciones, key=lambda x: float(x['monto']))
    return max_transaccion['id'], max_transaccion['monto']

def contar_transacciones(transacciones):
    """
    Cuenta las transacciones de tipo "Crédito" y "Débito".
    Retorna un diccionario con el conteo de cada tipo.
    """
    conteo = {'Crédito': 0, 'Débito': 0}
    for transaccion in transacciones:
        if transaccion['tipo'] == 'Crédito':
            conteo['Crédito'] += 1
        elif transaccion['tipo'] == 'Débito':
            conteo['Débito'] += 1
    return conteo

def leer_csv(file_path):
    """
    Lee un archivo CSV que contiene las transacciones.
    Retorna una lista de diccionarios, donde cada diccionario representa una transacción.
    """    
    transacciones = []
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transacciones.append(row)
    return transacciones
    