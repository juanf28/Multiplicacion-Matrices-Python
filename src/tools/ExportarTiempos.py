import os

class ExportarTiempos:
    algoritmo = ["NaivStandard", "NaivOnArray", "NaivKahan", "NaivLoopUnrollingTwo", "NaivLoopUnrollingThree", "NaivLoopUnrollingFour", "WinogradOriginal", "WinogradScaled", "StrassenNaiv", "StrassenWinograd", "III-SequentialBlock", "III-ParallelBlock"]

    matrices = ["matriz256x256", "matriz512x512", "matriz1024x1024", "matriz2048x2048", "matriz4096x4096", "matriz6144x6144", "matriz8192x8192", "matriz12288x12288"]

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
