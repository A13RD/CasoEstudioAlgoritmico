import time
import backtracking as bt
import divide_y_venceras as dv
import fuerza_bruta as fb
import greedy as gr
import recursivo as rec
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

###print("Pequeño:", paquetes_caso_pequeno, camiones_caso_pequeno)
###print("Mediano:", paquetes_caso_mediano, camiones_caso_mediano)
###print("Grande:", paquetes_caso_grande, camiones_caso_grande)

# =========================
# INPUTS
# =========================

print("\nAlgoritmos disponibles / grafica general:")
print("1. fuerza_bruta")
print("2. recursivo")
print("3. greedy")
print("4. backtracking")
print("5. divide_y_venceras")
print("6. grafica comparativa (todos)")

op_algoritmo = input("\nSeleccione algoritmo: ")

if op_algoritmo == "6":

    pass

else:

    print("\nCasos disponibles:")
    print("1. pequeno")
    print("2. mediano")
    print("3. grande")

    op_caso = input("\nSeleccione caso: ")


# =========================
# Seleccionar algoritmo
# =========================

if op_algoritmo == "1":

    #GRAFICAS
    #FUERZA BRUTA - TIEMPO VS TAMAÑO DE ENTRADA
    # Datos empíricos

    casos = [
        "Pequeño\n(80 paq, 15 cam)",
        "Mediano\n(700 paq, 120 cam)",
        "Grande\n(5000 paq, 900 cam)"]

    # Tiempos reales obtenidos (None = no terminó)
    tiempos = [None, None, None]

    # Valores para graficar (estimados para mediano y grande)
    tiempos_grafica = [10, 160, 770]

    colores = ["green", "orange", "red"]

    etiquetas = ["No terminó", "No terminó", "No terminó"]

    plt.figure(figsize=(10, 6))

    plt.bar(casos, tiempos_grafica, color=colores)

    for i, etiqueta in enumerate(etiquetas):
        plt.text(i, tiempos_grafica[i] + 1, etiqueta, ha="center", fontsize=10)

    plt.title("Fuerza Bruta — Tiempo de ejecución vs Tamaño de entrada", fontsize=13)
    plt.xlabel("Caso de prueba", fontsize=11)
    plt.ylabel("Tiempo (segundos)", fontsize=11)

    plt.tight_layout()
    plt.show()

    funcion = fb.resolver
    nombre_algoritmo = "Fuerza Bruta"

elif op_algoritmo == "2":
    #GRAFICAS
    #RECURSIVO - TIEMPO VS TAMAÑO DE ENTRADA
    # Datos empíricos

    casos = [
        "Pequeño\n(80 paq, 15 cam)",
        "Mediano\n(700 paq, 120 cam)",
        "Grande\n(5000 paq, 900 cam)"]

    # Tiempos reales obtenidos (None = no terminó)
    tiempos = [0.000854, 0.001466, None]

    # Valores para graficar (estimados para mediano y grande)
    tiempos_grafica = [0.0005, 0.005, 0.01]

    colores = ["green", "orange", "red"]

    etiquetas = ["0.000854 Segundos", "0.001466 Segundos", "No terminó"]

    plt.figure(figsize=(10, 6))

    plt.bar(casos, tiempos_grafica, color=colores)

    for i, etiqueta in enumerate(etiquetas):
        plt.text(i, tiempos_grafica[i] * 1.05, etiqueta, ha="center", fontsize=10)

    plt.title("Recursivo — Tiempo de ejecución vs Tamaño de entrada", fontsize=13)
    plt.xlabel("Caso de prueba", fontsize=11)
    plt.ylabel("Tiempo (segundos)", fontsize=11)

    plt.tight_layout()
    plt.show()

    funcion = rec.resolver
    nombre_algoritmo = "Recursivo"


elif op_algoritmo == "3":

    # GRAFICA - GREEDY
    

    casos = [
        "Pequeño\n(80 paq, 15 cam)",
        "Mediano\n(700 paq, 120 cam)",
        "Grande\n(5000 paq, 900 cam)"]
    
    tiempos = [0.000128, 0.001667, None]

    tiempos_grafica = [0.000128, 0.001667, 0.003]

    colores = ["green", "orange", "red"]

    etiquetas = [
        "0.000128 seg",
        "0.001667 seg",
        "No terminó"]

    plt.figure(figsize=(10, 6))

    plt.bar(casos, tiempos_grafica, color=colores)

    for i, etiqueta in enumerate(etiquetas):
        plt.text(i, tiempos_grafica[i] * 1.1, etiqueta, ha="center", fontsize=10)

    plt.ylim(0, max(tiempos_grafica) * 1.3)

    plt.title("Greedy — Tiempo de ejecución vs Tamaño de entrada", fontsize=13)
    plt.xlabel("Caso de prueba", fontsize=11)
    plt.ylabel("Tiempo (segundos)", fontsize=11)

    plt.tight_layout()
    plt.show()

    funcion = gr.resolver
    nombre_algoritmo = "Greedy"
    

