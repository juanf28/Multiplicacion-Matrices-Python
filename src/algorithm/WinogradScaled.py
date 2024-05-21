import numpy as np

class WinogradScaled:
    @staticmethod
    def algWinogradScaled(matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        M = len(matrizB[0])

        copyA = np.zeros((N, P))
        copyB = np.zeros((P, M))

        a = WinogradScaled.normInf(matrizA, N, P)
        b = WinogradScaled.normInf(matrizB, P, M)
        lambda_val = int(0.5 + np.log(b / a) / np.log(4))

        WinogradScaled.multiplyWithScalar(matrizA, copyA, N, P, 2 ** lambda_val)
        WinogradScaled.multiplyWithScalar(matrizB, copyB, P, M, 2 ** (-lambda_val))

        return WinogradScaled.algWinogradOriginal(copyA, copyB, N, P, M)

    @staticmethod
    def algWinogradOriginal(matrizA, matrizB, N, P, M):
        upsilon = P % 2
        gamma = P - upsilon

        y = np.zeros(M)
        z = np.zeros(N)

        for i in range(M):
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
    def multiplyWithScalar(matrizA, matrizB, N, M, scalar):
        for i in range(N):
            for j in range(M):
                matrizB[i][j] = matrizA[i][j] * scalar

    @staticmethod
    def normInf(matrizA, N, M):
        max_val = float('-inf')
        for i in range(N):
            suma = sum(abs(val) for val in matrizA[i])
            if suma > max_val:
                max_val = suma
        return max_val

    @staticmethod
    def multiply(matrizA, matrizB):
        matrizRes = WinogradScaled.algWinogradScaled(matrizA, matrizB)
        return matrizRes
