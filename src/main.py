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
      ##  Main.crearMatrices()
        
        Main.vaciar_tiempos()
        
        for algoritmo in range(1, 16):  # Solo de 4 a 15 según tu Java
            for caso in range(1, 9):  # Solo el caso 8 según tu Java
                Main.matrices(caso)
                Main.algorithm(algoritmo)
                print(f"Termino algoritmo: {algoritmo} caso {caso}\n")
                try:
                    ExportarTiempos.ExportarTiempos.exportar_tiempos_matriz(TiempoEjecucion.TiempoEjecucion.matrices_tiempo_algoritmos, caso)
                    ExportarTiempos.ExportarTiempos.exportar_tiempos(TiempoEjecucion.TiempoEjecucion.matrices_tiempo_algoritmos, algoritmo)
                except IOError as e:
                    print("Error de entrada/salida:", e)
                except RuntimeError as e:
                    print("Error en tiempo de ejecución:", e)
                TiempoEjecucion.TiempoEjecucion.matrices_tiempo_algoritmos.clear()
        
    ##    Main.mostrar_grafica()

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
       tamaños = [256, 512, 1024, 2048, 3072, 4096, 6144, 8192]  # Tamaños especificados

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
                Main.execute_algorithm(lambda: StrassenNaiv.multiply(matrizDouble1, matrizDouble2))
            elif option == 5:
                Main.execute_algorithm(lambda: WinogradOriginal.multiply(matrizDouble1, matrizDouble2))
            elif option == 6:
                Main.execute_algorithm(lambda: WinogradScaled.multiply(matrizDouble1, matrizDouble2))
            elif option == 7:
                Main.execute_algorithm(lambda: StrassenWinograd.multiply(matrizDouble1, matrizDouble2))
            elif option == 8:
                Main.execute_algorithm(lambda: III_3_Sequential_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 9:
                Main.execute_algorithm(lambda: IV_3_Sequential_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 10:
                Main.execute_algorithm(lambda: V_3_Sequential_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 11:
                Main.execute_algorithm(lambda: III_4_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 12:
                Main.execute_algorithm(lambda: IV_4_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 13:
                Main.execute_algorithm(lambda: V_4_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 14:
                Main.execute_algorithm(lambda: III_5_Enhanced_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
            elif option == 15:
                Main.execute_algorithm(lambda: IV_5_Enhanced_Parallel_Block.multiply(matrizDouble1, matrizDouble2))
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
        if caso == 1:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_256x256.txt", 256)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_256x256.txt", 256)
        elif caso == 2:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_512x512.txt", 512)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_512x512.txt", 512)
        elif caso == 3:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_1024x1024.txt", 1024)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_1024x1024.txt", 1024)
        elif caso == 4:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_2048x2048.txt", 2048)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_2048x2048.txt", 2048)
        elif caso == 5:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_3072x3072.txt", 3072)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_3072x3072.txt", 3072)
        elif caso == 6:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_4096x4096.txt", 4096)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_4096x4096.txt", 4096)
        elif caso == 7:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_6144x6144.txt", 6144)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_6144x6144.txt", 6144)
        elif caso == 8:
            Main.Matriz1 = LeerArchivoTxt.leer_archivo("src/1matriz/1matriz_8192x8192.txt", 8192)
            Main.Matriz2 = LeerArchivoTxt.leer_archivo("src/2matriz/2matriz_8192x8192.txt", 8192)
        else:
            print("Caso incorrecto")
            
    @staticmethod
    def mostrar_grafica():
        frame = GraphFrame()  # Crea una instancia de GraphFrame
        frame.mainloop()

if __name__ == "__main__":
     Main.main([])
