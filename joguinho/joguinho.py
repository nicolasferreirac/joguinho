print('********************************')
print('bem vindo no jogo de adivinhacao')
print('********************************')

numero_secreto = 5
total_de_tentativas = 3


for rodada in range (1, total_de_tentativas +1): # ou 4 
    print('tentativas {} de {}'. format(rodada, total_de_tentativas))
    chute_str = input('DIGITE UM NUMERO ENTRE 1 a 100: ')
    print('VOCE DIGITOU; ' , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('!.!.!.! E R R O U !.!.!.!')
        continue

    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto

    if(acertou):
        print('VOCE ACERTOU O NUMERO. ')
        break
    else:
        if(menor):
            print('VOCE ERRO, O NUMERO ESTA MENOR! TENTA NOVAMENTE.')
        elif(maior):
            print('VOCE ERROU, O NUMERO ESTA MAIOR! TENTE NOVAMENTE.')
          
          

print('G  A  M  E    O  V  E  R')

