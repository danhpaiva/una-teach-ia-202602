import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras

(x_tr, y_tr), (x_te, y_te) = keras.datasets.mnist.load_data()
print("treino:", x_tr.shape, y_tr.shape, " teste:", x_te.shape)
print("tipo:", x_tr.dtype, " minimo:", x_tr.min(), " maximo:", x_tr.max())
print("rotulos de 0 a 9; primeiros 10:", y_tr[:10].tolist())
print("exemplos por classe (treino):", np.bincount(y_tr).tolist())

x_tr = x_tr.astype("float32") / 255.0
x_te = x_te.astype("float32") / 255.0
print("depois de normalizar:", x_tr.min(), x_tr.max())
x_tr = x_tr[..., np.newaxis]               # (60000, 28, 28, 1): 1 canal
print("forma para a CNN:", x_tr.shape)
