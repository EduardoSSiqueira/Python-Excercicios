#Crie um programa que verifique se um texto digitado pelo usuário corresponde a uma data no formato "dd/mm/aaaa", considerando que a data deve ter 10 caracteres, "dd" deve variar de 01 a 31, "mm" de 01 a 12 e "aaaa" de 0001 a 9999. 
#Utilize colchetes para acessar os caracteres do texto pelo seu índice (exemplos: texto[0:2] pega os dois primeiros dígitos e texto[3:5] pega os dígitos nas posições 3 e 4).

data = input("Insira uma data no formato dd/mm/aaaa: ")


if len(data) == 10 and data[2] == '/' and data[5] == '/':
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:]

    if (dia.isdigit() and mes.isdigit() and ano.isdigit() and
        1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and
        1 <= int(ano) <= 9999):
        print("A data é válida.")
    else:
        print("A data é inválida.")
else:
    print("A data não está no formato correto.")
