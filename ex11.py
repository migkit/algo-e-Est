
novoEmail=str.lower(input("Insira um Email "))

novaSenha=input("Insira uma senha ")

print("Usuário criado. Para fazer login:")
if len(novaSenha) >= 8:
    email=input("Insira seu email ")
    senha=input("Insira sua senha ")
    if email == novoEmail and senha == novaSenha:
        print("Login efetuado")
    else:
        print("Email ou senha incorretos")
else:
    print("Sua senha precisa tem mais que 8 caracteres. Tente novamente.") 
