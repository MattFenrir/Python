# JOGO DA FORCA
from random import randint

# Criei uma lista de palavras pro jogo
# LISTA OU VETOR
palavras = ['Casa', 'Carro', 'Aviao', 'Moto', 'Mesa', 'Cadeira', 'Teto', 'Casarao', 'Terreno', 'Escola', 'Curso', 'Musica', 'Montanha', 'Piscina', 'Pia', 'Porto', 'Pa', 'Padaria', 'Empresa', 'Ilha', 'Televisao', 'Radio', 'Rua', 'Planta', 'Arvore', 'Portao', 'Computador', 'Escada', 'Sofa']

indice = randint(0, len(palavras) -1) # Recebe um número aleatório entre 0 e a quantidade total de palavras da lista
palavra_secreta = palavras[indice] # Palavra do jogo
tentativa = [] # LISTA DA PALAVRA _ _ _ _ _ ->
chutes = [] # LISTA DE CHUTES

for i in range(len(palavra_secreta)):
  tentativa.append('_')

print(palavra_secreta)
print(tentativa)

def exibirMsg(msg):
  print(msg)

def encontraLetra(chute): # K
  temLetra = False
  for i, letra in enumerate(palavra_secreta): # MOTO
    if(chute.upper() == letra.upper()):
      tentativa[i] = chute.upper()
      temLetra = True
  return temLetra

def jogar():
  tentativas = 5
  while(True):
    chute = input('Digite uma letra R: ') # K
    if(encontraLetra(chute)):
      exibirMsg(tentativa)
    else:
      exibirMsg(f'Letra {chute} não encontrada')
      chutes.append(chute.upper())
      exibirMsg(chutes)
      tentativas -= 1
      exibirMsg(f'Restam {tentativas} tentativas')
      exibirMsg(tentativa)

    if(tentativas <= 0):
      exibirMsg('VOCÊ PERDEU \nJOGUE NOVAMENTE')
      exibirMsg(f'A palavra secreta era {palavra_secreta.upper()}')
      break
      
while(True): # continuar == True
  exibirMsg('**** JOGO DA FORCA ****')
  menu = int(input(' 1 - Jogar \n 2 - Sair \n R: '))
  if(menu == 1):
    jogar()
  else:
    print('Tchau')
    break