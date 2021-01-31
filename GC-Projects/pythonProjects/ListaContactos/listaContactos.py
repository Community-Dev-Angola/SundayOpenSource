#  Copyright (c) 2019-2020 Nurul GC
#  Direitos Autorais (c) 2019-2020 Nurul GC
#
#  Jovem Programador
#  Estudante de Engenharia de Telecomunicaçoes
#  Tecnologia de Informação e de Medicina.
#  Foco Fé Força Paciência
#  Allah no Comando.

from tkinter import *
import tkinter.ttk as ttk
from tk_tools import ToolTip
from os import makedirs, path
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledlist import ScrolledList
from tkinter.scrolledtext import ScrolledText


class L4T8:
    
    def __init__(self):
        self.gc = Tk()
        self.gc.title('Contactos GC')
        # descomente a proxima linha se for executar num windows
        # self.gc.wm_iconbitmap("img/artesgc.ico")
        self.gc.resizable(0, 0)
        
        self.nome = StringVar(self.gc)
        self.numero = StringVar(self.gc)
        self.morada1 = StringVar(self.gc)
        self.morada2 = StringVar(self.gc)
        self.email = StringVar(self.gc)
        
        self.tab = ttk.Notebook(self.gc)
        self.tab.pack(expand=1, fill='both')
        self.janela = None
        self.janela_ed = None
        self.principal()
    
    def hello(self):
        showinfo('Sobre', '''Nome: ListaContactos GC
Versão: 0.6-012021
Designer e Programador: Nurul GC
Empresa: ArtesGC Inc.''')
    
    def editar_(self):
        if self.janela_ed is None:
            return self.editar()
        try:
            self.janela_ed.destroy()
            return self.editar()
        except TclError:
            return self.editar()
    
    def editar(self):
        try:
            if os.path.exists('GContactos'):
                contacto = askopenfilename(initialdir='GContactos')
                with open(contacto, 'r+') as f:
                    fc = f.read()
                
                self.janela_ed = LabelFrame(self.tab)
                self.tab.add(self.janela_ed, text='Editar')
                self.tab.select(self.janela_ed)
                self.janela_ed.configure(bg='AntiqueWhite1', padx=5, pady=5)
                
                lista = ScrolledText(self.janela_ed, font='Cambria 12', width=20, height=10, wrap=WORD)
                lista.pack(expand=1, fill='both')
                lista.insert(INSERT, fc)
                ToolTip(lista, 'Certifique-se de manter o Cursor no início da Página\nSempre Antes de Guardar!', 5000)
                
                def guardar():
                    with open(contacto, 'w+') as c:
                        c.write(lista.get(INSERT, END))
                    showinfo('Confirmação', 'Contacto Guardado\n 👌 👍')
                    self.janela_ed.destroy()
                
                Button(self.janela_ed, text='Fechar', bg='red', command=self.janela_ed.destroy).pack(side='right')
                Button(self.janela_ed, text='Guardar', bg='cyan', command=guardar).pack(side='right')
            else:
                showwarning('Aviso!', 'Ainda Não Tem Uma Lista de Contactos Criada..')
        except FileNotFoundError:
            showwarning('Aviso!', 'Processo de Leitura Cancelado..')
    
    def guardar_(self):
        self.moldura1.destroy()
        self.principal()
        self.nome.set('')
        self.numero.set('')
        self.morada1.set('')
        self.morada2.set('')
        self.email.set('')
    
    def guardar(self, n):
        if self.nome.get() == '' and self.numero.get() == '':
            showwarning('Aviso!', 'Contacto Não Guardado\n- Nome e Número Não Preenchidos..')
        else:
            if not path.exists('GContactos'):
                makedirs('GContactos')
            with open(f"GContactos/{self.nome.get()}.gcontact", 'w+') as file:
                if self.morada1.get() == '' and self.morada2.get() == '' and self.email.get() == '':
                    file.write(f'''Nome: {self.nome.get()}
Numero: {self.numero.get()}''')
                else:
                    file.write(f'''Nome: {self.nome.get()}
Numero: {self.numero.get()}
Morada: {self.morada1.get()}, {self.morada2.get()}
Email: {self.email.get()}''')
            self.guardar_()
            showinfo('Confirmação', 'Contacto Guardado\n 👌 👍')
    
    def mostrar(self):
        try:
            if os.path.exists('GContactos'):
                contacto = askopenfilename(initialdir='GContactos')
                with open(contacto, 'r+') as f:
                    fc = f.readlines()
                
                self.janela = LabelFrame(self.tab)
                self.tab.add(self.janela, text='Mostrar')
                self.tab.select(self.janela)
                self.janela.configure(bg='AntiqueWhite1', padx=5, pady=5)
                
                lista = ScrolledList(self.janela, font='Cambria 12', width=20, height=10)
                lista.pack(expand=1, fill='both')
                
                for lines in fc:
                    lista.insert(END, lines)
                
                Button(self.janela, text='Fechar', bg='red', command=self.janela.destroy).pack(side='right')
                Button(self.janela, text='Atualizar', bg='cyan', command=self.mostrar_).pack(side='right')
            else:
                showwarning('Aviso!', 'Ainda Não Tem Uma Lista de Contactos Criada..')
        except FileNotFoundError:
            showwarning('Aviso!', 'Processo de Leitura Cancelado..')
    
    def mostrar_(self):
        if self.janela is None:
            return self.mostrar()
        try:
            self.janela.destroy()
            return self.mostrar()
        except TclError:
            return self.mostrar()
    
    def principal(self):
        self.moldura1 = LabelFrame(self.tab, relief='groove')
        self.tab.add(self.moldura1, text='Novo Contacto')
        self.tab.select(self.moldura1)
        self.moldura1.configure(bg='AntiqueWhite1', padx=20, pady=10)
        
        self.menu = Menu(self.gc, tearoff=0, font='tahoma 8', bg='AntiqueWhite2')
        self.menu.add_command(label='Mostrar Contactos', command=self.mostrar_, underline=0)
        self.menu.add_command(label='Editar Contactos', command=self.editar_, underline=0)
        self.menu.add_separator()
        self.menu.add_command(label='Sair', command=self.gc.destroy, underline=0)
        detalhes = Menu(self.menu)
        detalhes.add_cascade(label='Opções', menu=self.menu, underline=0)
        detalhes.add_command(label='Sobre', command=self.hello, underline=0)
        self.gc.configure(menu=detalhes)
        
        Label(self.moldura1, text="'Nunca Confundas Talento Com Sorte!'\n- GC", font='cambria 12 italic', bg='AntiqueWhite1').pack(fill=BOTH, expand=1)
        moldura = Frame(self.moldura1, bg='AntiqueWhite1')
        moldura.pack()
        
        Label(moldura, bg='AntiqueWhite1', text='Nome: *', font='cambria 10', underline=0).grid(row=1, sticky=NSEW)
        nome = ttk.Entry(moldura, textvar=self.nome)
        nome.grid(row=1, column=1, sticky=NSEW)
        ToolTip(nome, 'Obrigatório!')
        
        Label(moldura, bg='AntiqueWhite1', text='Telefone: *', font='cambria 10', underline=0).grid(row=2, sticky=NSEW)
        numero = ttk.Entry(moldura, textvar=self.numero)
        numero.grid(row=2, column=1, pady=5, sticky=NSEW)
        ToolTip(numero, 'Obrigatório!')
        
        Label(moldura, bg='AntiqueWhite1', text='Morada:', font='cambria 10', underline=0).grid(column=0, rowspan=2, sticky=NSEW)
        morada1 = ttk.Entry(moldura, textvar=self.morada1)
        morada1.grid(row=3, column=1, sticky=NSEW)
        ToolTip(morada1, 'Opcional!')
        morada2 = ttk.Entry(moldura, textvar=self.morada2)
        morada2.grid(row=4, column=1, sticky=NSEW)
        ToolTip(morada2, 'Opcional!')
        
        Label(moldura, bg='AntiqueWhite1', text='Email:', font='cambria 10', underline=0).grid(row=5, sticky=NSEW)
        e = ttk.Entry(moldura, textvar=self.email)
        e.grid(row=5, column=1, pady=5, sticky=NSEW)
        e.bind("<Return>", self.guardar)
        ToolTip(e, 'Opcional!')
        
        b = Button(moldura, bg='cyan', text='Guardar')
        b.grid(row=6, column=1, sticky=E)
        b.bind("<Button-1>", self.guardar)


if __name__ == '__main__':
    app = L4T8()
    app.gc.mainloop()
