

numero = random.randint(1, 20)    #sorteio do numero de 1 a 20


palpites = []    #lista para guardar os palpites

acertou = False

while not acertou:
    palpite = int(input("Digite um número entre 1 e 20: "))
    palpites.append(palpite)

    if palpite == numero:
        print("Você acertou!")
        acertou = True
    elif palpite < numero:
        print("Tente um número MAIOR.")
    else:
        print("Tente um número MENOR.")


print("Palpites feitos:", palpites)   #mostra os palpites