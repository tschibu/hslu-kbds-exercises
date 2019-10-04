"""
Knowledge-based Decision Support Systems
    Natural Language Processing Basics 1
"""

from nltk import tokenize
from nltk import tag 
from nltk import chunk 
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import word_tokenize


NLP_TEXT = "I am a student at the Hochschule Luzern. I love IT."

def main():
    print("")
    print("Knowledge-based Decision Support Systems")
    print("\tNatural Language Processing Basics 1")
    print("")
    print("Satz Tokenizierung")
    satz_tokenizierung()
    print("Wort Tokenizierung")
    word_tokenizierung()
    print("Part of Speech Tagging")
    part_of_speech_tagging()
    print("NE Chunking")
    ne_chucking()
    print("Wort Stemming")
    wort_stemming()
    print("Satz Stemming")
    satz_stemming()
    print("Stop Word Removal")
    stop_word_removal()
    print("Wort Stemming & Lemmatization")
    wort_stemming_and_lemmatization()


def satz_tokenizierung():
    satz = tokenize.sent_tokenize(NLP_TEXT)
    print(satz)

def word_tokenizierung():
    token_wort = tokenize.word_tokenize(NLP_TEXT) 
    print(token_wort)
    return token_wort

def part_of_speech_tagging():
    tagged_pos = "I am a student at the Hochschule Luzern. I love IT."  
    tagged_pos = tag.pos_tag(word_tokenizierung()) 
    print(tagged_pos)
    return tagged_pos

def ne_chucking():
    tree = chunk.ne_chunk(part_of_speech_tagging())
    # print(tree)
    # tree.draw()

def wort_stemming():
    ps = PorterStemmer()
    example_words = ["go","goes","nogo","begone","gone"]
    for w in example_words:
        print(ps.stem(w))

def satz_stemming():
    ps = PorterStemmer()
    words = word_tokenize(NLP_TEXT)
    for w in words:
        print(ps.stem(w))

def stop_word_removal():
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(NLP_TEXT)
    #filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(word_tokens)
    print(filtered_sentence)


def wort_stemming_and_lemmatization():
    stemmer = PorterStemmer()
    lemmatiser = WordNetLemmatizer()

    wort = "going"

    print("Stem %s: %s" % ((wort), stemmer.stem((wort))))
    print("Lemmatise %s: %s" % ((wort), lemmatiser.lemmatize((wort))))

def exercice_01():
    exercice_01_text = "When Alexander Graham Bell invented the telephone he had three missed calls from Chuck Norris."
    token_wort = tokenize.word_tokenize(exercice_01_text) 
    print(token_wort)
    return token_wort

def exercice_02():
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []

    for w in exercice_01():
        if w not in stop_words:
            filtered_sentence.append(w)
    print(filtered_sentence)

def exercice_03():
    stemmer = PorterStemmer()
    lemmatiser = WordNetLemmatizer()
    exercice_03_text = "When Alexander Graham Bell invented the telephone he had three missed calls from Chuck Norris."
    print("Stem %s: %s" % ((exercice_03_text), stemmer.stem((exercice_03_text))))
    print("Lemmatise %s: %s" % ((exercice_03_text), lemmatiser.lemmatize((exercice_03_text))))

if __name__ == "__main__":
    # exercice_01()
    # exercice_02()
    exercice_03()