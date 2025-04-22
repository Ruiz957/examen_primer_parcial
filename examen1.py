def es_perfecto(numero):
    original = numero
    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10

    return original == invertido

# Llamada a la función y mensaje adecuado
numero = int(input("Ingresa un número entero: "))
if es_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")