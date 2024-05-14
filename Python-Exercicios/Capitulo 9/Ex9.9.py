#Crie uma função chamada read_file que recebe o nome de um arquivo como argumento e 
#imprime o conteúdo do arquivo. A função deve abrir o arquivo para leitura no bloco try,
#tratar exceções no bloco except para o caso do arquivo não existir, 
#e finalmente fechar o arquivo no bloco finally, independente de exceções terem sido lançadas ou não.

def read_file(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("O arquivo não pôde ser encontrado.")
    finally:
        if 'arquivo' in locals():
            arquivo.close()

nome_do_arquivo = "arquivo.txt"
read_file(nome_do_arquivo)
