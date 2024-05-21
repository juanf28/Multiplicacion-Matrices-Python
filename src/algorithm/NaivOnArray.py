from tools.Imprimir import Imprimir

class NaivOnArray(Imprimir):

    @staticmethod
    def naivOnArray(a, b):
        n = len(a)
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[i][j] = 0
                for k in range(n):
                    result[i][j] += a[i][k] * b[k][j]
        # imprimirMatriz(result) 
