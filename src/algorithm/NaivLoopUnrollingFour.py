from tools.Imprimir import Imprimir

class NaivLoopUnrollingFour(Imprimir):

    @staticmethod
    def naivLoopUnrollingFour(A, B):
        N = len(A)
        Result = [[0] * N for _ in range(N)]
        i, j, k = 0, 0, 0
        aux = 0

        if N % 4 == 0:
            for i in range(N):
                for j in range(N):
                    aux = 0
                    for k in range(0, N, 4):
                        aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                    Result[i][j] = aux
        elif N % 4 == 1:
            PP = N - 1
            for i in range(N):
                for j in range(N):
                    aux = 0
                    for k in range(0, PP, 4):
                        aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                    Result[i][j] = aux + A[i][PP] * B[PP][j]
        elif N % 4 == 2:
            PP = N - 2
            PPP = N - 1
            for i in range(N):
                for j in range(N):
                    aux = 0
                    for k in range(0, PP, 4):
                        aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                    Result[i][j] = aux + A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j]
        else:
            PP = N - 3
            PPP = N - 2
            PPPP = N - 1
            for i in range(N):
                for j in range(N):
                    aux = 0
                    for k in range(0, PP, 4):
                        aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                    Result[i][j] = aux + A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j] + A[i][PPPP] * B[PPPP][j]
        # imprimirMatriz(Result)