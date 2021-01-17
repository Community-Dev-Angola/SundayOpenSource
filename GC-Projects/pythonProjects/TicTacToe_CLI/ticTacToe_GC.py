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

# ************** IMPORTS DO ALGORITMO *****************
import os
from random import randint

# ********************** VARIAVEIS GLOBAIS **************************
peca = 'X'
rodada = 0
quadro = [' '] * 9


# ******************** FUNCAO QUE ORGANIZA O QUADRO DO JOGO *************************
def mostrarQuadro(qd):
    print()
    print(f"{qd[0]}|{qd[1]}|{qd[2]}")
    print('-+-+-')
    print(f"{qd[3]}|{qd[4]}|{qd[5]}")
    print('-+-+-')
    print(f"{qd[6]}|{qd[7]}|{qd[8]}")


# ************************** FUNCAO QUE VALIDA VITORIA **********************************
def vitoria():
    return quadro[0] == quadro[1] and quadro[0] == quadro[2] and quadro[0] != ' ' or \
           quadro[3] == quadro[4] and quadro[3] == quadro[5] and quadro[3] != ' ' or \
           quadro[6] == quadro[7] and quadro[6] == quadro[8] and quadro[6] != ' ' or \
           quadro[0] == quadro[3] and quadro[0] == quadro[6] and quadro[0] != ' ' or \
           quadro[1] == quadro[4] and quadro[1] == quadro[7] and quadro[1] != ' ' or \
           quadro[2] == quadro[5] and quadro[2] == quadro[8] and quadro[2] != ' ' or \
           quadro[0] == quadro[4] and quadro[0] == quadro[8] and quadro[0] != ' ' or \
           quadro[2] == quadro[4] and quadro[2] == quadro[6] and quadro[2] != ' '


# *************************** DEFININDO A FUNCAO PARA DOIS JOGADORES *********************************
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
                        os.system("pause")
                        break
                    peca = 'O'
                elif peca == 'O':
                    if vitoria():
                        print(f'\nFim do Jogo..\nVitória para Jogador [{peca}];')
                        mostrarQuadro(quadro)
                        os.system("pause")
                        break
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
        if not vitoria():
            if ' ' not in quadro[:]:
                print(f'\nFim do Jogo..\nEmpate;')
                mostrarQuadro(quadro)
                break


# *************************** DEFININDO IA DO JOGO ***********************************
def jogada_pc(p):
    pc = randint(0, 8)
    if quadro[pc] == ' ':
        quadro[pc] = p
        if vitoria():
            print('Fim do jogo..\nComputador Ganhou!')
            mostrarQuadro(quadro)
            os.system("pause")
    else:
        jogada_pc(p)


def jogada_hm(p):
    jogada_h = int(input('Selecione a sua posição de jogo: [0-8]\n> '))
    if quadro[jogada_h] == ' ':
        quadro[jogada_h] = p
        if vitoria():
            print('Fim do jogo..\nVocê Ganhou!')
            mostrarQuadro(quadro)
            os.system("pause")
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
                os.system("pause")
        except IndexError:
            rodada -= 1
            pass
        rodada += 1
        if not vitoria():
            if ' ' not in quadro[:]:
                print(f'\nFim do Jogo..\nEmpate;')
                mostrarQuadro(quadro)
                break


# ******************************* DEFININDO O RUN E CORPO DO JOGO ***************************************
if __name__ == '__main__':
    print('\n\t\t\t\t\t*** TicTacToe-GC ***')
    while not vitoria():
        try:
            print("\n************************************************************************")
            jogo = input('\nSelecione o nível: (1)Jogador ou (2)Jogadores | Ou (s)air..\n> ')
            if jogo == '1':
                um_jogador()
            elif jogo == '2':
                dois_jogadores()
            elif jogo == 's':
                exit()
            else:
                print('\nDigite 1, 2..\nOu s para sair!')
                pass
        except Exception as e:
            print("Terminando Jogo..")
            exit()
        if ' ' not in quadro[:]:
            confirma = input("\nPressione (s) para sair...\n> ")
            if confirma == 's':
                exit()
