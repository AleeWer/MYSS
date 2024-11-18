import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Coeficientes e interceptos
coef_DQO_salida = [0.2474, 1.2693, 0.3418, -0.2932]
intercept_DQO_salida = 927.32

coef_Temperatura_salida = [-0.0029, 0.0350, 0.0182, -0.0057]
intercept_Temperatura_salida = 32.34

coef_VFA_salida = [0.0235, 1.3224, 0.5286, -0.3056]
intercept_VFA_salida = 880.40

# Funciones de cálculo
def calcular_DQO_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada):
    return (coef_DQO_salida[0] * DQO_entrada +
            coef_DQO_salida[1] * Temperatura_entrada +
            coef_DQO_salida[2] * VFA_entrada +
            coef_DQO_salida[3] * flujo_reactor_entrada +
            intercept_DQO_salida)

def calcular_Temperatura_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada):
    return (coef_Temperatura_salida[0] * DQO_entrada +
            coef_Temperatura_salida[1] * Temperatura_entrada +
            coef_Temperatura_salida[2] * VFA_entrada +
            coef_Temperatura_salida[3] * flujo_reactor_entrada +
            intercept_Temperatura_salida)

def calcular_VFA_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada):
    return (coef_VFA_salida[0] * DQO_entrada +
            coef_VFA_salida[1] * Temperatura_entrada +
            coef_VFA_salida[2] * VFA_entrada +
            coef_VFA_salida[3] * flujo_reactor_entrada +
            intercept_VFA_salida)

def calcular_salidas():
    try:
        # Obtener valores de entrada
        DQO_entrada = float(entry_DQO.get())
        Temperatura_entrada = float(entry_Temperatura.get())
        VFA_entrada = float(entry_VFA.get())
        flujo_reactor_entrada = float(entry_flujo.get())

        # Calcular valores de salida
        DQO_salida = calcular_DQO_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada)
        Temperatura_salida = calcular_Temperatura_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada)
        VFA_salida = calcular_VFA_salida(DQO_entrada, Temperatura_entrada, VFA_entrada, flujo_reactor_entrada)

        # Mostrar gráficos y valores
        mostrar_graficas(DQO_entrada, DQO_salida, Temperatura_entrada, Temperatura_salida, VFA_entrada, VFA_salida)
        mostrar_valores_salida(DQO_salida, Temperatura_salida, VFA_salida)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def mostrar_graficas(DQO_entrada, DQO_salida, Temperatura_entrada, Temperatura_salida, VFA_entrada, VFA_salida):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle('Comparación de Datos de Entrada y Salida', fontsize=16)

    # Gráfica DQO
    axes[0].bar(['Entrada', 'Salida'], [DQO_entrada, DQO_salida], color=['blue', 'green'])
    axes[0].set_title('DQO')
    axes[0].set_ylabel('Valores')

    # Gráfica Temperatura
    axes[1].bar(['Entrada', 'Salida'], [Temperatura_entrada, Temperatura_salida], color=['blue', 'green'])
    axes[1].set_title('Temperatura')

    # Gráfica VFA
    axes[2].bar(['Entrada', 'Salida'], [VFA_entrada, VFA_salida], color=['blue', 'green'])
    axes[2].set_title('VFA')

    # Mostrar en ventana
    for ax in axes:
        ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, pady=10)

def mostrar_valores_salida(DQO_salida, Temperatura_salida, VFA_salida):
    label_resultado_DQO.config(text=f"DQO salida: {DQO_salida:.2f}")
    label_resultado_Temperatura.config(text=f"Temperatura salida: {Temperatura_salida:.2f}")
    label_resultado_VFA.config(text=f"VFA salida: {VFA_salida:.2f}")

# Configuración de la interfaz
root = ttk.Window(themename="litera")
root.title("Cálculo de Salidas")

ttk.Label(root, text="DQO_entrada:").grid(row=0, column=0, padx=10, pady=5)
entry_DQO = ttk.Entry(root)
entry_DQO.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Temperatura_entrada:").grid(row=1, column=0, padx=10, pady=5)
entry_Temperatura = ttk.Entry(root)
entry_Temperatura.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="VFA_entrada:").grid(row=2, column=0, padx=10, pady=5)
entry_VFA = ttk.Entry(root)
entry_VFA.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Flujo_reactor_entrada:").grid(row=3, column=0, padx=10, pady=5)
entry_flujo = ttk.Entry(root)
entry_flujo.grid(row=3, column=1, padx=10, pady=5)

btn_calcular = ttk.Button(root, text="Calcular Salidas", bootstyle=SUCCESS, command=calcular_salidas)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Etiquetas para mostrar resultados
label_resultado_DQO = ttk.Label(root, text="DQO salida: -")
label_resultado_DQO.grid(row=7, column=0, columnspan=2)

label_resultado_Temperatura = ttk.Label(root, text="Temperatura salida: -")
label_resultado_Temperatura.grid(row=8, column=0, columnspan=2)

label_resultado_VFA = ttk.Label(root, text="VFA salida: -")
label_resultado_VFA.grid(row=9, column=0, columnspan=2)

root.mainloop()
