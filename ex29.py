valores = []

for i in range(1, 5):
    numero = int(input(f"Digite o {i}º número: "))
    valores.append(numero)

multiplicador = int(input("Digite um número para multiplicar os elementos da lista: "))

for i in range(len(valores)):
    valores[i] *= multiplicador

print("Novos valores da lista:", valores)