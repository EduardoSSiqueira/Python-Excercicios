#:: Faça um programa que crie um objeto datetime que represente o instante atual. 
#Em seguida, formate esse instante para exibir o número do dia do ano entre 1 e 365 (ou 366 para anos bissextos).

from datetime import datetime

instante_atual = datetime.now()

dia_do_ano = instante_atual.timetuple().tm_yday

print("Número do dia do ano:", dia_do_ano)
