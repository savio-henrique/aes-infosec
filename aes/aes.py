"""
    Implementação do Algoritmo do AES (Advanced Encryption Standard)
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from utils import *
from modes import *

# Definição dos modos de operação
MOP = {"ECB": ecb(),
       "CTR": ctr(),
       "CBC": cbc(),
       "OFB": ofb(),
       "CFB": cfb(),
       "GCM": gcm()
       }

# Função principal
def main():
    key = input("Digite a chave de criptografia: ")
    bytes_to_matrix(key)
    """
    mode = make_menu(MOP, "Digite o modo de operação desejado: \nModos de operação:")
    print(f"Modo de operação escolhido: {MOP[mode]}")
    plaintext = input("Digite o texto a ser criptografado: ")
    key = input("Digite a chave de criptografia: ")
    rounds = int(input("Digite a quantidade de rodadas desejadas: "))
    """


# Condicional para rodar somente se for chamado como script principal
if __name__ == "__main__":
    main()
