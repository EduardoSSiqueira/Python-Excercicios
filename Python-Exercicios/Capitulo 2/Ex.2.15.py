#Crie um programa que peça ao usuário para digitar uma palavra. O programa deve então indicar se a palavra inserida começa com uma vogal ou uma consoante.


palavra = input("Digite uma palavra: ")


primeira_letra = palavra[0].lower()

if primeira_letra in ['a', 'e', 'i', 'o', 'u']:
    print("A palavra começa com uma vogal.")
else:
    print("A palavra começa com uma consoante.")
