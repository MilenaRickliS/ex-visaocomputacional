import cv2

# Carregar a imagem
imagem = cv2.imread("gramado.jpg")
imagem2 = cv2.imread("gramado.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar filtro de média (blur normal)
imagem_blur = cv2.blur(imagem, (5, 5))

# Aplicar filtro Canny
bordas_canny = cv2.Canny(imagem2, 50, 100)

# Obter as dimensões originais da imagem
altura, largura = imagem.shape[:2]
print(f"Dimensões originais: {largura}x{altura}")

# Definir novas dimensões (exemplo: 50% do tamanho original)
largura_nova = int(largura * 0.5)
altura_nova = int(altura * 0.5)
dimensoes = (largura_nova, altura_nova)

# Redimensionar a imagem
imagem_redimensionada = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

# Mostrar as imagens
cv2.imshow("Filtro Blur", imagem_blur)
cv2.imshow("Imagem em Escala de Cinza", imagem2)
cv2.imshow("Canny", bordas_canny)
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Redimensionada", imagem_redimensionada)

# Salvar as imagens processadas
cv2.imwrite("filtro_blur.jpg", imagem_blur)
cv2.imwrite("filtro_cinza.jpg", imagem2)
cv2.imwrite("filtro_bordascanny.jpg", bordas_canny)
cv2.imwrite("filtro_redimensionar.jpg", imagem_redimensionada)


cv2.waitKey(0)
cv2.destroyAllWindows()