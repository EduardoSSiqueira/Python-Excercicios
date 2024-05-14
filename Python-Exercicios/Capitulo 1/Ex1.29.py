#Crie um programa que tenha um dicionário com os nomes, idades e cor dos olhos de 5 membros da sua família. 
#Cada item do dicionário deve ter o nome da pessoa como chave e uma tupla associada contendo a idade e a cor dos olhos.


familia = {
    "Pai": (50, "Castanho"),
    "Mãe": (45, "Castanho escuro"),
    "Irmão": (25, "Castanho"),
    "Irmã": (20, "Castanho claro"),
    "Avô": (70, "Castranho claro")
}

print("Dados dos membros da minha família:")
for nome, (idade, cor_olhos) in familia.items():
    print("- Nome:", nome)
    print("  Idade:", idade)
    print("  Cor dos olhos:", cor_olhos)
