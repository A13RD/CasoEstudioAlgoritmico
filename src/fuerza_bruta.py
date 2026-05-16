from itertools import product

def resolver(paquetes, camiones):
    n = len(paquetes)
    m = len(camiones)
    
    mejor_cantidad = -1                    
    mejor_asignacion = {}
    mejor_detalle = None
    
    print(f"Combinaciones a probar: { (m+1)**n }")
    
    for combinacion in product(range(m + 1), repeat=n):
        carga_actual = [0] * m
        asignacion = [[] for _ in range(m)]
        cantidad = 0
        es_valido = True
        
        for i in range(n):
            camion = combinacion[i]
            
            if camion == m:
                continue
                
            peso = paquetes[i][1]
            
            if carga_actual[camion] + peso > camiones[camion][1]:
                es_valido = False
                break
                
            carga_actual[camion] += peso
            asignacion[camion].append(paquetes[i][0])  
            cantidad += 1
        
        if es_valido and cantidad > mejor_cantidad:
            mejor_cantidad = cantidad
            mejor_asignacion = {}
            for c in range(m):
                camion_id = camiones[c][0]
                mejor_asignacion[camion_id] = sorted(asignacion[c])
            
            mejor_detalle = {
                'total_entregados': cantidad,
                'asignacion': mejor_asignacion.copy(),
                'carga_usada': carga_actual.copy()}
    
    
    # Si no encontró ninguna solución válida
    if mejor_cantidad == -1:
        print("No se encontró ninguna asignación válida.")
        return {'total_entregados': 0, 'asignacion': {}}
    
    # Mostrar resultado
    print(f"\nPaquetes entregados: {mejor_cantidad}/{n}")
    for camion_id, lista in mejor_asignacion.items():
        print(f"Camión {camion_id}: {lista}")
    
    return mejor_detalle