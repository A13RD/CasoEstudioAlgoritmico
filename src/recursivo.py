def recursivo(paquetes, camiones, indice, cargas, asignacion):

    # Caso base: ya se procesaron todos los paquetes
    if indice == len(paquetes):
        return asignacion

    paquete = paquetes[indice]
    id_paquete = paquete[0]
    peso = paquete[1]

    # Caso recursivo: buscar el primer camion donde quepa el paquete
    for i in range(len(camiones)):

        capacidad = camiones[i][1]

        if cargas[i] + peso <= capacidad:

            cargas[i] += peso
            asignacion[i].append(id_paquete)

            return recursivo(paquetes, camiones, indice + 1, cargas, asignacion)

    # Si no cabe en ningun camion, saltar el paquete
    return recursivo(paquetes, camiones, indice + 1, cargas, asignacion)


def resolver(paquetes, camiones):

    cargas = [0] * len(camiones)
    asignacion = [[] for _ in camiones]

    resultado = recursivo(paquetes, camiones, 0, cargas, asignacion)

    asignacion_final = {}

    for i in range(len(camiones)):
        id_camion = camiones[i][0]
        asignacion_final[id_camion] = resultado[i]

    return {
        'total_entregados': sum(len(c) for c in resultado),
        'asignacion': asignacion_final}