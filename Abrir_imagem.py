import cv2

# Como achar a imagem:
# variavel = biblioteca.funcao(r"CAMINHO DA IMAGEM")
dg = cv2.imread(r"Fotos\dg_xadrez.jpg")
love = cv2.imread(r"Fotos\Love.jpg")


# Passo a passo:
# Ajustar a imagem
cv2.namedWindow("Dragao joga xadrez", cv2.WINDOW_NORMAL) #ajusta no monitor
cv2.namedWindow("Eu e a gabizinha", cv2.WINDOW_NORMAL) #ajusta no monitor


# Exibir a imagem
# biblioteca.funcao("TITULO", nome da varialvel) --- tipo um printf
cv2.imshow("Dragao joga xadrez", dg) # Abre uma janela
cv2.imshow("Eu e a gabizinha", love) # Abre uma janela


# sistem pause
cv2.waitKey(0) # Espera qlqr tecla ser precionada
#sistem close
cv2.destroyWindow("Dragao joga xadrez") # Fecha a janela do dg aberta

cv2.waitKey(0) # Espera qlqr tecla ser precionada
cv2.destroyWindow("Eu e a gabizinha") # Fecha a janela do love aberta

#cv2.destroyAllWindows() # Fecha TODAS as janelas abertas
