chances = 5
def inicio() :
  nome=input("   Por favor digite seu nome de usuario :")
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
        print("\nVocê acertou uma letra!")
    else:
        print("\nNão foi dessa vez. Tente novamente!")
        chances-=1
        tentativas+=1
        print(f"Você cometeu {tentativas} erros e {chances} chances")
    ganhou = True
  
    for i in sorteio:
        if i  not in digitadas:
            ganhou = False
    if chances == 0 or ganhou:
                break
        


