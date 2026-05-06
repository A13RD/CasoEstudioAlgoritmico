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
# Caso Pequeño
# =========================

ruta_caso_pequeno = "datos/caso_pequeno.txt"  

paquetes_caso_pequeno = []
camiones_caso_pequeno = []

with open(ruta_caso_pequeno, "r") as f:
    lineas = f.readlines()

# Limpiar líneas
lineas = [l.strip() for l in lineas if l.strip() and not l.startswith("#")]

# Primera línea
n, m = map(int, lineas[0].split())

for i in range(1, n + 1):
    partes = lineas[i].split()
    paquetes_caso_pequeno.append([
        int(partes[0]),  # id
        int(partes[1]),  # peso
        partes[2],       # destino
        int(partes[3]),  # inicio
        int(partes[4])   # fin
    ])

for i in range(n + 1, n + 1 + m):
    partes = lineas[i].split()
    camiones_caso_pequeno.append([
        int(partes[0]),  # id
        int(partes[1])   # capacidad
    ])

# =========================
# Verificacion Caso Pequeño
# =========================

print("Paquetes Caso Pequeño:", paquetes_caso_pequeno)
print("Camiones Caso Pequeño:", camiones_caso_pequeno)

# =========================
# Caso Mediano
# =========================

ruta_caso_mediano = "datos/caso_mediano.txt"  

paquetes_caso_mediano = []
camiones_caso_mediano = []

with open(ruta_caso_mediano, "r") as f:
    lineas = f.readlines()

# Limpiar líneas
lineas = [l.strip() for l in lineas if l.strip() and not l.startswith("#")]

# Primera línea
n, m = map(int, lineas[0].split())

for i in range(1, n + 1):
    partes = lineas[i].split()
    paquetes_caso_mediano.append([
        int(partes[0]),  # id
        int(partes[1]),  # peso
        partes[2],       # destino
        int(partes[3]),  # inicio
        int(partes[4])   # fin
    ])

for i in range(n + 1, n + 1 + m):
    partes = lineas[i].split()
    camiones_caso_mediano.append([
        int(partes[0]),  # id
        int(partes[1])   # capacidad
    ])

# =========================
# Verificacion Caso Mediano
# =========================

print("Paquetes Caso Mediano:", paquetes_caso_mediano)
print("Camiones Caso Mediano:", camiones_caso_mediano)

# =========================
# Caso Grande
# =========================

ruta_caso_grande = "datos/caso_grande.txt"  

paquetes_caso_grande = []
camiones_caso_grande = []

with open(ruta_caso_grande, "r") as f:
    lineas = f.readlines()

# Limpiar líneas
lineas = [l.strip() for l in lineas if l.strip() and not l.startswith("#")]

# Primera línea
n, m = map(int, lineas[0].split())

for i in range(1, n + 1):
    partes = lineas[i].split()
    paquetes_caso_grande.append([
        int(partes[0]),  # id
        int(partes[1]),  # peso
        partes[2],       # destino
        int(partes[3]),  # inicio
        int(partes[4])   # fin
    ])

for i in range(n + 1, n + 1 + m):
    partes = lineas[i].split()
    camiones_caso_grande.append([
        int(partes[0]),  # id
        int(partes[1])   # capacidad
    ])

# =========================
# Verificacion Caso Grande
# =========================

print("Paquetes Caso Grande:", paquetes_caso_grande)
print("Camiones Caso Grande:", camiones_caso_grande)