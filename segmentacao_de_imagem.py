import cv2
import numpy as np

img_colorida = cv2.imread(r"projetos_treinamento\Fotos\yumi.jpg")
img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

# =====================================================================
# METODO 1: Limiarização Binária (Thresholding)
# =====================================================================
def segmentar_threshold(imagem_cinza, valor_limiar=127):
    _, seg_binaria = cv2.threshold(imagem_cinza, valor_limiar, 255, cv2.THRESH_BINARY)
    return seg_binaria

# =====================================================================
# METODO 2: Segmentação por Cores (Espaço HSV)
# =====================================================================
def segmentar_por_cor_hsv(imagem_colorida):
    # Converter para HSV
    hsv = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2HSV)
    
    # Definição dos limites para o Amarelo
    amarelo_baixo = np.array([20, 100, 100])
    amarelo_alto  = np.array([32, 255, 255])
    
    # Cria a máscara onde apenas o raio da cor selecionada vira branco
    mascara_amarelo = cv2.inRange(hsv, amarelo_baixo, amarelo_alto)
    return mascara_amarelo

# =====================================================================
# METODO 3: Algoritmo Watershed (Divisor de Águas)
# =====================================================================
def segmentar_watershed(imagem_colorida, imagem_cinza):
    # Copia a imagem para não alterar a original externa
    img_resultado = imagem_colorida.copy()
    
    # 1. Binarização usando o Threshold de Otsu automático
    _, thresh = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 2. Remoção de ruídos básicos
    kernel = np.ones((3, 3), np.uint8)
    abertura = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # 3. Mapeamento de Fundo e Objeto garantidos
    fundo_garantido = cv2.dilate(abertura, kernel, iterations=3)
    
    dist_transform = cv2.distanceTransform(abertura, cv2.DIST_L2, 5)
    _, objeto_garantido = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    
    # 4. Região de fronteira (desconhecida)
    objeto_garantido = np.uint8(objeto_garantido)
    desconhecido = cv2.subtract(fundo_garantido, objeto_garantido)
    
    # 5. Criação e ajuste dos Marcadores para a inundação
    _, marcadores = cv2.connectedComponents(objeto_garantido)
    marcadores = marcadores + 1
    marcadores[desconhecido == 255] = 0
    
    # 6. Aplicação do Watershed
    marcadores = cv2.watershed(img_resultado, marcadores)
    
    # Pinta as linhas divisórias encontradas (-1) de vermelho na imagem
    img_resultado[marcadores == -1] = [0, 0, 255]
    return img_resultado


# =====================================================================
# METODO 4: Algoritmo GrabCut (Interativo / Remoção de Fundo)
# =====================================================================
def segmentar_grabcut(imagem_colorida):
    # Cria uma máscara vazia do mesmo tamanho da imagem
    mascara = np.zeros(imagem_colorida.shape[:2], np.uint8)
    
    # Matrizes internas temporárias exigidas pelo GrabCut
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    
    # Define o retângulo de corte: (X_inicial, Y_inicial, Largura, Altura)
    altura, largura = imagem_colorida.shape[:2]
    retangulo = (10, 10, largura - 10*2, altura - 10*2) # Cria uma margem padrão de 10px nas bordas por exemplo
    
    # Executa o algoritmo com 5 iterações de refinamento
    cv2.grabCut(imagem_colorida, mascara, retangulo, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    
    # Filtra a máscara: Mantém apenas Objeto Garantido (1) e Provável Objeto (3)
    mascara_final = np.where((mascara == 2) | (mascara == 0), 0, 1).astype('uint8')
    
    # Recorta o fundo aplicando a máscara de volta na imagem colorida
    img_recortada = imagem_colorida * mascara_final[:, :, np.newaxis]
    return img_recortada


# =====================================================================
# BLOCO DE EXECUÇÃO E TESTES
# =====================================================================
if __name__ == "__main__":
    
    # Executa cada uma das funções criadas acima
    resultado_thresh = segmentar_threshold(img_cinza, valor_limiar=127)
    resultado_hsv = segmentar_por_cor_hsv(img_colorida)
    resultado_watershed = segmentar_watershed(img_colorida, img_cinza)
    resultado_grabcut = segmentar_grabcut(img_colorida)
    
    cv2.imshow("Original Base (Cinza)", img_cinza)
    cv2.imshow("1. Resultado Threshold", resultado_thresh)
    cv2.imshow("2. Resultado HSV (Amarelo)", resultado_hsv)
    cv2.imshow("3. Resultado Watershed", resultado_watershed)
    cv2.imshow("4. Resultado GrabCut", resultado_grabcut)

    cv2.waitKey(0)
    cv2.destroyAllWindows()