import numpy as np
from multiprocessing import Pool

class III_4_Parallel_Block:
    @staticmethod
    def alg_III_4_Parallel_Block(matrizA, matrizB, size1, size2):
        matrizRes = np.zeros((size1, size2))
        pool = Pool()
        args = [(matrizA, matrizB, matrizRes, size1, size2, i1) for i1 in range(0, size1, size2)]
        pool.map(III_4_Parallel_Block.calculate_block, args)
        pool.close()
        pool.join()
        return matrizRes

    @staticmethod
    def calculate_block(args):
        matrizA, matrizB, matrizRes, size1, size2, i1 = args
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
        return III_4_Parallel_Block.alg_III_4_Parallel_Block(matrizA, matrizB, N, P)