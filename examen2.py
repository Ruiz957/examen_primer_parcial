def cantidad_leds(numero):
    # Diccionario con la cantidad de LEDs por cada dígito
    leds_por_digito = {
        0: 6, 1: 2, 2: 5, 3: 5, 4: 4,
        5: 5, 6: 6, 7: 3, 8: 7, 9: 6
    }
    
    total_leds = 0
    
    if numero == 0:  # Caso especial para el número 0
        return leds_por_digito[0]
    
    while numero > 0:
        digito = numero % 10
        total_leds += leds_por_digito[digito]
        numero = numero // 10

    return total_leds
    
numero = int(input("Ingresa un número entero para contar los LEDs: "))
print(f"Se necesitan {cantidad_leds(numero)} LEDs para formar el número {numero}.")
