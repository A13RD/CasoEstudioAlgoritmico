import time
import backtracking as bt
import divide_y_venceras as dv
import fuerza_bruta as fb
import greedy as gr
import recursivo as re
import matplotlib.pyplot as plt 

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

# =========================
# INPUTS
# =========================

print("\nAlgoritmos disponibles:")
print("1. fuerza_bruta")
print("2. greedy")
print("3. backtracking")
print("4. recursivo")
print("5. divide_y_venceras")

op_algoritmo = input("\nSeleccione algoritmo: ")

print("\nCasos disponibles:")
print("1. pequeno")
print("2. mediano")
print("3. grande")

op_caso = input("\nSeleccione caso: ")


# =========================
# Seleccionar algoritmo
# =========================

if op_algoritmo == "1":

    funcion = fb.resolver
    nombre_algoritmo = "Fuerza Bruta"

elif op_algoritmo == "2":

    funcion = gr.resolver
    nombre_algoritmo = "Greedy"

elif op_algoritmo == "3":

    funcion = bt.resolver
    nombre_algoritmo = "Backtracking"

elif op_algoritmo == "4":

    funcion = re.resolver
    nombre_algoritmo = "Recursivo"

elif op_algoritmo == "5":

    funcion = dv.resolver
    nombre_algoritmo = "Divide y Vencerás"

else:

    print("Algoritmo inválido")
    exit()


# =========================
# Seleccionar caso
# =========================

if op_caso == "1":

    paquetes = paquetes_caso_pequeno
    camiones = camiones_caso_pequeno
    nombre_caso = "Pequeño"

elif op_caso == "2":

    paquetes = paquetes_caso_mediano
    camiones = camiones_caso_mediano
    nombre_caso = "Mediano"

elif op_caso == "3":

    paquetes = paquetes_caso_grande
    camiones = camiones_caso_grande
    nombre_caso = "Grande"

else:

    print("Caso inválido")
    exit()

# =========================
# Ejecutar
# =========================

print("\n========================")
print("Algoritmo:", nombre_algoritmo)
print("Caso:", nombre_caso)
print("========================")

inicio = time.time()

resultado = funcion(
    paquetes,
    camiones
)

fin = time.time()

print("\nResultado:")
print(resultado)

print("\nTiempo:")
print(fin - inicio)


# --------------------------------------------------------------------------------------------
#ENTREGA 1
#GRAFICAS

#FUERZA BRUTA - TIEMPO VS TAMAÑO DE ENTRADA


# Datos empíricos

casos = ["Pequeño\n(5 paq, 2 cam)", "Mediano\n(15 paq, 4 cam)", "Grande\n(40 paq, 8 cam)"]
tiempos = [0.000123, 80.95, None]
combinaciones = [32, 1073741824, float('inf')]

# Para graficar el caso grande usamos una estimacion visual ya que no obtuvimos un tiempo real
tiempos_grafica = [0.000123, 80.95, 150]  # 150 es solo para mostrar que sigue subiendo

colores = ["green", "orange", "red"]

# Grafica

plt.figure(figsize=(10, 6))

barras = plt.bar(casos, tiempos_grafica, color=colores)

# Etiquetas
plt.text(0, tiempos_grafica[0] + 1, "0.000123 seg", ha="center", fontsize=10)
plt.text(1, tiempos_grafica[1] + 1, "80.95 seg", ha="center", fontsize=10)
plt.text(2, tiempos_grafica[2] + 1, "No terminó", ha="center", fontsize=10)

plt.title("Fuerza Bruta — Tiempo de ejecución vs Tamaño de entrada", fontsize=13)
plt.xlabel("Caso de prueba", fontsize=11)
plt.ylabel("Tiempo (segundos)", fontsize=11)

plt.tight_layout()
