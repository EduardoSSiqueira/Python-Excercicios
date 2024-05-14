#Você é um investigador e precisa decifrar uma mensagem secreta escondida em um texto. 
#Cada letra da mensagem foi substituída pela letra do alfabeto que vem imediatamente depois dela. 
#Por exemplo, "a" foi substituída por "b", "b" foi substituída por "c", e assim por diante. 
#A letra "z" foi substituída por "a". Escreva uma função recursiva chamada decifrar_mensagem que aceite a mensagem codificada 
#como uma string e retorne a mensagem decodificada. A regra é que a função deve ser recursiva!

def decifrar_mensagem(mensagem_codificada):
    if not mensagem_codificada:
        return ""

    if mensagem_codificada[0] == 'a':
        letra_original = 'z'
    else:
        letra_original = chr(ord(mensagem_codificada[0]) - 1)

    mensagem_decifrada = decifrar_mensagem(mensagem_codificada[1:])
    return letra_original + mensagem_decifrada

mensagem_codificada = "fsd rds"
mensagem_decifrada = decifrar_mensagem(mensagem_codificada)
print("Mensagem decifrada:", mensagem_decifrada)

