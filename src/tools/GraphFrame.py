import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk

class GraphFrame(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Visualización de tiempos de ejecución")
        self.create_tabs()

    def create_tabs(self):
        self.matrix_sizes = self.get_available_matrix_sizes()

        self.combo_frame = Frame(self)
        self.combo_frame.pack(pady=10)

        self.label = Label(self.combo_frame, text="Selecciona el tamaño de la matriz:")
        self.label.pack(side="left")

        self.combo = ttk.Combobox(self.combo_frame, values=self.matrix_sizes)
        self.combo.current(0)
        self.combo.pack(side="left")
        self.combo.bind("<<ComboboxSelected>>", self.update_tab)

        self.canvas = Canvas(self, width=1000, height=600)
        self.canvas.pack()

        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.ax.set_title("Tiempos de ejecución para matriz")
        self.ax.set_xlabel("Algoritmos")
        self.ax.set_ylabel("Tiempo de Ejecución (ms)")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        # Mostrar automáticamente el tamaño 256x256 al iniciar
        self.update_tab()

    def update_tab(self, event=None):
        tamano = self.combo.get()
        self.clear_chart()
        self.create_chart(tamano)

    def clear_chart(self):
        self.ax.clear()

    def create_chart(self, tamano):
        algoritmos = self.get_available_algorithms()
        tiempos = self.load_execution_times(tamano)
        self.ax.bar(algoritmos, tiempos)
        self.ax.set_title(f"Tiempos de ejecución para matriz {tamano}")
        self.ax.set_xlabel("Algoritmos")
        self.ax.set_ylabel("Tiempo de Ejecución (ms)")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        self.canvas.draw()

    def get_available_matrix_sizes(self):
        return ["16x16", "32x32", "64x64", "128x128", "256x256", "512x512", "1024x1024", "2048x2048"]

    def get_available_algorithms(self):
        return [
            "NaivOnArray", "NaivLoopUnrollingTwo", "NaivLoopUnrollingFour", "StrassenNaiv", "WinogradOriginal", 
            "WinogradScaled", "StrassenWinograd", "III_3_Sequential_Block", "IV_3_Sequential_Block", "V_3_SequentialBlock", 
            "III_4_Parallel_Block", "IV_4_Parallel_Block", "V_4_Parallel_Block", "III_5_Enhanced_Parallel_Block", 
            "IV_5_Enhanced_Parallel_Block"
        ]

    def load_execution_times(self, tamano):
        tiempos = []
        try:
            with open(f"src/TimeResultMatriz/matriz{tamano}.txt", "r") as file:
                for line in file:
                    tiempo = int(line.strip())
                    tiempos.append(tiempo)
        except FileNotFoundError:
            print(f"Archivo {tamano}.txt no encontrado.")
        return tiempos
