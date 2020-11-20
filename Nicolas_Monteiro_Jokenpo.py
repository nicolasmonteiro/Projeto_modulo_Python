print('------Bem vindo ao Jokenpo-------\n')
pedra = papel = tesoura = 0
cont = 0
vit1 = vit2 = 0
jog1 = str(input('Informe nome do jogador 1\n'))
jog2 = str(input('Informe nome do jogador 2\n'))
while cont < 3:
    if vit1 == 2 or vit2 == 2:
        if vit1 > vit2 or vit2 > vit1:
            break
    print()
    print('1- Pedra 2- Papel 3- Tesoura\n')
    print(jog1, ', escolha um número relacionado as opções')
    esc1 = int(input())
    print(jog2, ', escolha um número relacionado as opções')
    esc2 = int(input())
    if (esc1 == esc2):
        print('Rodada empatada')
        cont += 1
    if ((esc1 == 1 and esc2 == 3) or (esc1 == 2 and esc2 == 1) or (esc1 == 3 and esc2 == 2)):
        vit1 += 1
        cont += 1
        print(jog1, 'venceu essa rodada')
        print(jog1, vit1, jog2, vit2)
    if ((esc1 == 1 and esc2 == 2) or (esc1 == 2 and esc2 == 3) or (esc1 == 3 and esc2 == 1)):
        vit2 += 1
        cont += 1
        print(jog2, 'venceu essa rodada')
        print(jog1, vit1, jog2, vit2)
if vit1 > vit2:
    print(jog1, 'venceu o jogo!')
    print("Por", vit1, 'a', vit2, 'com', cont, 'rodadas')
else:
    if vit2 > vit1:
        print(jog2, "venceu o jogo! ")
        print('Por', vit2, 'a', vit1, 'com', cont, 'rodadas')
    else:
        print('Jogo terminou empatado, com ', cont, 'rodadas')
print('--------Fim de jogo---------')
