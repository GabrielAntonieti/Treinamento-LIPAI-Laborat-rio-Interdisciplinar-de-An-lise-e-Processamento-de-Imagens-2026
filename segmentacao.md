1. Limiarização (Thresholding) (Imagem cinza):
    - Deixa a imagem branca e preta baseado em uma tonalidade de cinza
    - Exemplo: tom(127):
        - Pixels > 127 ficam brancos 
        - pixels <= 127 ficam pretos
    - Função no OpenCV: cv2.threshold() ou cv2.adaptiveThreshold() (para imagens com iluminação irregular).
    # Exemplo:
        cv2.threshold(img_cinza, 127, 255, cv2.THRESH_BINARY)
            - img_cinza: imagem
            - 127: Parametro medio para limiarização
            - 255: Valor máximo para os pixels virarem 
            - cv2.THRESH_BINARY: Regra utilizada
    - Enxerga os objetos diferentes mas juntos como um só


2. Segmentação por Cores (Imagem HSV):
    - Define-se um limite inferior e um limite superior da cor que deseja capturar
    - O OpenCV cria uma máscara mantendo apenas os pixels que estão dentro desse intervalo
    # Exemplo:
        hsv = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2HSV)
        azul_baixo = np.array([100, 50, 50]) # Limite mais escuro / cinzento
        azul_alto = np.array([140, 255, 255]) # Limite mais claro / vivo

        #Cria uma máscara onde apenas o que é azul fica branco
        mascara_azul = cv2.inRange(hsv, azul_baixo, azul_alto) # Funciona tipo um if(está no raio dos limites)

3. Algoritmo Watershed (Divisor de Águas) (Separar os objetos juntos) (Imagem colorida[RGB/BGR]):
    - Separa os objetos por meio de uma "inuncação" feita na imagem cinza
    - Para inundar, a maquina detecta a diferença de "altura" da imagem
        - Escuros: Vales
        - Claros: picos

    # Passo a passo:
        - Aplica o filtro cinza
        - Limiariza (img cinza)
        - cv2.distanceTransform: Essa função calcula a distância de cada pixel branco até o pixel preto mais próximo
            - O centro dos objetos vira o ponto mais brilhante (o pico do relevo)
        -  Encontrar os Marcadores (onde vai inundar) (onde os objetos iguais se encontram)
        - Aplicar o Watershed (img colorida)
    # Exemplo: 
        # Binarização (Threshold de Otsu para separar fundo e objeto)
        thresh = cv2.threshold(img_cinza, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Descobrir o que é FUNDO garantido (Expandindo os objetos)
        fundo_garantido = cv2.dilate(abertura, kernel, iterations=3)

        # Descobrir o que é OBJETO garantido (Usando a Transformada de Distância)
        dist_transform = cv2.distanceTransform(abertura, cv2.DIST_L2, 5)
        objeto_garantido = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

        # Descobrir a região desconhecida (Onde eles se encostam)
        objeto_garantido = np.uint8(objeto_garantido)
        desconhecido = cv2.subtract(fundo_garantido, objeto_garantido)

        # Criar os Marcadores para a inundação
        marcadores = cv2.connectedComponents(objeto_garantido)
        marcadores = marcadores + 1     # Impede de ser 0 (igual a borda)
        marcadores[desconhecido == 255] = 0     # marcadores[desconhecido == 255] = 0

        # Aplicar o WATERSHED
        marcadores = cv2.watershed(img_colorida, marcadores)

        # O Watershed marca as linhas divisórias com o valor -1 na matriz de marcadores
        # Pinta-se essas linhas de vermelho na imagem original para ver o resultado:
        img_colorida[marcadores == -1] = [0, 0, 255]

        # Exibir o resultado
        cv2.imshow("Objetos Separados", img_colorida)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

4. Algoritmo GrabCut (Segmentação Baseada em Interação)
    - É um algoritmo para remoção de fundo
    - Desenha-se um polígono ao redor do objeto principal
    - O algoritmo analisa o que está dentro e fora do polígono (retângulo), estima os modelos de cor do fundo e do objeto, e faz uma segmentação refinada da silhueta
    - Função no OpenCV: cv2.grabCut()
       - Para o algoritmo funcionar, ele classifica cada pixel da imagem em uma de 4 categorias (rótulos):
            - cv2.GC_BGD (0): Fundo garantido (pixels fora da caixa)
            - cv2.GC_FGD (1): Objeto garantido
            - cv2.GC_PR_BGD (2): Provável Fundo (pixels dentro da caixa que se parecem com o fundo)
            - cv2.GC_PR_FGD (3): Provável Objeto (pixels dentro da caixa que se parecem com o objeto)
            No final, o GrabCut transforma tudo o que for "Provável" em "Garantido", gerando a máscara final

    # Exemplo: 

        # Matrizes internas que o algoritmo usa para guardar dados (obrigatórias)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        # Definir o Retângulo [X_inicial, Y_inicial, Largura, Altura]
        retangulo = (50, 50, 450, 550)

        # Executar o GrabCut
        cv2.grabCut(img, mascara, retangulo, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT) 
            # O número 5 significa quantas vezes (iterações) o algoritmo vai refinar o corte

        # Filtrar a máscara resultante
        mascara_final = np.where((mascara == 2) | (mascara == 0), 0, 1).astype('uint8')

        # Multiplicar a máscara pela imagem original para recortar o fundo
        img_recortada = img * mascara_final[:, :, np.newaxis]