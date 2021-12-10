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

Para remover sinais / ruídos indesejados, usamos filtros de diferentes tipos e especificações. Geralmente, na indústria, precisamos escolher o melhor ajuste testando-o com o sinal para localizar o melhor filtro a ser usado para remover o ruído em um determinado caso de uso.

Vamos implementar um filtro Lowpass Digital Butterworth para remover o sinal / ruído indesejado de uma combinação de ondas sinusoidais.
Utilizando esse código:


import numpy as np 
import scipy.signal as signal 
import matplotlib.pyplot as plt 

# definindo o sinal 
f1 = 25 
f2 = 50 
N = 10 
  
t = np.linspace(0, 1, 1000) 
sig = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) 

# plotando o sinal original com ruido
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True) 
ax1.plot(t, sig) 
ax1.set_title('25 Hz and 50 Hz sinusoids') 
ax1.axis([0, 1, -2, 2]) 
sos = signal.butter(50, 35, 'lp', fs=1000, output='sos') 
  
filtered = signal.sosfiltfilt(sos, sig) # filtragem do ruido 
  
# plotando o sinal original sem ruido
ax2.plot(t, filtered) 
ax2.set_title('After 35 Hz Low-pass filter') 
ax2.axis([0, 1, -2, 2]) 
ax2.set_xlabel('Time [seconds]') 
plt.tight_layout() 
plt.show()
