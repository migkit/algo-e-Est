palavras = []
palindromos = []

for i in range(1, 6):
    palavra = input(f"Digite a {i}ª palavra: ")
    palavras.append(palavra)

for palavra in palavras:
    if palavra == palavra[::-1]:
        palindromos.append(palavra)

print("Palavras palíndromas:", palindromos)