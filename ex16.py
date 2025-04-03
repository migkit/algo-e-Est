nota1 = float(input("insira a primeira nota: " ))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insira a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media>= 7 :
    print("aprovado")

elif media<7 and media>=5 :
    print("recuperaçao")

elif media<5 :
    print("reprovado")