nomes = []

for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º amigo: ")
    nomes.append(nome)

nomes.sort()

print("\nNomes em ordem alfabética:")
for nome in nomes:
    print(nome)