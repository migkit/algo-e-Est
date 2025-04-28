def tabuada_personalizada(base,inicio,fim):
    print(f"tabuada do {base} de {inicio} a {fim}:")
    for j in range(inicio,fim+1):
            print(f"{base}  x{j}= {base*j}")


tabuada_personalizada=int(input("insira um numero"))