elif op_algoritmo == "4":

    
    #GRAFICAS
    #BACKTRACKING - TIEMPO VS TAMAÑO DE ENTRADA
    # Datos empíricos

    casos = [
        "Pequeño\n(80 paq, 15 cam)",
        "Mediano\n(700 paq, 120 cam)",
        "Grande\n(5000 paq, 900 cam)"]

    # Tiempos reales obtenidos (None = no terminó)
    tiempos = [0.001530, 0.3733164, None]

    # Valores para graficar (estimados para mediano y grande)
    tiempos_grafica = [0.001, 0.3, 0.9]

    colores = ["green", "orange", "red"]

    etiquetas = ["0.001530 Segundos", "0.3733164 Segundos", "No terminó"]

    plt.figure(figsize=(10, 6))

    plt.bar(casos, tiempos_grafica, color=colores)

    for i, etiqueta in enumerate(etiquetas):
        plt.text(i, tiempos_grafica[i] + tiempos_grafica[i] * 0.1, etiqueta, ha="center", fontsize=10)

    plt.title("BackTracking — Tiempo de ejecución vs Tamaño de entrada", fontsize=13)
    plt.xlabel("Caso de prueba", fontsize=11)
    plt.ylabel("Tiempo (segundos)", fontsize=11)

    plt.tight_layout()
    plt.show()

    funcion = bt.resolver
    nombre_algoritmo = "Backtracking"

elif op_algoritmo == "5":

    #GRAFICAS
    #DIVIDE Y VENCERAS - TIEMPO VS TAMAÑO DE ENTRADA
    # Datos empíricos

    casos = [
        "Pequeño\n(80 paq, 15 cam)",
        "Mediano\n(700 paq, 120 cam)",
        "Grande\n(5000 paq, 900 cam)"]

    # Tiempos reales obtenidos (None = no terminó)
    tiempos = [0.0000935, 0.001338, 0.05358]

    # Valores para graficar (estimados para mediano y grande)
    tiempos_grafica = [0.001, 0.3, 0.9]

    colores = ["green", "orange", "red"]

    etiquetas = ["0.0000935 seg", "0.001338 seg", "0.05358 seg"]

    plt.figure(figsize=(10, 6))

    plt.bar(casos, tiempos_grafica, color=colores)

    for i, etiqueta in enumerate(etiquetas):
        plt.text(i, tiempos_grafica[i] + tiempos_grafica[i] * 0.1, etiqueta, ha="center", fontsize=10)

    plt.title("Divide y Vencerás — Tiempo de ejecución vs Tamaño de entrada", fontsize=13)
    plt.xlabel("Caso de prueba", fontsize=11)
    plt.ylabel("Tiempo (segundos)", fontsize=11)

    plt.tight_layout()
    plt.show()


    funcion = dv.resolver
    nombre_algoritmo = "Divide y Vencerás"

elif op_algoritmo == "6":

    # GRAFICA COMPARATIVA - TODOS LOS ALGORITMOS

    casos = [
        "Pequeño\n(80 paq, 15 cam)",
        "Mediano\n(700 paq, 120 cam)",
        "Grande\n(5000 paq, 900 cam)"]

    datos = {
        "Recursivo":        [0.000854, 0.001466, None],
        "Greedy":           [0.000128, 0.001667, None],
        "Backtracking":     [0.001530, 0.3733164, None],
        "Divide y Vencerás":[0.0000935, 0.001338, 0.05358],}

    colores = {
        "Recursivo": "purple",
        "Greedy": "blue",
        "Backtracking": "orange",
        "Divide y Vencerás": "green",}

    plt.figure(figsize=(10, 6))

    for algoritmo, tiempos in datos.items():

        x = []
        y = []

        for i, t in enumerate(tiempos):
            if t is not None:
                x.append(casos[i])
                y.append(t)

        plt.plot(x, y, marker="o", label=algoritmo, color=colores[algoritmo])

        for xi, yi in zip(x, y):
            plt.text(xi, yi + yi * 0.05, f"{yi} seg", ha="center", fontsize=8)

    plt.yscale("log")
    plt.title("Comparativa de algoritmos — Tiempo vs Tamaño de entrada", fontsize=13)
    plt.xlabel("Caso de prueba", fontsize=11)
    plt.ylabel("Tiempo (segundos)", fontsize=11)
    plt.legend()
    plt.tight_layout()
    plt.show()
    exit()

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
    camiones)

fin = time.time()

print("\nResultado:")
print(resultado)

print("\nTiempo:")
print(fin - inicio)
