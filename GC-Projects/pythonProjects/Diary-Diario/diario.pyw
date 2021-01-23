#  Copyright (c) 2019-2020 Nurul GC
#  Direitos Autorais (c) 2019-2020 Nurul GC
#
#  Jovem Programador
#  Estudante de Engenharia de Telecomunicaçoes
#  Tecnologia de Informação e de Medicina.
#  Foco Fé Força Paciência
#  Allah no Comando.

import os
from pickle import *
import tkinter.ttk as ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledlist import ScrolledList
from tkinter.scrolledtext import *
from tk_tools.tooltips import ToolTip


def encrypt(p: str):
    encriptar = p.encode()
    encriptado = int.from_bytes(encriptar, 'little')
    return encriptado


def decrypt(p):
    try:
        palavra_encriptada = int(p)
        desencriptada = palavra_encriptada.to_bytes((palavra_encriptada.bit_length() + 7) // 8, 'little')
        return desencriptada.decode()
    except TypeError:
        palavra_encriptada = p
        desencriptada = palavra_encriptada.decode()
        return desencriptada


class Bloco:
    def __init__(self):
        self.janelant = None
        self.mostra = None
        self.janela = None
        self.gc = Tk()
        self.gc.title('  🙋')
        # self.gc.iconbitmap(default='img/diario_gc.ico')
        self.gc.resizable(0, 0)
        self.gc.minsize(350, 350)
        
        #
        self.foto = PhotoImage(file='img/1245.png')
        self.foto2 = PhotoImage(file='img/1232.png')
        self.foto3 = PhotoImage(file='img/1231.png')
        self.foto4 = PhotoImage(file='img/1287.png')
        self.foto5 = PhotoImage(file='img/Artes_GC_IV.png')
        self.foto6 = PhotoImage(file='img/calendar.png')
        
        #
        self.titulo_nota = StringVar()
        self.nome_cadastro = StringVar()
        self.nome_inicio = StringVar()
        self.codigo_inicio = StringVar()
        self.codigo_cadastro = StringVar()
        self.codigo_cadastro_ = StringVar()
        
        #
        self.menu = Menu(self.gc, tearoff=0, bg='black', fg='white')
        self.tab = ttk.Notebook(self.gc)
        self.tab.pack(expand=1, fill='both')
        self.launch()
    
    # português
    def bloco_pt(self):
        def hello():
            showinfo('Sobre', '''Nome: Meu Diário (GC)
Versão: 0.8-052020
Designer e Programador: Nurul GC
Empresa: ArtesGC, Inc. - https://nurulgc.home.blog''')
        
        # notas
        def ver_():
            if self.janela is None:
                return ver()
            try:
                self.janela.destroy()
                return ver()
            except TclError:
                return ver()
        
        def ver():
            try:
                if os.path.isdir(f'B4N4-{self.nome_inicio.get()}\\notas') is True:
                    self.f_pen = askopenfilename(initialdir=f'B4N4-{self.nome_inicio.get()}\\notas')
                    if self.f_pen.endswith('txt'):
                        with open(self.f_pen, 'r+') as f_pen:
                            file = f_pen.readlines()
                        self.janela = LabelFrame(self.tab, takefocus=1)
                        self.tab.add(self.janela, text='Leitura de Nota', underline=0)
                        self.tab.select(self.janela)
                        self.janela.configure(padx=5, pady=5, bg='#53f4c0')
                        
                        lista = ScrolledList(self.janela, font='cambria', takefocus=1)
                        lista.pack(expand=1, fill='both')
                        Button(self.janela, text='Fechar', bg='red', command=self.janela.destroy).pack(side='right')
                        Button(self.janela, text='Atualizar', bg='cyan', command=ver_).pack(side='right')
                        
                        for linha in file:
                            lista.insert(END, linha)
                    elif self.f_pen.endswith('gc'):
                        with open(self.f_pen, 'r+') as f_pen:
                            file = decrypt(f_pen.read())
                        self.janela = LabelFrame(self.tab, takefocus=1)
                        self.tab.add(self.janela, text='Leitura de Nota', underline=0)
                        self.tab.select(self.janela)
                        self.janela.configure(padx=5, pady=5, bg='#53f4c0')
                        
                        lista = Label(self.janela, font='cambria', bg='White')
                        lista.pack(expand=1, fill='both')
                        Button(self.janela, text='Fechar', bg='red', command=self.janela.destroy).pack(side='right')
                        Button(self.janela, text='Atualizar', bg='cyan', command=ver_).pack(side='right')
                        lista.config(text=file)
                    else:
                        pass
                else:
                    showwarning('Aviso!', 'Ficheiro Não Encontrado..\nPossivelmente Ainda Não Tenha Criado uma Nota!')
            except Exception as e:
                self.janela.destroy()
                showwarning('Aviso!', 'Ficheiro Não Encontrado ou Processo Cancelado..')
        
        def mostrar_():
            if self.mostra is None:
                return mostrar()
            try:
                self.mostra.destroy()
                return mostrar()
            except TclError:
                return mostrar()
        
        def mostrar():
            try:
                if os.path.isdir(f'B4N4-{self.nome_inicio.get()}\\notas') is True:
                    self.file = askopenfilename(initialdir=f'B4N4-{self.nome_inicio.get()}\\notas')
                    
                    if self.file.endswith('txt'):
                        self.mostra = LabelFrame(self.tab, takefocus=1)
                        self.tab.add(self.mostra, text=f'Editar Nota', underline=0)
                        self.tab.select(self.mostra)
                        self.mostra.config(padx=10, pady=10, bg='#53f4c0')
                        
                        #
                        def guardar(n):
                            if var.get() == opcao2:
                                try:
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(f"{nota_.get(INSERT, END)}")
                                except FileNotFoundError:
                                    os.makedirs(self.file)
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(f"{nota_.get(INSERT, END)}")
                            elif var.get() == opcao1:
                                try:
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(str(encrypt(f"{nota_.get(INSERT, END)}")))
                                except FileNotFoundError:
                                    os.makedirs(self.file)
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(str(encrypt(f"{nota_.get(INSERT, END)}")))
                            
                            self.mostra.destroy()
                            showinfo('Confirmação', 'Pensamento Guardado..')
                        
                        Label(self.mostra, image=self.foto3, bg='#53f4c0', justify='center').pack()
                        Label(self.mostra, text='OS SEUS PENSAMENTOS', font='times 10 bold', bg='#53f4c0', justify='center').pack()
                        
                        nota_ = ScrolledText(self.mostra, tabs=4, wrap='word', takefocus=1, width=30, height=10)
                        nota_.pack(expand=1, fill='both')
                        ToolTip(nota_, 'Certifique-se de Manter Sempre\nO Cursor no Início da Página Antes de Guardar!')
                        
                        with open(self.file, 'r+') as file_:
                            f = file_.read()
                            nota_.insert(INSERT, f)
                        
                        Button(self.mostra, text='Fechar', command=self.mostra.destroy, bg='red').pack(side='right')
                        default = 'Guardar'
                        opcao1 = 'Guardar(CODIFICADO)'
                        opcao2 = 'Guardar(TEXTO)'
                        var = StringVar()
                        ttk.OptionMenu(self.mostra, var, default, opcao1, opcao2, command=guardar, direction='flush').pack(side='right')
                    elif self.file.endswith('gc'):
                        self.mostra = LabelFrame(self.tab, takefocus=1)
                        self.tab.add(self.mostra, text=f'Editar Nota', underline=0)
                        self.tab.select(self.mostra)
                        self.mostra.config(padx=10, pady=10, bg='#53f4c0')
    
                        #
                        def guardar(n):
                            if var.get() == opcao2:
                                try:
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(f"{nota_.get(INSERT, END)}")
                                except FileNotFoundError:
                                    os.makedirs(self.file)
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(f"{nota_.get(INSERT, END)}")
                            elif var.get() == opcao1:
                                try:
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(str(encrypt(f"{nota_.get(INSERT, END)}")))
                                except FileNotFoundError:
                                    os.makedirs(self.file)
                                    with open(self.file, 'w+') as FILE:
                                        FILE.write(str(encrypt(f"{nota_.get(INSERT, END)}")))
        
                            self.mostra.destroy()
                            showinfo('Confirmação', 'Pensamento Guardado..')
    
                        Label(self.mostra, image=self.foto3, bg='#53f4c0', justify='center').pack()
                        Label(self.mostra, text='OS SEUS PENSAMENTOS', font='times 10 bold', bg='#53f4c0', justify='center').pack()
    
                        nota_ = ScrolledText(self.mostra, tabs=4, wrap='word', takefocus=1, width=30, height=10)
                        nota_.pack(expand=1, fill='both')
                        ToolTip(nota_, 'Certifique-se de Manter Sempre\nO Cursor no Início da Página Antes de Guardar!')
    
                        with open(self.file, 'r+') as file_:
                            f = decrypt(file_.read())
                            nota_.insert(INSERT, f)
    
                        Button(self.mostra, text='Fechar', command=self.mostra.destroy, bg='red').pack(side='right')
                        default = 'Guardar'
                        opcao1 = 'Guardar(CODIFICADO)'
                        opcao2 = 'Guardar(TEXTO)'
                        var = StringVar()
                        ttk.OptionMenu(self.mostra, var, default, opcao1, opcao2, command=guardar, direction='flush').pack(side='right')
                    else:
                        pass
                else:
                    showwarning('Aviso!', 'Ficheiro Não Encontrado..\nPossivelmente Ainda Não Tenha Criado uma Nota!')
            except Exception as e:
                self.mostra.destroy()
                showwarning('Aviso!', 'Ficheiro Não Encontrado ou Processo Cancelado..')
        
        def nota1_():
            if self.janelant is None:
                return nota1()
            try:
                self.janelant.destroy()
                return nota1()
            except TclError:
                return nota1()
        
        def nota1():
            self.janelant = LabelFrame(self.tab, takefocus=1)
            self.tab.add(self.janelant, text='Nova Nota', underline=0)
            self.tab.select(self.janelant)
            self.janelant.config(padx=10, pady=10, bg='#53f4c0')
            
            Label(self.janelant, image=self.foto, bg='#53f4c0').pack()
            Label(self.janelant, text="Digite um Título Para Seu Pensamento", font='Consolas 10', bg='#53f4c0').pack()
            Entry(self.janelant, textvar=self.titulo_nota, justify='center', bd=2).pack()
            
            Label(self.janelant, text='Digite o seu Pensamento', font='Consolas 10', bg='#53f4c0').pack()
            nota = ScrolledText(self.janelant, width=30, height=10, wrap='word')
            nota.pack(expand=1, fill='both')
            ToolTip(nota, 'Certifique-se de Manter Sempre\nO Cursor no Início da Página antes de Guardar!')
            
            def registrado(n):
                if var.get() == opcao2:
                    try:
                        with open(f"B4N4-{self.nome_inicio.get()}/notas/{self.titulo_nota.get()}.txt", 'w+') as fa:
                            fa.write(f"""• {self.titulo_nota.get()}:
{nota.get(INSERT, END)}""")
                    except FileNotFoundError:
                        os.makedirs(f'B4N4-{self.nome_inicio.get()}/notas')
                        with open(f"B4N4-{self.nome_inicio.get()}/notas/{self.titulo_nota.get()}.txt", 'w+') as fa:
                            fa.write(f"""• {self.titulo_nota.get()}:
{nota.get(INSERT, END)}""")
                elif var.get() == opcao1:
                    try:
                        with open(f"B4N4-{self.nome_inicio.get()}/notas/{self.titulo_nota.get()}.gc", 'w+') as fa:
                            fa.write(str(encrypt(f"""• {self.titulo_nota.get()}:
{nota.get(INSERT, END)}""")))
                    except FileNotFoundError:
                        os.makedirs(f'B4N4-{self.nome_inicio.get()}/notas')
                        with open(f"B4N4-{self.nome_inicio.get()}/notas/{self.titulo_nota.get()}.gc", 'w+') as fa:
                            fa.write(str(encrypt(f"""• {self.titulo_nota.get()}:
{nota.get(INSERT, END)}""")))
                else:
                    pass
                
                showinfo('Confirmação', 'Pensamento Guardado!')
                self.janelant.destroy()
            
            Button(self.janelant, text='Fechar', bg='red', command=self.janelant.destroy).pack(side='right')
            default = 'Guardar'
            opcao1 = 'Guardar(CODIFICADO)'
            opcao2 = 'Guardar(TEXTO)'
            var = StringVar()
            ttk.OptionMenu(self.janelant, var, default, opcao1, opcao2, command=registrado, direction='flush').pack(side='right')
        
        def bloco_notas():
            #
            self.anote = LabelFrame(self.tab, takefocus=1)
            self.tab.add(self.anote, text='Primeira Página', underline=0)
            self.tab.select(self.anote)
            self.anote.configure(pady=10, padx=10, bg='#53f4c0')
            self.gc.configure(menu=detalhes)
            #
            Label(self.anote, text='''"SEJA SEMPRE VOCÊ MESMO"
"NÃO TE IMPORTES COM O QUE AS PESSOAS DIZEM OU PENSAM"
"DEUS FÊZ-TE SEMELHANTE A ELE POR UMA RAZÃO!"
GC''', font='Cambria 10 italic', justify='center', bg='#53f4c0', fg='black').pack(expand=1, fill='both')
            b = Button(self.anote, image=self.foto2, relief='ridge', bg='white', command=nota1_)
            b.pack(expand=1, fill='both')
        
        # inicio de sessão
        def janela_inicio_sessao():
            root.destroy()
            janela_var = LabelFrame(self.tab, takefocus=1)
            self.tab.add(janela_var, text='Início Sessão')
            self.tab.select(janela_var)
            janela_var.configure(pady=10, padx=10, bg='#53f4c0')
            
            Label(janela_var, text='Olá Bem-Vindo de Volta!\n', font='Arial 11 bold', fg='green', bg='#53f4c0').grid(row=0, columnspan=2)
            
            def iniciar(m):
                janela_var.destroy()
                
                try:
                    with open(f"B4N4-{self.nome_inicio.get()}/Utilizador.log", 'r+b') as fr:
                        file_ = load(fr)
                        if self.nome_inicio.get() in file_ and self.codigo_inicio.get() in file_:
                            return bloco_notas()
                        else:
                            return inicio_acesso_negado()
                except FileNotFoundError:
                    return inicio_acesso_negado()
            
            Label(janela_var, text='Nome', font='Arial 10', underline=0, bg='#53f4c0').grid(row=1, column=0)
            Entry(janela_var, textvar=self.nome_inicio, takefocus=1, bd=2).grid(row=1, column=1)
            
            Label(janela_var, text='Senha', font='Arial 10', underline=0, bg='#53f4c0').grid(row=3, column=0)
            e = Entry(janela_var, textvar=self.codigo_inicio, show='*', bd=2, takefocus=1)
            e.grid(row=3, column=1)
            e.bind("<Return>", iniciar)
            
            b = Button(janela_var, text='Iniciar', bg='green', fg='white')
            b.grid(row=4, column=1, sticky=E)
            b.bind("<Button-1>", iniciar)
        
        def inicio_acesso_negado():
            erro = askyesno('Erro ao Iniciar Sessão!', f'''Lamento {self.nome_inicio.get()}
Você Ainda Não Tem Sessão Iniciada..
Inicie Uma para Ter Acesso!?''')
            
            if erro is True:
                return cadastro()
            elif erro is False:
                self.gc.destroy()
        
        # Cadastro
        def codigo_errado():
            showerror('Erro ao Iniciar Sessão', f'Lamento {self.nome_cadastro.get()} os códigos não correspondem!')
        
        def cadastro():
            root.destroy()
            janela_cadastro = LabelFrame(self.tab, takefocus=1)
            self.tab.add(janela_cadastro, text='Novo Utilizador')
            self.tab.select(janela_cadastro)
            janela_cadastro.configure(pady=15, padx=15, bg='#53f4c0')
            
            #
            Label(janela_cadastro, text='Cadastre-se Para Ter Acesso!\n', fg='blue', font='Arial 11 bold', bg='#53f4c0').grid(row=0, columnspan=2)
            
            #
            Label(janela_cadastro, text='Nome', font='Arial 10', bg='#53f4c0', underline=0).grid(row=1, column=0)
            Entry(janela_cadastro, textvar=self.nome_cadastro, takefocus=1, bd=2).grid(row=1, column=1)
            
            Label(janela_cadastro, text='Senha', font='Arial 10', bg='#53f4c0', underline=0).grid(row=2, column=0)
            e2_ = Entry(janela_cadastro, textvar=self.codigo_cadastro_, show='*', takefocus=1, bd=2)
            e2_.grid(row=2, column=1)
            
            #
            def registrar(n):
                try:
                    if self.codigo_cadastro_.get() == self.codigo_cadastro.get():
                        with open(f"B4N4-{self.nome_cadastro.get()}/Utilizador.log", 'w+b') as fw:
                            dump(f'''BEM-VINDO..
Nome: {self.nome_cadastro.get()}
Senha: {self.codigo_cadastro.get()}''', fw)
                        janela_cadastro.destroy()
                        janela_inicio_sessao()
                    else:
                        return codigo_errado()
                except FileNotFoundError:
                    os.makedirs(f'B4N4-{self.nome_cadastro.get()}')
                    if self.codigo_cadastro_.get() == self.codigo_cadastro.get():
                        with open(f"B4N4-{self.nome_cadastro.get()}/Utilizador.log", 'w+b') as fw:
                            dump(f'''BEM-VINDO..
Nome: {self.nome_cadastro.get()}
Senha: {self.codigo_cadastro.get()}''', fw)
                        janela_cadastro.destroy()
                        janela_inicio_sessao()
                    else:
                        return codigo_errado()
            
            #
            Label(janela_cadastro, text='Reintroduza a Senha', font='Arial 10', bg='#53f4c0').grid(row=3, column=0)
            e2 = Entry(janela_cadastro, textvar=self.codigo_cadastro, show='*', takefocus=1, bd=2)
            e2.grid(row=3, column=1)
            e2.bind("<Return>", registrar)
            
            registro = Button(janela_cadastro, text='Registrar', bg='green', fg='white')
            registro.grid(row=4, column=1, sticky=E)
            registro.bind("<Button-1>", registrar)
        
        self.gc.title('Meu Diário')
        self.tab1.destroy()
        root = LabelFrame(self.tab)
        self.tab.add(root, text='Bem-Vindo', underline=0)
        self.tab.select(root)
        root.configure(bg='#53f4c0', padx=20, pady=10)
        
        #
        menu_pt = Menu(self.menu, tearoff=0, bg='#53f4c0', font='tahoma 8')
        menu_pt.add_command(label='Editar', command=mostrar_, underline=0)
        menu_pt.add_command(label='Escrever', command=nota1_, underline=0)
        menu_pt.add_command(label='Ler', command=ver_, underline=0)
        detalhes = Menu(self.menu)
        notas = Menu(detalhes, tearoff=0, bg='#53f4c0', font='tahoma 8')
        notas.add_cascade(label='Diário', menu=menu_pt, underline=0)
        notas.add_separator()
        notas.add_command(label='Sair', command=self.gc.destroy, underline=0)
        detalhes.add_cascade(label='Opções', menu=notas, underline=0)
        detalhes.add_command(label='Sobre', command=hello, underline=0)
        
        #
        Label(root, text='''Bem Vindo ao Seu Diário
O Mundo dos Seus Pensamentos''', font='Consolas 10 bold', justify='center', bg='#53f4c0').grid(row=0, column=0)
        l = Label(root, image=self.foto4, bg='#53f4c0')
        l.grid(row=1, column=0, pady=10)
        
        #
        f_ = LabelFrame(root, text=' Escolha Uma Para Começar ', bg='#53f4c0', font='consolas 8 bold')
        f_.grid(row=2, column=0)
        Button(f_, text='Criar Conta', bg='green', fg='white', command=cadastro).grid(row=0, column=0, padx=10)
        Button(f_, text='Iniciar Sessão', bg='cyan', command=janela_inicio_sessao).grid(row=0, column=1, padx=10)
    
    # intro
    def launch(self):
        self.tab1 = LabelFrame(self.tab)
        self.tab.add(self.tab1, text='Bem-Vindo')
        self.tab.select(self.tab1)
        self.tab1.configure(bg='white', pady=5, padx=55)
        
        #
        Label(self.tab1, text='📓 MEU DIÁRIO 📓', font='constantia 12', bg='white', fg='magenta').grid(row=0, columnspan=1)
        Label(self.tab1, image=self.foto5, bg='white').grid(row=1, column=0, pady=10)
        
        f = LabelFrame(self.tab1, bg='white')
        f.grid(row=2, column=0)
        Radiobutton(f, text='ENTRAR ', command=self.bloco_pt, fg='magenta', font='Cambria 7 bold', indicatoron=0).grid(row=0, column=0, padx=5, pady=5)


if __name__ == '__main__':
    app = Bloco()
    app.gc.mainloop()
