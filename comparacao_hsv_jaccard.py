import cv2
import math
import numpy as np

def indice_jaccard_imagem(img1, img2):
    if img1.shape != img2.shape:
        print("Erro: As imagens precisam ter o mesmo tamanho!")
        return 0.0

    linhas, colunas = img1.shape[:2]
    
    # Converte os pixels para tuplas para o set poder processar
    conjunto_a = set(
        (tuple(img1[i, j]) if img1.ndim == 3 else img1[i, j], i, j) 
        for i in range(linhas) for j in range(colunas)
    )
    conjunto_b = set(
        (tuple(img2[i, j]) if img2.ndim == 3 else img2[i, j], i, j) 
        for i in range(linhas) for j in range(colunas)
    )
    
    intersecao = len(conjunto_a & conjunto_b)
    uniao = len(conjunto_a | conjunto_b)
    
    return intersecao / uniao

# --- Carregamento da Imagem ---
img_bgr = cv2.imread(r"projetos_treinamento\Fotos\yumi.jpg")

if img_bgr is None:
    print("Erro: Imagem não encontrada. Verifique o caminho!")
else:
    # 1. HSV Nativo do OpenCV para comparação
    img_hsv_opencv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # 2. Construindo o HSV na mão
    altura, largura, canais = img_bgr.shape
    img_hsv_manual = np.zeros((altura, largura, 3), dtype="uint8")

    for y in range(altura):
        for x in range(largura):
            pixel = img_bgr[y, x]
            b_bruto, g_bruto, r_bruto = int(pixel[0]), int(pixel[1]), int(pixel[2])
            
            # Normalizando para [0.0, 1.0]
            b = b_bruto / 255.0
            g = g_bruto / 255.0
            r = r_bruto / 255.0

            # --- CANAL V (VALUE) ---
            value = max(r, g, b)

            # --- CANAL S (SATURATION) ---
            min_rgb = min(r, g, b)
            delta = value - min_rgb
            
            if value == 0:
                saturacao = 0.0
            else:
                saturacao = delta / value

            # --- CANAL H (HUE) ---
            if delta == 0:
                hue = 0.0
            elif value == r:
                hue = 60.0 * (((g - b) / delta) % 6)
            elif value == g:
                hue = 60.0 * (((b - r) / delta) + 2.0)
            elif value == b:
                hue = 60.0 * (((r - g) / delta) + 4.0)
                
            if hue < 0:
                hue += 360.0

            h_final = int(round(hue / 2))         
            s_final = int(round(saturacao * 255))  
            v_final = int(round(value * 255))     

            # Correção de limites para segurança e padronização do OpenCV
            h_final = min(180, max(0, h_final))
            if h_final == 180: 
                h_final = 0

            img_hsv_manual[y, x] = [h_final, s_final, v_final]

    similaridade = indice_jaccard_imagem(img_hsv_manual, img_hsv_opencv)
    
    print(f"Jaccard (Seu HSV Manual vs OpenCV HSV Nativo): {similaridade * 100:.2f}%")

    cv2.imshow("HSV Funcao", img_hsv_opencv)
    cv2.imshow("HSV Manual", img_hsv_manual)

    cv2.waitKey(0)
    cv2.destroyAllWindows()