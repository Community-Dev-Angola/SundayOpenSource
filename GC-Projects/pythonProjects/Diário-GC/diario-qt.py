#  Copyright (c) 2019-2020 Nurul GC
#  Direitos Autorais (c) 2019-2020 Nurul GC
#
#  Jovem Programador
#  Estudante de Engenharia de Telecomunicaçoes
#  Tecnologia de Informação e de Medicina.
#  Foco Fé Força Paciência
#  Allah no Comando.

from os import mkdir, path
from time import asctime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt, QSize, QCoreApplication
from sys import argv
from logging import *
import webbrowser

if not path.exists('DIARIOGC-{nome.text()}/debug'):
    mkdir("DIARIOGC-{nome.text()}/debug")
basicConfig(filename=f'DIARIOGC-{nome.text()}/debug/{asctime}.gc-log', level=INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def isEmpty(string: str):
    """funcao verificadora de strings vazias"""
    if (string.isspace()) or (string is "") or (string is None):
        return True
    return False





class DiarioGC:
    def __init__(self):
        self.gc = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(400, 400)
        self.ferramentas.setWindowTitle("Diario-GC")
        self.ferramentas.setPalette(QPalette(QColor("magenta")))

        # criando menus para melhor configuração e explanação
        self.menu = QMenuBar(self.ferramentas)
        menu = self.menu.addMenu('Opções')
        menu.setPalette(QPalette(QColor('white')))
        instrucoes = menu.addAction('Instruções')
        instrucoes.triggered.connect(self.instrucoes)
        menu.addSeparator()
        _sair_ = lambda: self.gc.instance().exit()
        sair = menu.addAction('Sair')
        sair.triggered.connect(_sair_)
        sobre = self.menu.addAction('Sobre')
        sobre.triggered.connect(self.sobre)

        # criando abas para melhor organização
        self.tab = QTabWidget(self.ferramentas)
        self.tab.setFixedSize(400, 380)
        self.tab.move(0, 25)

        self.abertura()

    # @staticmethod
    def abertura(self):
        janela1 = QWidget()

        layout = QVBoxLayout()

        labelIntro = QLabel('<h1>Bem-Vindo</h1>')
        labelIntro.setAlignment(Qt.AlignCenter)
        labelIntro.setFont(QFont('consolas', 9))
        layout.addWidget(labelIntro)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/artesgc_05.png"))
        labelImagem.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelImagem)

        def redirCadastro():
            """funcao redirecionadora para pagina cadastro
            com fechamento automatico da aba atual"""
            self.tab.removeTab(0)
            return self.cadastro()

        botaoCadastro = QPushButton('Cadastrar')
        botaoCadastro.clicked.connect(redirCadastro)
        botaoCadastro.setDefault(True)
        layout.addWidget(botaoCadastro)

        def redirIniciar():
            """funcao redirecionadora para pagina inicio-sessao
            com fechamento automatico da aba atual"""
            self.tab.removeTab(0)
            return self.iniciar()

        botaoInicio = QPushButton('Iniciar Sessão')
        botaoInicio.clicked.connect(redirIniciar)
        botaoInicio.setDefault(True)
        layout.addWidget(botaoInicio)

        janela1.setLayout(layout)
        self.tab.addTab(janela1, "🙋")
        self.tab.setCurrentWidget(janela1)

    # @staticmethod
    def cadastro(self):
        """funcao para cadastramento"""
        def guardar():
            if senha.text() is not confirmarSenha.text():
                QMessageBox.critical(self.ferramentas, "Falha", f"Lamento {self.nome.text()} as senhas não correspondem..")
                critical('senhas nao correspondem!')
                pass
            elif isEmpty(self.nome.text()) and isEmpty(senha.text()) and isEmpty(respostaEspecial.text()):
                QMessageBox.critical(self.ferramentas, "Falha", "Lamento, mas você precisa prencher devidamente os seus dados antes de iniciar..")
                critical('dados nao preenchidos!')
                pass
            else:
                try:
                    if not path.exists(f'DIARIOGC-{self.nome.text()}'):
                        mkdir(f'DIARIOGC-{self.nome.text()}')
                    with open(f'DIARIOGC-{self.nome.text()}/utilizador.log', 'w+') as salvarDados:
                        salvarDados.write(f"""*** Bem-Vindo ***
Nome: {selfnome.text()}
Senha: {senha.text()}
Resposta: {respostaEspecial.text()}""")
                        QMessageBox.information(self.ferramentas, "Bem-Vindo", "Cadastro Concluido..\nAgora inicie sessao para confirmar os seus dados!")
                        self.tab.removeTab(0)
                        return self.iniciar()
                except Exception as e:
                    QMessageBox.warning(self.ferramentas, "Falha", f"Lamento ocorreu um erro inesperado:\n\t{e}\n\nTente verificar e preencher propriamente os seus dados..")
                    warning(f'{e}')
                    pass

        janela2 = QWidget()
        self.ferramentas.setPalette(QPalette(QColor('blue')))

        layout = QFormLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/01.png"))
        labelImagem.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelImagem)

        self.nome = QLineEdit()
        self.nome.setToolTip('*: OBRIGATORIO!')
        layout.addRow('&Nome: *', self.nome)

        senha = QLineEdit()
        senha.setToolTip('*: OBRIGATORIO!')
        senha.setEchoMode(senha.PasswordEchoOnEdit)
        layout.addRow('&Senha: *', senha)

        confirmarSenha = QLineEdit()
        confirmarSenha.setToolTip('*: OBRIGATORIO!')
        confirmarSenha.setEchoMode(confirmarSenha.PasswordEchoOnEdit)
        layout.addRow('Redigite a &Senha: *', confirmarSenha)

        respostaEspecial = QLineEdit()
        respostaEspecial.setToolTip('*: OBRIGATORIO!\nResposta especial que usaremos para recuperar o seu login..')
        layout.addRow('Qual seu bem mais precioso? *', respostaEspecial)

        botaoCadastrar = QPushButton('Cadastrar')
        botaoCadastrar.clicked.connect(guardar)
        botaoCadastrar.setDefault(True)
        layout.addWidget(botaoCadastrar)

        janela2.setLayout(layout)
        self.tab.addTab(janela2, "Cadastro")
        self.tab.setCurrentWidget(janela2)

    # @staticmethod
    def iniciar(self):
        def confirmar():
            if isEmpty(self.nome.text()) and isEmpty(senha.text()):
                QMessageBox.critical(self.ferramentas, "Falha", "Lamento, mas você precisa preencher devidamente os seus dados antes de iniciar..")
                critical('dados nao preenchidos!')
                pass
            else:
                try:
                    with open(f'DIARIOGC-{self.nome.text()}/utilizador.log', 'r+') as lerDados:
                        confirmarDados = lerDados.read()
                        if (self.nome.text() in confirmarDados) and (senha.text() in confirmarDados):
                            self.tab.removeTab(0)
                            return self.diario()
                        elif (self.nome.text() not in confirmarDados) and (senha.text() not in confirmarDados):
                            pergunta = QMessageBox.question(self.ferramentas, "Atenção", f"Lamento {self.nome.text()} voccê aind não tem uma conta..\nCadastre-se para ter acesso ao programa?")
                            if pergunta == 1638:
                                self.tab.removeTab(0)
                                return self.cadastro()
                            elif pergunta == 65536:
                                return self.gc.instance().exit()
                            else:
                                pass
                        else:
                            pass
                except Exception as e:
                    QMessageBox.warning(self.ferramentas, "Falha", f"Lamento ocorreu um erro inesperado:\n\t{e}\n\nTente verificar e preencher propriamente os seus dados..")
                    warning(f'{e}')
                    pass

        janela3 = QWidget()
        self.ferramentas.setPalette(QPalette(QColor('pink')))

        layout = QFormLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/03.png"))
        labelImagem.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelImagem)

        self.nome = QLineEdit()
        self.fnome.setToolTip('*: OBRIGATORIO!')
        layout.addRow('&Nome: *', self.nome)

        senha = QLineEdit()
        senha.setToolTip('*: OBRIGATORIO!')
        senha.setEchoMode(senha.PasswordEchoOnEdit)
        layout.addRow('&Senha: *', senha)

        labelRecuperarSenha = QLabel('<a href="#" style="text-decoration:none;">Esqueceu a sua senha?</a>')
        labelRecuperarSenha.linkActivated.connect(self.recuperarSenha)
        labelRecuperarSenha.setAlignment(Qt.AlignRight)
        layout.addWidget(labelRecuperarSenha)

        botaoIniciar = QPushButton('Iniciar')
        botaoIniciar.clicked.connect(confirmar)
        botaoIniciar.setDefault(True)
        layout.addWidget(botaoIniciar)

        janela3.setLayout(layout)
        self.tab.addTab(janela3, "Iniciar Sessão")
        self.tab.setCurrentWidget(janela3)

    def recuperarSenha(self):
        def confirmar():
            if isEmpty(self.nome.text()) and isEmpty(respostaEspecial.text()):
                QMessageBox.critical(self.ferramentas, "Falha", "Lamento, mas você precisa preencher devidamente os seus dados antes de iniciar..")
                critical('dados nao preenchidos!')
                pass
            else:
                try:
                    with open(f'DIARIOGC-{self.nome.text()}/utilizador.log', 'r+') as lerDados:
                        confirmarDados = lerDados.read()
                        if (self.nome.text() in confirmarDados) and (respostaEspecial.text() in confirmarDados):
                            self.tab.removeTab(0)
                            return self.diario()
                        elif (self.nome.text() not in confirmarDados) and (senha.text() not in confirmarDados):
                            pergunta = QMessageBox.question(self.ferramentas, "Atenção", f"Lamento {self.nome.text()} voccê aind não tem uma conta..\nCadastre-se para ter acesso ao programa?")
                            if pergunta == 1638:
                                self.tab.removeTab(0)
                                return self.cadastro()
                            elif pergunta == 65536:
                                return self.gc.instance().exit()
                            else:
                                pass
                        else:
                            pass
                except Exception as e:
                    QMessageBox.warning(self.ferramentas, "Falha", f"Lamento ocorreu um erro inesperado:\n\t{e}\n\nTente verificar e preencher propriamente os seus dados..")
                    warning(f'{e}')
                    pass

        janela4 = QWidget()
        janela4.setFixedSize(250, 250)
        janela4.setPalette(QPalette(QColor('Wheat')))

        layout = QFormLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/06.png"))
        labelImagem.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelImagem)

        self.nome = QLineEdit()
        self.nome.setToolTip('*: OBRIGATORIO!')
        layout.addRow('&Nome: *', self.nome)

        respostaEspecial = QLineEdit()
        respostaEspecial.setToolTip('*: OBRIGATORIO!\nResposta especial que usaremos para recuperar o seu login..')
        layout.addRow('Qual seu bem mais precioso? *', respostaEspecial)

        botaoIniciar = QPushButton("Iniciar")
        botaoIniciar.clicked.connect(confirmar)
        botaoIniciar.setDefault(True)
        layout.addWidget(botaoIniciar)

        janela4.setLayout(layout)
        janela4.show()

    def diario(self):
        janela5 = QWidget()
        self.ferramentas.setPalette(QPalette(QColor('antiquewhite')))

        layout = QFormLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap('img/02.png'))
        labelImagem.setAlignment(Qt.AlignCenter)
        labelImagem.setToolTip('Mesmo que nada esteje bem, certifica te que tudo corra bem..\nDEUS TE OFERECEU MAIS UM DIA APROVEITE AO MAXIMO!')
        layout.addRow(labelImagem)

        labelIntro = QLabel('Selecione a Operação a Executar')
        labelIntro.setFont(QFont('cambria', 12))
        labelIntro.setAlignment(Qt.AlignCenter)
        layout.addRow(labelIntro)

        escreverBotao = QPushButton('Escrever')
        escreverBotao.clicked.connect(self.codificar1)
        escreverBotao.setDefault(True)
        layout.addRow(escreverBotao)

        lerBotao = QPushButton('Ler')
        lerBotao.clicked.connect(self.ler)
        lerBotao.setDefault(True)
        layout.addRow(lerBotao)

        editarBotao = QPushButton('Editar')
        editarBotao.clicked.connect(self.editar)
        editarBotao.setDefault(True)
        layout.addRow(editarBotao)

        browser = lambda p: webbrowser.open('https://artesgc.home.blog')
        labeLink = QLabel("<a href='#' style='text-decoration:none;'>ArtesGC, Inc</a>")
        labeLink.setAlignment(Qt.AlignRight)
        labeLink.setToolTip('Acesso a pagina oficial da ArtesGC!')
        labeLink.linkActivated.connect(browser)
        layout.addWidget(labeLink)

        janela5.setLayout(layout)
        self.tab.addTab(janela5, 'Pagina-Inicial')
        self.tab.setCurrentWidget(janela5)

    def escrever(self):
        janela6 = QWidget()

        layout = QVBoxLayout()

        hl = QFormLayout()
        titulo = QLineEdit()
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setToolTip('*: OBRIGATORIO!')
        hl.addRow('Digite um &Nome para o Arquivo: *', titulo)
        layout.addLayout(hl)

        texto = QTextEdit()
        texto.setFont(QFont('cambria', 10))
        texto.setAcceptRichText(True)
        texto.setAcceptDrops(True)
        layout.addWidget(texto)

        def guardar():
            if isEmpty(titulo.text()):
                QMessageBox.warning(self.ferramentas, 'Falha', f'Por favor atribua um nome ao documento antes de guarda-lo!')
                warning('ficheiro não nomeado!')
            else:
                try:
                    if not path.exists(f'DIARIOGC-{self.nome.text()}/pensamentos'):
                        mkdir(f'DIARIOGC-{self.nome.text()}/pensamentos')
                    with open(f'DIARIOGC-{self.nome.text()}/pensamentos/{titulo.text()}.gc-txt', 'w+') as fileCodificado:
                        doc1, doc2 = encrypt(texto.toPlainText())
                        fileCodificado.write(str(doc1) + '\n' + str(doc2))
                        QMessageBox.information(self.ferramentas, 'Concluido', 'Codificação Bem Sucedida..')
                        self.tab.removeTab(1)
                        self.main0()
                except Exception as e:
                    QMessageBox.warning(self.ferramentas, "Falha", f"Lamento, ocorreu um erro inesperado..\n\t{e}")
                    warning(f'{e}')

        hl = QHBoxLayout()
        guardarBotao = QPushButton('Guardar (Codificado)')
        guardarBotao.clicked.connect(guardar)
        guardarBotao.setDefault(True)
        hl.addWidget(guardarBotao)

        cancelar = lambda p: self.tab.removeTab(1)
        cancelarBotao = QPushButton('Cancelar')
        cancelarBotao.clicked.connect(cancelar)
        cancelarBotao.setDefault(True)
        hl.addWidget(cancelarBotao)
        layout.addLayout(hl)

        janela6.setLayout(layout)
        self.tab.addTab(janela6, 'Novo-Arquivo')
        self.tab.setCurrentWidget(janela6)

    def ler(self):
        nome_file_open = QFileDialog.getOpenFileName(parent=self.ferramentas, directory=f'DIARIOGC-{self.nome.text()}/pensamentos', filter='Ficheiros (*.gc-txt)')
        try:
            with open(nome_file_open[0], 'r+') as file_decod:
                file_ = file_decod.readlines()
                file = decrypt(file_[0], file_[1])

            moldura_decod = QWidget()
            layout = QVBoxLayout()

            texto = QTextEdit(self.moldura_decod)
            texto.setReadOnly(True)
            texto.setFont(QFont('cambria', 10))
            texto.insertPlainText(file)
            layout.addWidget(texto)

            fechar = lambda: self.tab.removeTab(1)
            fecharBotao = QPushButton('Fechar')
            fecharBotao.clicked.connect(fechar)
            layout.addWidget(fecharBotao)

            moldura_decod.setLayout(layout)
            self.tab.addTab(moldura_decod, 'Lendo-Arquivo')
            self.tab.setCurrentWidget(moldura_decod)
        except FileNotFoundError:
            QMessageBox.warning(self.ferramentas, 'Aviso', 'Ficheiro Não Encontrado ou Processo Cancelado!')

    def editar(self):
        self.utilizador = (self.utilizador_is.text() or self.utilizador_cd.text())
        nome_file_open = QFileDialog.getOpenFileName(parent=self.ferramentas, directory=f'C9R{self.utilizador}', filter='Ficheiros (*.gc)')
        try:
            with open(nome_file_open[0], 'r+') as file_decod:
                file_ = file_decod.readlines()
                file = decrypt(file_[0], file_[1])

            self.moldura_editar = QFrame()
            self.moldura_editar.setPalette(QPalette(QColor('Wheat')))
            self.tab.addTab(self.moldura_editar, 'Editando Arquivo')
            self.tab.setCurrentWidget(self.moldura_editar)
            layout = QVBoxLayout()

            texto = QTextEdit()
            texto.setFont(QFont('cambria', 10))
            texto.insertPlainText(file)
            layout.addWidget(texto)

            def guardar():
                with open(nome_file_open[0], 'w+') as file_enc:
                    doc1, doc2 = encrypt(texto.toPlainText())
                    file_enc.write(str(doc1) + '\n' + str(doc2))

                QMessageBox.information(self.ferramentas, 'Concluido', 'Codificação Bem Sucedida..')
                self.tab.removeTab(1)
                self.main0()

            guardar_botao = QPushButton('Guardar (Recodificado)')
            guardar_botao.clicked.connect(guardar)
            layout.addWidget(guardar_botao)

            fechar = lambda: self.tab.removeTab(1)
            fechar_botao = QPushButton('Fechar')
            fechar_botao.clicked.connect(fechar)
            layout.addWidget(fechar_botao)
            self.moldura_editar.setLayout(layout)
        except FileNotFoundError:
            QMessageBox.warning(self.ferramentas, 'Aviso', 'Ficheiro Não Encontrado ou Processo Cancelado!')

    def instrucoes(self):
        QMessageBox.information(self.ferramentas, "Instruções", "")

    def sobre(self):
        QMessageBox.information(self.ferramentas, "Sobre", "")


if __name__ == '__main__':
    app = DiarioGC()
    app.ferramentas.show()
    app.gc.exec_()
