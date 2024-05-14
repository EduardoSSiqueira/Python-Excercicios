#Implemente um jogo de adivinhação em que o usuário deve acertar um número entre 1 e 10. 
#Utilize tratamento de exceções para garantir que o usuário insira apenas números válidos.

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 3 
    print("Bem-vindo ao Jogo de Adivinhação!")
    print(f"Tente adivinhar o número secreto entre 1 e 10. Você tem {tentativas} tentativas.")

    while tentativas > 0:
        try:
            chute = int(input("Digite seu chute: "))
            if chute < 1 or chute > 10:
                raise ValueError("Digite um número entre 1 e 10.")
            
            if chute == numero_secreto:
                print("Parabéns! Você acertou!")
                break
            elif chute < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
            
            tentativas -= 1
            if tentativas > 0:
                print(f"Você ainda tem {tentativas} tentativas restantes.")
            else:
                print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
        except ValueError:
            print("Digite um número válido.")

jogo_adivinhacao()
