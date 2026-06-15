# deteccao de borda com o Operador Laplaciano
# gera bordas muito finas (1 pixel)
# sensível a ruídos
"""
cv2.Laplacian(src, ddepth, ksize)
src = variavel cinza da imagem
ddepth = quant de bytes
ksize = tamanho da abertura da segunda derivada (opicional)
"""

# deteccao de borda com o Operador Canny
# gera bordas muito finas (1 pixel)
# segue a uma lógica parecida com laplace mas pega as borda fracas melhor
# menos sensível
"""
cv2.Canny(src, threshold1, threshold2, L2gradient)
src = variavel cinza da imagem
threshold1 / threshold2: Os dois valores de limiar para a Histerese

L2gradient (Opcional): Booleano.
Se True, usa uma fórmula mais precisa para o cálculo da magnitude do gradiente.
Se False, usa uma aproximação mais rápida (soma absoluta).
"""

import cv2

img = cv2.imread(r"projetos_treinamento\Fotos\piramides.jpg")
img_cinza =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# laplaciano
laplacian = cv2.Laplacian(img_cinza, cv2.CV_64F)

# Canny
canny = cv2.Canny(img_cinza, 100, 100)

cv2.imshow("img cinza", img_cinza)
cv2.imshow("laplacinao ", laplacian)
cv2.imshow("canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()