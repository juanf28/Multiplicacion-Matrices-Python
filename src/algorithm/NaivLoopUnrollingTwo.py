from tools.Imprimir import Imprimir

class NaivLoopUnrollingTwo(Imprimir):

    @staticmethod
    def naiveLoopUnrollingTwo(a, b):
        n = len(a)
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(0, n, 2):
                sum1, sum2 = 0, 0
                for k in range(n):
                    sum1 += a[i][k] * b[k][j]
                    sum2 += a[i][k] * b[k][j + 1]
                result[i][j] = sum1
                result[i][j + 1] = sum2
        # imprimirMatriz(result) -> Comentario: ¿Dónde está definido el método imprimirMatriz?
