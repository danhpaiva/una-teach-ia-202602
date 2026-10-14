import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras
from keras import layers

keras.utils.set_random_seed(0)
(x_tr, y_tr), (x_te, y_te) = keras.datasets.fashion_mnist.load_data()
x_tr, y_tr = x_tr[:2000], y_tr[:2000]            # so 2000 imagens de treino
x_te, y_te = x_te[:1000], y_te[:1000]
x_tr = x_tr[..., np.newaxis].astype("float32")
x_te = x_te[..., np.newaxis].astype("float32")

# 1) CNN pequena treinada do zero
do_zero = keras.Sequential([
    layers.Input(shape=(28, 28, 1)), layers.Rescaling(1 / 255),
    layers.Conv2D(32, 3, activation="relu"), layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu"), layers.MaxPooling2D(),
    layers.Flatten(), layers.Dense(10, activation="softmax")])
do_zero.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
                metrics=["accuracy"])
do_zero.fit(x_tr, y_tr, epochs=10, batch_size=64, verbose=0)
acc_zero = do_zero.evaluate(x_te, y_te, verbose=0)[1]

# 2) MobileNetV2 pre-treinada (ImageNet) e congelada + uma camada nova
base = keras.applications.MobileNetV2(input_shape=(96, 96, 3), include_top=False,
                                      weights="imagenet", pooling="avg")
base.trainable = False
entrada = layers.Input(shape=(28, 28, 1))
x = layers.Resizing(96, 96)(entrada)
x = layers.Concatenate()([x, x, x])                 # 1 canal -> 3 canais
x = layers.Rescaling(1 / 127.5, offset=-1)(x)       # pixels de 0-255 para -1 a 1
x = base(x, training=False)
saida = layers.Dense(10, activation="softmax")(x)
transfer = keras.Model(entrada, saida)
transfer.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
                 metrics=["accuracy"])
transfer.fit(x_tr, y_tr, epochs=5, batch_size=64, verbose=0)
acc_transfer = transfer.evaluate(x_te, y_te, verbose=0)[1]

print("treino: 2000 imagens | teste: 1000 imagens")
print("CNN do zero      :", round(acc_zero, 3))
print("transfer learning:", round(acc_transfer, 3))
print("parametros treinaveis (transfer):",
      int(sum(np.prod(w.shape) for w in transfer.trainable_weights)))
