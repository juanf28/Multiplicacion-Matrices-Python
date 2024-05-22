class V_3_Sequential_Block:
    @staticmethod
    def alg_V_3_Sequential_Block(matrizA, matrizB):
        size1 = len(matrizA)
        size2 = len(matrizB)
        if size1 == 0 or size2 == 0 or len(matrizA[0]) != size2:
            raise ValueError("Dimensiones de matrices incompatibles para la multiplicación.")

        block_size = 64  # Tamaño del bloque, ajústalo según sea necesario
        matrizRes = [[0 for _ in range(size1)] for _ in range(size1)]

        for i1 in range(0, size1, block_size):
            for j1 in range(0, size1, block_size):
                for k1 in range(0, size2, block_size):
                    for i in range(i1, min(i1 + block_size, size1)):
                        for j in range(j1, min(j1 + block_size, size1)):
                            sum = 0
                            for k in range(k1, min(k1 + block_size, size2)):
                                sum += matrizA[i][k] * matrizB[k][j]
                            matrizRes[i][j] += sum

        return matrizRes

    @staticmethod
    def multiply(matrizA, matrizB):
        return V_3_Sequential_Block.alg_V_3_Sequential_Block(matrizA, matrizB)