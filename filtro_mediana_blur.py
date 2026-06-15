import cv2

# N = 15   # Tamanho da Matriz (ímpar) - Deixei 3 para rodar mais rápido no laço for
N = int(input("Digite um número inteiro: "))

lateral = N // 2    # Quantos pixels olhar para cada lado
area = N * N

piramides = cv2.imread(r"projetos_treinamento\Fotos\piramides.jpg")

piramides_cinza = cv2.cvtColor(piramides, cv2.COLOR_BGR2GRAY)

# Função pronta de MEDIANA do OpenCV para comparar (o equivalente ao cv2.blur)
piramides_median_funcao = cv2.medianBlur(piramides_cinza, N)

# na mao
# Faz uma cópia da imagem original
piramides_mediana = piramides_cinza.copy()

# Descobre a altura e largura da imagem
altura, largura = piramides_cinza.shape

# Começa na lateral e para antes da borda para não ler fora
for i in range(lateral, altura - lateral):
    for j in range(lateral, largura - lateral):
        
        # Criamos uma lista para guardar todos os vizinhos da janela N x N
        vizinhos = []

        # Varrer a matriz N x N ao redor do pixel atual [i, j]
        for k in range(-lateral, lateral + 1):
            for l in range(-lateral, lateral + 1):          
                pixel_vizinho = int(piramides_cinza[i + k, j + l])
                
                # Guardamos o pixel na nossa lista
                # append adiciona um elemento no final
                vizinhos.append(pixel_vizinho)
        
        # ORDENAMOS a lista do menor para o maior valor de cinza
        vizinhos.sort()
        
        # Pegamos o valor que ficou exatamente no MEIO da lista ordenada
        mediana = vizinhos[area // 2]
        
        # Aplicamos o resultado no pixel da imagem de saída
        piramides_mediana[i, j] = mediana

# Mostra os resultados na tela
cv2.imshow("Piramide Original Cinza", piramides_cinza)
cv2.imshow("Mediana Feita na Mao", piramides_mediana)
cv2.imshow("Mediana da Funcao", piramides_median_funcao)

# Sua estrutura de fechar com a tecla 'q'
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()