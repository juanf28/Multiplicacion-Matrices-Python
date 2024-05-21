class StrassenNaiv:
    @staticmethod
    def multiply(A, B):
        n = len(A)

        # Si el tamaño de la matriz es 1x1, realiza la multiplicación directamente
        if n == 1:
            C = [[A[0][0] * B[0][0]]]
            return C

        # Si el tamaño de la matriz es pequeño, usa la multiplicación naive
        if n <= 2:
            return StrassenNaiv.multiply_naive(A, B)

        # Inicialización de las submatrices
        new_size = n // 2
        A11 = [row[:new_size] for row in A[:new_size]]
        A12 = [row[new_size:] for row in A[:new_size]]
        A21 = [row[:new_size] for row in A[new_size:]]
        A22 = [row[new_size:] for row in A[new_size:]]
        B11 = [row[:new_size] for row in B[:new_size]]
        B12 = [row[new_size:] for row in B[:new_size]]
        B21 = [row[:new_size] for row in B[new_size:]]
        B22 = [row[new_size:] for row in B[new_size:]]

        # Calculo de las M's
        M1 = StrassenNaiv.multiply(StrassenNaiv.add(A11, A22), StrassenNaiv.add(B11, B22))
        M2 = StrassenNaiv.multiply(StrassenNaiv.add(A21, A22), B11)
        M3 = StrassenNaiv.multiply(A11, StrassenNaiv.subtract(B12, B22))
        M4 = StrassenNaiv.multiply(A22, StrassenNaiv.subtract(B21, B11))
        M5 = StrassenNaiv.multiply(StrassenNaiv.add(A11, A12), B22)
        M6 = StrassenNaiv.multiply(StrassenNaiv.subtract(A21, A11), StrassenNaiv.add(B11, B12))
        M7 = StrassenNaiv.multiply(StrassenNaiv.subtract(A12, A22), StrassenNaiv.add(B21, B22))

        # Calculo de las submatrices de C
        C11 = StrassenNaiv.add(StrassenNaiv.subtract(StrassenNaiv.add(M1, M4), M5), M7)
        C12 = StrassenNaiv.add(M3, M5)
        C21 = StrassenNaiv.add(M2, M4)
        C22 = StrassenNaiv.add(StrassenNaiv.subtract(StrassenNaiv.add(M1, M3), M2), M6)

        # Combinación de las submatrices en la matriz resultante
        C = [[0] * n for _ in range(n)]
        StrassenNaiv.join_matrix(C11, C, 0, 0)
        StrassenNaiv.join_matrix(C12, C, 0, new_size)
        StrassenNaiv.join_matrix(C21, C, new_size, 0)
        StrassenNaiv.join_matrix(C22, C, new_size, new_size)
        return C

    @staticmethod
    def multiply_naive(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    @staticmethod
    def add(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
        return C

    @staticmethod
    def subtract(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
        return C

    @staticmethod
    def split_matrix(P, C, iB, jB):
        for i1, i2 in enumerate(range(iB, iB + len(C))):
            for j1, j2 in enumerate(range(jB, jB + len(C))):
                C[i1][j1] = P[i2][j2]

    @staticmethod
    def join_matrix(C, P, iB, jB):
        for i1, i2 in enumerate(range(iB, iB + len(C))):
            for j1, j2 in enumerate(range(jB, jB + len(C))):
                P[i2][j2] = C[i1][j1]

    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print(' '.join(map(str, row)))
