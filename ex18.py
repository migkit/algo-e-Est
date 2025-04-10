salario = float(input("insira seu salario base: "))
horasextras = float(input("insira quanto você ganha por hora extra: "))
horas = float(input("insira a quantidade de horas extras deste mes: "))

salariofinal = horasextras * horas + salario  
print(f"o salario deste mês é:{salariofinal}")
