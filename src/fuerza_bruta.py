def resolver(paquetes, camiones):

    mejor = []
    max_paquetes = 0

    def fuerza_bruta(indice, asignacion, cargas):

        nonlocal mejor
        nonlocal max_paquetes

        if indice == len(paquetes):

            cantidad = sum(len(c) for c in asignacion)

            if cantidad > max_paquetes:
                max_paquetes = cantidad
                mejor = [c.copy() for c in asignacion]

            return

        paquete = paquetes[indice]
        id_paquete = paquete[0]
        peso = paquete[1]

        for i in range(len(camiones)):

            capacidad = camiones[i][1]

            if cargas[i] + peso <= capacidad:

                cargas[i] += peso
                asignacion[i].append(id_paquete)

                fuerza_bruta(indice + 1, asignacion, cargas)

                cargas[i] -= peso
                asignacion[i].pop()

        fuerza_bruta(indice + 1, asignacion, cargas)

    asignacion_inicial = [[] for _ in camiones]
    cargas_iniciales = [0] * len(camiones)

    fuerza_bruta(0, asignacion_inicial, cargas_iniciales)

    # Formatear igual que el otro
    asignacion_final = {}

    for i in range(len(camiones)):
        id_camion = camiones[i][0]
        asignacion_final[id_camion] = mejor[i] if i < len(mejor) else []

    return {
        "total_entregados": max_paquetes,
        "asignacion": asignacion_final
    }