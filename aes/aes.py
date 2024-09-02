"""
    Implementação do Algoritmo do AES (Advanced Encryption Standard)
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from utils import *
from modes import *
from constants import *


# Modo de cifra/decifra de imagem
def imageMode(key, mode, rounds, mop):
    if mode == 0:
        file = input("Digite o nome da imagem com extensão a ser cifrada (deve estar na pasta ./images): ")
        filename = input("Digite o nome das imagens a serem salvas: ")
        img_bytes = imageToBytes(f"./images/{file}")
        blocks = toBlocks(img_bytes, 16)
        cipher = mop(key, mode, rounds, blocks)

        with open(f"./images/{filename}", 'w') as f:
            f.write(cipher.hex())
            print(f"Arquivo cifrado salvo em ./files/{filename}")
            f.close()bytesToImage(cipher, f"./images/{filename}")

    elif mode == 1:
        file = input("Digite o nome da imagem com extensão a ser decifrada (deve estar na pasta ./images): ")
        filename = input("Digite o nome do arquivo a ser salvo: ")

        with open(f"./images/{file}",'r') as f:
            text = f.read()
            blocks = toBlocks(bytes.fromhex(text), 16)
            plain = mop(key, mode, rounds, blocks)
            f.close()

        bytesToImage(plain, f"./images/{filename}")
        print(f"Arquivo decifrado salvo em ./files/{filename}")


# Modo de cifra/decifra de arquivo
def fileMode(key, mode, rounds, mop):
    if mode == 0:
        file = input("Digite o nome do arquivo com extensão a ser cifrado (deve estar na pasta ./files): ")
        filename = input("Digite o nome do arquivo a ser salvo: ")
        with open(f"./files/{file}", 'r') as f:
            text = f.read()
            blocks = toBlocks(text.encode('utf-8'), 16)
            cipher = mop(key, mode, rounds, blocks)
            f.close()

            print(cipher)
        with open(f"./files/{filename}", 'w') as f:
            f.write(cipher.hex())
            print(f"Arquivo cifrado salvo em ./files/{filename}")
            f.close()

        print(f"Texto cifrado: {cipher.hex()}")
    elif mode == 1:
        file = input("Digite o nome do arquivo com extensão a ser decifrado (deve estar na pasta ./files): ")
        filename = input("Digite o nome do arquivo a ser salvo: ")
        with open(f"./files/{file}",'r') as f:
            text = f.read()
            blocks = toBlocks(bytes.fromhex(text), 16)
            plain = mop(key, mode, rounds, blocks)
            f.close()

        with open(f"./files/{filename}", 'w') as f:
            f.write(plain.decode('utf-8'))
            print(f"Arquivo decifrado salvo em ./files/{filename}")
            f.close()

        print(f"Texto decifrado: {plain.decode('utf-8')}")

# Modo de cifra/decifra de texto
def textMode(key, mode, rounds, mop):
    if mode == 0:
        text = input("Digite o texto a ser cifrado: ")
        blocks = toBlocks(text.encode('utf-8'), 16)
        cipher = mop(key, mode, rounds, blocks)
        print(f"Texto cifrado: {cipher.hex()}")
    elif mode == 1:
        text = input("Digite o texto a ser decifrado: ")
        blocks = toBlocks(bytes.fromhex(text), 16)
        plain = mop(key, mode, rounds, blocks)
        print(f"Texto decifrado: {plain.decode('utf-8')}")

# Função principal
def main():
    mop_options = list(MOP.keys())
    round_options = list(RSize.keys())
    
    selected_mop = makeMenu(mop_options, "Digite o modo de operação desejado: \nModos de operação:")
    print(f"Modo de operação escolhido: {mop_options[selected_mop]}")
    
    mode = makeMenu(["Cifrar", "Decifrar"], "Digite a opção desejada: \nOpções:")
    
    text_type = makeMenu(["Texto", "Arquivo", "Imagem"], "Digite o tipo de entrada desejada: \nTipo de entrada:")
    
    selected_rounds = makeMenu(round_options, "Digite a quantidade de rodadas desejadas: \nQuantidade de rodadas:")
    rounds = int(round_options[selected_rounds])
    
    key = genKey(rounds)

    if text_type == 0:
        textMode(key, mode, rounds, MOP[mop_options[selected_mop]])
    elif text_type == 1:
        fileMode(key, mode, rounds, MOP[mop_options[selected_mop]])
    elif text_type == 2:
        imageMode(key, mode, rounds, MOP[mop_options[selected_mop]])
    else:
        print("Opção inválida")
        return

# Condicional para rodar somente se for chamado como script principal
if __name__ == "__main__":
    main()
