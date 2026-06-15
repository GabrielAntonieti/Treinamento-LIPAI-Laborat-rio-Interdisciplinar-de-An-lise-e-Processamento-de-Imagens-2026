import cv2
import numpy as np

# Carrega a imagem
raiox = cv2.imread(r"projetos_treinamento\Fotos\Love.jpg")
raiox_cinza = cv2.cvtColor(raiox, cv2.COLOR_BGR2GRAY)

# Passo 1: Contagem das tonalidades
tonalidades = [0] * 256
altura, largura = raiox_cinza.shape

for i in range(altura):
    for j in range(largura):
        pixel_raiox = raiox_cinza[i, j] 
        tonalidades[pixel_raiox] += 1

# Passo 2: Criação do histograma acumulado (CDF)
acumulado = [0] * 256
soma = 0

for i in range(256):
    soma += tonalidades[i]
    acumulado[i] = soma

# Passo 3: Aplicação do mapeamento na nova imagem
equalizada = np.zeros((altura, largura), dtype=np.uint8)

for i in range(altura):
    for j in range(largura):
        pixel_novo = (acumulado[raiox_cinza[i, j]]) / acumulado[255] * 255
        equalizada[i, j] = round(pixel_novo)

# Mostrar img x img equalizada
cv2.imshow("Raio-X Original", raiox_cinza)
cv2.imshow("Raio-X Equalizado Manual", equalizada)
cv2.waitKey(0)
cv2.destroyAllWindows()