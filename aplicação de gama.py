# aplicação de gamma

"""
Como a curva se comporta:
Gamma = 1.0: É uma linha diagonal reta. A entrada é igual à saída.
Gamma < 1.0 : A curva fica acima da diagonal. Isso "empurra" os tons médios para valores mais altos (mais claros), revelando detalhes que estavam escondidos nas sombras. É o que chamamos de Gamma encoding.
Gamma > 1.0 : A curva fica abaixo da diagonal. Isso comprime os tons, tornando a imagem mais escura e aumentando o contraste percebido nas áreas mais claras. É o que chamamos de Gamma decoding (usado pelos monitores para exibir a imagem corretamente).
"""
import cv2
import numpy as np

img = cv2.imread(r"Fotos\piramides.jpg")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gama = float(input("Digite o valor de Gamma: "))

altura, largura = img_cinza.shape

# cria imagem vazia
img_gamma = np.zeros((altura, largura), dtype=np.uint8)

for i in range(altura):
    for j in range(largura):
        # Normaliza o pixel atual (0-255 -> 0-1)
        pixel_norm = img_cinza[i, j] / 255.0
        
        # Aplica a potência (curva gama)
        pixel_gamma = pow(pixel_norm, gama)
        
        # Escala de volta para 0-255 e salva na nova imagem
        img_gamma[i, j] = int(pixel_gamma * 255)

cv2.imshow("Original Cinza", img_cinza)
cv2.imshow("Gama Cinza", img_gamma)

cv2.waitKey(0)
cv2.destroyAllWindows()