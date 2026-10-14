import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

d = load_digits()
fig, eixos = plt.subplots(2, 5, figsize=(7.5, 3.8))
for ax, img, rot in zip(eixos.ravel(), d.images[:10], d.target[:10]):
    ax.imshow(img, cmap="gray_r")
    ax.set_title(str(rot), fontsize=12)
    ax.axis("off")
plt.tight_layout(h_pad=3.0)
plt.savefig("digitos.png", dpi=170)
print("ok")
