import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import keras
from conv_manual import convolucao

(x_tr, y_tr), (x_te, y_te) = keras.datasets.mnist.load_data()
modelo = keras.models.load_model("mnist_cnn.keras")

# 1) amostra de digitos
fig, ax = plt.subplots(2, 5, figsize=(7.5, 3.6))
for k, a in enumerate(ax.ravel()):
    idx = int(np.where(y_tr == k)[0][0])
    a.imshow(x_tr[idx], cmap="gray_r"); a.set_title(str(k), fontsize=12); a.axis("off")
plt.tight_layout(h_pad=2.5); plt.savefig("mnist_amostra.png", dpi=150); plt.close()

# 2) bordas com filtros manuais
img = x_tr[0] / 255.0
v = np.array([[-1, 0, 1]] * 3); h = v.T
fig, ax = plt.subplots(1, 3, figsize=(9, 3.4))
for a, im, t in zip(ax, (img, convolucao(img, v), convolucao(img, h)),
                    ("imagem original", "borda vertical", "borda horizontal")):
    a.imshow(im, cmap="gray_r" if t == "imagem original" else "RdBu_r"); a.set_title(t, fontsize=12); a.axis("off")
plt.tight_layout(); plt.savefig("filtros_manuais.png", dpi=150); plt.close()

# 3) filtros aprendidos pela primeira camada
w = modelo.layers[0].get_weights()[0]            # (3, 3, 1, 32)
fig, ax = plt.subplots(4, 8, figsize=(8, 4.3))
for k, a in enumerate(ax.ravel()):
    a.imshow(w[:, :, 0, k], cmap="RdBu_r"); a.axis("off")
plt.tight_layout(); plt.savefig("filtros_aprendidos.png", dpi=150); plt.close()

# 4) mapas de caracteristicas da camada 1
sub = keras.Model(modelo.inputs, modelo.layers[0].output)
mapas = sub.predict((x_tr[0] / 255.0)[np.newaxis, ..., np.newaxis], verbose=0)[0]
fig, ax = plt.subplots(2, 5, figsize=(8, 3.5))
ax[0, 0].imshow(x_tr[0], cmap="gray_r"); ax[0, 0].set_title("entrada", fontsize=10)
for k in range(9):
    a = ax.ravel()[k + 1]; a.imshow(mapas[:, :, k], cmap="viridis"); a.set_title("mapa " + str(k), fontsize=10)
for a in ax.ravel(): a.axis("off")
plt.tight_layout(); plt.savefig("mapas.png", dpi=150); plt.close()

# 5) erros
xt = (x_te / 255.0)[..., np.newaxis]
pred = modelo.predict(xt, verbose=0).argmax(axis=1)
erros = np.where(pred != y_te)[0][:12]
fig, ax = plt.subplots(2, 6, figsize=(9, 3.8))
for a, i in zip(ax.ravel(), erros):
    a.imshow(x_te[i], cmap="gray_r"); a.set_title(f"real {y_te[i]}, previsto {pred[i]}", fontsize=9); a.axis("off")
plt.tight_layout(h_pad=2); plt.savefig("erros.png", dpi=150); plt.close()

# curvas
hm, hc = json.load(open("hist_mlp.json")), json.load(open("hist_cnn.json"))
json.dump({"mlp_val": [round(v, 4) for v in hm["val_accuracy"]], "cnn_val": [round(v, 4) for v in hc["val_accuracy"]],
           "mlp_tr": [round(v, 4) for v in hm["accuracy"]], "cnn_tr": [round(v, 4) for v in hc["accuracy"]],
           "mlp_loss": [round(v, 4) for v in hm["val_loss"]], "cnn_loss": [round(v, 4) for v in hc["val_loss"]]},
          open("curvas14.json", "w"))
print("ok")
