import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras
from keras import layers

(x_tr, y_tr), (x_te, y_te) = keras.datasets.mnist.load_data()
x_tr = (x_tr[:1000] / 255.0)[..., np.newaxis]     # so 1000 exemplos de treino
y_tr = y_tr[:1000]
x_te = (x_te / 255.0)[..., np.newaxis]

def construir(dropout=0.0, aumento=False):
    camadas = [layers.Input(shape=(28, 28, 1))]
    if aumento:
        camadas += [layers.RandomRotation(0.08), layers.RandomTranslation(0.1, 0.1)]
    camadas += [layers.Conv2D(32, 3, activation="relu"), layers.MaxPooling2D(),
                layers.Conv2D(64, 3, activation="relu"), layers.MaxPooling2D(),
                layers.Flatten(), layers.Dropout(dropout),
                layers.Dense(10, activation="softmax")]
    m = keras.Sequential(camadas)
    m.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
    return m

casos = (("sem regularizacao", {}), ("dropout 0.5", {"dropout": 0.5}),
         ("aumento de dados", {"aumento": True}))
for nome, kw in casos:
    keras.utils.set_random_seed(0)
    m = construir(**kw)
    h = m.fit(x_tr, y_tr, epochs=15, batch_size=32, verbose=0)
    acc_te = m.evaluate(x_te, y_te, verbose=0)[1]
    print(nome, "| treino", round(h.history["accuracy"][-1], 3),
          "| teste", round(acc_te, 3))
