import os

class ExportarTiempos:
    algoritmo = ["NaivOnArray", "NaivLoopUnrollingTwo", "NaivLoopUnrollingFour", "StrassenNaiv", "WinogradOriginal", "WinogradScaled", "StrassenWinograd", "III_3_Sequential_Block", "IV_3_Sequential_Block", "V_3_SequentialBlock", "III_4_Parallel_Block", "IV_4_Parallel_Block", "V_4_Parallel_Block", "III_5_Enhanced_Parallel_Block", "IV_5_Enhanced_Parallel_Block"]

    matrices = ["matriz16x16", "matriz32x32", "matriz64x64", "matriz128x128", "matriz256x256", "matriz512x512", "matriz1024x1024", "matriz2048x2048"]

    @staticmethod
    def getAlgoritmo():
        return ExportarTiempos.algoritmo

    @staticmethod
    def getMatrices():
        return ExportarTiempos.matrices

    @staticmethod
    def exportar_tiempos(lista, item):
        ruta_archivo = os.path.join("src", "TimeResult", f"{ExportarTiempos.algoritmo[item - 1]}.txt")
        with open(ruta_archivo, "w") as archivo:
            for numero in lista:
                archivo.write(str(numero) + "\n")

    @staticmethod
    def exportar_tiempos_matriz(lista, item):
        ruta_archivo = os.path.join("src", "TimeResultMatriz", f"{ExportarTiempos.matrices[item - 1]}.txt")
        with open(ruta_archivo, "w") as archivo:
            for numero in lista:
                archivo.write(str(numero) + "\n")
