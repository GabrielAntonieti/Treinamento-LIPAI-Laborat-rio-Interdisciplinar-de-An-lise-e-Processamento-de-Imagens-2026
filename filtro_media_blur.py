import cv2

# N = 15   # Tamanho da Matriz (ímpar)
N = int(input("Digite um número inteiro: "))

lateral = N // 2    # Quantos pixels olhar para cada lado (para N=15, olhar 7 pixels)
area = N * N

piramides = cv2.imread(r"projetos_treinamento\Fotos\piramides.jpg")
piramides_cinza = cv2.cvtColor(piramides, cv2.COLOR_BGR2GRAY)

# variavel = funcao blur (img cinza , (malha impar))
piramides_blur_funcao = cv2.blur(piramides_cinza,(N,N))

# POR FOR

# Faz uma copia
piramides_blur = piramides_cinza.copy()

# Descobre a altura e largura da imagem
altura, largura = piramides_cinza.shape

# Filtro de média:
# Começa na lateral e para antes da borda para nao ler fora
for i in range(lateral, altura - lateral):
    for j in range(lateral, largura - lateral):
        soma_pixels = 0

        # varrer a matriz N x N ao redor do pixel atual [i, j]
        # vai de -X para X, sendo X+1 por causa do zero
        for k in range(-lateral, lateral + 1):
            for l in range(-lateral, lateral + 1):          
                # i+k pegam os vizinhos de cima, j+l de baixo, da esquerda e da direita
                pixel_vizinho = int(piramides_cinza[i + k, j + l])
                soma_pixels += pixel_vizinho
        media = soma_pixels // area
        piramides_blur[i, j] = media

"""
# Filtro de média:
# POR SLICE

# Faz uma copia
piramides_blur = piramides_cinza.copy()

# Descobre a altura e largura da imagem
altura, largura = piramides_cinza.shape

# Começa na lateral e para antes da borda para nao ler fora
for i in range(lateral, altura - lateral):
    for j in range(lateral, largura - lateral):
        
        # Recortamos a janela N x N ao redor do pixel [i, j] de uma vez só
        # os : faz o fatiamento da matriz [inicio : fim], assim fica [ fatiamento_das_linhas , fatiamento_das_colunas ]
        janela = piramides_cinza[i - lateral : i + lateral + 1, j - lateral : j + lateral + 1]
        
        # Somamos todos os pixels da janela na raça
        soma_pixels = janela.sum() #permite sair dos 8 bits do cv2
        
        # Calculamos a média (divisão inteira)
        media = soma_pixels // area
        
        # Aplicamos o resultado
        piramides_blur[i, j] = media
"""

cv2.imshow("piramides_cinza_resultado", piramides_cinza)
cv2.imshow("piramides_blur_na_mao", piramides_blur)
cv2.imshow("piramides_blur_funcao", piramides_blur_funcao)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

""""
# Estava dando KeyboardInterrupt
cv2.imshow("piramides_cinza_resultado", piramides_cinza)
cv2.imshow("piramides_blur_na_mao", piramides_blur)
cv2.imshow("piramides_blur_funcao", piramides_blur_funcao)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""