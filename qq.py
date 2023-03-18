import random


numero = random.randint(1,100)
tentativas =0

while tentativas < 10:
    
    palpite = int(input("Escolha um numero"))
    tentativas =tentativas +1
    if palpite == numero:
        print("Você acertou")
        break
    elif palpite > numero:
        print("É menor né")
        
    else:
        print("É maior né")
        
else:
    print("Você perdeu")



