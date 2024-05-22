class V_3_Sequential_Block:
    @staticmethod
    def alg_V_3_Sequential_Block(matrizA, matrizB):
        size1 = len(matrizA)
        size2 = len(matrizB)
        matrizRes = [[0 for _ in range(size1)] for _ in range(size1)]

        for i1 in range(0, size1, size2):
            for j1 in range(0, size1, size2):
                for k1 in range(0, size1, size2):
                    for i in range(i1, min(i1 + size2, size1)):
                        for j in range(j1, min(j1 + size2, size1)):
                            for k in range(k1, min(k1 + size2, size1)):
                                matrizRes[k][i] += matrizA[k][j] * matrizB[j][i]

        return matrizRes

    @staticmethod
    def multiply(matrizA, matrizB):
        return V_3_Sequential_Block.alg_V_3_Sequential_Block(matrizA, matrizB)
