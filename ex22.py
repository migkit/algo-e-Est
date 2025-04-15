palavras = []
quantidade=0

for i in range(1,7):
    palavra = input(f"insira a {i}° palavra: ")
    palavras.append(palavra)

for palavra in palavras:
    if len(palavra) > 5:
        quantidade += 1 

print(f"tiveram {quantidade}° palavras com mais de 5 caracteres")