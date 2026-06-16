import cv2
import math
import numpy as np

img_bgr = cv2.imread(r"projetos_treinamento\Fotos\yumi.jpg")

if img_bgr is None:
    print("Erro: Imagem não encontrada. Verifique o caminho!")
else:
    # BGR é o padrão do OpenCV
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)

    # =====================================================================================================================
    # RGB para HSI na mao
    altura, largura, canais = img_bgr.shape

    img_hsi = np.zeros((altura, largura, 3), dtype="uint8")

    for y in range(altura):
        for x in range(largura):
            
            # Pegar os canais inteiros (até 255)
            pixel = img_bgr[y, x]
            b_bruto = int(pixel[0])
            g_bruto = int(pixel[1])
            r_bruto = int(pixel[2])
            
            # Normalizando os valores para a escala [0.0, 1.0]
            b = b_bruto / 255.0
            g = g_bruto / 255.0
            r = r_bruto / 255.0

            # Calculo da Intensidade em cada pixel (media aritimetica simples)
            intensidade = (r + g + b) / 3.0

            # Calculo Satuação (menor intensidade enter cada um)
            min_rgb = min(r, g, b)

            # Se o pixel for totalmente preto, evita-se a divisão por zero
            if (r + g + b) == 0:
                saturacao = 0.0
            else:
                    saturacao = 1.0 - (3.0 / (r + g + b) * min_rgb)

            # Calculo Hue / Matriz
            numerador = ((r - g) + (r - b)) / 2 # Se o Vermelho for a cor predominante dará valores positivos bem altos
            denominador = math.sqrt((r - g)**2 + (r - b) * (g - b) + 1e-6) # Adicionamos 1e-6 (0.000001) para o "denominador" nunca ser zero

            theta = math.acos(numerador / denominador) # Calcula o ângulo em radianos e converte para graus
            hue_graus = math.degrees(theta)

            # Regra do HSI: Se o Azul for maior que o Verde, o ângulo faz a volta
            if b > g:
                hue = 360.0 - hue_graus
            else:
                hue = hue_graus

            # APLICAR O H, S, I NA NOVA IMAGEM
            h_final = int(hue / 2) # O Hue vai de 0 a 360. Dividimos por 2 para caber em 180 (padrão OpenCV)
            s_final = int(saturacao * 255) # A Saturação vai de 0.0 a 1.0. Multiplicamos por 255
            i_final = int(intensidade * 255) # A Intensidade vai de 0.0 a 1.0. Multiplicamos por 255

            img_hsi[y, x] = [h_final, s_final, i_final]

    # =====================================================================================================================

    # Exibição
    # Para o RGB, ele mostrará as cores trocadas (azul e vermelho invertidos)
    cv2.imshow("01. Original (BGR)", img_bgr)
    cv2.imshow("02. RGB (Invertido no OpenCV)", img_rgb)
    cv2.imshow("03. Escala de Cinza", img_gray)
    cv2.imshow("04. HSV", img_hsv)
    cv2.imshow("05. HLS", img_hls)
    cv2.imshow("06. Nova Imagem HSI Convertida na Mao", img_hsi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()