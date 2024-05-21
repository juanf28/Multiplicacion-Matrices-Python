class TiempoEjecucion:
    matrices_tiempo_algoritmos = []
    matriz256x256 = []
    matriz512x512 = []
    matriz1024x1024 = []
    matriz2048x2048 = []
    matriz4096x4096 = []
    matriz6144x6144 = []
    matriz8192x8192 = []
    matriz10240x10240 = []

    @staticmethod
    def time_algorithm(inicio, fin):
        tiempo = fin - inicio
        TiempoEjecucion.matrices_tiempo_algoritmos.append(tiempo)
        print(" Tiempo:", tiempo, "ns")

    @staticmethod
    def result_time_matrix(parametro):
        for i in range(1, parametro + 1):
            if i == 1:
                TiempoEjecucion.matriz256x256.append(TiempoEjecucion.matrices_tiempo_algoritmos[0])
            elif i == 2:
                TiempoEjecucion.matriz512x512.append(TiempoEjecucion.matrices_tiempo_algoritmos[1])
            elif i == 3:
                TiempoEjecucion.matriz1024x1024.append(TiempoEjecucion.matrices_tiempo_algoritmos[2])
            elif i == 4:
                TiempoEjecucion.matriz2048x2048.append(TiempoEjecucion.matrices_tiempo_algoritmos[3])
            elif i == 5:
                TiempoEjecucion.matriz4096x4096.append(TiempoEjecucion.matrices_tiempo_algoritmos[4])
            elif i == 6:
                TiempoEjecucion.matriz6144x6144.append(TiempoEjecucion.matrices_tiempo_algoritmos[5])
            elif i == 7:
                TiempoEjecucion.matriz8192x8192.append(TiempoEjecucion.matrices_tiempo_algoritmos[6])
            elif i == 8:
                TiempoEjecucion.matriz10240x10240.append(TiempoEjecucion.matrices_tiempo_algoritmos[7])
