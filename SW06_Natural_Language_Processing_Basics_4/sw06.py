import os
import sys
import gensim
from nltk.data import find

root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
got_model = os.path.join(root_dir, "data", "models", "GOT-vectors.w2v")

if not os.path.exists(got_model):
    print("FATAL: GOT-vectors.w2v not found - please run Aufgabe_01.py from SW05 first to generate the model!")
    sys.exit(1)

model = gensim.models.Word2Vec.load(got_model)

import numpy as np
labels = []
count = 0
max_count = 50
X = np.zeros(shape=(max_count, len(model['dog'])))

for term in model.wv.vocab:
    X[count] = model[term]
    labels.append(term)
    count += 1
    if count >= max_count: break

#it's recommended to use PCA first to reduce to ~50 dimensions
from sklearn.decomposition import PCA
pca = PCA(n_components=50)
X_50 = pca.fit_transform(X)

#using TSNE to further reduce to 2 dimensions
from sklearn.manifold import TSNE
model_tsne = TSNE(n_components=2, random_state=0)
Y = model_tsne.fit_transform(X_50)

#show scatter plot
import matplotlib.pyplot as plt
plt.scatter(Y[:,0], Y[:,1], 20)

#add label
for label, x, y in zip(labels, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy = (x,y), xytext = (0, 0), textcoords = 'offset points', size = 10)

plt.show()