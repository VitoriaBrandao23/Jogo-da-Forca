print(" "*10,"JOGO DA FORCA"," "*10)
print("\nOlá, seja bem vindo!")
print("\nATENÇÃO!\n\nA cada rodada aparecerão duas dicas!\nVocê terá 5 chances de acertar a palavra!\n\nBoa Sorte!\n")

#logica
import random

palavras = ["smartphone", "fogueira", "Silvio Santos", "Queen", "manteiga", "rede", "piloto", "Maria Leopoldina", "fronteira"]
sorteio = random.choice(palavras)
tentativas = 0
chances = 5
letras_usuario = []
escolhas = []

print(f"A palavra tem {len(sorteio)} letra\n")
tracos = ("_") * len(sorteio)
print(tracos, end=" \n\n")

for i in range(0, len(sorteio)):
    letras_usuario.append("_")

if sorteio == "smartphone":
        print("1º DICA: Tecnologia\n2º DICA: Usamos no dia a dia")
if sorteio == "fogueira":
        print("1º DICA: Aquece\n2º DICA: Lenha")
if sorteio == "Silvio Santos":
        print("1º DICA: Televisão\n2º DICA: aviãzinho")
if sorteio == "Queen":
        print("1º DICA: Banda famosa\n2ºDICA: Champions League")
if sorteio == "manteiga":
        print("1º DICA: Derrete\n2º DICA: Amarelo")
if sorteio == "rede":
        print("1º DICA: Descanso\n2º DICA: Balança")
if sorteio == "piloto":
        print("1º DICA: Cabine de avião\n2º DICA: Professor usa")
if sorteio == "Maria Leopoldina":
        print("1º DICA: Imperatriz \n 2º DICA: Áustria")
if sorteio == "fronteira":
        print("1º DICA: Divisão\n2º DICA: Estar em dois lugares ao mesmo tempo")

while tentativas < chances:
    letra = input("\nDigite uma letra: ")

    while letra in escolhas: 
        print("Não pode usar a mesma letra duas vezes!\n")
        letra = input("Digite uma letra: ")
    
    escolhas.append(letra)
    #substituindo as letras certas na palavra desconhecida
    for i in range(0, len(sorteio)):
        if letra == sorteio[i]:
            letras_usuario[i] = letra
            print(letras_usuario)

    if letra in sorteio:
        print("\nVocê acertou uma letra!")
    else:
        print("\nNão foi dessa vez. Tente novamente!")
        tentativas += 1
        print(f"Você tem {tentativas} erros e {chances-tentativas} chances")
    
    if letra in escolhas:
        print(f"Você já escolheu essas letras: {escolhas}\n")
    
#fim do jogo
if tentativas == chances:
    print("GAME OVER")
else:
    print("VOCÊ GANHOU A RODADA")

print(f"\nA palavra era: {sorteio}")
