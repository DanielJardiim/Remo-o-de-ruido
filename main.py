import cv2
from matplotlib import pyplot as plt

# Lendo a imagem com ruido
img = cv2.imread('einsteinRuido.png')

# Aplicando o filtro de mediana da biblioteca OpenCV
# que é importada como cv2 e atribuindo a variavel einstein
# utilizando uma mascara 5x5
einstein = cv2.medianBlur(img,5)

# Codigo reponsavel por plotar a imagem original e 
# o resultado lado a lado
plt.subplot(1,2,1),plt.imshow(img),plt.title('Com Ruído')
plt.subplot(1,2,2),plt.imshow(einstein),plt.title('Sem Ruído')

plt.show()