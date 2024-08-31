temperaturas = []
print("Por favor, ingresas 10 temperaturas:")

for i in range(10):
    temperatura = float(input(f"temperatura {i + 1 }:"))
    temperaturas.append(temperatura)

promedio = sum(temperaturas) / len(temperaturas)

print(f"\nEl promedio de las temperaturas es: {promedio: .2f}")

while True:
    opcion = input("\n¿Ver alguna temperatura en especifico? (yes/no): ").strip().lower()

    if opcion == "yes":
        posicion = int(input("Ingresa la posicion (1-10) de la temperatura que deseas ver: "))
        if 1 <= posicion >= 10:
            print(f"La temperatura en la posicion {posicion} es: {temperaturas[posicion - 1]}:.2f")
        else:
            print("Posicion fuera de rango. Por favor, ingrese un numero entre 1 y 10.")
    elif opcion  == "no":
        print("Cierre del programa.")
        break

    else:
        print("Por favor, ingrese 'yes' o 'no'.")