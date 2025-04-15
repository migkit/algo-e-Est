numero = int(input("insira um numero: "))
tabuada = []

for i in range(1,11):
    produto = numero *i 
    tabuada.append (produto)

for i in range(1,11):
    print(f"{numero}*{i} = {tabuada[i-1]}")


    