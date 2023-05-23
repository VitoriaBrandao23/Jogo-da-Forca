#aqui fica o boneco da forca
#interface_nao_grafica
print(" "*10,"JOGO DA FORCA"," "*10)
print("\nOlá, seja bem vindo!")
print("\nATENÇÃO!\n\nA cada rodada aparecerão duas dicas!\nVocê terá 5 chances de acertar a palavra!\n\nBoa Sorte!\n")

#logica
import random

palavras = ["smartphone", "fogueira", "Silvio Santos", "Queen", "manteiga", "rede", "piloto", "Maria Leopoldina", "fronteira"]
sorteio = random.choice(palavras)
letras_sorteio = [" " for letra in sorteio]
tentativas = 0
chances = 5
letras_usuario = []

print(f"A palavra tem {len(sorteio)} letras\n")
tracos = ("_") * len(sorteio)
print(tracos, end=" \n\n")

while True:
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

    letra = input("\nDigite uma letra: ")

    while letra in letras_usuario: 
        print("Não pode usar a mesma letra duas vezes!\n")
        letra = input("Digite uma letra: ")
    
    letras_usuario.append(letra)

    if letra in sorteio:
        print("\nVocê acertou uma letra!")
        '''acertos = " "
        for certo in sorteio: 
            if certo in letras_usuario: #rever essa parte novamente
                acertos += certo
            else:
                acertos += "_" '''
    else:
        print("\nNão foi dessa vez. Tente novamente!")
        tentativas += 1
    print(f"Você tem {tentativas} tentativas e {chances-tentativas} chances")
    #print(f"{acertos}\n")
    
    if letra in letras_usuario:
        print(f"Você já escolheu essas letras: {letras_usuario}\n")
    
    palavra_correta = " "
    for i in letras_sorteio:
        palavra_correta += i  

    if sorteio == palavra_correta:
        break

print(f"\nA palavra era: {sorteio}")