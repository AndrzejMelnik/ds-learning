"""Zadanie 5 -- Wizualizacja embeddingów
Wytrenuj model Word2Vec na prostym korpusie (np. 20 zdan o zwierzetach, kolorach,
rozmiarach). Zwizualizuj embeddingi za pomoca PCA (2D). Sprawdz czy semantycznie
podobne slowa sa blisko siebie.
Oczekiwany wynik: wykres PCA z pogrupowanymi slowami"""

from gensim.models import Word2Vec
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

sentences = [
    ["mały", "biały", "pies", "biega"], ["duży", "czarny", "pies", "szczeka"],
    ["mały", "biały", "kot", "śpi"], ["duży", "czarny", "kot", "mruczy"],
    ["czerwony", "duży", "ptak", "lata"], ["niebieski", "mały", "ptak", "śpiewa"],
    ["zielony", "mały", "żaba", "skacze"], ["żółty", "duży", "lew", "ryczy"],
    ["mały", "biały", "chomik", "je"], ["duży", "szary", "słoń", "trąbi"],
    ["mały", "czarny", "pająk", "tka"], ["duży", "brązowy", "niedźwiedź", "ryczy"],
    ["niebieski", "duży", "wieloryb", "płynie"], ["mały", "żółty", "kanarek", "śpiewa"],
    ["zielony", "duży", "krokodyl", "pływa"], ["biały", "duży", "koń", "galopuje"],
    ["czarny", "mały", "kret", "kopie"], ["szary", "mały", "wilk", "wyje"],
    ["brązowy", "duży", "jeleń", "biegnie"], ["czerwony", "mały", "lis", "poluje"]
]

model = Word2Vec(
    sentences,
    vector_size=50,
    window=3,
    min_count=1,
    sg=1,
    epochs=100,
    seed=42
)

words = list(model.wv.index_to_key)
word_vectors = np.array([model.wv[w] for w in words])

pca = PCA(n_components=2)
result = pca.fit_transform(word_vectors)

plt.figure(figsize=(12, 10))
plt.scatter(result[:, 0], result[:, 1], edgecolors='k', c='lightblue', s=100)
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]), xytext=(5, 2),
                 textcoords='offset points', fontsize=12)

plt.title('Wizualizacja embeddingów Word2Vec (PCA 2D)', fontsize=15, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.show()