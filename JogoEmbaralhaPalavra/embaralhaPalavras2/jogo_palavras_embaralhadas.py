from palavras import aleatoriza_palavra
from frases import frase
from embaralhador import embaralhar


def main(tema):
    tentativas = 0
    sorteada, dificuldade = aleatoriza_palavra(tema)
    embaralhada = embaralhar(sorteada)

    while True:
        frase_apoio = frase()

        print("A palavra embaralhada é ", embaralhada)
        print("Na dificuldade: ", dificuldade)

        tent = input("Qual é a palavra embaralhada? \n> ")
        tentativas += 1

        if tentativas == 5: 
            print(f"Ah não... Todas as tentativas foram usadas :( \n 5/5 tentativas")
            break

        if tent.upper() == sorteada.upper():
            print(f"Parabéns! Você conseguiu! :D \nVocê acertou em {tentativas} / 5 tentativas")
            break 
        print(f"\n{frase_apoio}")

if __name__ == "__main__":
    while True:
        tema = int(
            input(
            "Escolha um tema (1 - ANIMAIS / 2 - OBJETOS / 3 - CORES): "
            )
        )
        break
    main(tema)