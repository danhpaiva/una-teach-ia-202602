"""Gabarito da Aula 14 - exercicios 1 a 4 (autocontido)."""
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras
from keras import layers


def saida_conv(n, k):
    return n - k + 1


def dense(n_in, n_out):
    return (n_in + 1) * n_out


def conv(k, c_in, filtros):
    return (k * k * c_in + 1) * filtros


print("Exercicio 1 (formas)")
n = saida_conv(28, 5)
print("apos Conv2D 5x5:", n, "x", n)
print("apos MaxPooling 2x2:", n // 2, "x", n // 2)

print("\nExercicio 2 (parametros)")
print("Conv2D(16, 5x5) em imagem RGB:", conv(5, 3, 16))
print("Dense(10) depois de Flatten (12x12x16):", dense(12 * 12 * 16, 10))

print("\nExercicio 3 (MLP contra CNN no Fashion-MNIST, 3 epocas)")
(x_tr, y_tr), (x_te, y_te) = keras.datasets.fashion_mnist.load_data()
x_tr = (x_tr / 255.0)[..., np.newaxis]
x_te = (x_te / 255.0)[..., np.newaxis]


def treinar(camadas, x, y, epocas=3):
    keras.utils.set_random_seed(0)
    m = keras.Sequential([layers.Input(shape=(28, 28, 1))] + camadas)
    m.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
    m.fit(x, y, epochs=epocas, batch_size=128, verbose=0)
    return m, m.evaluate(x_te, y_te, verbose=0)[1]


mlp = [layers.Flatten(), layers.Dense(128, activation="relu"),
       layers.Dense(10, activation="softmax")]
cnn = [layers.Conv2D(32, 3, activation="relu"), layers.MaxPooling2D(),
       layers.Conv2D(64, 3, activation="relu"), layers.MaxPooling2D(),
       layers.Flatten(), layers.Dense(10, activation="softmax")]
for nome, camadas in (("MLP", mlp), ("CNN", cnn)):
    m, acc = treinar(camadas, x_tr, y_tr)
    print(nome, "| parametros", m.count_params(), "| teste", round(acc, 3))

print("\nExercicio 4 (numero de filtros da 1a camada, 20000 imagens)")
for filtros in (8, 64):
    camadas = [layers.Conv2D(filtros, 3, activation="relu"), layers.MaxPooling2D(),
               layers.Flatten(), layers.Dense(10, activation="softmax")]
    m, acc = treinar(camadas, x_tr[:20000], y_tr[:20000])
    print(filtros, "filtros | parametros", m.count_params(), "| teste", round(acc, 3))
