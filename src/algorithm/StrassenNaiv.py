class StrassenNaiv:
    @staticmethod
    def multiply(A, B):
        n = len(A)

        # Si el tamaño de la matriz es 1x1, realiza la multiplicación directamente
        if n == 1:
            return [[A[0][0] * B[0][0]]]

        # Si el tamaño de la matriz es pequeño, usa la multiplicación naive
        if n <= 2:
            return StrassenNaiv.multiplyNaive(A, B)

        # Inicialización de las submatrices
        newSize = n // 2
        A11 = [[0] * newSize for _ in range(newSize)]
        A12 = [[0] * newSize for _ in range(newSize)]
        A21 = [[0] * newSize for _ in range(newSize)]
        A22 = [[0] * newSize for _ in range(newSize)]
        B11 = [[0] * newSize for _ in range(newSize)]
        B12 = [[0] * newSize for _ in range(newSize)]
        B21 = [[0] * newSize for _ in range(newSize)]
        B22 = [[0] * newSize for _ in range(newSize)]

        # División de las matrices en submatrices
        StrassenNaiv.splitMatrix(A, A11, 0, 0)
        StrassenNaiv.splitMatrix(A, A12, 0, newSize)
        StrassenNaiv.splitMatrix(A, A21, newSize, 0)
        StrassenNaiv.splitMatrix(A, A22, newSize, newSize)
        StrassenNaiv.splitMatrix(B, B11, 0, 0)
        StrassenNaiv.splitMatrix(B, B12, 0, newSize)
        StrassenNaiv.splitMatrix(B, B21, newSize, 0)
        StrassenNaiv.splitMatrix(B, B22, newSize, newSize)

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
        StrassenNaiv.joinMatrix(C11, C, 0, 0)
        StrassenNaiv.joinMatrix(C12, C, 0, newSize)
        StrassenNaiv.joinMatrix(C21, C, newSize, 0)
        StrassenNaiv.joinMatrix(C22, C, newSize, newSize)
        return C

    @staticmethod
    def multiplyNaive(A, B):
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
    def splitMatrix(P, C, iB, jB):
        for i1, i2 in enumerate(range(iB, iB + len(C))):
            for j1, j2 in enumerate(range(jB, jB + len(C))):
                C[i1][j1] = P[i2][j2]

    @staticmethod
    def joinMatrix(C, P, iB, jB):
        for i1, i2 in enumerate(range(iB, iB + len(C))):
            for j1, j2 in enumerate(range(jB, jB + len(C))):
                P[i2][j2] = C[i1][j1]

    @staticmethod
    def printMatrix(matrix):
        for row in matrix:
            print(" ".join(map(str, row)))