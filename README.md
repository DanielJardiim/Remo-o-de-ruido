# Remocao-de-ruido
Noise Removal

Se tratando de incrementar consideravelmente a qualidade dos arquivos de imagem obtidos, podemos utilizar algoritmos que permitam tratar determinadas regiões corrompidas da imagem; as vezes por falha na transmissão, por excesso de brilho, altas temperaturas ou outros motivos, com isso são gerados ruídos que são um dos principais problemas relacionados.

O uso de máscaras espaciais no processamento de imagens é normalmente denominado filtragem espacial (em contraste com a expressão filtragem no domínio da frequência, utilizada quando se opera sobre a transformada de Fourier da imagem original) e as máscaras são conhecidas como filtros espaciais. A suavização de imagens no domínio espacial baseia-se no uso de máscaras de convolução adequadas para o objetivo em questão, normalmente o borramento da imagem (para eliminar detalhes que não são de interesse para as etapas subsequentes do processamento) ou a remoção de ruídos nela presentes. Dentre as técnicas mais conhecidas de suavização estão a filtragem pela média e o filtro da mediana.

Um exemplo utilizando o filtro da mediana é:
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

Esse foi só um exemplo de como a a biblioteca OpenCv pode ser utilizada com a linguagem Python para processamento digital de imagens, existem vários outros exemplos. A biblioteca se mostra uma ótima opção para processamento de imagens digitais e aliada a linguagem de programação Python, torna o desenvolvimento mais rápido e produtivo como podemos ver com o exemplo dado onde foram geradas pouquissimas linhas de código para a implementação.
