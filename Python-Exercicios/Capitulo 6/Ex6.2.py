#Faça um programa que use List Comprehension para criar uma lista com as palavras que contêm a letra "a" em 
#uma frase digitada pelo usuário, substituindo a letra por "o".

frase = input("Digite uma frase: ")

palavras_com_a_substituido = [''.join(['o' if letra == 'a' else letra for letra in palavra]) for palavra in frase.split() if 'a' in palavra]

print("Palavras com 'a' substituído por 'o':", palavras_com_a_substituido)
