# deteccao de borda com o Operador Sobel
# operadores como Roberts, Prewitt funcional de forma muito similar, com a mesma lógica (mudando apenas o np.array)
# gera bordas grossas

"""
ele pega a matriz np.array e multiplica ponto por ponto da imagem para que gere as bordas, exemplo:
imagem
0 0 0 100 100 100
0 0 0 100 100 100
0 0 0 100 100 100

ele vai pegar de 3x3 por vez, e somar tudo, assim vai ver se tem borda caso de uma diferenca muito grante
ex:                     resultado:          soma:
0x1 100x0 100x-1        0 0 -100            -500
0x2 100x0 100x-2        0 0 -200
0x1 100x0 100x-1        0 0 -100

assim ele percebe a borda
"""

import cv2
import numpy as np

sobel_horizontal = np.array([[1, 0, -1],
                             [2, 0, -2],
                             [1, 0, -1]])

sobel_vertical = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

img = cv2.imread(r"projetos_treinamento\Fotos\piramides.jpg")
img_cinza =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


borda_vertical = cv2.filter2D(img_cinza, cv2.CV_32F, sobel_vertical)
borda_horizontal = cv2.filter2D(img_cinza, cv2.CV_32F, sobel_horizontal)

borda_final = cv2.sqrt(cv2.pow(borda_vertical,2) + cv2.pow(borda_horizontal, 2))


# converter para uint8 usando convertScaleAbs
# isso tira o valor absoluto e ajusta para a escala 0-255
cv2.imshow("img cinza", img_cinza)
cv2.imshow("vertical", cv2.convertScaleAbs(borda_vertical))
cv2.imshow("horizontal", cv2.convertScaleAbs(borda_horizontal))
cv2.imshow("final", cv2.convertScaleAbs(borda_final))

cv2.waitKey(0)
cv2.destroyAllWindows()