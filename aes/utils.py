"""
    Utilitários utilizados para a implementação da criptografia AES
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from constants import *
from Crypto.Random import get_random_bytes
from PIL import Image
import io

# Transforma bytes em matrizes separada em 4 linhas de acordo com o tamanho do texto
def bytesToMatrix(text):
    text_bytes = list(text)
    matrix = []

    # Pra cada linha, pegue os bytes de 4 em 4 bytes
    for line_num in range(4):
        line = text_bytes[line_num::4]
        matrix.append(line)

    return matrix

def matrixToBytes(matrix):
    text_bytes = []
    for line in matrix:
        text_bytes += line

    return bytes(text_bytes)

# Transforma bytes em uma lista de palavras de 4 bytes de acordo com a quantidade de colunas
def bytesToWords(text, columnqty=4):
    text_bytes = list(text)
    words = []

    # Pra cada coluna, pegar os 4 bytes para formar uma palavra
    for col_num in range(columnqty):
        index = 4 * col_num
        word = text_bytes[index:4+index]
        words.append(word)

    return words

# Implementação do Exclusive Or utilizando bytes
# Retirada de: stackoverflow.com/questions/29408173/byte-operations-xor-in-python
def xor(bin,key):
    return list(bytes(a ^ b for a,b in zip(bin,key)))

# Expande a chave de acordo com a quantidade de rounds/tamanho da chave
def keyExpansion(key, rounds=10):
    columns_size = RSize[rounds]
    kmatrix = bytesToWords(key, columns_size)

    # Contador para separar a chave em 4 bytes
    counter = columns_size - 4

    # Separa as chaves em listas com 4 palavras cada, uma lista de matrizes
    keys = [kmatrix[:-counter]] if counter != 0 else []  
     
    # Para cada rodada gere uma quantidade columns_size de chaves
    for round in range(rounds+1):
        if (len(keys) <= rounds+1):
            index = round*(columns_size)

            # Seleciona palavras em um box de column_size bytes. Ex: para chaves de 192 bits, 6 palavras
            words = kmatrix[index:index+columns_size+1]
            
            # Seleciona a chave restante para a rodada 
            round_key = words[-counter:]

            last_word = round_key[-1]
            
            # Gera a palavra com a ultima palavra para utilizar no xor da proxima chave
            xor_word = generateWord(last_word,round)

            for boxsize in range(columns_size):
                # Caso o contador seja maior que 3 reseta a chave da rodada
                if counter >  3 or counter == 0:
                    counter = 0
                    keys.append(round_key)
                    round_key = []

                xor_word = xor(words[boxsize],xor_word)
                round_key.append(xor_word)
                kmatrix.append(xor_word)
                counter += 1

    return keys

# Gera uma palavra para utilizar no xor da proxima chave de acordo com a rodada
def generateWord(word, round):
    # Rotaciona a palavra
    rword = word[1:] + [word[0]]

    # Substitui os bytes da palavra
    for i in range(4):
        rword[i] = SBox[rword[i]]

    # Realiza o xor com a constante da rodada
    result = list(xor(rword,[RCon[round],0,0,0]))
    return result

# Gera um nonce aleatório se for nulo
def genIV():
    nonce = input("Digite o nonce em hexadecimal (Deixe vazio se não possuir um nonce):\n")
    if len(nonce) != 24:
        print("Nonce inválido, gerando nonce aleatório")
        nonce = ""

    nonce = get_random_bytes(12) if nonce == "" else bytes.fromhex(nonce)
    print(f"O seu nonce é: {nonce.hex()}")

    return nonce

# Gera uma chave aleatória se for nula
def genKey(rounds):
    keysize = RSize[rounds]*4
    key = input("Digite a chave em hexadecimal (Deixe vazio se não possuir uma chave):\n")
    if len(key) != keysize*2:
        print("Chave inválida, gerando chave aleatória")
        key = ""

    key = get_random_bytes(keysize) if key == "" else bytes.fromhex(key)
    print(f"A sua chave é: {key.hex()}")

    return key

# Adiciona a chave no estado da matriz
def addRoundKey(matrix, key):
    for i in range(4):
        line = xor(matrix[i],key[i])
        matrix[i] = line

# Função de substituição de bytes
def subBytes(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = SBox[matrix[i][j]]

# Função de deslocamento de linhas
def shiftRows(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][i:] + matrix[i][:i]   

# Função de mistura de colunas
# Retirada de: https://en.wikipedia.org/wiki/Rijndael_MixColumns
def mixColumns(matrix):
    new_matrix = [[0] * 4 for _ in range(4)]

    for col in range(4):
        new_matrix[0][col] = gMul(2, matrix[0][col]) ^ gMul(3, matrix[1][col]) ^ matrix[2][col] ^ matrix[3][col]
        new_matrix[1][col] = matrix[0][col] ^ gMul(2, matrix[1][col]) ^ gMul(3, matrix[2][col]) ^ matrix[3][col]
        new_matrix[2][col] = matrix[0][col] ^ matrix[1][col] ^ gMul(2, matrix[2][col]) ^ gMul(3, matrix[3][col])
        new_matrix[3][col] = gMul(3, matrix[0][col]) ^ matrix[1][col] ^ matrix[2][col] ^ gMul(2, matrix[3][col])

    for i in range(4):
        matrix[i] = new_matrix[i]

# Função de multiplicação de bytes
# Retirada de: https://en.wikipedia.org/wiki/Rijndael_MixColumns
def gMul(a,b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p & 0xFF


# Função de rodada recursiva do AES
def round(current_round,keys,matrix,qty):
    key = keys[(qty-1) - current_round]
    if current_round == 0:
        subBytes(matrix)
        shiftRows(matrix)
        addRoundKey(key,matrix)
        return
    else:
        subBytes(matrix)
        shiftRows(matrix)
        mixColumns(matrix)
        addRoundKey(key,matrix)
        round(current_round - 1, keys, matrix, qty)
    return

# Função para gerar um menu
def makeMenu(options, title):
    while True:
        print(title)
        for option in options:
            print(f"{options.index(option) + 1} - {option}")

        response = int(input("Digite a opção desejada: "))

        if ((response - 1) in range(len(options))):
            break
        else:
            print("Opção inválida, tente novamente")

    return response - 1

# Função de separação de blocos de texto
def toBlocks(text, blocksize):
    blocks = []
    for i in range(0, len(text), blocksize):
        block = text[i:i+blocksize]
        blocks.append(block)

    return blocks

# Função de leitura de imagem
def imageToBytes(image):
    with Image.open(image) as img:
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
    return img_bytes

# Função de escrita de imagem
def bytesToImage(image, path):
    img_bytes = io.BytesIO(image)
    with Image.open(img_bytes) as img:
        img.save(path)
