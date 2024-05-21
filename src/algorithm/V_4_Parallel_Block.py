import numpy as np
from multiprocessing import Pool

class V_4_Parallel_Block:
    @staticmethod
    def alg_V_4_ParallelBlockTres(matrizA, matrizB, size1, size2):
        matrizC = np.zeros((size1, size1))

        def update_cell(i1):
            for j1 in range(0, size1, size2):
                for k1 in range(0, size1, size2):
                    for i in range(i1, min(i1 + size2, size1)):
                        for j in range(j1, min(j1 + size2, size1)):
                            for k in range(k1, min(k1 + size2, size1)):
                                matrizC[k, i] += matrizA[k, j] * matrizB[j, i]

        with Pool() as pool:
            pool.map(update_cell, range(0, size1, size2))

        return matrizC

    @staticmethod
    def multiply(matrizA, matrizB):
        N, P = matrizA.shape[0], matrizB.shape[0]
        return V_4_Parallel_Block.alg_V_4_ParallelBlockTres(matrizA, matrizB, N, P)
