import numpy as np

class III_5_Enhanced_Parallel_Block:

    @staticmethod
    def alg_III_5_Enhanced_Parallel_Block(matrizA, matrizB, size1, size2):
        matrizRes = np.zeros((size1, size2))

        # Primera mitad de la matriz
        for i1 in range(0, size1 // 2, size2):
            for j1 in range(0, size1, size2):
                for k1 in range(0, size1, size2):
                    for i in range(i1, min(i1 + size2, size1)):
                        for j in range(j1, min(j1 + size2, size1)):
                            for k in range(k1, min(k1 + size2, size1)):
                                matrizRes[i][j] += matrizA[i][k] * matrizB[k][j]

        # Segunda mitad de la matriz
        for i1 in range(size1 // 2, size1, size2):
            for j1 in range(0, size1, size2):
                for k1 in range(0, size1, size2):
                    for i in range(i1, min(i1 + size2, size1)):
                        for j in range(j1, min(j1 + size2, size1)):
                            for k in range(k1, min(k1 + size2, size1)):
                                matrizRes[i][j] += matrizA[i][k] * matrizB[k][j]

    @staticmethod
    def multiply(matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        III_5_Enhanced_Parallel_Block.alg_III_5_Enhanced_Parallel_Block(matrizA, matrizB, N, P)
