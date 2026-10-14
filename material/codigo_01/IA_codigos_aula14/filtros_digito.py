import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras
from conv_manual import convolucao

(x_tr, y_tr), _ = keras.datasets.mnist.load_data()
img = x_tr[0] / 255.0                         # o primeiro digito do treino: um 5
vertical = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
horizontal = vertical.T
bordas_v = convolucao(img, vertical)
bordas_h = convolucao(img, horizontal)
print("imagem:", img.shape, " mapa de bordas:", bordas_v.shape)
print("maior resposta vertical  :", round(float(bordas_v.max()), 2))
print("maior resposta horizontal:", round(float(bordas_h.max()), 2))
print("pixels com resposta forte (> 1.5): vertical",
      int((np.abs(bordas_v) > 1.5).sum()), " horizontal", int((np.abs(bordas_h) > 1.5).sum()))
