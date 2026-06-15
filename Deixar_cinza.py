import cv2

piramides = cv2.imread(r"projetos_treinamento\Fotos\piramides.jpg")

cv2.namedWindow("piramides", cv2.WINDOW_NORMAL)
cv2.imshow("piramides", piramides)

#deixando cinza
#imagem cinza = funcao converter cor em (imagem original para funcao cor cinza)
piramides_cinza = cv2.cvtColor(piramides, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("piramides cinza", cv2.WINDOW_NORMAL)
cv2. imshow("piramide cinza", piramides_cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()