#Faça um programa com duas listas contendo 3 valores cada, uma com chaves (string) e outra com os valores (int),
#e retorne um dicionário criado a partir destas duas listas.

chaves = ['a', 'b', 'c']
valores = [1, 2, 3]

dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}

print("Dicionário criado a partir das listas:")
print(dicionario)
