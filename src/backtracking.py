def backtracking(paquetes, camiones, indice,
                 cargas, asignacion,
                 mejor):

    # Caso base
    if indice == len(paquetes):

        total = sum(len(c) for c in asignacion)

        if total > mejor["total"]:
            mejor["total"] = total

            mejor["asignacion"] = [
                lista[:] for lista in asignacion
            ]

        return

    # PODA
    restantes = len(paquetes) - indice
    actual = sum(len(c) for c in asignacion)

    if actual + restantes <= mejor["total"]:
        return

    paquete = paquetes[indice]

    id_paquete = paquete[0]
    peso = paquete[1]

    # Intentar asignar a cada camión
    for i in range(len(camiones)):

        capacidad = camiones[i][1]

        if cargas[i] + peso <= capacidad:

            # HACER
            cargas[i] += peso
            asignacion[i].append(id_paquete)

            # RECURSION
            backtracking(
                paquetes,
                camiones,
                indice + 1,
                cargas,
                asignacion,
                mejor
            )

            # DESHACER
            cargas[i] -= peso
            asignacion[i].pop()

    # Opción: no asignar paquete
    backtracking(
        paquetes,
        camiones,
        indice + 1,
        cargas,
        asignacion,
        mejor
    )


def resolver(paquetes, camiones):

    cargas = [0] * len(camiones)

    asignacion = [
        [] for _ in camiones
    ]

    mejor = {
        "total": 0,
        "asignacion": []
    }

    backtracking(
        paquetes,
        camiones,
        0,
        cargas,
        asignacion,
        mejor
    )

    asignacion_final = {}

    for i in range(len(camiones)):

        id_camion = camiones[i][0]

        asignacion_final[id_camion] = (
            mejor["asignacion"][i]
            if mejor["asignacion"]
            else []
        )

    return {
        "total_entregados": mejor["total"],
        "asignacion": asignacion_final
    }