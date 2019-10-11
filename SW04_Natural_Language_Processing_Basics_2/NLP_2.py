"""
Knowledge-based Decision Support Systems    
    Natural Language Processing Basics 2
"""

import nltk, re, string, collections
from nltk.util import ngrams
from nltk.corpus import stopwords

# Download Stopwords
nltk.download('stopwords')

# Download MacBeth from Gutenberg
nltk.download('gutenberg')
nltk.corpus.gutenberg.fileids()
['shakespeare-macbeth.txt']

macbeth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')

## Exercise 1

# Satzzeichen entfernen
text_ohne_satzzeichen = "[" + re.sub("\.","",string.punctuation) + "]"
macbeth_ohne_satzzeichen = []

for word in macbeth:
    word = re.sub(text_ohne_satzzeichen, "", word)
    if word != "":
        macbeth_ohne_satzzeichen.append(word)

# Stopwörter entfernen
stop_words = set(stopwords.words('english'))

token_clean = [w for w in macbeth_ohne_satzzeichen if not w in stop_words]

# Bigrams definieren
listBigrams = nltk.bigrams(token_clean)

freq_bi = nltk.FreqDist(listBigrams)

fdist = nltk.FreqDist(freq_bi)
print("\n \n Bigrams: \n")
for k,v in fdist.most_common():
    if v > 8:
        print (k,v)

# Trigrams definieren
listTrigrams = nltk.trigrams(token_clean)

freq_tri = nltk.FreqDist(listTrigrams)

fdist = nltk.FreqDist(freq_tri)
print("\n \n Trigrams: \n")
for k,v in fdist.most_common():
    if v > 2:
        print (k,v)


## Exercise 2
