from random import randint


def frase():
    frases = [
        'Tente de novo, você consegue!', 
        'Mantenha a calma, ainda tem mais chances de acertar!', 
        'Força, guerreiro!',
        'Vamos lá, essa foi quase!',
        'Desiste não!',
    ]

    frase_apoio = frases[randint(0, len(frases) - 1)]
    return frase_apoio