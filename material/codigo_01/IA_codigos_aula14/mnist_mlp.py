import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import json
import keras
from keras import layers

keras.utils.set_random_seed(0)
(x_tr, y_tr), (x_te, y_te) = keras.datasets.mnist.load_data()
x_tr, x_te = x_tr / 255.0, x_te / 255.0

modelo = keras.Sequential([
    layers.Input(shape=(28, 28)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax"),
])
modelo.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])
print("parametros:", modelo.count_params())
hist = modelo.fit(x_tr, y_tr, epochs=5, batch_size=128,
                  validation_split=0.1, verbose=0)
for ep in range(5):
    print("epoca", ep + 1, "acc", round(hist.history["accuracy"][ep], 4),
          "val_acc", round(hist.history["val_accuracy"][ep], 4))
perda, acc = modelo.evaluate(x_te, y_te, verbose=0)
print("teste: perda", round(perda, 4), "acuracia", round(acc, 4))
json.dump(hist.history, open("hist_mlp.json", "w"))
