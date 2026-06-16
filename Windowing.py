import cv2
import numpy as np

raiox = cv2.imread(r"projetos_treinamento\Fotos\raio_x_pneumonia.jpg")

if raiox is None:
    print("Erro: Imagem não encontrada.")
else:
    img_cinza = cv2.cvtColor(raiox, cv2.COLOR_BGR2GRAY)

    # =====================================================================
    # PASSO 1: EXPANSÃO PARA 16 BITS (Upscaling Simulado)
    # =====================================================================
    img_16bits = img_cinza.astype(np.uint16) * 257

    # =====================================================================
    # PASSO 2: JANELAMENTO E DOWN SCALING (16 bits -> 8 bits)
    # =====================================================================
    # Como não temos as Unidades Hounsfield (HU) reais de Tomografia,
    # vamos criar limites matemáticos fictícios na escala de 0 a 65535.
    # O objetivo é ignorar os ossos muito brancos e focar no tecido mole do pulmão.
    Min = 20000  # Corta tons escuros (ar do fundo)
    Max = 45000  # Corta tons extremamente claros (ossos densos)

    # Aplica o corte (Clamping) e a fórmula das suas anotações:
    # Pixel(8bits) = [ (Pixel16bits - Min) / (Max - Min) ] * 255
    img_janelada = np.clip(img_16bits, Min, Max)
    img_8bits_focada = (((img_janelada - Min) / (Max - Min)) * 255).astype(np.uint8)

    # =====================================================================
    # PASSO 3: SEGMENTAÇÃO (Detectando a Pneumonia)
    # Limiarização (Thresholding)
    # =====================================================================
    # A pneumonia se manifesta como "manchas" (opacidades) brilhantes.
    # Pegar a imagem focada e transformar tudo o que for mais brilhante ue 140 em BRANCO (255) e o resto em PRETO (0).
    _, mascara_pneumonia = cv2.threshold(img_8bits_focada, 140, 255, cv2.THRESH_BINARY)

    # =====================================================================
    # PASSO 4: EXIBIÇÃO VISUAL (Pintando em BGR)
    # =====================================================================
    # Criamos uma cópia da imagem original para não estragá-la.
    resultado = raiox.copy()
    
    # Onde a máscara for branca (255), pintamos o pixel de Vermelho no BGR (0, 0, 255)
    resultado[mascara_pneumonia == 255] = [0, 0, 255]

    # Exibe as etapas
    cv2.imshow("01. Original (Cinza)", img_cinza)
    cv2.imshow("02. Simulacao de Janelamento (Foco no pulmao)", img_8bits_focada)
    cv2.imshow("03. Deteccao da Pneumonia", resultado)

    cv2.waitKey(0)
    cv2.destroyAllWindows()