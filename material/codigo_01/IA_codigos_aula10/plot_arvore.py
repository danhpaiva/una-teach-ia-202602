import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

iris = load_iris()
X_tr, X_te, y_tr, y_te = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42, stratify=iris.target)
arvore = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_tr, y_tr)

nomes = ["sepala_c", "sepala_l", "petala_c", "petala_l"]
plt.figure(figsize=(10, 5.6))
plot_tree(arvore, feature_names=nomes, class_names=list(iris.target_names),
          filled=True, rounded=True, fontsize=11)
plt.tight_layout()
plt.savefig("arvore_iris.png", dpi=170)
print("ok")
