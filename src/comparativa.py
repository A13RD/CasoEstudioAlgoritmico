import time
import backtracking as bt
import divide_y_venceras as dv
import fuerza_bruta as fb
import greedy as gr
import recursivo as re

#inicio = time.time()
#  algoritmo
#fin = time.time()
#print(fin - inicio)

# =========================
# Rutas
# =========================

rutas = [
    ("pequeno", "datos/caso_pequeno.txt"),
    ("mediano", "datos/caso_mediano.txt"),
    ("grande", "datos/caso_grande.txt")
]

# =========================
# Listas finales
# =========================

paquetes_caso_pequeno = []
camiones_caso_pequeno = []

paquetes_caso_mediano = []
camiones_caso_mediano = []

paquetes_caso_grande = []
camiones_caso_grande = []

# =========================
# Lectura en un solo for
# =========================

for nombre, ruta in rutas:

    paquetes_temp = []
    camiones_temp = []

    with open(ruta, "r") as f:
        lineas = f.readlines()

    # Limpiar líneas
    lineas = [l.strip() for l in lineas if l.strip() and not l.startswith("#")]

    # Primera línea
    n, m = map(int, lineas[0].split())

    # Paquetes
    for i in range(1, n + 1):
        partes = lineas[i].split()
        paquetes_temp.append([
            int(partes[0]),
            int(partes[1]),
            partes[2],
            int(partes[3]),
            int(partes[4])
        ])

    # Camiones
    for i in range(n + 1, n + 1 + m):
        partes = lineas[i].split()
        camiones_temp.append([
            int(partes[0]),
            int(partes[1])
        ])

    # Asignar según el caso
    if nombre == "pequeno":
        paquetes_caso_pequeno = paquetes_temp
        camiones_caso_pequeno = camiones_temp

    elif nombre == "mediano":
        paquetes_caso_mediano = paquetes_temp
        camiones_caso_mediano = camiones_temp

    elif nombre == "grande":
        paquetes_caso_grande = paquetes_temp
        camiones_caso_grande = camiones_temp

# =========================
# Verificación
# =========================

print("Pequeño:", paquetes_caso_pequeno, camiones_caso_pequeno)
print("Mediano:", paquetes_caso_mediano, camiones_caso_mediano)
print("Grande:", paquetes_caso_grande, camiones_caso_grande)