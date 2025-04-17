umeros = []
pares = []
impares = []

for i in range(1, 9):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números ímpares:", impares)