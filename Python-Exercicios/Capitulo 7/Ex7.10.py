#:: Faça um programa que crie um diretório chamado "Textos" e que, dentro desse diretório, 
#crie 3 arquivos com os nomes "arquivo1.txt", "arquivo2.txt" e "arquivo3.txt" todos contendo o texto 
#"Python Essencial". Em seguida, o programa deve criar um arquivo compactado (.zip) contendo o diretório 
#"Textos".

import os
import zipfile

if not os.path.exists("Textos"):
    os.mkdir("Textos")

for i in range(1, 4):
    filename = f"arquivo{i}.txt"
    with open(os.path.join("Textos", filename), "w") as file:
        file.write("Python Essencial")

with zipfile.ZipFile("Textos.zip", "w") as zip_file:
    for foldername, subfolders, filenames in os.walk("Textos"):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zip_file.write(file_path, os.path.relpath(file_path, "Textos"))

print("Arquivos criados e compactados com sucesso!")
