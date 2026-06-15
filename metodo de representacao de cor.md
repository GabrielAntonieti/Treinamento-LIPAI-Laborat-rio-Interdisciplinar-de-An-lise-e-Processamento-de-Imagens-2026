HSV
    - H (Hue / Matiz): É a cor pura propriamente dita (se é vermelho, amarelo, verde, azul). Matematicamente, ela funciona como um círculo de ângulo de 0° a 360°.
        - No OpenCV, como o valor máximo de um pixel de 8 bits é 255, eles dividiram esse círculo por 2, então o canal H varia de 0 a 180.

    -  S (Saturation / Saturação): É a pureza ou vivacidade da cor. Vai de 0 a 255.
        - Um valor perto de 0 é uma cor muito "desbotada" (cinzenta), e perto de 255 é uma cor extremamente viva e neon.

    - V (Value / Valor): É o brilho da imagem. Vai de 0 (totalmente escuro/preto) a 255 (totalmente brilhante/claro)

    Escalas:
        - Vermelho: 0 a 10 (e também de 171 a 180, porque o círculo fecha em si mesmo)
        - Laranja: 11 a 25
        - Amarelo: 26 a 35
        - Verde: 36 a 85
        - Azul: 86 a 130
        - Violeta/Roxo: 131 a 170