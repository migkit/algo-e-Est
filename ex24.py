
for i in range(5):           #recebe os 5 numeros do usuario
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)


maior = numeros[0]
menor = numeros[0]


for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")