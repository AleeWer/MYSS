import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# Coeficientes e interceptos obtenidos de la regresión
coef_DQO_salida = [0.2474, 1.2693, 0.3418, -0.2932]
intercept_DQO_salida = 927.32

coef_Temperatura_salida = [-0.0029, 0.0350, 0.0182, -0.0057]
intercept_Temperatura_salida = 32.34

coef_VFA_salida = [0.0235, 1.3224, 0.5286, -0.3056]
intercept_VFA_salida = 880.40

# Función para calcular DQO_salida
def calcular_DQO_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada):
    return (coef_DQO_salida[0] * DQO_entrada +
            coef_DQO_salida[1] * Temperatura_entrada +
            coef_DQO_salida[2] * VFA_entrada +
            coef_DQO_salida[3] * flujo_reactor_entrada +
            intercept_DQO_salida)

# Función para calcular Temperatura_salida
def calcular_Temperatura_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada):
    return (coef_Temperatura_salida[0] * DQO_entrada +
            coef_Temperatura_salida[1] * Temperatura_entrada +
            coef_Temperatura_salida[2] * VFA_entrada +
            coef_Temperatura_salida[3] * flujo_reactor_entrada +
            intercept_Temperatura_salida)

# Función para calcular VFA_salida
def calcular_VFA_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada):
    return (coef_VFA_salida[0] * DQO_entrada +
            coef_VFA_salida[1] * Temperatura_entrada +
            coef_VFA_salida[2] * VFA_entrada +
            coef_VFA_salida[3] * flujo_reactor_entrada +
            intercept_VFA_salida)

# Función para procesar los datos ingresados por el usuario
def calcular_salidas():
    try:
        # Obtener valores de entrada
        DQO_entrada = float(entry_DQO.get())
        Temperatura_entrada = float(entry_Temperatura.get())
        VFA_entrada = float(entry_VFA.get())
        flujo_reactor_entrada = float(entry_flujo.get())

        # Calcular salidas
        DQO_salida = calcular_DQO_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada)
        Temperatura_salida = calcular_Temperatura_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada)
        VFA_salida = calcular_VFA_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada)

        # Mostrar resultados en un mensaje
        messagebox.showinfo("Resultados", f"DQO_salida: {DQO_salida:.2f}\n"
                                          f"Temperatura_salida: {Temperatura_salida:.2f}\n"
                                          f"VFA_salida: {VFA_salida:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Cálculo de Salidas")

# Crear etiquetas y entradas
tk.Label(root, text="DQO_entrada:").grid(row=0, column=0, padx=10, pady=5)
entry_DQO = tk.Entry(root)
entry_DQO.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Temperatura_entrada:").grid(row=1, column=0, padx=10, pady=5)
entry_Temperatura = tk.Entry(root)
entry_Temperatura.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="VFA_entrada:").grid(row=2, column=0, padx=10, pady=5)
entry_VFA = tk.Entry(root)
entry_VFA.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Flujo_reactor_entrada:").grid(row=3, column=0, padx=10, pady=5)
entry_flujo = tk.Entry(root)
entry_flujo.grid(row=3, column=1, padx=10, pady=5)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular Salidas", command=calcular_salidas)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar la ventana principal
root.mainloop()
