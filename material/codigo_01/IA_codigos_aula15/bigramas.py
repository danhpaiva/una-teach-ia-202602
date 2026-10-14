import random
from collections import Counter, defaultdict

texto = ("o gato dorme no sofa . o gato come o peixe . o cao dorme no tapete . "
         "o cao come a carne . a menina le o livro . a menina come o peixe . "
         "o cao le o jornal . o gato dorme no tapete .")
palavras = texto.split()

contagem = defaultdict(Counter)
for atual, proxima in zip(palavras, palavras[1:]):
    contagem[atual][proxima] += 1

print("palavras diferentes:", len(set(palavras)))
for p in ("o", "gato", "come"):
    total = sum(contagem[p].values())
    top = contagem[p].most_common(3)
    print(p, "->", [(w, round(c / total, 2)) for w, c in top])

random.seed(1)
atual, frase = "o", ["o"]
while atual != "." and len(frase) < 12:
    candidatas = list(contagem[atual])
    pesos = [contagem[atual][w] for w in candidatas]
    atual = random.choices(candidatas, weights=pesos)[0]
    frase.append(atual)
print("frase gerada:", " ".join(frase))
