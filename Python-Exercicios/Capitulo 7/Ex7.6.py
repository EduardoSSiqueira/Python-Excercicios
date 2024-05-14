#:: Crie um programa que solicite ao usuário o nome de arquivo existente na mesma pasta, 
#copie-o para um novo arquivo mudando a extensão para ".cópia" e exiba o resultado da operação na tela.

import os
import shutil

def main():
    filename = input("Digite o nome do arquivo existente na mesma pasta: ")

    if os.path.isfile(filename):
        new_filename = os.path.splitext(filename)[0] + ".cópia"

        shutil.copy2(filename, new_filename)

        print(f"Arquivo '{filename}' copiado com sucesso para '{new_filename}'.")
    else:
        print(f"O arquivo '{filename}' não existe nesta pasta.")

if __name__ == "__main__":
    main()
