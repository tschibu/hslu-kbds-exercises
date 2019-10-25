import logging
import os
import pyemd
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from nltk.tokenize import sent_tokenize

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
        self.sentence_count = 0

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            with open(os.path.join(self.dirname, fname)) as f_input:
                corpus = f_input.read()
            raw_sentences = sent_tokenize(corpus)
            for sentence in raw_sentences:
                if len(sentence) > 0:
                    self.sentence_count += 1
                    yield simple_preprocess(sentence) # tokenization, lowercasing ect... => retrun a list o

parent_dir = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(os.path.dirname(parent_dir), 'data', 'got')
sentences = MySentences(data_path)

model = Word2Vec(sg=1, # 1 for skip-gram; otherwise CBOW
                 size=300, # num of features
                 window=5,
                 #min_count=3,
                 workers=4)
model.build_vocab(sentences)
model.train(sentences=sentences, total_examples=model.corpus_count, epochs=model.epochs)
model.save('GOT-vectors.w2v')  # Save the model for later use

text1 = 'Hodor That was all he ever said'.lower().split()
text2 = 'Hold the door'.lower().split()
similarity = model.wv.wmdistance(text1, text2)
print (similarity)