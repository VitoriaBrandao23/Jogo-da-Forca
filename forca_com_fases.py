from time import sleep
from os import system
#estrutura do boneco
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

#cabeçalho
chances = 6

def inicio() :
  nome=input("   Por favor, digite seu nome de usuário: ")
  print("|","-"*42,"|")
  sleep(1)
  print("|"," "*6,f" Olá, seja bem vindo {nome} ao "," "*6,"|")
  print("|","-="*21,"|")
  sleep(1)
  print("|"," "*7,"JOGO DA FORCA DAS VITÓRIAS"," "*7,"|")
  print("|","-="*21,"|")
  sleep(1)

def o_placar():
  inicio()
  print("|","-"*42,"|")
  print("|" ," " *14," VIDAS = ",chances, " " *15,"|","\n|    A cada erro uma vida será descontada    |")
  print("|","-="*21,"|")

o_placar()
def linhas ():
  print("|","-"*42,"|")
  sleep(1)

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
print("|"," "*8,'DIGITE 1 PARA NÍVEL BÁSICO'," "*6, "|")
print("|"," "*6,'DIGITE 2 PARA NÍVEL AVANÇADO'," "*6, "|")
linhas()
nivel=int(input("\nAgora  escolha o nível que você quer jogar: "))
sleep(2)
system('cls') or None

x=0
while nivel !=1 and nivel !=2:
    print("\033[31mVocê digitou uma fase não existente , por favor digite novamente uma das opções disponiveis.\033[m")
    nivel=int(input("Agora  escolha o nível que você quer jogar: "))
    x+=1
if nivel==1:
  print("|"," "*9,f"A palavra tem {len(sorteio)}  letras", " "*9,"|")
  tracos =  ( "_") * len(sorteio)
  print(" "* 15 ,tracos, end=" \n\n")
  
  for i in range(0, len(sorteio)):
      letras_certas.append("_")
    
  while True:
      letra = input("\nDigite uma letra: ").lower()
      linhas()
      if len(letra)>1:
        print("Não entendi, por favor digite uma letra")
        continue
      while letra in digitadas: 
          print("Não pode usar a mesma letra duas vezes!\n")
          letra = input("Digite outra letra: ")
      
      digitadas.append(letra)
      #substituindo as letras certas na palavra desconhecida
      for i in range(0, len(sorteio)):
          if letra == sorteio[i]:
              letras_certas[i] = letra
      print(letras_certas)

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
          if sorteio == "queen":
            print('Você precisa de ajuda! \nDica: Banda famosa')
          if sorteio == "rede":
            print('Você precisa de ajuda! \nDica: Balança')
    
          if sorteio == "fogueira":
            print('Você precisa de ajuda! \nDica: Aquece')
    
          if sorteio == "manteiga":
            print('Você precisa de ajuda! \nDica: Derrete')

          if sorteio == "piloto":
            print('Você precisa de ajuda! \nDica: Cabine de avião')  
            
        if chances == 3:
          print(corpo[3])
          c = corpo[3]
        if chances == 2:
          print(corpo[4])
          c = corpo[4]
          if sorteio == "queen":
            print('Você precisa de mais uma ajuda! \nDica 2: Champions League')
          if sorteio == "rede":
            print('Você precisa de mais uma ajuda! \nDica 2: Descanso')
    
          if sorteio == "fogueira":
            print('Você precisa de mais uma ajuda! \nDica 2: Lenha')
    
          if sorteio == "manteiga":
            print('Você precisa de mais uma ajuda! \nDica 2: Amarelo')

          if sorteio == "piloto":
            print('Você precisa de mais uma ajuda! \nDica 2: Professor usa')  
            
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
  #final do jogo para a fase 1
  if ganhou:
    print("\033[1;46mParabéns, você ganhou!!!!!!!!!!!!!!\033[m")
    sleep(5)
    system('cls') or None
  else:
    print(f"\033[31mVocê perdeu! A palavra era: {sorteio.capitalize()}\033[m")
    sleep(5)
    system('cls') or None
    
#nivel 2
if nivel==2:
  print("|"," "*9,f"A palavra tem {len(sorteio2)}  letras", " "*9,"|")
  tracos =  ( "_") * len(sorteio2)
  print(" "* 15 ,tracos, end=" \n\n")
  
  for i in range(0, len(sorteio2)):
      letras_certas.append("_")

  while True:
      letra = input("\nDigite uma letra: ").lower()
      linhas()
      if len(letra)>1:
        print("Não entendi! Por favor, digite uma letra.")
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

          if sorteio2 == "silvio santos":
              print('Você precisa de ajuda! \nDica: Aviãozinho')
            
          if sorteio2 == "fronteira":
              print('Você precisa de ajuda! \nDica: Está em dois lugares ao mesmo tempo')
          
          if sorteio2 == "maria leopoldina":
            print('Você precisa de ajuda! \nDica: Imperatriz')
            
          if sorteio2 == "smartphone":
            print('Você precisa de ajuda! \nDica: Usamos no dia a dia')
            
        if chances == 3:
          print(corpo[3])
          c = corpo[3]
        if chances == 2:
          print(corpo[4])
          c = corpo[4]

          if sorteio2 == "silvio santos":
              print('Você precisa de mais uma ajuda! \nDica 2: Televisão')
            
          if sorteio2 == "maria leopoldina":
            print('Você precisa de mais uma ajuda! \nDica 2: Áustria')
            
          if sorteio2 == "fronteira":
           print('Você precisa de mais uma ajuda! \nDica 2: Divisão')
            
          if sorteio2 == "smartphone":
            print('Você precisa de mais uma ajuda! \nDica 2: Tecnologia')
            
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
  #final do jogo para a fase 2
  if ganhou:
    print("\033[1;46mParabéns, você ganhou!!!!!!!!!!!!!!\033[m")
    sleep(5)
    system('cls') or None
  else:
    print(f"\033[31mVocê perdeu! A palavra era: {sorteio2.title()}\033[m")
    sleep(5)
    system('cls') or None
