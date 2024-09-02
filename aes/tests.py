"""
    Testes de funções utilitárias
    Autor: Sávio Henrique Chaves Mendes
"""

# Importação de módulos
from utils import *

# Teste de bytesToMatrix
def testBytesToMatrix():
    # Teste 1
    text = "00112233445566778899aabbccddeeff"
    expected = [[0,68,136,204],[17,85,153,221],[34,102,170,238],[51,119,187,255]]
    result = bytesToMatrix(text)
    assert result == expected, f"Erro: {result} != {expected}"


def testGenerateWord():
    # Teste 1
    word = [0,68,136,204]
    expected = [68,136,204,0]
    result = generateWord(word,10)
    assert result == expected, f"Erro: {result} != {expected}"

def testMixColumns():
    # Teste 1
    state = [
        [198,1,45,219],
        [198,1,38,19],
        [198,1,49,83],
        [198,1,76,69]
    ]
    expected = [
        [198,1,77,142],
        [198,1,126,77],
        [198,1,189,161],
        [198,1,248,188]
    ]
    mixColumns(state)
    assert state == expected, f"Erro: {state} != {expected}"

def testAddRoundKey():
    # Teste 1
    state = [
        [198,1,45,219],
        [198,1,38,19],
        [198,1,49,83],
        [198,1,76,69]
    ]
    key = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
    ]
    expected = [
        [199,0,44,218],
        [199,0,39,18],
        [199,0,48,82],
        [199,0,77,68]
    ]
    addRoundKey(state,key)
    assert state == expected, f"Erro: {state} != {expected}"

testMixColumns()
testAddRoundKey()
