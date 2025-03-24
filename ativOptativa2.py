import cv2

# Carregar a imagem
imagem = cv2.imread("gramado.jpg")

# A - Desenhar um retângulo na margem interna da imagem com a distância de 10px e cor azul
altura, largura = imagem.shape[:2]
margem = 10  # Margem de 10px
cv2.rectangle(imagem, (margem, margem), (largura - margem, altura - margem), (255, 0, 0), 2)

# B - Aplicar um círculo com raio de 200px no centro da imagem e cor vermelha
centro = (largura // 2, altura // 2)
raio = 200
cv2.circle(imagem, centro, raio, (0, 0, 255), 1)

# C - Aplicar um círculo com raio de 50px no centro do círculo anterior e cor verde
raio_interno = 50
cv2.circle(imagem, centro, raio_interno, (0, 255, 0), -1)

# D - Escrever "Engenharia de Software" no canto inferior direito da imagem na cor preta
texto = "Engenharia de Software"
fonte = cv2.FONT_HERSHEY_SIMPLEX
tamanho_fonte = 1
espessura = 2
text_size = cv2.getTextSize(texto, fonte, tamanho_fonte, espessura)[0]
text_x = largura - text_size[0] - 10  # Coloca o texto no canto inferior direito
text_y = altura - 10
cv2.putText(imagem, texto, (text_x, text_y), fonte, tamanho_fonte, (0, 0, 0), espessura)

# Mostrar a imagem final
cv2.imshow('Imagem Modificada', imagem)

# Aguardar a tecla 'q' para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
