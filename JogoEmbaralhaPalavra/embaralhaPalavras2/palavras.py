from random import randint


def aleatoriza_palavra(tema):
    animais = {
        "F": [
            'PATO', 
            'GATO', 
            'RATO', 
            'SAPO', 
            'GALO',
        ],
        "M": [
            'RAPOSA', 
            'GALINHA', 
            'TUCANO', 
            'BALEIA',
        ],
        "D": [
            'CHIMPANZE', 
            'CACHORRO', 
            'FLAMINGO', 
            'SALAMANDRA',
        ],
    }

    objetos = {
        "F": [
            'VASO', 
            'BOLA', 
            'CAIXA', 
            'FACA',
        ],
        "M": [
            'ABAJUR', 
            'PANELA', 
            'VASSOURA', 
            'BANHEIRA',
        ],
        "D": [
            'CANDELABRO', 
            'AMPULHETA', 
            'XILOFONE', 
            'DESFIBRILADOR',
        ],
    }

    cores = {
        "F": [
            'ROSA', 
            'PRETO', 
            'ROXO', 
            'CINZA',
        ],
        "M": [
            'BRANCO', 
            'VIOLETA', 
            'CARMESIM', 
            'AMARELO',
            'LARANJA'
        ],
        "D": [
            'CASTANHO', 
            'DOURADO', 
            'ESCARLATE', 
            'HELIOTROPIO', 
            'PURPURA',
            'VERMILION'
        ],
    }

    lista_temas = {1: animais, 2: objetos, 3: cores}

    dificuldades = ["FACIL", "MEDIO", "DIFICIL"]
    dificuldade_escolhida = dificuldades[randint(0, len(dificuldades) - 1)]

    lista_palavras = lista_temas[tema][dificuldade_escolhida[0]]

    sorteada = lista_palavras[randint(0, len(lista_palavras) - 1)]
    return (sorteada, dificuldade_escolhida)