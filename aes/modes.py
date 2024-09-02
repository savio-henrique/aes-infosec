"""
    Implementação dos diferentes modos de operação do AES (Advanced Encryption Standard)
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from utils import *

# Implementação da Cifração
def encrypt(key, rounds, text):
    keys = keyExpansion(key, rounds)
    state = bytesToMatrix(text)
    addRoundKey(state, keys[0])
    round(rounds-1, keys[1:], state, rounds)

    return matrixToBytes(state)

# Implementação do modo ECB (Electronic Codebook)
def ecb():
    pass

# Implementação do modo CTR (Counter)
def ctr(key, mode, rounds, blocks):
    nonce = genIV()
    counter = 0
    output = []
    for block in blocks:
        nonce_counter = nonce + counter.to_bytes(4, byteorder='big')
        cipher = encrypt(key, rounds, nonce_counter)
        counter += 1
        output += xor(block, cipher)

    return bytes(output)

# Implementação do modo CBC (Cipher Block Chaining)
def cbc():
    pass

# Implementação do modo OFB (Output Feedback)
def ofb():
    pass

# Implementação do modo CFB (Cipher Feedback)
def cfb():
    pass

# Implementação do modo GCM (Galois/Counter Mode)    
def gcm():
    pass

# Dicionário de referência para os modos
MOP = {"ECB (não implementado ainda)": ecb,
       "CTR": ctr,
       "CBC (não implementado ainda)": cbc,
       "OFB (não implementado ainda)": ofb,
       "CFB (não implementado ainda)": cfb,
       "GCM (não implementado ainda)": gcm
       }

