import os

def leer_tiempos_matriz(nombre_archivo):
    tiempos = []
    ruta_archivo = os.path.join("TimeResultMatriz", nombre_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                tiempo = float(linea.strip())
                tiempos.append(tiempo)
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
    return tiempos

def leer_todos_los_tiempos():
    resultados = {}
    nombres_archivos = os.listdir("TimeResultMatriz")
    for nombre_archivo in nombres_archivos:
        matriz = nombre_archivo.split(".")[0]
        tiempos = leer_tiempos_matriz(nombre_archivo)
        resultados[matriz] = tiempos
    return resultados

# Ejemplo de uso:
resultados = leer_todos_los_tiempos()
print(resultados)