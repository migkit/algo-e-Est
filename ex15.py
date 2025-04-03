produto = input("insira nome do produto: ")
quanti = int(input("insira a quantidade desse produto: "))
valor = float(input("insira o valor do produto: "))

valorfinal = quanti * valor
desconto5 = valorfinal - valorfinal * 0.05
 
if valorfinal <= 100:
    print(f"Total: R$ {valorfinal}") 
else:
    print(desconto5)
