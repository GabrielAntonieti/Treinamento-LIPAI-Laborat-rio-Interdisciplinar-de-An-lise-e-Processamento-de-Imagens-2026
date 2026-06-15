import cv2

# chama a imagem
xadrez = cv2.imread(r"projetos_treinamento\Fotos\xadrez.jpg")
love = cv2.imread(r"projetos_treinamento\Fotos\Love_20x20.jpg")

#transforma em cinza (BGR em GRAY)
#imagem cinza = funcao converter cor em (imagem original para funcao cor cinza)
xadrez_cinza = cv2.cvtColor(xadrez, cv2.COLOR_BGR2GRAY)
love_cinza = cv2.cvtColor(love, cv2.COLOR_BGR2GRAY)

# mostrar a imagem
cv2.imshow("xadrez colorido", xadrez)
cv2.imshow("xadrez cinza", xadrez_cinza)

cv2.imshow("love colorido", love)
cv2.imshow("love cinza", love_cinza)


# Verifica as dimenções
# linhas, coluna
altura, largura = xadrez_cinza.shape
altura2, largura2 = love_cinza.shape

#printar
print("TABELA DE PIXELS xadrez_cinza (0=Preto a 255=Branco)")
print("-" * 100)

for linha in range(altura):
    for coluna in range(largura):
        pixel_xadrez = xadrez_cinza[linha, coluna] #pega o pixel x cruzado na linha e coluna

        # O ':3' serve para alinhar os números (ex: o número '0' vira '  0' para não desalinhar a tabela)
        # O end="  " impede o Python de pular linha a cada pixel
        print(f"{pixel_xadrez:3}", end="  ")

    #pula uma linha
    print()

print("-" * 100)

#printar
print("TABELA DE PIXELS love_cinza (0=Preto a 255=Branco)")
print("-" * 100)

for linha in range(altura2):
    for coluna in range(largura2):
        pixel_love = love_cinza[linha, coluna] #pega o pixel x cruzado na linha e coluna

        # O ':3' serve para alinhar os números (ex: o número '0' vira '  0' para não desalinhar a tabela)
        # O end="  " impede o Python de pular linha a cada pixel
        print(f"{pixel_love:3}", end="  ")

    #pula uma linha
    print()

print("-" * 100)

# Sistem pause
cv2.waitKey(0)
cv2.destroyAllWindows()