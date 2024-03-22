# Lista de frutas
frutas = ['manzana', 'banana', 'naranja', 'pera']

# Utilizando enumerate para obtener el índice y el elemento
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

# Dos listas de números
numeros1 = [1, 2, 3, 4]
numeros2 = [10, 20, 30, 40]

# Utilizando zip para combinar las listas
for num1, num2 in zip(numeros1, numeros2):
    print(f"Número 1: {num1}, Número 2: {num2}")








# Dos listas de frutas
frutas = ['manzana', 'banana', 'naranja', 'pera']
precios = [1.50, 0.75, 2.00, 1.25]

# Utilizando enumerate y zip juntos para imprimir el índice, la fruta y su precio
for indice, (fruta, precio) in enumerate(zip(frutas, precios)):
    print(f"Índice: {indice}, Fruta: {fruta}, Precio: {precio}")
