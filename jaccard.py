"""
O indice de jaccardd mede a similiaridade de dois conjuntos de dados, sendo escrito em quatro formas diferentes:
    - Indice = (Elementos iguais em A e B) / (Todos elementos de A e B sem repetir) 
    - Indice = (intersecção de A e B) / (União de A e B)
    - Indice = (Elementos em Comum) ÷ (Total de Elementos Únicos Combinados)
    - Indice = X / (Y-X)
        - X = Elementos iguais em A e B
        - Y = Todos elementos de A + Todos elementos de B
Resultando em 0 a 1 (0% a 100%)

em [.py] é implementado por:
    - Uma lista dada por [set]
        - conjunto_a = set(lista1)
    - Calcula a interseção [&] e a união [|]
        - intersecao = len(conjunto_a & conjunto_b)
        - uniao = len(conjunto_a | conjunto_b)
"""

import cv2
import numpy as np

def indice_jaccard_lista_simples(lista1, lista2):
    #convertendo listas em conjuntos
    conjunto_a = set(lista1)
    conjunto_b = set(lista2)

    # Calcula a interseção e a união
    intersecao = len(conjunto_a & conjunto_b)
    uniao = len(conjunto_a | conjunto_b)

    # retorna o índice pela formula
    return intersecao / uniao

def indice_jaccard_imagem(img1, img2):
    # Cria uma lista de tuplas: (cor_do_pixel, linha, coluna)
    linhas, colunas = img1.shape
    
    conjunto_a = set(
        #   1. O que guardar   |       2. Loop das Linhas     |    3. Loop das Colunas
        (img1[i, j], i, j) for i in range(linhas) for j in range(colunas)
        # img1[i, j]: Pega o valor da cor (de 0 a 255)
        # i e j: São as coordenadas exatas daquele pixel
    )
    conjunto_b = set(
        (img2[i, j], i, j) for i in range(linhas) for j in range(colunas)
    )
    
    intersecao = len(conjunto_a & conjunto_b)
    uniao = len(conjunto_a | conjunto_b)
    
    return intersecao / uniao

#Execução:
fruta1 = ["banana", "uva", "laranja", "pera"]
fruta2 = ["pera", "beringela", "melancia", "banana", "batata"]

similaridade = indice_jaccard_lista_simples(fruta1, fruta2)
print(f"Índice do exemplo das frutas: {similaridade:.2f} ({similaridade * 100:.1f}%)")

img_original = cv2.imread(r"projetos_treinamento\Fotos\bandeira_brasil_original.jpg", cv2.IMREAD_GRAYSCALE)
img_comparar = cv2.imread(r"projetos_treinamento\Fotos\bandeira_brasil.jpg", cv2.IMREAD_GRAYSCALE)

similaridade_bandeiras = indice_jaccard_imagem(img_original, img_comparar)
print(f"Índice do exemplo das bandeiras: {similaridade_bandeiras:.2f} ({similaridade_bandeiras * 100:.1f}%)")

cv2.imshow("Original", img_original)
cv2.imshow("Comparar", img_comparar)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
