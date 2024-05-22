import os
from tools.GraphFrame import GraphFrame

def ensure_directories_exist():
    os.makedirs("src/TimeResult", exist_ok=True)
    os.makedirs("src/TimeResultMatriz", exist_ok=True)
    os.makedirs("src/1matriz", exist_ok=True)
    os.makedirs("src/2matriz", exist_ok=True)

ensure_directories_exist()

from algorithm.NaivOnArray import NaivOnArray
from algorithm.III_3_Sequential_Block import III_3_Sequential_Block
from algorithm.III_4_Parallel_Block import III_4_Parallel_Block
from algorithm.III_5_Enhanced_Parallel_Block import III_5_Enhanced_Parallel_Block
from algorithm.IV_3_Sequential_Block import IV_3_Sequential_Block
from algorithm.IV_4_Parallel_Block import IV_4_Parallel_Block
from algorithm.IV_5_Enhanced_Parallel_Block import IV_5_Enhanced_Parallel_Block
from algorithm.V_3_Sequential_Block import V_3_Sequential_Block
from algorithm.V_4_Parallel_Block import V_4_Parallel_Block
from algorithm.WinogradOriginal import WinogradOriginal
from algorithm.WinogradScaled import WinogradScaled
from algorithm.NaivLoopUnrollingTwo import NaivLoopUnrollingTwo
from algorithm.NaivLoopUnrollingFour import NaivLoopUnrollingFour
from algorithm.StrassenNaiv import StrassenNaiv
from algorithm.StrassenWinograd import StrassenWinograd

import time
from tools import LeerArchivoTxt, TiempoEjecucion, ExportarTiempos

import random

