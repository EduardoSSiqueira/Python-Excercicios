#Faça um programa que adicione 30 dias à data atual utilizando timedelta.

from datetime import datetime, timedelta

# Obtém a data atual
data_atual = datetime.now()

# Adiciona 30 dias à data atual
data_nova = data_atual + timedelta(days=30)

# Imprime a data atual e a nova data
print("Data atual:", data_atual.strftime("%d/%m/%Y"))
print("Nova data após adicionar 30 dias:", data_nova.strftime("%d/%m/%Y"))
