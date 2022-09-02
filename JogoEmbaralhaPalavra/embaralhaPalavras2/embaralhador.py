from random import shuffle


def embaralhar(palavra, antes=""):
    antes = palavra
    palavra = list(palavra)
    shuffle(palavra)
    palavra = "".join(palavra)

    if palavra == antes:
        return embaralhar(palavra, antes)
    return palavra