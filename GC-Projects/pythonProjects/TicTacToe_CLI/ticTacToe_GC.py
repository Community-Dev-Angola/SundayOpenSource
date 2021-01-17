#! python

# ******************************************************************************
#  Direitos Autorais (c) 2019-2020 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from random import randint

peca = 'X'
rodada = 0

quadro = [' '] * 9


def mostrarQuadro(quadro):
    print()
    print(f"{quadro[0]}|{quadro[1]}|{quadro[2]}")
    print('-+-+-')
    print(f"{quadro[3]}|{quadro[4]}|{quadro[5]}")
    print('-+-+-')
    print(f"{quadro[6]}|{quadro[7]}|{quadro[8]}")


def vitoria():
    return quadro[0] == quadro[1] and quadro[0] == quadro[2] and quadro[0] != ' ' or \
           quadro[3] == quadro[4] and quadro[3] == quadro[5] and quadro[3] != ' ' or \
           quadro[6] == quadro[7] and quadro[6] == quadro[8] and quadro[6] != ' ' or \
           quadro[0] == quadro[3] and quadro[0] == quadro[6] and quadro[0] != ' ' or \
           quadro[1] == quadro[4] and quadro[1] == quadro[7] and quadro[1] != ' ' or \
           quadro[2] == quadro[5] and quadro[2] == quadro[8] and quadro[2] != ' ' or \
           quadro[0] == quadro[4] and quadro[0] == quadro[8] and quadro[0] != ' ' or \
           quadro[2] == quadro[4] and quadro[2] == quadro[6] and quadro[2] != ' '


def dois_jogadores():
    global rodada, peca, quadro
    while True:
        print(f'\n\nNivel: 2-Jogadores\nRodada: {rodada}')
        mostrarQuadro(quadro)

        jogada = int(input(f'\nSelecione aonde irá Jogar [{peca}]:\n[0-8]> '))
        try:
            if quadro[jogada] == ' ':
                quadro[jogada] = peca
                if peca == 'X':
                    if vitoria():
                        print(f'\nFim do Jogo..\nVitória para Jogador [{peca}];')
                        mostrarQuadro(quadro)
                        exit()
                    peca = 'O'
                elif peca == 'O':
                    if vitoria():
                        print(f'\nFim do Jogo..\nVitória para Jogador [{peca}];')
                        mostrarQuadro(quadro)
                        exit()
                    peca = 'X'
                else:
                    peca = ' '
            else:
                rodada -= 1
                print(f'\nSelecione outra Posição de Jogo para [{peca}]!')
                pass
        except IndexError:
            print('\nPosição Inválida, Tente Novamente;')
            rodada -= 1
            pass
        rodada += 1
        if ' ' not in quadro[:]:
            print(f'\nFim do Jogo..\nEmpate;')
            mostrarQuadro(quadro)
            exit()


def jogada_pc(p):
    pc = randint(0, 8)
    if quadro[pc] == ' ':
        quadro[pc] = p
        if vitoria():
            print('Fim do jogo..\nComputador Ganhou!')
            mostrarQuadro(quadro)
            exit()
    else:
        jogada_pc(p)


def jogada_hm(p):
    jogada_h = int(input('Selecione a sua posição de jogo: [0-8]\n> '))
    if quadro[jogada_h] == ' ':
        quadro[jogada_h] = p
        if vitoria():
            print('Fim do jogo..\nVocê Ganhou!')
            mostrarQuadro(quadro)
            exit()
    else:
        print('Selecione outra posição de jogo;')
        pass


def um_jogador():
    global rodada, peca, quadro
    while True:
        try:
            if ' ' in quadro[:]:
                if peca == 'X':
                    print(f'\n\nNível: 1-Jogador\nRodada: {rodada}')
                    mostrarQuadro(quadro)
                    jogada_hm(peca)
                    peca = 'O'
                elif peca == 'O':
                    jogada_pc(peca)
                    peca = 'X'
            else:
                print(f'\nFim do Jogo..\nEmpate;')
                mostrarQuadro(quadro)
                exit()
        except IndexError:
            rodada -= 1
            pass
        rodada += 1


if __name__ == '__main__':
    print('\n***TicTacToe-GC***')
    while True:
        try:
            jogo = input('\nSelecione o nível: (1)Jogador ou (2)Jogadores\n> ')
            if jogo == '1':
                um_jogador()
            elif jogo == '2':
                dois_jogadores()
            else:
                print('\nDigite 1 ou 2..')
                pass
        except KeyboardInterrupt:
            print("Terminando Jogo..")
            exit()
