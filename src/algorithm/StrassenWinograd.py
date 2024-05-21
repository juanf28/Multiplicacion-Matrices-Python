class StrassenWinograd:
    @staticmethod
    def multiply(A, B):
        n = len(A)
        result = [[0] * n for _ in range(n)]
        if n == 1:
            result[0][0] = A[0][0] * B[0][0]
        else:
            A11 = [row[:n // 2] for row in A[:n // 2]]
            A12 = [row[n // 2:] for row in A[:n // 2]]
            A21 = [row[:n // 2] for row in A[n // 2:]]
            A22 = [row[n // 2:] for row in A[n // 2:]]

            B11 = [row[:n // 2] for row in B[:n // 2]]
            B12 = [row[n // 2:] for row in B[:n // 2]]
            B21 = [row[:n // 2] for row in B[n // 2:]]
            B22 = [row[n // 2:] for row in B[n // 2:]]

            # Strassen-Winograd algorithm calculations
            P1 = StrassenWinograd.multiply(StrassenWinograd.add(A11, A22), StrassenWinograd.add(B11, B22))
            P2 = StrassenWinograd.multiply(StrassenWinograd.add(A21, A22), B11)
            P3 = StrassenWinograd.multiply(A11, StrassenWinograd.subtract(B12, B22))
            P4 = StrassenWinograd.multiply(A22, StrassenWinograd.subtract(B21, B11))
            P5 = StrassenWinograd.multiply(StrassenWinograd.add(A11, A12), B22)
            P6 = StrassenWinograd.multiply(StrassenWinograd.subtract(A21, A11), StrassenWinograd.add(B11, B12))
            P7 = StrassenWinograd.multiply(StrassenWinograd.subtract(A12, A22), StrassenWinograd.add(B21, B22))

            C11 = StrassenWinograd.add(StrassenWinograd.subtract(StrassenWinograd.add(P1, P4), P5), P7)
            C12 = StrassenWinograd.add(P3, P5)
            C21 = StrassenWinograd.add(P2, P4)
            C22 = StrassenWinograd.add(StrassenWinograd.subtract(StrassenWinograd.add(P1, P3), P2), P6)

            # Combine 4 submatrices into one
            StrassenWinograd.join(C11, result, 0, 0)
            StrassenWinograd.join(C12, result, 0, n // 2)
            StrassenWinograd.join(C21, result, n // 2, 0)
            StrassenWinograd.join(C22, result, n // 2, n // 2)
        return result

    @staticmethod
    def add(A, B):
        n = len(A)
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = A[i][j] + B[i][j]
        return result

    @staticmethod
    def subtract(A, B):
        n = len(A)
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = A[i][j] - B[i][j]
        return result

    @staticmethod
    def split(P, C, iB, jB):
        for i1, i2 in enumerate(range(iB, iB + len(C))):
            for j1, j2 in enumerate(range(jB, jB + len(C))):
                C[i1][j1] = P[i2][j2]

    @staticmethod
    def join(C, P, iB, jB):
        for i1, i2 in enumerate(range(iB, iB + len(C))):
            for j1, j2 in enumerate(range(jB, jB + len(C))):
                P[i2][j2] = C[i1][j1]
