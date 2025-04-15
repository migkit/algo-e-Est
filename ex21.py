numeros = []
soma = 0

for i in range(1,11):
    numero=int(input(f"insira o {i}° numero: "))
    numeros.append(numero)

for numero in numeros:
    print(numero)

for numero in numeros:
    soma += numero

print(f"soma dos numeros {numeros} é {soma}")


    