ativada = True
saldo=float(input("Insira o saldo da conta "))
if saldo == 0:
    ativada = False
if ativada == True:
    print("Conta ativa")
else:
    print("Conta desativada")