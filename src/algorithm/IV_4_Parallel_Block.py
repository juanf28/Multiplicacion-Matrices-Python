from multiprocessing import Pool

class IV_4_Parallel_Block:
    @staticmethod
    def _multiply_block(args):
        matrizA, matrizB, size1, size2, i1 = args
        matrizRes = [[0 for _ in range(size2)] for _ in range(size1)]

        for j1 in range(0, size1, size2):
            for k1 in range(0, size1, size2):
                for i in range(i1 * size2, min((i1 + 1) * size2, size1)):
                    for j in range(j1, min(j1 + size2, size1)):
                        for k in range(k1, min(k1 + size2, size1)):
                            matrizRes[i][k] += matrizA[i][j] * matrizB[j][k]

        return matrizRes

    @staticmethod
    def alg_IV_4_Parallel_Block(matrizA, matrizB, size1, size2):
        # Determine number of processes to use
        num_processes = 4  # Adjust according to your system's capabilities
        pool = Pool(processes=num_processes)

        # Define arguments for each block computation
        block_args = [(matrizA, matrizB, size1, size2, i1) for i1 in range(size1 // size2)]

        # Parallel computation of block multiplication
        result_matrices = pool.map(IV_4_Parallel_Block._multiply_block, block_args)

        # Combine results into final result matrix
        matrizRes = [[0 for _ in range(size2)] for _ in range(size1)]
        for res in result_matrices:
            for i in range(size1):
                for j in range(size2):
                    matrizRes[i][j] += res[i][j]

        return matrizRes

    @staticmethod
    def multiply(matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        return IV_4_Parallel_Block.alg_IV_4_Parallel_Block(matrizA, matrizB, N, P)
