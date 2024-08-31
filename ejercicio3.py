filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingresa el numero de columnas: "))

matriz = []
print("\nPor favor,  ingrese los valores de la matriz:")
for i in range(filas):
    filas = []
    for j in range(columnas):
        valor = float(input(f"elemento [{i + 1}][{j + 1}]:"))
        filas.append(valor)
        matriz.append(filas)

print("\nLa matriz ingresada es:")
for fila in matriz:
    print(fila)