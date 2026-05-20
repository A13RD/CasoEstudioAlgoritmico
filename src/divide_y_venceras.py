def dividir(paquetes, camiones, cargas, asignacion):

    # Caso base: no hay paquetes
    if len(paquetes) == 0:
        return asignacion

    # Caso base: un solo paquete
    if len(paquetes) == 1:

        paquete = paquetes[0]
        id_paquete = paquete[0]
        peso = paquete[1]

        for i in range(len(camiones)):

            if cargas[i] + peso <= camiones[i][1]:

                cargas[i] += peso
                asignacion[i].append(id_paquete)
                break

        return asignacion

    # Dividir la lista de paquetes a la mitad
    mitad = len(paquetes) // 2
    izquierda = paquetes[:mitad]
    derecha = paquetes[mitad:]

    # Resolver cada mitad por separado
    dividir(izquierda, camiones, cargas, asignacion)
    dividir(derecha, camiones, cargas, asignacion)

    return asignacion


def resolver(paquetes, camiones):

    cargas = [0] * len(camiones)
    asignacion = [[] for _ in camiones]

    resultado = dividir(paquetes, camiones, cargas, asignacion)

    asignacion_final = {}

    for i in range(len(camiones)):
        id_camion = camiones[i][0]
        asignacion_final[id_camion] = resultado[i]

    return {
        'total_entregados': sum(len(c) for c in resultado),
        'asignacion': asignacion_final}