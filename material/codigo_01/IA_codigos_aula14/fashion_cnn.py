import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras
from keras import layers

nomes = ["camiseta", "calca", "pulover", "vestido", "casaco",
         "sandalia", "camisa", "tenis", "bolsa", "bota"]
keras.utils.set_random_seed(0)
(x_tr, y_tr), (x_te, y_te) = keras.datasets.fashion_mnist.load_data()
x_tr = (x_tr / 255.0)[..., np.newaxis]
x_te = (x_te / 255.0)[..., np.newaxis]

modelo = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, 3, activation="relu"), layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu"), layers.MaxPooling2D(),
    layers.Flatten(), layers.Dropout(0.3),
    layers.Dense(10, activation="softmax"),
])
modelo.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])
modelo.fit(x_tr, y_tr, epochs=5, batch_size=128, validation_split=0.1, verbose=0)
prob = modelo.predict(x_te, verbose=0)
pred = prob.argmax(axis=1)
print("acuracia no teste:", round(float((pred == y_te).mean()), 4))
for c in range(10):
    acerto = float((pred[y_te == c] == c).mean())
    print(f"{nomes[c]:9s} {acerto:.3f}")
