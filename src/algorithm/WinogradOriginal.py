import numpy as np

class WinogradOriginal:
    @staticmethod
    def algWinogradOriginal(matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        M = len(matrizB[0])

        upsilon = P % 2
        gamma = P - upsilon

        y = np.zeros(M)
        z = np.zeros(N)

        for i in range(N):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += matrizA[i][j] * matrizA[i][j + 1]
            y[i] = aux

        for i in range(N):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += matrizB[j][i] * matrizB[j + 1][i]
            z[i] = aux

        matrizRes = np.zeros((N, M))

        if upsilon == 1:
            PP = P - 1
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (matrizA[i][j] + matrizB[j + 1][k]) * (matrizA[i][j + 1] + matrizB[j][k])
                    matrizRes[i][k] = aux - y[i] - z[k] + matrizA[i][PP] * matrizB[PP][k]
        else:
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (matrizA[i][j] + matrizB[j + 1][k]) * (matrizA[i][j + 1] + matrizB[j][k])
                    matrizRes[i][k] = aux - y[i] - z[k]

        return matrizRes

    @staticmethod
    def multiply(matrizA, matrizB):
        matrizRes = WinogradOriginal.algWinogradOriginal(matrizA, matrizB)
        return matrizRes
