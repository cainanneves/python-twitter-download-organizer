# import required module
from pathlib import Path
import os
import re
import shutil

matches = [".mp4", ".jpg", ".jpeg"]

def organizeFiles(directory):
    for file in os.scandir(directory):
        # Se for arquivo, nao quero ver diretorios
        if os.path.isfile(file.path):
            filename = file.name.split('-')
            username = filename[0]

            # Caso nao siga o padrao do twiisave
            if any(x in username for x in matches):
                username = '@randomsingles'

            # Caminho para a pasta desse user
            folderpath = os.path.join(directory, username)

            # Se nao houver pasta, cria
            if not os.path.exists(folderpath):
                os.mkdir(folderpath)

            # Caminho para a copia = caminho da pasta do usuario / nome do arquivo
            newpath = f"{folderpath}/{file.name}"

            # Move o arquivo
            shutil.move(file.path, newpath)

def findDuplicates(directory):
    # iterate over files in
    # that directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            match = re.search(r'([\w\.-]+)\s(\(\d\)).(\w+)', filename)
            if match:
                # Caminho para a duplicata que tem (*)
                duplicatePath = os.path.join(root, filename)
                # Caminho para o arquivo original
                originalPath = f"{root}/{match.group(1)}.{match.group(3)}"
                # Deleta duplicatas
                if os.path.exists(originalPath):
                    os.remove(duplicatePath)

def main():
    diretorio = input("Digite o diretório:")
    print("1 - Organizar pasta")
    print("2 - Buscar duplicatas")
    escolha = input("Digite sua escolha:")
    if escolha == '1':
        organizeFiles(diretorio)
    elif escolha == '2':
        findDuplicates(diretorio)

if __name__ == "__main__":
    main()
