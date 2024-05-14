#Faça um programa que use Dict Comprehension para criar um dicionário com as raízes quadradas dos 
#números de 1 a 10. Utilize os números como chave e as raízes quadradas como valor.

from math import sqrt

raizes_quadradas = {numero: sqrt(numero) for numero in range(1, 10)}

print("Raízes quadradas dos números de 1 a 10:")
print(raizes_quadradas)
