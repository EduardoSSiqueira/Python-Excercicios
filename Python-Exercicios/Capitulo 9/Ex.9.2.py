#Crie uma função que receba uma lista de números e retorne a média aritmética deles.
#Trate exceções caso a lista seja vazia ou contenha valores não numéricos.


def calcular_media(lista):
    try:
        if not lista:
            raise ValueError("A lista está vazia. Não é possível calcular a média.")
        
        valores_numericos = [valor for valor in lista if isinstance(valor, (int, float))]
        
        if not valores_numericos:
            raise ValueError("A lista não contém valores numéricos.")
        
        media = sum(valores_numericos) / len(valores_numericos)
        return media
    except ValueError as e:
        return str(e)

minha_lista = [1, 2, 3, 4, 5, 6]
media_resultante = calcular_media(minha_lista)
print(f"Média: {media_resultante:.2f}")

