# coding=utf-8

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC

import pickle
import os, re

from variables import *

ps = PorterStemmer()

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
NB_FEATURES = 3000
RATE_LEARNER = 0.8

stop_words = set(stopwords.words('english'))


#################################################
###       Import files

def readAllData():
    listFile = os.listdir(PATH + 'Courses')
    listFile = ['Courses\\' + name for name in listFile]
    listFile = []
    listFile.append('gatech_wiki_clean_v3.csv')
    data = []
    for file in listFile:
        data += loadFile(file)
    return data


def readAllData_dico():
    listFile = os.listdir(PATH + 'Courses')
    listFile = ['Courses\\' + name for name in listFile]
    # listFile = []
    listFile.append('gatech_wiki_clean_v3.csv')
    data = []
    for file in listFile:
        data.append({'name': file, 'text': loadFile(file)})
    return data


def loadFile(filename):
    file = open(PATH+filename, 'r')
    text = [line[:-2].decode('utf-8') for line in file.readlines()]
    file.close()
    return text

    # text = "Other Georgia Tech-affiliated buildings in the area host the Center for Quality Growth and Regional Development, the Georgia Tech Enterprise Innovation Institute, the Advanced Technology Development Center, VentureLab, and the Georgia Electronics Design Center. Technology Square also hosts a variety of restaurants and businesses, including the headquarters of notable consulting companies like Accenture and also including the official Institute bookstore, a Barnes & Noble bookstore, and a Georgia Tech-themed Waffle House.[57][61]"
    # text = text.decode('utf-8')
    # return [text]



#################################################
###       Process data

def preproc(data):
    txt = []
    for text in data:
        # txt.append(generateIdeas(text))
        txt.append(preproc_it(text))
        # txt += preproc_it(text)
        # txt.append(preproc_tag(text))
    return txt


def preproc_it(data):
    return [w.lower().encode('utf-8', 'ignore') for w in word_tokenize(data) if not w in stop_words]
    # return [lemmatizer.lemmatize(w).lower().encode('ascii', 'ignore') for w in word_tokenize(data) if not w in stop_words]

pattern = re.compile(("[a-zA-Z\s]+"))
""" From a list of words, try to keep only diverse idea
Input:
    - data: [word1, word2, ...]
    - all: Boolean; True => keep all words (keep duplicate), False: keep unique
Output:
    - [word1, word2, ...]
"""
def merge_synonym(data, all=False):
    n_data = []
    for w in data:
        try:
            if pattern.match(w):
                if not ' ' in w:
                    n_w = lemmatizer.lemmatize(w.encode('utf-8', 'ignore'))
                    if n_w not in n_data or all:
                        n_data.append(n_w)
                else:
                    l_w = w.split(' ')
                    n_w = ' '.join(merge_synonym(l_w))
                    if n_w not in n_data or all:
                        n_data.append(n_w)
            else:
                n_data.append(w)
        except Exception as e:
            print w
            raise e
    return n_data


def preproc_tag(data):
    custom_sent_tokenizer = PunktSentenceTokenizer(data)
    tokenized = custom_sent_tokenizer.tokenize(data)
    return tokenized



#################################################
###       Useful functions

""" Merge sublist =>[[]] to []
"""
def mergeData(data):
    n_data = []
    for d in data:
        n_data += d
    return n_data


""" Convert ideas to something learnable
"""
def preproc_learn(ideas):
    data_to_learn = []
    for idea in ideas:
        data_to_learn.append((idea.features, idea.id))
    return data_to_learn


def saveData(fileName, data):
    file = open(fileName, 'w')
    for d in data:
        file.writelines(str(d)+"\n")
    file.close()

SEPARATOR = ';'
def saveData_dico(fileName, data):
    file = open(fileName, 'w')
    file.writelines(SEPARATOR.join(data[0].keys())+"\n")
    for d in data:
        file.writelines(SEPARATOR.join([str(d[key]) for key in d])+"\n")
    file.close()


def loadClassifier(name):
    classifier_f = open(name, "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
    return classifier


def test_learner(training_set, testing_set):
    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(training_set)
    print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

    BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
    BernoulliNB_classifier.train(training_set)
    print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

    LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
    LogisticRegression_classifier.train(training_set)
    print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

    SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
    SGDClassifier_classifier.train(training_set)
    print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

    SVC_classifier = SklearnClassifier(SVC())
    SVC_classifier.train(training_set)
    print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

    LinearSVC_classifier = SklearnClassifier(LinearSVC())
    LinearSVC_classifier.train(training_set)
    print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

    LinearSVC_classifier.p
#
#
# if __name__ == '__main__':
#     main_preprocess()