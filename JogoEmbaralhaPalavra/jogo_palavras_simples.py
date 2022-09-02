import random

tentativas = 0

frases = 'Tente de novo, você consegue!', 'Mantenha a calma, ainda tem mais chances de acertar!', 
'Força, guerreiro!','Vamos lá, essa foi quase!','Desiste não!'

palavras = 'ABACAXI','VALSA','ANIMADO','ACHATADO','BARCO','PYTHON','AVIADOR',
'PARALELEPIPEDO','OTORRINOLARINGOLOGISTA','FUSCA','CARMESIM','RAPOSA','TRANSPARENTE'

sorteado = random.choice(palavras)

while tentativas < 5:
    embaralha = random.sample(sorteado, len(sorteado))
    juntar_palavra_embaralhada = ''.join(embaralha)
    print(juntar_palavra_embaralhada)
    print("="*20)

    tent = input("Digite a palavra: ").upper()
    tentativas += 1

    if tent == sorteado:
        print(f"Parabéns! Você conseguiu! Tentativas usadas no total: {tentativas}/5")   
        break
    elif tentativas == 5:
        print(f"Ah não... Todas as tentativas foram usadas :(")
        print("="*20)
        break

    print(f"{random.choice(frases)}")


