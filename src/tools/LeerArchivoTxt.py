def leer_archivo(ruta, n):
    matriz = [[0] * n for _ in range(n)]  # Crear una matriz de tamaño nxn con ceros
    
    try:
        with open(ruta, 'r') as archivo:
            for i in range(n):
                linea = archivo.readline().strip()  # Leer una línea del archivo y quitar espacios en blanco
                valores = linea.split()  # Dividir la línea en valores separados por espacios
                for j in range(n):
                    matriz[i][j] = int(valores[j])  # Convertir cada valor a entero y asignarlo a la matriz
    except FileNotFoundError as e:
        print("Archivo no encontrado:", e)
    
    return matriz
