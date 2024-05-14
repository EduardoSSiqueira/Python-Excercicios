#:: Crie um arquivo vazio qualquer. Agora, na mesma pasta, 
#crie um programa que solicite ao usuário que digite o nome desse arquivo e exclua-o.

import os

nome_arquivo = input("Digite o nome do arquivo a ser excluído: ")

if os.path.exists(nome_arquivo):
    os.remove(nome_arquivo)
    print("O arquivo", nome_arquivo, "foi excluído com sucesso.")
else:
    print("O arquivo", nome_arquivo, "não existe na pasta.")
