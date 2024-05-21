import numpy as np
import math

from tools.Imprimir import Imprimir

class StrassenNaiv(Imprimir):

    @staticmethod
    def max_val(N, P):
        return max(N, P)

    @staticmethod
    def plus(matrizA, matrizB, matrizRes, N, M):
        for i in range(N):
            for j in range(M):
                matrizRes[i][j] = matrizA[i][j] + matrizB[i][j]

    @staticmethod
    def minus(matrizA, matrizB, matrizRes, N, M):
        for i in range(N):
            for j in range(M):
                matrizRes[i][j] = matrizA[i][j] - matrizB[i][j]

    @staticmethod
    def algoritmoNaivStandard(matrizA, matrizB, matrizRes, N, P, M):
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(P):
                    aux += matrizA[i][k] * matrizB[k][j]
                matrizRes[i][j] = aux

    @staticmethod
    def strassenNaivStep(matrizA, matrizB, matrizRes, N, m):
        if (N % 2 == 0) and (N > m):
            newSize = N // 2

            varA11 = np.zeros((newSize, newSize))
            varA12 = np.zeros((newSize, newSize))
            varA21 = np.zeros((newSize, newSize))
            varA22 = np.zeros((newSize, newSize))
            varB11 = np.zeros((newSize, newSize))
            varB12 = np.zeros((newSize, newSize))
            varB21 = np.zeros((newSize, newSize))
            varB22 = np.zeros((newSize, newSize))

            resultadoPart11 = np.zeros((newSize, newSize))
            resultadoPart12 = np.zeros((newSize, newSize))
            resultadoPart21 = np.zeros((newSize, newSize))
            resultadoPart22 = np.zeros((newSize, newSize))

            helper1 = np.zeros((newSize, newSize))
            helper2 = np.zeros((newSize, newSize))

            aux1 = np.zeros((newSize, newSize))
            aux2 = np.zeros((newSize, newSize))
            aux3 = np.zeros((newSize, newSize))
            aux4 = np.zeros((newSize, newSize))
            aux5 = np.zeros((newSize, newSize))
            aux6 = np.zeros((newSize, newSize))
            aux7 = np.zeros((newSize, newSize))

            # Fill the new matrices
            for i in range(newSize):
                for j in range(newSize):
                    varA11[i][j] = matrizA[i][j]
                    varA12[i][j] = matrizA[i][newSize + j]
                    varA21[i][j] = matrizA[newSize + i][j]
                    varA22[i][j] = matrizA[newSize + i][newSize + j]
                    varB11[i][j] = matrizB[i][j]
                    varB12[i][j] = matrizB[i][newSize + j]
                    varB21[i][j] = matrizB[newSize + i][j]
                    varB22[i][j] = matrizB[newSize + i][newSize + j]

            # Calculate the steps
            StrassenNaiv.plus(varA11, varA22, helper1, newSize, newSize)
            StrassenNaiv.plus(varB11, varB22, helper2, newSize, newSize)
            StrassenNaiv.strassenNaivStep(helper1, helper2, aux1, newSize, m)

            StrassenNaiv.plus(varA21, varA22, helper1, newSize, newSize)
            StrassenNaiv.strassenNaivStep(helper1, varB11, aux2, newSize, m)

            StrassenNaiv.minus(varB12, varB22, helper1, newSize, newSize)
            StrassenNaiv.strassenNaivStep(varA11, helper1, aux3, newSize, m)

            StrassenNaiv.minus(varB21, varB11, helper1, newSize, newSize)
            StrassenNaiv.strassenNaivStep(varA22, helper1, aux4, newSize, m)

            StrassenNaiv.plus(varA11, varA12, helper1, newSize, newSize)
            StrassenNaiv.strassenNaivStep(helper1, varB22, aux5, newSize, m)

            StrassenNaiv.minus(varA21, varA11, helper1, newSize, newSize)
            StrassenNaiv.plus(varB11, varB12, helper2, newSize, newSize)
            StrassenNaiv.strassenNaivStep(helper1, helper2, aux6, newSize, m)

            StrassenNaiv.minus(varA12, varA22, helper1, newSize, newSize)
            StrassenNaiv.plus(varB21, varB22, helper2, newSize, newSize)
            StrassenNaiv.strassenNaivStep(helper1, helper2, aux7, newSize, m)

            # Calculate the result parts
            StrassenNaiv.plus(aux1, aux4, resultadoPart11, newSize, newSize)
            StrassenNaiv.minus(resultadoPart11, aux5, resultadoPart11, newSize, newSize)
            StrassenNaiv.plus(resultadoPart11, aux7, resultadoPart11, newSize, newSize)

            StrassenNaiv.plus(aux3, aux5, resultadoPart12, newSize, newSize)
            StrassenNaiv.plus(aux2, aux4, resultadoPart21, newSize, newSize)

            StrassenNaiv.plus(aux1, aux3, resultadoPart22, newSize, newSize)
            StrassenNaiv.minus(resultadoPart22, aux2, resultadoPart22, newSize, newSize)
            StrassenNaiv.plus(resultadoPart22, aux6, resultadoPart22, newSize, newSize)

            # Store the results in the resulting matrix
            for i in range(newSize):
                for j in range(newSize):
                    matrizRes[i][j] = resultadoPart11[i][j]
                    matrizRes[i][newSize + j] = resultadoPart12[i][j]
                    matrizRes[newSize + i][j] = resultadoPart21[i][j]
                    matrizRes[newSize + i][newSize + j] = resultadoPart22[i][j]
        else:
            StrassenNaiv.algoritmoNaivStandard(matrizA, matrizB, matrizRes, N, N, N)

    @staticmethod
    def algStrassenNaiv(matrizA, matrizB, matrizRes, N, P, M):
        maxSize = StrassenNaiv.max_val(N, P)
        if maxSize < 16:
            maxSize = 16

        k = int(math.floor(math.log(maxSize) / math.log(2)) - 4)
        m = int(math.floor(maxSize * math.pow(2, -k)) + 1)
        newSize = m * int(math.pow(2, k))

        newA = np.zeros((newSize, newSize))
        newB = np.zeros((newSize, newSize))
        auxResult = np.zeros((newSize, newSize))

        for i in range(N):
            for j in range(P):
                newA[i][j] = matrizA[i][j]

        for i in range(N):
            for j in range(M):
                newB[i][j] = matrizB[i][j]

        StrassenNaiv.strassenNaivStep(newA, newB, auxResult, newSize, m)

        for i in range(N):
            for j in range(M):
                matrizRes[i][j] = auxResult[i][j]

    @staticmethod
    def multiply(matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        M = len(matrizB[0])
        matrizRes = np.zeros((N, M))
        StrassenNaiv.algStrassenNaiv(matrizA, matrizB, matrizRes, N, P, M)
        return matrizRes

