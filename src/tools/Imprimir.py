class Imprimir:
    @staticmethod
    def imprimir_matriz(matriz):
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                print(matriz[i][j], end=" ")
            print()
