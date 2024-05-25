def cantidad_minima_de_cambio(monedas):
    monedas.sort()  # Ordenar las monedas en orden ascendente
    min_change = 1  # Inicializar la cantidad mínima de cambio que no se puede dar
    print(monedas)
    for moneda in monedas:
        print('valor de moneda',moneda)
        if moneda > min_change:
            print('valor de moneda dentro del if ', moneda)
            break  # Si encontramos una moneda mayor que min_change, terminamos
        
        min_change += moneda  # Aumentar min_change sumando el valor de la moneda actual
        print('valor de min_change',min_change)
    
    return min_change

# Ejemplos de uso
# print(cantidad_minima_de_cambio([1,2,4,9]))  # Output: 15
# print(cantidad_minima_de_cambio([1, 1, 1, 1, 1]))         # Output: 6
print(cantidad_minima_de_cambio([ 17, 52, 53, 54, 56, 76, 80, 93]))  # Output: 55
