corpo = [
"""
  *-----*
  |     |
        |
        |
        |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
        |
        |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
  |     |
        |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|     |
        |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|\    |
        |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|\    |
 /      |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|\    |
 / \    |
        |
        |
"""
]
#cabeçalho
chances = 6
def inicio() :
  nome=input("   Por favor digite seu nome de usuario: ")
  print("|","-"*42,"|")
  print("|"," "*9,f" Olá,seja bem vindo {nome}"," "*10,"|")
  print("|","-="*21,"|")
  print("|"," "*13,"JOGO DA FORCA"," "*14,"|")
  print("|","-="*21,"|")
def o_placar():
  inicio()
  print("|","-"*42,"|")
  print("|" ," " *14," VIDAS = ",chances, " " *15,"|","\n|    A cada erro uma vida será descontada    |")
  print("|","-="*21,"|")

o_placar()
def linhas ():
  print("|","-"*42,"|")

#logica
import random

palavras = ["smartphone", "fogueira", "Silvio Santos", "Queen", "manteiga", "rede", "piloto", "Maria Leopoldina", "fronteira"]
sorteio = random.choice(palavras)
tentativas = 0
letras_certas = []
digitadas = []
ganhou = False

print("|"," "*9,f"A palavra tem {len(sorteio)}  letra", " "*9,"|")
tracos =  ( "_") * len(sorteio)
print(" "* 15 ,tracos, end=" \n\n")

for i in range(0, len(sorteio)):
    letras_certas.append("_")

if sorteio == "smartphone":
        print("1º DICA: Tecnologia\n2º DICA: Usamos no dia a dia")
        linhas()
if sorteio == "fogueira":
        print("1º DICA: Aquece\n2º DICA: Lenha")
        linhas()
if sorteio == "Silvio Santos":
        print("1º DICA: Televisão\n2º DICA: aviãzinho")
        linhas()
if sorteio == "Queen":
        print("1º DICA: Banda famosa\n2ºDICA: Champions League")
        linhas()
if sorteio == "manteiga":
        print("1º DICA: Derrete\n2º DICA: Amarelo")
        linhas()
if sorteio == "rede":
        print("1º DICA: Descanso\n2º DICA: Balança")
        linhas()
if sorteio == "piloto":
        print("1º DICA: Cabine de avião\n2º DICA: Professor usa")
        linhas()
if sorteio == "Maria Leopoldina":
        print("1º DICA: Imperatriz \n 2º DICA: Áustria")
        linhas()
if sorteio == "fronteira":
        print("1º DICA: Divisão\n2º DICA: Estar em dois lugares ao mesmo tempo")
        linhas()

while True:
    letra = input("\nDigite uma letra: ").lower()
    linhas()
    while letra in digitadas: 
        print("Não pode usar a mesma letra duas vezes!\n")
        letra = input("Digite uma letra: ")
    
    digitadas.append(letra)
    #substituindo as letras certas na palavra desconhecida
    for i in range(0, len(sorteio)):
        if letra == sorteio[i]:
            letras_certas[i] = letra
    print(letras_certas)
  
    if letra in sorteio.lower():
      print(corpo[0])
      print("\nVocê acertou uma letra!")
      print(f"Letras digitadas: {digitadas}")
    else:
      chances-=1
      if chances == 5:
        print(corpo[1])
      if chances == 4:
         print(corpo[2])
      if chances == 3:
          print(corpo[3])
      if chances == 2:
        print(corpo[4])
      if chances == 1:
        print(corpo[5])
      if chances == 0:
        print(corpo[6])
      print("\nNão foi dessa vez. Tente novamente!")
      tentativas+=1
      print(f"Você cometeu {tentativas} erros e tem {chances} chances")
      print(f"Letras digitadas: {digitadas}")
    ganhou = True
    #finalização
    for i in sorteio:
      if i  not in digitadas:
        ganhou = False
    if chances == 0 or ganhou:
      break
#fim do jogo
if ganhou:
  print("Parabéns, você ganhou!!!")
else:
  print(f"Você perdeu! A palavra era: {sorteio}")
  
  
  #com duas listas_obs  #com duas listas_obs

corpo = [ 
"""
  *-----*
  |     |
        |
        |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
        |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
  |     |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|     |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|\    |
        |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|\    |
 /      |
        |
""",
"""
  *-----*
  |     |
  O     |
 /|\    |
 / \    |
        |
"""]
chances = 6
def inicio() :
  nome=input("   Por favor digite seu nome de usuario: ")
  print("|","-"*42,"|")
  print("|"," "*9,f" Olá,seja bem vindo {nome}"," "*10,"|")
  print("|","-="*21,"|")
  print("|"," "*13,"JOGO DA FORCA"," "*14,"|")
  print("|","-="*21,"|")
def o_placar():
  inicio()
  print("|","-"*42,"|")
  print("|" ," " *14," VIDAS = ",chances, " " *15,"|","\n|    A cada erro uma vida será descontada    |")
  print("|","-="*21,"|")

o_placar()
def linhas ():
  print("|","-"*42,"|")

#logica
import random

palavras= ["Queen", "rede","fogueira","piloto","manteiga"]
palavras_2=["fronteira","smartphone","Silvio Santos","Maria Leopoldina"]
sorteio = random.choice(palavras).lower()
sorteio2 = random.choice(palavras_2).lower()
tentativas = 0
letras_certas = []
digitadas = []
c = []
ganhou = False
print(" "*8,'DIGITE 1 PARA NÍVEL BÁSICO\n'," "*8, 'DIGITE 2 PARA NÍVEL AVANÇADO\n')
linhas()
nivel=int(input("Agora  escolha o nível que você quer jogar: "))
x=0
while nivel !=1 and nivel !=2:
    print("Você digitou uma fase não existente , por favor digite novamente uma das opções disponiveis .")
    nivel=int(input("Agora  escolha o nível que você quer jogar: "))
    x+=1
