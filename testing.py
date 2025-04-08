import project1 as p1
import utils
import numpy as np

train_data = utils.load_data('reviews_train.tsv')

train_texts, train_labels = zip(*((sample['text'], sample['sentiment']) for sample in train_data))


stop_words = np.genfromtxt('stopwords.txt', delimiter=",", dtype= str)

indices_by_word = {}  # maps word to unique index
for text in train_texts:
    word_list = p1.extract_words(text)
    for word in word_list:
        if word in indices_by_word: continue
        #if word in stopword: continue
        indices_by_word[word] = len(indices_by_word)