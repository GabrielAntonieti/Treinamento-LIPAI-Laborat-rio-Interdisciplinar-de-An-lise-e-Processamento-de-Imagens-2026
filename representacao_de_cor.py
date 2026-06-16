import cv2

img_bgr = cv2.imread(r"projetos_treinamento\Fotos\yumi.jpg")

if img_bgr is None:
    print("Erro: Imagem não encontrada. Verifique o caminho!")
else:
    # BGR é o padrão do OpenCV
    # HSI é igual ao HLS
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)

    # Exibição
    # Para o RGB, ele mostrará as cores trocadas (azul e vermelho invertidos)
    cv2.imshow("01. Original (BGR)", img_bgr)
    cv2.imshow("02. RGB (Invertido no OpenCV)", img_rgb)
    cv2.imshow("03. Escala de Cinza", img_gray)
    cv2.imshow("04. HSV", img_hsv)
    cv2.imshow("05. HLS", img_hls)

    cv2.waitKey(0)
    cv2.destroyAllWindows()