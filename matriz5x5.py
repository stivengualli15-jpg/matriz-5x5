# Inicializar una matriz de 5x5 llena de ceros
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Recorrer la matriz para solicitar los 25 valores al usuario
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        matriz[i][j] = valor

# Mostrar la matriz resultante organizada por filas y columnas
print("\nMatriz ingresada:")

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()