class Main:
    inicio = 0
    fin = 0
    Matriz1 = None
    Matriz2 = None

    @staticmethod
    def main(args):
    # Main.crearMatrices()
     #Main.vaciar_tiempos()
     #Main.calcular_tiempos()
     Main.mostrar_grafica()
    @staticmethod
    def calcular_tiempos():
        for algoritmo in range(9, 16):  # Solo de 4 a 15 según tu Java
                    for caso in range(1, 9):  # Solo el caso 8 según tu Java
                        print(f"Ejecutando algoritmo {algoritmo} caso {caso}...")
                        Main.matrices(caso)
                        Main.algorithm(algoritmo)
                        print(f"Termino algoritmo {algoritmo} caso {caso}\n")
                        try:
                            ExportarTiempos.ExportarTiempos.exportar_tiempos_matriz(TiempoEjecucion.TiempoEjecucion.matrices_tiempo_algoritmos, caso)
                            ExportarTiempos.ExportarTiempos.exportar_tiempos(TiempoEjecucion.TiempoEjecucion.matrices_tiempo_algoritmos, algoritmo)
                        except IOError as e:
                            print("Error de entrada/salida:", e)
                        except RuntimeError as e:
                            print("Error en tiempo de ejecución:", e)
                        TiempoEjecucion.TiempoEjecucion.matrices_tiempo_algoritmos.clear()
    @staticmethod
    def vaciar_tiempos():
        try:
            for algoritmo in ExportarTiempos.ExportarTiempos.getAlgoritmo():
                with open(f"src/TimeResult/{algoritmo}.txt", 'w') as file:
                    file.close()
            for matriz in ExportarTiempos.ExportarTiempos.getMatrices():
                with open(f"src/TimeResultMatriz/{matriz}.txt", 'w') as file:
                    file.close()
            print("Archivos de tiempos vaciados correctamente.")
        except IOError as e:
            print(e)


    @staticmethod
    def crearMatrices():
       
       ruta = "src/"
       os.makedirs(ruta + "1matriz", exist_ok=True)
       os.makedirs(ruta + "2matriz", exist_ok=True)
       tamaños = [16, 32, 64, 128, 256, 512, 1024, 2048]  # Tamaños especificados

       for tamaño in tamaños:
            matriz = Main.generarMatriz(tamaño, tamaño)
            Main.guardarMatrizEnArchivo(matriz, f"{ruta}1matriz/1matriz_{tamaño}x{tamaño}.txt")
            Main.guardarMatrizEnArchivo(matriz, f"{ruta}2matriz/2matriz_{tamaño}x{tamaño}.txt")

       print("Matrices generadas")

    @staticmethod
    def generarMatriz(n, m):
        matriz = [[0] * n for _ in range(m)]
        rand = random.Random()

        for i in range(m):
            for j in range(n):
                matriz[i][j] = rand.randint(100000, 999999)  # Generar número aleatorio de 6 dígitos
        return matriz

    @staticmethod
    def guardarMatrizEnArchivo(matriz, nombreArchivo):
        try:
            with open(nombreArchivo, 'w') as writer:
                for fila in matriz:
                    writer.write(' '.join(map(str, fila)) + '\n')  # Escribir cada elemento de la matriz
        except IOError as e:
            print(e)

    @staticmethod
    def algorithm(option):
        global inicio, fin
        matrizDouble1 = Main.convert_to_int_to_double(Main.Matriz1)
        matrizDouble2 = Main.convert_to_int_to_double(Main.Matriz2)
        try:
            if option == 1:
                Main.execute_algorithm(lambda: NaivOnArray.naivOnArray(Main.Matriz1, Main.Matriz2))
            elif option == 2:
                Main.execute_algorithm(lambda: NaivLoopUnrollingTwo.naiveLoopUnrollingTwo(Main.Matriz1, Main.Matriz2))
            elif option == 3:
                Main.execute_algorithm(lambda: NaivLoopUnrollingFour.naivLoopUnrollingFour(Main.Matriz1, Main.Matriz2))
            elif option == 4:
                Main.execute_algorithm(lambda: WinogradOriginal.multiply(matrizDouble1, matrizDouble2))
            elif option == 5:
                Main.execute_algorithm(lambda: WinogradScaled.multiply(matrizDouble1, matrizDouble2))
            elif option == 6:
                Main.execute_algorithm(lambda: StrassenNaiv.multiply(matrizDouble1, matrizDouble2))
            elif option == 7:
                Main.execute_algorithm(lambda: StrassenWinograd.multiply(matrizDouble1, matrizDouble2))
            elif option == 8:
                Main.execute_algorithm(lambda: III_3_Sequential_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 9:
                Main.execute_algorithm(lambda: III_4_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 10:
                Main.execute_algorithm(lambda: III_5_Enhanced_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 11:
                Main.execute_algorithm(lambda: IV_3_Sequential_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 12:
                Main.execute_algorithm(lambda: IV_4_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 13:
                Main.execute_algorithm(lambda: IV_5_Enhanced_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 14:
                Main.execute_algorithm(lambda: V_3_Sequential_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 15:
                Main.execute_algorithm(lambda: V_4_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            else:
                print("Opción incorrecta")

        finally:
            Main.Matriz1 = None
            Main.Matriz2 = None

    @staticmethod
    def execute_algorithm(algorithm):
        Main.inicio = time.time_ns()
        algorithm()
        Main.fin = time.time_ns()
        TiempoEjecucion.TiempoEjecucion.time_algorithm(Main.inicio, Main.fin)

    @staticmethod
    def convert_to_int_to_double(matrix):
        return [[float(element) for element in row] for row in matrix]

    @staticmethod
    def matrices(caso):
        tam=0
        if caso == 1:
            tam=16
        elif caso == 2:
            tam=32
        elif caso == 3:
            tam=64
        elif caso == 4:
            tam=128
        elif caso == 5:
            tam=256
        elif caso == 6:
            tam=512
        elif caso == 7:
            tam=1024
        elif caso == 8:
            tam=2048
        else:
            print("Caso incorrecto")
        Main.Matriz1 = LeerArchivoTxt.leer_archivo(f"src/1matriz/1matriz_{tam}x{tam}.txt", tam)
        Main.Matriz2 = LeerArchivoTxt.leer_archivo(f"src/2matriz/2matriz_{tam}x{tam}.txt", tam)
            
    @staticmethod
    def mostrar_grafica():
        frame = GraphFrame()  # Crea una instancia de GraphFrame
        frame.mainloop()

if __name__ == "__main__":
     Main.main([])
