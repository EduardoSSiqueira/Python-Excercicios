#Implemente um jogo de adivinhação em que o usuário deve acertar uma palavra secreta. 
#Utilize tratamento de exceções para garantir que o usuário insira apenas letras do alfabeto.

import random
import string

def gerar_palavra_secreta():

    palavras = ["python", "HTML", "Java", "computador", "desenvolvimento"]

    # Escolhe uma palavra aleatoriamente
    return random.choice(palavras)

def jogar_adivinhacao():
    palavra_secreta = gerar_palavra_secreta()
    tentativas = 6  

    print("Bem-vindo ao Jogo de Adivinhação de Palavras!")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
    print("Tente adivinhar a palavra digitando uma letra de cada vez.")

    letras_adivinhadas = set()

    while tentativas > 0:
        try:
            letra_digitada = input("Digite uma letra: ").lower()

            if len(letra_digitada) != 1 or letra_digitada not in string.ascii_lowercase:
                raise ValueError("Digite apenas uma letra do alfabeto.")

            if letra_digitada in letras_adivinhadas:
                print("Você já tentou essa letra. Tente outra.")
            elif letra_digitada in palavra_secreta:
                letras_adivinhadas.add(letra_digitada)
                print("Letra correta! Você adivinhou uma parte da palavra.")
            else:
                print("Letra incorreta. Tente novamente.")

            palavra_atual = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta])
            print(f"Palavra atual: {palavra_atual}")

            if palavra_atual == palavra_secreta:
                print("Parabéns! Você acertou a palavra secreta.")
                break

            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")
        except ValueError as e:
            print(e)

    print(f"A palavra secreta era: {palavra_secreta}")

jogar_adivinhacao()
