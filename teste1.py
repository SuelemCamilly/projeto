import random

tentativa = 5
palavras = (
    "Abacaxi",
    "Valsa",
    "Anime",
    "Achatado",
    "Barco",
    "Python",
    "Aviador",
    "Paralelepipedo",
    "Otorrinolaringologista",
    "Fusca",
    "Carmesim",
    "Raposa",
    "Transparente",
)
sorteado = random.choice(palavras)
while tentativa != 0:
    embaralha = random.sample(sorteado, len(sorteado))

    juntar_palavra_embaralhada = "".join(embaralha)
    print(juntar_palavra_embaralhada)
    print("=" * 20)

    tent = input("Digite a palavra: ").upper()

    if tent == sorteado:
        print("\nParabens! Voce acertou!")
        break
    else:
        tentativa -= 1
        print("f\nVoce errou! Tentativas restantes {tentativa}")
        print("=" * 20)
