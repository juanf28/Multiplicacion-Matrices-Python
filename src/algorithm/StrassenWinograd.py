import numpy as np
from tools.Imprimir import Imprimir

class StrassenWinograd(Imprimir):
    
    def multiply(A, B):
        N = len(A)
        P = len(A[0])
        M = len(B[0])

        Result = np.zeros((N, M))

        multiply_recursive(A, B, Result, N, P, M)
        return Result

def multiply_recursive(A, B, Result, N, P, M):
    MaxSize = max(N, P, M)

    if MaxSize < 16:
        MaxSize = 16

    k = int(np.floor(np.log2(MaxSize)) - 4)
    m = int(np.floor(MaxSize * 2**(-k)) + 1)
    NewSize = m * (2**k)

    NewA = np.zeros((NewSize, NewSize))
    NewB = np.zeros((NewSize, NewSize))
    AuxResult = np.zeros((NewSize, NewSize))

    NewA[:N, :P] = A
    NewB[:P, :M] = B

    strassen_winograd_step(NewA, NewB, AuxResult, NewSize, m)

    Result[:N, :M] = AuxResult[:N, :M]

def strassen_winograd_step(A, B, Result, N, m):
    if (N % 2 == 0) and (N > m):
        NewSize = N // 2

        A11 = A[:NewSize, :NewSize]
        A12 = A[:NewSize, NewSize:]
        A21 = A[NewSize:, :NewSize]
        A22 = A[NewSize:, NewSize:]

        B11 = B[:NewSize, :NewSize]
        B12 = B[:NewSize, NewSize:]
        B21 = B[NewSize:, :NewSize]
        B22 = B[NewSize:, NewSize:]

        A1 = np.zeros((NewSize, NewSize))
        A2 = np.zeros((NewSize, NewSize))
        B1 = np.zeros((NewSize, NewSize))
        B2 = np.zeros((NewSize, NewSize))

        ResultPart11 = np.zeros((NewSize, NewSize))
        ResultPart12 = np.zeros((NewSize, NewSize))
        ResultPart21 = np.zeros((NewSize, NewSize))
        ResultPart22 = np.zeros((NewSize, NewSize))

        Helper1 = np.zeros((NewSize, NewSize))
        Helper2 = np.zeros((NewSize, NewSize))

        Aux1 = np.zeros((NewSize, NewSize))
        Aux2 = np.zeros((NewSize, NewSize))
        Aux3 = np.zeros((NewSize, NewSize))
        Aux4 = np.zeros((NewSize, NewSize))
        Aux5 = np.zeros((NewSize, NewSize))
        Aux6 = np.zeros((NewSize, NewSize))
        Aux7 = np.zeros((NewSize, NewSize))
        Aux8 = np.zeros((NewSize, NewSize))
        Aux9 = np.zeros((NewSize, NewSize))

        minus(A11, A21, A1)
        minus(A22, A1, A2)
        minus(B22, B12, B1)
        plus(B1, B11, B2)

        strassen_winograd_step(A11, B11, Aux1, NewSize, m)
        strassen_winograd_step(A12, B21, Aux2, NewSize, m)
        strassen_winograd_step(A2, B2, Aux3, NewSize, m)

        plus(A21, A22, Helper1)
        minus(B12, B11, Helper2)
        strassen_winograd_step(Helper1, Helper2, Aux4, NewSize, m)
        strassen_winograd_step(A1, B1, Aux5, NewSize, m)

        minus(A12, A2, Helper1)
        strassen_winograd_step(Helper1, B22, Aux6, NewSize, m)
        minus(B21, B2, Helper1)
        strassen_winograd_step(A22, Helper1, Aux7, NewSize, m)

        plus(Aux1, Aux3, Aux8)
        plus(Aux8, Aux4, Aux9)

        plus(Aux1, Aux2, ResultPart11)
        plus(Aux9, Aux6, ResultPart12)
        plus(Aux8, Aux5, Helper1)
        plus(Helper1, Aux7, ResultPart21)
        plus(Aux9, Aux5, ResultPart22)

        Result[:NewSize, :NewSize] = ResultPart11
        Result[:NewSize, NewSize:] = ResultPart12
        Result[NewSize:, :NewSize] = ResultPart21
        Result[NewSize:, NewSize:] = ResultPart22

    else:
        naiv_standard(A, B, Result, N, N, N)

    def plus(A, B, Result):
        Result[:,:] = A + B

    def minus(A, B, Result):
        Result[:,:] = A - B

    def naiv_standard(A, B, Result, N, P, M):
        for i in range(N):
            for j in range(M):
                Result[i, j] = np.dot(A[i, :P], B[:P, j])

    
