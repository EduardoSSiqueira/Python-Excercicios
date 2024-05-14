#Crie um programa que leia um arquivo texto, inverta o conteúdo de cada linha e salve o 
#resultado em um novo arquivo.


def inverter_linhas(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, "r") as f_in:
            linhas = f_in.readlines()

        linhas_invertidas = [linha.strip()[::-1] for linha in linhas]

        with open(arquivo_saida, "w") as f_out:
            f_out.writelines(linhas_invertidas)

        print(f"Conteúdo invertido salvo em '{arquivo_saida}'.")
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_entrada}' não encontrado.")

nome_arquivo_entrada = "exemplo.txt"
nome_arquivo_saida = "exemplo_invertido.txt"
inverter_linhas(nome_arquivo_entrada, nome_arquivo_saida)
