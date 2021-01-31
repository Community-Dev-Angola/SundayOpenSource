#  Copyright (c) 2019-2020 Nurul GC
#  Direitos Autorais (c) 2019-2020 Nurul GC
#
#  Jovem Programador
#  Estudante de Engenharia de Telecomunicaçoes
#  Tecnologia de Informação e de Medicina.
#  Foco Fé Força Paciência
#  Allah no Comando.

from math import *
from tkinter import *
from time import sleep
from tkinter.messagebox import *
from tkinter.scrolledlist import ScrolledList
from tkinter.ttk import Notebook, Progressbar


class C8GC:
    """
Nome: GCalculadora GC
Projectado por: https://@nurulgc.home.blog - Nurul GC
inicio do projecto - 11:00h 20-03-2020
edição - 04:37h 04-04-2020
versão: 0.1-032020 - 0.2-042020 - 0.3-052020
"""

    def __init__(self):
        self.gc = Tk()
        self.gc.title('GCalculadora GC')
        self.gc.resizable(0, 0)
        # descomente a proxima linha se for urodar o script num Windows
        # self.gc.iconbitmap('', 'img/artesgc.ico')

        self.valor1 = DoubleVar(self.gc)
        self.valor2 = DoubleVar(self.gc)
        self.resultado = DoubleVar(self.gc)
        self.tab = Notebook(self.gc)
        self.tab.pack(expand=1, fill='both')
        self.janela = None

        self.soma = lambda: self.resultado.set(self.valor1.get() + self.valor2.get())
        self.subtracao = lambda: self.resultado.set(self.valor1.get() - self.valor2.get())
        self.multiplicacao = lambda: self.resultado.set(self.valor1.get() * self.valor2.get())
        self.expoente = lambda: self.resultado.set(pow(self.valor1.get(), self.valor2.get()))
        self.expoente_v1 = lambda: self.resultado.set(pow(self.valor1.get(), self.valor1.get()))
        self.expoente_v2 = lambda: self.resultado.set(pow(self.valor2.get(), self.valor2.get()))
        self.expoente_neg_v1 = lambda: self.resultado.set(expm1(self.valor1.get()))
        self.expoente_neg_v2 = lambda: self.resultado.set(expm1(self.valor2.get()))
        self.raiz_quad_v1 = lambda: self.resultado.set(sqrt(self.valor1.get()))
        self.raiz_quad_v2 = lambda: self.resultado.set(sqrt(self.valor2.get()))
        self.modulo = lambda: self.resultado.set(fmod(self.valor1.get(), self.valor2.get()))
        self.modulo_v1 = lambda: self.resultado.set(modf(self.valor1.get()))
        self.modulo_v2 = lambda: self.resultado.set(modf(self.valor2.get()))
        self.logo1 = lambda: self.resultado.set(log(abs(self.valor1.get()), abs(self.valor2.get())))
        self.logo1_ = lambda: self.resultado.set(log(abs(self.valor2.get()), abs(self.valor1.get())))
        self.logo2 = lambda: self.resultado.set(log10(self.valor1.get()))
        self.logo2_ = lambda: self.resultado.set(log10(self.valor2.get()))
        self.logo3 = lambda: self.resultado.set(log2(abs(self.valor1.get())))
        self.logo3_ = lambda: self.resultado.set(log2(abs(self.valor2.get())))
        self.sen_v1 = lambda: self.resultado.set(sin(self.valor1.get()))
        self.sen_v2 = lambda: self.resultado.set(sin(self.valor2.get()))
        self.cosen_v1 = lambda: self.resultado.set(cos(self.valor1.get()))
        self.cosen_v2 = lambda: self.resultado.set(cos(self.valor2.get()))
        self.tang_v1 = lambda: self.resultado.set(tan(self.valor1.get()))
        self.tang_v2 = lambda: self.resultado.set(tan(self.valor2.get()))
        self.fat_v1 = lambda: self.resultado.set(factorial(self.valor1.get()))
        self.fat_v2 = lambda: self.resultado.set(factorial(self.valor2.get()))

        self.main()

    def decimal(self):
        if self.valor1.get() == 0:
            showerror('Erro!', 'Divisão por Zero Sem Solução..')
        else:
            self.resultado.set(1 / self.valor1.get())

    def decimal_(self):
        if self.valor2.get() == 0:
            showerror('Erro!', 'Divisão por Zero Sem Solução..')
        else:
            self.resultado.set(1 / self.valor2.get())

    def divisao_inteira(self):
        if self.valor2.get() == 0:
            showerror('Erro!', 'Divisão por Zero Sem Solução..')
        else:
            self.resultado.set(self.valor1.get() // self.valor2.get())

    def divisao(self):
        if self.valor2.get() == 0:
            showerror('Erro!', 'Divisão por Zero Sem Solução..')
        else:
            self.resultado.set(self.valor1.get() / self.valor2.get())

    #
    @staticmethod
    def hello():
        showinfo('Sobre', '''Nome: GCalculadora GC
Versão: 0.4-052020
Designer e Programador: Nurul GC
Empresa: ArtesGC, Inc. - https://nurulgc.home.blog''')

    def instr(self):
        adicao = '<v1+v2> - Adição, retorna o resultado da operação (n1 + n2)'
        subtracao = '<v1-v2> - Subtração, retorna o resultado da operação (n1 - n2)'
        multiplicacao = '<v1*v2> - Multiplicação, retorna o resultado da operação (n1 x n2)'
        divisao_inteira = '<v1//v2> - Divisão Inteira, retorna apenas o resultado da parte inteira da operação (n1 / n2)'
        divisao_natural = '<v1/v2> - Divisão Natural, retorna o resultado da operação (n1 / n2)'
        exponenciacao = '<v1exp(v2)>, <v2exp(v1)> - Expoente, retorna o resultado de n1 elevado a n2, ex:(n1^n2) ou (n1**n2)'
        exponenciacao_neg = '<v1exp(-1)>, <v2exp(-1)> - Expoente Negativo, retorna o resultado de (n) elevado (-1)'
        potencia = '<exp(v1)>, <exp(v2)> - Potenciação, retorna o resultado de expoente (n) na base (n)'
        raiz_quad = '<Rq(v1)>, <Rq(v2)> - Raiz Quadrada, retorna o resultado da raiz de (n)'
        modulo = '<Md(v1,v2)> - Modulo, retorna o valor modular de n1 por n2, ex:|n1,n2| ou (n1 % n2)'
        modulo_sing = '<Md(v1)>, <Md(v2)> - Modulo Singular,retorna a parte fraccional e inteira de (n)'
        logoritmo_i = '<logv1(v2)>, <logv2(v1)> - Logoritmo I, retorna o resultado do logoritmo de (n1) na base (n2) ou vise-versa'
        logoritmo_ii = '<log10(v1)>, <log10(v2)> - Logoritmo II, retorna o resultado do logoritmo de 10 na base (n)'
        logoritmo_iii = '<log2(v1)>, <log2(v2)> - Logoritmo III, retorna o resultado do logoritmo de 2 na base (n)'
        decimal = '<1/v1>, <1/v2> - Decimal, retorna o resultado da operação (1/n)'
        seno = '<sen(v1)>, <sen(v2)> - Seno, retorna o resultado de sen(n) em radianos'
        coseno = '<cos(v1)>, <cos(v2)> - Coseno, retorna o resultado de cosen(n) em radianos'
        tangente = '<tan(v1)>, <tan(v2)> - Tangente, retorna o resultado de tan(n) em radianos'
        factorial_ = '<fact(v1)>, <fact(v2)> - Factorial, retorna o resultado factorial de (n)'

        #
        self.janela = LabelFrame(self.tab)
        self.tab.add(self.janela, text='Instruções')
        self.tab.select(self.janela)
        self.janela.configure(padx=5, pady=5, bg='white')

        #
        lv = [f'{adicao}', f'{subtracao}', f'{divisao_natural}', f'{multiplicacao}',
              f'{divisao_inteira}', f'{potencia}',
              f'{factorial_}', f'{exponenciacao}',
              f'{exponenciacao_neg}', f'{raiz_quad}', f'{modulo}',
              f'{modulo_sing}', f'{logoritmo_i}', f'{logoritmo_iii}',
              f'{logoritmo_ii}', f'{decimal}',
              f'{seno}\n', f'{coseno}', f'{tangente}']

        lst = ScrolledList(self.janela, font='courier 9', bg='PeachPuff')
        lst.pack(expand=1, fill='both')

        #
        for lista in sorted(lv):
            lst.insert(END, lista)
            lst.insert(END, '-----------------------------------------------------------------------------------------------------------')

        Button(self.janela, text='Fechar', command=self.janela.destroy, bg='red').pack(side='right')

    def instr_(self):
        if self.janela is None:
            return self.instr()
        try:
            self.janela.destroy()
            return self.instr()
        except TclError:
            return self.instr()

    def principal(self):
        #
        tab_principal = LabelFrame(self.tab)
        self.tab.add(tab_principal, text='Calculando')
        self.tab.select(tab_principal)

        #
        moldura = LabelFrame(tab_principal, bg='PeachPuff')
        moldura.pack(fill='both')

        Label(moldura, text='Primeiro Valor:', fg='blue', font='Arial 10', bg='PeachPuff').grid(row=0)
        Entry(moldura, bd=5, textvar=self.valor1, width=10).grid(row=0, column=1)
        Label(moldura, text='Segundo Valor:', fg='blue', font='Arial 10', bg='PeachPuff').grid(row=1)
        Entry(moldura, bd=5, textvar=self.valor2, width=10).grid(row=1, column=1)
        Label(moldura, text=f'Resultado:', fg='red', font='Arial 10', bg='PeachPuff').grid(row=2)
        Entry(moldura, state='disabled', bd=3, textvar=self.resultado, width=30).grid(row=2, column=1)

        #
        moldura_ = LabelFrame(tab_principal)
        moldura_.pack()
        #
        s = Button(moldura_, relief='ridge', width=10, text='v1+v2', command=self.soma)
        s.grid(row=1)
        sb = Button(moldura_, relief='ridge', width=10, text='v1-v2', command=self.subtracao)
        sb.grid(row=1, column=1)
        exp_v1_v2 = Button(moldura_, relief='ridge', width=10, text='v1exp(v2)', command=self.expoente)
        exp_v1_v2.grid(row=1, column=2)
        mt = Button(moldura_, relief='ridge', width=10, text='v1*v2', command=self.multiplicacao)
        mt.grid(row=1, column=3)
        dv = Button(moldura_, relief='ridge', width=10, text='v1/v2', command=self.divisao)
        dv.grid(row=1, column=4)
        #
        dv_i = Button(moldura_, relief='ridge', width=10, text='v1//v2', command=self.divisao_inteira)
        dv_i.grid(row=2)
        exp_v1 = Button(moldura_, relief='ridge', width=10, text='exp(v1)', command=self.expoente_v1)
        exp_v1.grid(row=2, column=1)
        exp_v2 = Button(moldura_, relief='ridge', width=10, text='exp(v2)', command=self.expoente_v2)
        exp_v2.grid(row=2, column=2)
        expng_v1 = Button(moldura_, relief='ridge', width=10, text='v1exp(-1)', command=self.expoente_neg_v1)
        expng_v1.grid(row=2, column=3)
        expng_v2 = Button(moldura_, relief='ridge', width=10, text='v2exp(-1)', command=self.expoente_neg_v2)
        expng_v2.grid(row=2, column=4)
        #
        rz_v1 = Button(moldura_, relief='ridge', width=10, text='Rq(v1)', command=self.raiz_quad_v1)
        rz_v1.grid(row=3)
        rz_v2 = Button(moldura_, relief='ridge', width=10, text='Rq(v2)', command=self.raiz_quad_v2)
        rz_v2.grid(row=3, column=1)
        mod = Button(moldura_, relief='ridge', width=10, text='Md(v1,v2)', command=self.modulo)
        mod.grid(row=3, column=2)
        mod_v1 = Button(moldura_, relief='ridge', width=10, text='Md(v1)', command=self.modulo_v1)
        mod_v1.grid(row=3, column=3)
        mod_v2 = Button(moldura_, relief='ridge', width=10, text='Md(v2)', command=self.modulo_v2)
        mod_v2.grid(row=3, column=4)
        #
        log0 = Button(moldura_, relief='ridge', width=10, text='logv1(v2)', command=self.logo1)
        log0.grid(row=4)
        log_ = Button(moldura_, relief='ridge', width=10, text='logv2(v1)', command=self.logo1_)
        log_.grid(row=4, column=1)
        log1 = Button(moldura_, relief='ridge', width=10, text='log10(v1)', command=self.logo2)
        log1.grid(row=4, column=2)
        log1_ = Button(moldura_, relief='ridge', width=10, text='log10(v2)', command=self.logo2_)
        log1_.grid(row=4, column=3)
        log_v2 = Button(moldura_, relief='ridge', width=10, text='log2(v1)', command=self.logo3)
        log_v2.grid(row=4, column=4)
        #
        log_v2_ = Button(moldura_, relief='ridge', width=10, text='log2(v2)', command=self.logo3_)
        log_v2_.grid(row=5)
        dec = Button(moldura_, relief='ridge', width=10, text='1/v1', command=self.decimal)
        dec.grid(row=5, column=1)
        dec_ = Button(moldura_, relief='ridge', width=10, text='1/v2', command=self.decimal_)
        dec_.grid(row=5, column=2)
        s_v1 = Button(moldura_, relief='ridge', width=10, text='sen(v1)', command=self.sen_v1)
        s_v1.grid(row=5, column=3)
        s_v2 = Button(moldura_, relief='ridge', width=10, text='sen(v2)', command=self.sen_v2)
        s_v2.grid(row=5, column=4)
        #
        cs_v1 = Button(moldura_, relief='ridge', width=10, text='cos(v1)', command=self.cosen_v1)
        cs_v1.grid(row=6)
        cs_v2 = Button(moldura_, relief='ridge', width=10, text='cos(v2)', command=self.cosen_v2)
        cs_v2.grid(row=6, column=1)
        tn_v1 = Button(moldura_, relief='ridge', width=10, text='tan(v1)', command=self.tang_v1)
        tn_v1.grid(row=6, column=2)
        tn_v2 = Button(moldura_, relief='ridge', width=10, text='tan(v2)', command=self.tang_v2)
        tn_v2.grid(row=6, column=3)
        ft_v1 = Button(moldura_, relief='ridge', width=10, text='fact(v1)', command=self.fat_v1)
        ft_v1.grid(row=6, column=4)
        #
        ft_v2 = Button(moldura_, relief='ridge', width=56, text='fact(v2)', command=self.fat_v2)
        ft_v2.grid(row=8, columnspan=5)

    def main(self):
        #
        menu = Menu(self.gc, tearoff=0, font='tahoma 8', bg='white')
        menu.add_command(label='Instruções', command=self.instr_, underline=0)
        menu.add_separator()
        menu.add_command(label='Sair', command=self.gc.destroy, underline=0)
        info = Menu(menu, tearoff=0)
        info.add_cascade(label='Ajuda', menu=menu, underline=0)
        info.add_command(label='Sobre', command=self.hello, underline=0)
        self.gc.configure(menu=info)

        #
        tab_abertura = LabelFrame(self.tab)
        self.tab.add(tab_abertura, text='Bem-Vindo')
        self.tab.select(tab_abertura)

        #
        def iniciar():
            processar['maximum'] = 100
            for v in range(0, 101, 2):
                sleep(0.2)
                processar['value'] = v
                processar.update()
            if processar['value'] == 100:
                tab_abertura.destroy()
                return self.principal()

        intro = ['BEM - VINDO A CALCULADORA-GC', '',
                 '    A CALCULADORA MAIS SIMPLES E PRÁTICA DO MUNDO',
                 '    ELA TE PERMITE FAZER CÁLCULOS DOS MAIS COMPLEXOS AOS MAIS SIMPLES',
                 '    DE FORMA RESUMIDA E SEM MUITOS DETALHES, BASTA INTRODUZIR:',
                 '    - O [PRIMEIRO VALOR] E O [SEGUNDO VALOR]',
                 '    - PRESSIONAR O BOTÃO DA OPERAÇÃO DESEJADA,',
                 '    - E O [RESULTADO] SURGIRÁ.. COMO QUE POR MAGIA!',
                 '    ELA TAMBÉM TE PERMITE EFETUAR',
                 '    OPERAÇÕES SINGULARES (COM APENAS UM DOS VALORES)..', ' ',
                 '    NA BARRA DE MENU (AJUDA) LHE É DISPONIBILIZADO',
                 '    AS INSTRUÇÕES PARA QUE POSSA CONHECER MELHOR',
                 '    OS COMANDOS E FUNÇÕES DA CALCULADORA-GC', ' ',
                 'Obrigado Pelo Apoio (^_~)',
                 '© 2019-2021 Nurul-GC',
                 '™ ArtesGC']
        lista_intro = ScrolledList(tab_abertura, width=70, height=20, bg='wheat')
        for i in intro:
            lista_intro.insert(END, i)
        lista_intro.pack()

        processar = Progressbar(tab_abertura, orient='horizontal', mode='determinate', value='0')
        processar.pack(side='left', expand=1, fill=BOTH)
        Button(tab_abertura, text='Iniciar', command=iniciar, bg='cyan').pack(side='left')


if __name__ == '__main__':
    app = C8GC()
    app.gc.mainloop()
