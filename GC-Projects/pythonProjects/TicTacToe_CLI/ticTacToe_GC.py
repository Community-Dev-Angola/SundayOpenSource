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
import colorama

# ************ INICIANDO A CLASSE QUE VAI COLORIR O TERMINAL ************
colorama.init(autoreset=True)

# ********************** VARIAVEIS GLOBAIS **************************
peca = 'X'
rodada = 0
quadro = [' '] * 9


# ******************** FUNCAO QUE ORGANIZA O QUADRO DO JOGO *************************
def mostrarQuadro(qd):
    print()
    print(f"{qd[0]}|{qd[1]}|{qd[2]}")
    print(f"-+-+-")
    print(f"{qd[3]}|{qd[4]}|{qd[5]}")
    print(f"-+-+-")
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
        print(f'\n\n{colorama.Back.WHITE}{colorama.Fore.BLACK}Nivel: 2-Jogadores\nRodada: {rodada}')
        mostrarQuadro(quadro)

        jogada = int(input(f'\n{colorama.Fore.LIGHTYELLOW_EX}Selecione aonde irá Jogar [{peca}]:\n[0-8]> '))
        try:
            if quadro[jogada] == ' ':
                quadro[jogada] = peca
                if peca == 'X':
                    if vitoria():
                        print(f'\n{colorama.Fore.GREEN}Fim do Jogo..\nVitória para Jogador [{peca}];')
                        mostrarQuadro(quadro)
                        os.system("pause")
                        break
                    peca = 'O'
                elif peca == 'O':
                    if vitoria():
                        print(f'\n{colorama.Fore.GREEN}Fim do Jogo..\nVitória para Jogador [{peca}];')
                        mostrarQuadro(quadro)
                        os.system("pause")
                        break
                    peca = 'X'
                else:
                    peca = ' '
            else:
                rodada -= 1
                print(f'\n{colorama.Fore.RED}Selecione outra Posição de Jogo para [{peca}]!')
                pass
        except IndexError:
            print(f'\n{colorama.Back.RED}{colorama.Fore.LIGHTYELLOW_EX}Posição Inválida, Tente Novamente;')
            rodada -= 1
            pass
        rodada += 1
        if not vitoria():
            if ' ' not in quadro[:]:
                print(f'\n{colorama.Fore.LIGHTBLUE_EX}Fim do Jogo..\nEmpate;')
                mostrarQuadro(quadro)
                break


# *************************** DEFININDO IA DO JOGO ***********************************
def jogada_pc(p):
    pc = randint(0, 8)
    if quadro[pc] == ' ':
        quadro[pc] = p
        if vitoria():
            print(f'{colorama.Fore.GREEN}Fim do jogo..\nComputador Ganhou!')
            mostrarQuadro(quadro)
            os.system("pause")
    else:
        jogada_pc(p)


def jogada_hm(p):
    jogada_h = int(input(f'{colorama.Fore.LIGHTYELLOW_EX}Selecione a sua posição de jogo: [0-8]\n> '))
    if quadro[jogada_h] == ' ':
        quadro[jogada_h] = p
        if vitoria():
            print(f'{colorama.Fore.GREEN}Fim do jogo..\nVocê Ganhou!')
            mostrarQuadro(quadro)
            os.system("pause")
    else:
        print(f'{colorama.Fore.RED}Selecione outra posição de jogo;')
        pass


def um_jogador():
    global rodada, peca, quadro
    while True:
        try:
            if ' ' in quadro[:]:
                if peca == 'X':
                    print(f'\n\n{colorama.Back.WHITE}{colorama.Fore.BLACK}Nível: 1-Jogador\nRodada: {rodada}')
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
                print(f'\n{colorama.Fore.LIGHTBLUE_EX}Fim do Jogo..\nEmpate;')
                mostrarQuadro(quadro)
                break


# ******************************* DEFININDO O RUN E CORPO DO JOGO ***************************************
if __name__ == '__main__':
    print(f'\n\t\t\t\t\t{colorama.Back.WHITE}{colorama.Fore.LIGHTCYAN_EX}*** TicTacToe-GC ***')
    while not vitoria():
        try:
            print(f"\n{colorama.Fore.RED}************************************************************************")
            jogo = input(f'\n{colorama.Fore.LIGHTYELLOW_EX}Selecione o nível: (1)Jogador ou (2)Jogadores | Ou (s)air..\n> ')
            if jogo == '1':
                um_jogador()
            elif jogo == '2':
                dois_jogadores()
            elif jogo == 's':
                print(f"{colorama.Fore.RED}Terminando Jogo..")
                exit()
            else:
                print(f'\n{colorama.Fore.LIGHTRED_EX}Digite [1], [2] ou [s] para sair!')
                pass
        except Exception as e:
            print(f"{colorama.Fore.RED}Terminando Jogo..")
            exit()
        if ' ' not in quadro[:]:
            confirma = input(f"\n{colorama.Fore.LIGHTRED_EX}Pressione (s) para sair...\n> ")
            if confirma == 's':
                exit()
