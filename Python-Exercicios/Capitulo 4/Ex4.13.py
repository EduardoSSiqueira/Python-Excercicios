#:: Crie um programa que peça ao usuário para digitar uma frase, divida-a em palavras, remova todos os espaços 
#em branco desnecessários dessas palavras, e componha a frase novamente com apenas 1 espaço entre as palavras.

def remover_espacos_desnecessarios(frase):
    palavras = frase.split()

    palavras_sem_espaco = [palavra.strip() for palavra in palavras]

    nova_frase = ' '.join(palavras_sem_espaco)

    return nova_frase

frase_usuario = input("Escreva algo: ")

nova_frase = remover_espacos_desnecessarios(frase_usuario)

print("Frase com espaços em branco desnecessários removidos:", nova_frase)