if nivel==1:
  print("|"," "*9,f"A palavra tem {len(sorteio)}  letra", " "*9,"|")
  tracos =  ( "_") * len(sorteio)
  print(" "* 15 ,tracos, end=" \n\n")
  
  for i in range(0, len(sorteio)):
      letras_certas.append("_")
  
  if sorteio == "smartphone":
          print("1º DICA: Tecnologia\n2º DICA: Usamos no dia a dia")
          linhas()
  if sorteio == "rede":
          print("1º DICA: Descanso\n2º DICA: Balança")
          linhas()
  if sorteio == "fogueira":
    print("1º DICA: Aquece\n2º DICA: Lenha")
    linhas()
  if sorteio == "manteiga":
    print("1º DICA: Derrete\n2º DICA: Amarelo")
    linhas()
  if sorteio == "piloto":
    print("1º DICA: Cabine de avião\n2º DICA: Professor usa")
    linhas()
  while True:
      letra = input("\nDigite uma letra: ").lower()
      linhas()
      if len(letra)>1:
        print("você errou, não pode digitar")
        continue
      while letra in digitadas: 
          print("Não pode usar a mesma letra duas vezes!\n")
          letra = input("Digite uma letra: ")
      
      digitadas.append(letra)
      #substituindo as letras certas na palavra desconhecida
      for i in range(0, len(sorteio)):
          if letra == sorteio[i]:
              letras_certas[i] = letra
      #print(letras_certas)

      if letra in sorteio.lower():
        if tentativas == 0:
          print(corpo[0])
        else:
          print(c)
        print(letras_certas)
        print("\nVocê acertou uma letra!")
        print(f"Letras digitadas: {digitadas}")
        print(f"Você cometeu {tentativas} erros e tem {chances} chances")
      else:
        chances-=1
        if chances == 5:
          print(corpo[1])
          c = corpo[1]
        if chances == 4:
          print(corpo[2])
          c = corpo[2]
        if chances == 3:
          print(corpo[3])
          c = corpo[3]
        if chances == 2:
          print(corpo[4])
          c = corpo[4]
        if chances == 1:
          print(corpo[5])
          c = corpo[5]
        if chances == 0:
          print(corpo[6])
          c = corpo[6]
          
        print("\nNão foi dessa vez. Tente novamente!")
        tentativas+=1
        print(f"Você cometeu {tentativas} erros e tem {chances} chances")
        print(f"Letras digitadas: {digitadas}")
        
      ganhou = True
    
      for i in sorteio:
          if i  not in digitadas:
              ganhou = False
      if chances == 0 or ganhou:
                  break
  
  
  if ganhou:
  
      print("Parabéns, você ganhou!!!!!!!!!!!!!!")
  
  else:
  
      print(f"Você perdeu! A palavra era: {sorteio}")
  
#nivel 2
if nivel==2:
  print("|"," "*9,f"A palavra tem {len(sorteio2)}  letra", " "*9,"|")
  tracos =  ( "_") * len(sorteio2)
  print(" "* 15 ,tracos, end=" \n\n")
  
  for i in range(0, len(sorteio2)):
      letras_certas.append("_")


  if sorteio2 == "fronteira":
    d1 = ('Divisão')
          #print("1º DICA: Divisão\n2º DICA: Estar em dois lugares ao mesmo tempo")
          #linhas()
  if sorteio2 == "Queen":
    print("1º DICA: Banda famosa\n2ºDICA: Champions League")
    linhas()
  if sorteio2 == "Maria Leopoldina":
    print("1º DICA: Imperatriz \n 2º DICA: Áustria")
    linhas()
  if sorteio2 == "Silvio Santos":
    print("1º DICA: Televisão\n2º DICA: aviãzinho")
    linhas()
    
  while True:
      letra = input("\nDigite uma letra: ").lower()
      linhas()
      if len(letra)>1:
        print("você errou, não pode digitar")
        continue
      while letra in digitadas: 
          print("Não pode usar a mesma letra duas vezes!\n")
          letra = input("Digite uma letra: ")
      
      
      digitadas.append(letra)
      #substituindo as letras certas na palavra desconhecida
      for i in range(0, len(sorteio2)):
          if letra == sorteio2[i]:  
            letras_certas[i] = letra
      print(letras_certas)
    
      if letra in sorteio2.lower():
        if tentativas == 0:
          print(corpo[0])
        else:
          print(c)
        print(letras_certas)
        print("\nVocê acertou uma letra!")
        print(f"Letras digitadas: {digitadas}")
      else:
        chances-=1
        if chances == 5:
          print(corpo[1])
          c = corpo[1]
        if chances == 4:
          print(corpo[2])
          c = corpo[2]
          print('Você precisa dede ajuda! \nDica {}'format(d1))
        if chances == 3:
          print(corpo[3])
          c = corpo[3]
        if chances == 2:
          print(corpo[4])
          c = corpo[4]
        if chances == 1:
          print(corpo[5])
          c = corpo[5]
        if chances == 0:
          print(corpo[6])
          c = corpo[6]
          
        print("\nNão foi dessa vez. Tente novamente!")
        tentativas+=1
        print(f"Você cometeu {tentativas} erros e tem {chances} chances")
        print(f"Letras digitadas: {digitadas}")
      ganhou = True
    
      for i in sorteio2:
          if i  not in digitadas:
              ganhou = False
      if chances == 0 or ganhou:
                  break
  
  
  if ganhou:
    print("Parabéns, você ganhou!!!!!!!!!!!!!!")

  
  else:
    print(f"Você perdeu! A palavra era: {sorteio2}")
    
#import os
#os.system('cls') or None

