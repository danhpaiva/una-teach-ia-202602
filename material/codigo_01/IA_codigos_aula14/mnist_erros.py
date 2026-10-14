import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras

(_, _), (x_te, y_te) = keras.datasets.mnist.load_data()
x_te = (x_te / 255.0)[..., np.newaxis]
modelo = keras.models.load_model("mnist_cnn.keras")

prob = modelo.predict(x_te, verbose=0)
pred = prob.argmax(axis=1)
erros = np.where(pred != y_te)[0]
print("erros:", len(erros), "de", len(y_te))

pares = {}
for i in erros:
    pares[(int(y_te[i]), int(pred[i]))] = pares.get((int(y_te[i]), int(pred[i])), 0) + 1
print("confusoes mais comuns (real -> previsto: quantas):")
for (real, prev), q in sorted(pares.items(), key=lambda kv: -kv[1])[:5]:
    print(" ", real, "->", prev, ":", q)

confianca = prob.max(axis=1)
print("confianca media nos acertos:", round(float(confianca[pred == y_te].mean()), 3))
print("confianca media nos erros  :", round(float(confianca[erros].mean()), 3))
