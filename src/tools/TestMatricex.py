from tools.ExportarTiempos import ExportarTiempos

def export_all_matrices():
    try:
        ExportarTiempos.exportar_tiempos_matriz(matriz256x256, 1)
        ExportarTiempos.exportar_tiempos_matriz(matriz512x512, 2)
        ExportarTiempos.exportar_tiempos_matriz(matriz1024x1024, 3)
        ExportarTiempos.exportar_tiempos_matriz(matriz2048x2048, 4)
        ExportarTiempos.exportar_tiempos_matriz(matriz4096x4096, 5)
        ExportarTiempos.exportar_tiempos_matriz(matriz6144x6144, 6)
        ExportarTiempos.exportar_tiempos_matriz(matriz8192x8192, 7)
        ExportarTiempos.exportar_tiempos_matriz(matriz12288x12288, 8)
    except Exception as e:
        print("Error:", e)