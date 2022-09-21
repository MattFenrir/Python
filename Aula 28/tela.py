from tkinter import *

telaInicial = Tk() # Instanciar
telaInicial['bg'] = '#cccccc' # Alterar a cor de fundo
telaInicial.title('Home') # Alterar Título

largura = 800 # Altura do programa
altura = 650 # Largura do programa
larguraUser = telaInicial.winfo_screenwidth() # 1920 - 850 = 1070 /2 = 535
alturaUser = telaInicial.winfo_screenheight()
print(larguraUser, alturaUser) # Tela do Usuário
larguraX = int((larguraUser - largura)/2)
alturaY = int((alturaUser - altura)/2)
telaInicial.geometry(f'{largura}x{altura}+{larguraX}+{alturaY}')
telaInicial.resizable(False, False) # Permite o redimensionamento 1 = True 0 = False
telaInicial.minsize(850, 650)
telaInicial.maxsize(1920, 1080)
# telaInicial.state('zoomed') # zoomed / iconic

labelUsu = Label(telaInicial, text='Usuário: ')
labelUsu.pack()
labelSenha = Label(telaInicial, text='Senha: ')
labelSenha.pack()

def entrar():
    #print('Olá, Mundo!')
    labelMsg.config(text='Olá, Mundo!')

btmEntrar = Button(telaInicial, text='Entrar', command=entrar) # Criar instância do botão
btmEntrar.pack()

labelMsg = Label(telaInicial, text='')
labelMsg.pack()


# Última linha
telaInicial.mainloop() # Abre a tela