def medios_cuadrados(seed, n):
    numeros = []
    for _ in range(n):
        # Eleva la semilla al cuadrado y convierte a cadena
        seed_squared = str(seed ** 2).zfill(8)  # Asegura que el resultado tenga 8 dígitos
        # Extraer los 4 dígitos centrales
        middle = seed_squared[2:6]
        # Convertir el centro a entero
        seed = int(middle)
        numeros.append(seed)
    return numeros

# Semilla inicial
semilla_inicial = 1234  # Puedes cambiar la semilla a tu gusto
# Generar 100 números
numeros_aleatorios = medios_cuadrados(semilla_inicial, 100)

# Mostrar los números en consola
for num in numeros_aleatorios:
    print(num)
5