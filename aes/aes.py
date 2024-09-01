"""
    Implementação do Algoritmo do AES (Advanced Encryption Standard)
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from utils import *
from modes import *

# Função principal
def main():
    rounds = input("Digite a quantidade de rodadas desejada: ")
    key = input("Digite uma chave válida para a quantidade de rodadas: ")

    keys = keyExpansion(key,int(rounds))
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
