notas = []
soma = 0


for i in range(1, 6):
    nota = float(input(f"Digite a nota do {i}º aluno: "))   #coleta as 5 notas
    notas.append(nota)


for nota in notas:   # soma todas as notas
    soma += nota


media = soma / 5   #calcula a media


print(f"A média das notas é: {media}")   #exibe a media