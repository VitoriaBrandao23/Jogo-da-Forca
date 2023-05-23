#aqui fica o boneco da forca
#interface_nao_grafica
print(" "*10,"JOGO DA FORCA"," "*10)
print("\nOlá, seja bem vindo!")
print("\nATENÇÃO!\n\nVocê terá 5 chances de acertar a palavra!\nCaso erre duas vezes, terá direito a uma dica!\n\nBoa Sorte!\n")

#logica
import random

palavras = ["smartphone", "fogueira", "Silvio Santos", "Queen", "manteiga", "rede", "piloto", "Maria Leopoldina", "fronteira"]
sorteio = random.choice(palavras)
tentativas = 0
chances = 5
letras_usuario = []

tracos = ("_") * len(sorteio)


while tentativas < chances :
    letra = input("Digite uma letra: ")

    while letra in letras_usuario: 
        print("Não pode usar a mesma letra duas vezes!\n")
        letra = input("Digite uma letra: ")
    
    letras_usuario.append(letra)

    if letra in sorteio:
        print("Você acertou uma letra!")
        acertos = " "
        for certo in sorteio: 
            if certo in letras_usuario: #rever essa parte novamente
                acertos += certo
            else:
                acertos += "_"
    else:
        print("Não foi dessa vez. Tente novamente!")
        tentativas += 1
    print(f"Você tem {tentativas} tentativas e {chances-tentativas} chances")
    #print(f"{acertos}\n")
    
    if letra in letras_usuario:
        print(f"Você já escolheu essas letras: {letras_usuario}")

#fim do jogo
if tentativas == chances:
    print("GAME OVER")
else:
    print("VOCÊ GANHOU A RODADA")

print(f"A palavra era: {sorteio}")
