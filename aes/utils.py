"""
    Utilitários utilizados para a implementação da criptografia AES
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from constants import *
from Crypto.Random import get_random_bytes

# Transforma bytes em matrizes separada em 4 linhas de acordo com o tamanho do texto
def bytesToMatrix(text):
    text_bytes = list(bytes.fromhex(text))
    matrix = []

    # Pra cada linha, pegue os bytes de 4 em 4 bytes
    for line_num in range(4):
        line = text_bytes[line_num::4]
        matrix.append(line)

    return matrix

# Transforma bytes em uma lista de palavras de 4 bytes de acordo com a quantidade de colunas
def bytesToWords(text, columnqty=4):
    text_bytes = list(bytes.fromhex(text))
    words = []

    # Pra cada coluna, pegar os 4 bytes para formar uma palavra
    for col_num in range(columnqty):
        index = 4 * col_num
        word = text_bytes[index:4+index]
        words.append(word)

    return words

# Implementação do Exclusive Or utilizando bytes
# Utilizada em: stackoverflow.com/questions/29408173/byte-operations-xor-in-python
def xor(bin,key):
    return bytes(a ^ b for a,b in zip(bin,key))

# Expande a chave de acordo com a quantidade de rounds/tamanho da chave
def keyExpansion(key, rounds=10):
    kmatrix = bytesToWords(key, RSize[rounds])
    pass

def addRoundKey():
    pass

def subBytes():
    pass

def shiftRows():
    pass

def mixColumns():
    pass

def round(qty):
    pass

def makeMenu(options, title):
    print(title)
    for option in options:
        print(f"{options.index(option) + 1} - {option}")

    return int(input("Digite a opção desejada: ")) - 1
