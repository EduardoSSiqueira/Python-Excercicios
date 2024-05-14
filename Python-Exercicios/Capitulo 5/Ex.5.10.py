#:: Crie uma função de ordem superior chamada transformarLista que aceite uma lista de números inteiros 
#e uma função como parâmetros. Aplique a função do parâmetro a cada um dos elementos da lista passada como 
#argumento, retornando uma nova lista de mesmo tamanho, porém, com os elementos transformados. 
#Agora crie uma função chamada porExtenso que receba um número inteiro entre 0 e 9 como argumento e 
#retorne seu nome por extenso. Para concluir, chame a função transformarLista passando [1, 2, 3, 4, 5] 
#como primeiro argumento e a função porExtenso como segundo argumento, mostrando a lista resultante.

def transformar_lista(lista, funcao):
    lista_transformada = [funcao(elemento) for elemento in lista]
    return lista_transformada

def por_extenso(numero):
    numeros_por_extenso = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove"
    }
    return numeros_por_extenso.get(numero, "Número fora do intervalo [0, 9]")

lista_transformada = transformar_lista([1, 2, 3, 4, 5], por_extenso)

print("Lista transformada:", lista_transformada)
