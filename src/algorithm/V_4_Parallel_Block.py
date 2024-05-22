import numpy as np
from multiprocessing import Pool

class V_4_Parallel_Block:
    @staticmethod
    def update_cell(i1, size1, size2, matrizA, matrizB, matrizC):
        for j1 in range(0, size1, size2):
            for k1 in range(0, size1, size2):
                for i in range(i1, min(i1 + size2, size1)):
                    for j in range(j1, min(j1 + size2, size1)):
                        for k in range(k1, min(k1 + size2, size1)):
                            matrizC[k, i] += matrizA[k][j] * matrizB[j][i]  # Convertir a acceso de lista

    @staticmethod
    def alg_V_4_ParallelBlockTres(matrizA, matrizB, size1, size2):
        matrizC = np.zeros((size1, size1))

        with Pool() as pool:
            arguments = [(i1, size1, size2, matrizA, matrizB, matrizC) for i1 in range(0, size1, size2)]
            pool.starmap(V_4_Parallel_Block.update_cell, arguments)

        return matrizC

    @staticmethod
    def multiply(matrizA, matrizB):
        N, P = len(matrizA), len(matrizB[0])  # Corregir longitud de listas
        matrizA_np = np.array(matrizA)  # Convertir lista a matriz NumPy
        matrizB_np = np.array(matrizB)  # Convertir lista a matriz NumPy
        return V_4_Parallel_Block.alg_V_4_ParallelBlockTres(matrizA_np, matrizB_np,N,P)