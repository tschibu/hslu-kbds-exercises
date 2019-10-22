from nltk.data import find
import gensim

word2vec_sample = str(find('models/word2vec_sample/pruned.word2vec.txt'))
model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)

# Rohe Vektorwerte für spezifische Wörter
print(model['dog'])

# Anzahl Wörter im Vokabular
print(len(model.vocab))

# Anzahl Dimensionen/Features
print(len(model['dog']))

