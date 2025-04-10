idade = int(input("insira sua idade: "))
genero = input("insira seu genero: ")
atleta = input("voce e atleta: ")

if idade <= 15 :
    print("aqui estao os artigos infantis")
elif idade >= 15 and idade <= 21 and genero == "feminino" :
    print("aqui estao as maquiagens e moda feminina")
elif idade >= 15 and idade <= 32 and genero == "masculino":
    print("aqui esta o artigo esportivo")
elif idade >= 15 and idade <= 21 and atleta == "nao" and genero == "masculino":
    print("aqui estao os video games")
elif idade >= 21 and idade <= 32 and atleta == "nao" and genero == "masculino":
    print ("aqui estao os livros, jardinagem e eletrodomesticos")
elif idade >= 22 and idade <= 35 and genero == "feminino":
    print("aqui estao os arigos espotivos e itens de casa")