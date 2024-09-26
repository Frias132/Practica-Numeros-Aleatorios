def cuadrados_medios(seed, n):
    numeros = []
    for _ in range(n):
        # Eleva la semilla al cuadrado y convierte a cadena
        seed = str(seed ** 2).zfill(8)  # Rellenar con ceros a la izquierda para tener siempre 8 dígitos
        # Extraer el centro (4 dígitos)
        middle = seed[2:6]
        # Convertir de nuevo a entero
        seed = int(middle)
        numeros.append(seed)
    return numeros

# Semilla inicial
semilla_inicial = 1234  # Puedes cambiar la semilla a tu gusto
# Generar 100 números
numeros_aleatorios = cuadrados_medios(semilla_inicial, 100)

# Mostrar los números en consola
for num in numeros_aleatorios:
    print(num)
