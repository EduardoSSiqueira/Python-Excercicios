#Faça um programa que crie um objeto datetime representando o instante atual.
#Em seguida, formate esse instante para exibir o número da semana do ano (de 1 a 52).

import datetime

instante_atual = datetime.datetime.now()

numero_semana_ano = instante_atual.strftime("%U")

print("Número da semana do ano:", numero_semana_ano)


