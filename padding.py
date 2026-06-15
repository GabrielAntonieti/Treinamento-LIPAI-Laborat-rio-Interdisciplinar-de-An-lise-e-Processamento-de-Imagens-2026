import cv2
import numpy as np

img = cv2.imread("projetos_treinamento\Fotos\yumi.jpg", cv2.IMREAD_GRAYSCALE)
altura, largura = img.shape

# quantos pixels na borda
p = 100

# Novos tamanhos:
nova_altura = altura + 2*p
nova_largura = largura + 2*p

# =============================================================================================

# METODO 1: CONSTANT (Preenche as bordas com um valor fixo)
def padding_constant(img, p, valor_borda = 0):
    # Cria a imagem nova já pré-preenchida com o valor da borda
    img_pad = np.full((nova_altura, nova_largura), valor_borda, dtype=np.uint8)

    # copia a img nessa nova img_pad pulando o valor de p para manter a borda
    for i in range(altura):
        for j in range (largura):
            img_pad[i+p, j+p] = img[i,j]

    return img_pad
# =============================================================================================

# METODO 2: REPLICATE (Repete o pixel da extremidade mais próxima)
def padding_replicate(img, p):
    img_pad = np.zeros((nova_altura, nova_largura), dtype=np.uint8)

    for i in range(nova_altura):
        for j in range(nova_largura):
            # Limita os índices para que eles fiquem travados nas extremidades da imagem original
            orig_i = max(0, min(i - p, altura - 1))
            orig_j = max(0, min(j - p, largura - 1))

            img_pad[i, j] = img[orig_i, orig_j]

    return img_pad
# =============================================================================================

# METODO 3: REFLECT (Espelha incluindo o pixel da borda)
def padding_reflect(img, p):
    img_pad = np.zeros((nova_altura, nova_largura), dtype=np.uint8)

    for i in range(nova_altura):
        for j in range(nova_largura):
            # Lógica para rebater o índice caso ele saia da imagem original
            orig_i = i - p
            if orig_i < 0:
                orig_i = -orig_i - 1  # Espelha para cima
            elif orig_i >= altura:
                orig_i = 2 * altura - orig_i - 1  # Espelha para baixo
                
            orig_j = j - p
            if orig_j < 0:
                orig_j = -orig_j - 1  # Espelha para a esquerda
            elif orig_j >= largura:
                orig_j = 2 * largura - orig_j - 1  # Espelha para a direita
                
            img_pad[i, j] = img[orig_i, orig_j]
            
    return img_pad
# =============================================================================================
# METODO 4: REFLECT 101 / DEFAULT (Espelha sem o pixel da borda)

def padding_reflect101(img, p):
    img_pad = np.zeros((nova_altura, nova_largura), dtype=np.uint8)
    
    for i in range(nova_altura):
        for j in range(nova_largura):
            # mesma lógica do método 3, mas muda o 1 para 0 ou 2 (casos)
            orig_i = i - p
            if orig_i < 0:
                orig_i = -orig_i - 0  # Espelha para cima (1 -> 0)
            elif orig_i >= altura:
                orig_i = 2 * altura - orig_i - 2  # Espelha para baixo (1 -> 2)
                
            orig_j = j - p
            if orig_j < 0:
                orig_j = -orig_j - 0 # Espelha para a esquerda (1 -> 0)
            elif orig_j >= largura:
                orig_j = 2 * largura - orig_j - 2 # Espelha para a direita (1 -> 2)
                
            img_pad[i, j] = img[orig_i, orig_j]
            
    return img_pad
# =============================================================================================
# Executando
img_constant = padding_constant(img, p)
img_replicate = padding_replicate(img, p)
img_reflect = padding_reflect(img, p)
img_reflect101 = padding_reflect101(img, p)

cv2.imshow("Original", img)
cv2.imshow("1. Constant Manual", img_constant)
cv2.imshow("2. Replicate Manual", img_replicate)
cv2.imshow("3. Reflect Manual", img_reflect)
cv2.imshow("4. Reflect101 Manual", img_reflect101)

cv2.waitKey(0) 
cv2.destroyAllWindows() 