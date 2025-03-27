preco = float (input("Insira o valor de sua compra: ")) 
 
if preco >= 100: 
    preco_desc =preco-( preco * 0.1)
    print (f"O valor de sua compra é: R$ {preco_desc}") 
else: 
    print (f"O valor de sua compra é: R$ {preco}")