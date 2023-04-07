import random
from listaDePalavras import listaPalavras
from desenhoDaForca import desenhoForca

vetorPalavra = []
palavraEscolhida = random.choice(listaPalavras)
tamanhoPalavra = len(palavraEscolhida)
gameOver = False
vidas = 6

for i in range(tamanhoPalavra):
    vetorPalavra.append("_")

while not gameOver:
    print(vetorPalavra)
    palpiteLetra = input("Qual letra você escolhe? ").lower()

    if palpiteLetra in vetorPalavra:
        print(f"Você já usou a letra {palpiteLetra}.")

    if palpiteLetra not in palavraEscolhida:
        print(f"A letra {palpiteLetra} não está na palavra. Você perdeu uma vida.")
        vidas -= 1
    else:
        for i in range(tamanhoPalavra):
            if palavraEscolhida[i] == palpiteLetra:
                vetorPalavra[i] = palpiteLetra

    print(desenhoForca[vidas])

    if vidas == 0:
        gameOver = True
        print(f"Você perdeu! A palavra era {palavraEscolhida}")
    if "_" not in vetorPalavra:
        gameOver = True
        print("Você ganhou!")
