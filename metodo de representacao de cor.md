1. # RGB
    - R: Red
    - G: Grren
    - B: Blue

    + Escala:
        - O modelo utiliza uma escala de 3 canais (R, G, B) em que cada um vai até 255, sendo que:
            - Branco: Os três em 255
            - Preto: Os três em 0

==========================================================================================================================
==========================================================================================================================

2. # BGR
    - B: Blue
    - G: Grren
    - R: Red

    + Escala:
        - O modelo utiliza uma escala de 3 canais (R, G, B) em que cada um vai até 255, sendo que:
            - Branco: Os três em 255
            - Preto: Os três em 0

    + Utilizado no OpenCV por causa que era utilizado antigamente devido às máquinas ultrapassadas e foi mantida hoje em dia
    + Problema: ao ler direto com o cv2 as cores ficam invertidas, sendo necessário converter com:
        - img_correta = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    
==========================================================================================================================
==========================================================================================================================

3. # Escala de Cinza (Grayscale)
    - Mantém apenas o brilho (Luminância) da imagem
    - Para transformar na escala cinza basta fazer uma média simples: Ciza = {(R+G+B)/3}, entretanto para optimizar a transformação por causa do olho humano ver mais o Verde do que o Azul, utiliza-se uma média ponderada (padrão ITU-R BT.601):
        - Cinza = (0.299 * R) + (0.587 * G) + (0.114 * B)

    + Escala:
        - Preto: 0
        - Branco: 255

    + Utilizado no processamento de imagem, possibilitando aplicar algorítimos, acelerar o processamento e diminuir custos

==========================================================================================================================
==========================================================================================================================

4. # HSV
    - H (Hue / Matiz): A própria cor em escala matemática
        - Matematicamente, ela funciona como um círculo de ângulo de 0° a 360°
        - No OpenCV, como o valor máximo de um pixel de 8 bits é 255, eles dividiram esse círculo por 2, então o canal H varia de 0 a 180

        + Escalas:
        - Vermelho: 0 a 10 (e também de 171 a 180, porque o círculo fecha em si mesmo)
        - Laranja: 11 a 25 
        - Amarelo: 26 a 35
        - Verde: 36 a 85
        - Azul: 86 a 130
        - Violeta/Roxo: 131 a 170

    -  S (Saturation / Saturação): É a pureza ou vivacidade da cor. Vai de 0 a 255
        - Um valor perto de 0 é uma cor "desbotada" (cinzenta), e perto de 255 é uma cor viva e neon

    - [V] (Value / Valor): É o brilho da imagem. Vai de 0 (totalmente escuro/preto) a 255 (totalmente brilhante/claro)

    + Utilizado em visão computacional, Controle de Qualidade Industrial e Automação, Editores de Imagem e Design Gráfico, Processamento de Imagens Médicas e Biológicas, Indústria Têxtil e de Tintas

==========================================================================================================================
==========================================================================================================================

5. # HSI
    - H (Hue): Idêntico ao HSV
        - vermelho: 0°/360°
        - verde: 120°
        - azul: 240°
    - S (Saturation): Mede o quão distante a cor está do eixo central cinza, a menor entre as r,g,b normalizadas (r,g,b/255)
        > S = 1 - (min(r,g,b)) / I  
    - [I] (Intensity): É a média aritmética simples dos canais: Intensidade = {(R+G+B)/3}

    + Utlizado no aprimoramento de imagem, técnicas de filtragem de frequência, análise de imagens de satélite, reconstruindo a luz para ficar mais fiel, diferente do RGB

==========================================================================================================================
==========================================================================================================================

6. # HLS
    - H (Hue): Idêntico ao HSV
    - [L] (Lightness): gerencia a quantidade de Branco ou Preto injetada na cor, variando de 0 a 255
        - L = 127 (Metade): É a Cor pura e perfeita. Na metade da escala, você tem o tom mais vívido possível da matiz escolhida.
    - S (Saturation): Mede o quão distante a cor está do eixo central cinza

    + Utilizado em Iluminação e Sombras em Linhas de Trânsito, Edição de Fotos Profissional, Equalização de Histograma Colorido

==========================================================================================================================
==========================================================================================================================

7. # Escalas de Tons de Cinza Médicos (DICOM, HU e Windowing)
    - Escala utilizada em equipamentos médicos, os quais salvam imagens em [.dcm] (DICOM) para averiguar com precisão as imagens obtidas, utilizando 12 ou 16 pixel, com isso, é possível ter uma variação de 4096 a 65536 tons de cinza
    + Escala:
        - -1000 HU: Ar (totalmente preto)
        -  +20 HU a +80 HU: Tumores e Sangramentos
        - 0 HU: Água destilada
        - +100 a +300 HU: Contraste iodado
        - +200 a +1000 HU: Tecido ósseo (totalmente branco)

    + # Técnica de Janelamento (Windowing)
        - Recorta a imagem para focar apenas no que importa para o diagnóstico, utilizando dois processos:
            - Window Width (WW / Largura da Janela): Quantos tons da escala HU nós vamos focar
            - Window Level (WL / Nível ou Centro da Janela): Qual é o centro da densidade que queremos estudar

        - Para fazer esse recorte é necessário programar 3 janelas:
            - Janela de Tecido Mole / Cérebro (Ex: WW: 80, WL: 40):
                - Destaca AVCs, tumores cerebrais e sangramentos
                - Todo o osso do crânio vira branco, o ar vira preto, e o cérebro ganha contraste

        - Janela de Osso (Ex: WW: 2000, WL: 500):
            - Ignora o cérebro (que vira um borrão) para focar em encontrar microfraturas no crânio

        - Janela de Pulmão (Ex: WW: 1500, WL: -600):
            - Como o pulmão é cheio de ar, a janela é jogada lá para os valores negativos da escala, permitindo que veja a textura interna dos alvéolos e detecte casos como a pneumonia, nódulos ou enfisema
        
    + Assim é possível converter as imagens de (-1000 HU a +1000 HU) para (0 a 255)
        +----------------------------------------------------------------------------------+
        |  Mundo Médico (DICOM 16 bits)  ===>  Janelamento  ===>  Mundo IA (OpenCV 8 bits) |
        |      (-1000 HU a +1000 HU)             (WW / WL)             (0 a 255)           |
        +----------------------------------------------------------------------------------+

    
    + # Conversão de profundidade de 8 para 16/12 bits (Expansão / Upscaling):
        - Para 12 bits: (4095/255) = 16.05
        - para 16 bits: (65535/255) = 257.0
            - Basta multipliar o valor do bit cinza (0 a 255) pelo desejado (16.05 ou 257.0)
    
    + # Conversão de profundidade de 16/12 para 8 bits (Compressão / Downscaling):
        - Definir o valor Mínimo e o Máximo da janela:
            > Mínimo (Limite Inferior): Min = WL - (WW/2)
            > Máximo (Limite Superior): Max = WL + (WW/2)
        - Aplicar a fórmula:
            > Pixel(8bits) = [ (Pixel12/16bits - Min) / (Max - Min) ] *255
