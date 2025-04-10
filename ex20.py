idade = int(input("insira sua idade: "))
membro = input("voce e um membro?  ")
junto = input("voce esta acompanhado?  ")

if idade <  18 :
    print("voce nao pode entrar nao tem idade suficiente")
elif idade >= 18 :
    print("va para proxima pergunta")
elif membro == "nao":
    print("deve pagar um ingresso,  va para a proxima pergunta")
elif membro == "sim":
    print("nao precisa pagar, va para a proxima pergunta")
elif junto == "sim":
    print("o acompanhante paga meia-entrada")
elif junto == "nao":
    print("pode entrar!")