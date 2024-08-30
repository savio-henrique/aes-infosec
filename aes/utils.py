"""
    Utilitários utilizados para a implementação da criptografia AES
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from Crypto.Random import get_random_bytes

def bytes_to_matrix(text):
    text_bytes = bytes.fromhex(text)
    print(list(text_bytes))
    print(text_bytes.hex())

def key_expansion(key, rounds):
    pass

def add_round_key():
    pass

def sub_bytes():
    pass

def shift_rows():
    pass

def mix_columns():
    pass

def round(qty):
    pass

def make_menu(options, title):
    print(title)
    for option in options:
        print(f"{options.index(option) + 1} - {option}")

    return int(input("Digite a opção desejada: ")) - 1
