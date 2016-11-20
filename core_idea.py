# coding=utf-8
import nltk
from nltk.corpus import wordnet
from nltk.corpus import state_union
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer

from variables import WEIGHT_SENTENCE, MAIN_ATTRIBUTE
from Knowledges.preprocessing import *


class Idea:
    def __init__(self, text):
        self.text = text
        self.frame = {}

    def __str__(self):
        return str(self.frame)

    def __repr__(self):
        return str(self.frame)

    def generate(self):
        # print begin
        self.frame = generateIdea(self.text)
        return self

    def compare(self, idea):
        out = 0
        for label in self.frame.keys():
            label_wordnet = select_wordnet(label)
            if label in idea.frame and label in MAIN_ATTRIBUTE and label_wordnet:
                mean_all_label = 0.0
                for word in self.frame[label]:
                    try:
                        w1 = wordnet.synset(str(word)+'.'+label_wordnet+'.01')
                        mean_label = 0.0
                        for word2 in idea.frame.get(label, []):
                            try:
                                w2 = wordnet.synset(str(word2)+'.'+label_wordnet+'.01')
                                mean_label += w1.wup_similarity(w2)
                            except:
                                print word2
                        mean_all_label += mean_label / float(len(idea.frame.get(label, [''])))
                        print mean_all_label, mean_label
                    except:
                        mean_all_label = 0
                out += WEIGHT_SENTENCE.get(label, 'DEFAULT') * mean_all_label / float(len(self.frame.get(label, [''])))
        return out

def select_wordnet(label):
    if label in ['VBP', 'VBD', 'VBD', 'VB']:
        return 'v'
    elif label in ['NNP', 'NNS', 'NN', 'NNPS']:
        return 'n'


def init_tokenizer():
    train_text = state_union.raw("2005-GWBush.txt")
    sample_text = state_union.raw("2006-GWBush.txt")
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    print "custom_sent_tokenizer", custom_sent_tokenizer
    # Create String of meaning
    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    print len(tokenized)
    tokenized = custom_sent_tokenizer.tokenize(train_text)
    print len(tokenized)
    print "tokenized", tokenized

    for i in tokenized:
        # Label all string
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        # print tagged
        chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        # print(chunked)
        # for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        #     print(subtree)

        chunkGram = r"""Chunk: {<.*>+}
                                }<VB.?|IN|DT|TO>+{"""

        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        createFrame(tagged)
    print attribute

master_tokenizer = PunktSentenceTokenizer(state_union.raw("2005-GWBush.txt"))

""" From a text, the function generate frames of common sens
Input:
    - text: String
Output:
    - [ frame={ 'DT', 'VB':, ...}, ... ]
"""
def generateIdeas_(text):
    # Cut sentences by meaning
    tokenized_txt = master_tokenizer.tokenize(text)

    # Label content
    labeled_txt = []
    frames_txt = []
    for token in tokenized_txt:
        # words = nltk.word_tokenize(token)
        words = preproc_it(token)
        tagged = nltk.pos_tag(words)
        labeled_txt.append(tagged)
        frames_txt.append(createFrame(tagged))

    return frames_txt

def generateIdeas(text):
    # Cut sentences by meaning
    tokenized_txt = master_tokenizer.tokenize(text)

    # Label content
    ideas = []
    for token in tokenized_txt:
        ideas.append(Idea(token).generate())

    return ideas


def generateIdea(text):
    words = preproc_it(text)
    tagged = nltk.pos_tag(words)
    return createFrame(tagged)



attribute = []
""" Function
"""
def createFrame(sentence, frame={}):
    for _value, att in sentence:
        if att not in attribute:
            attribute.append(att)
        if att not in frame:
            frame[att] = [_value.lower()]
        else:
            frame[att].append(_value.lower())
    return frame


if __name__ == '__main__':
    # init_tokenizer()

    text = "﻿Other Georgia Tech-affiliated buildings in the area host the Center for Quality Growth and Regional Development, the Georgia Tech Enterprise Innovation Institute, the Advanced Technology Development Center, VentureLab, and the Georgia Electronics Design Center. Technology Square also hosts a variety of restaurants and businesses, including the headquarters of notable consulting companies like Accenture and also including the official Institute bookstore, a Barnes & Noble bookstore, and a Georgia Tech-themed Waffle House.[57][61]"
    text = text.decode('utf-8')
    id = Idea(text).generate()
    text2 = "﻿Other Georgia Tech-affiliated house in the area host the higher for Quality Decrease and Country Development, the Georgia Tech Enterprise Innovation Institute, the Advanced Technology Development Center, VentureLab, and the Georgia Electronics Design Center. Technology Square also hosts a variety of restaurants and businesses, including the headquarters of notable consulting companies like Accenture and also including the official Institute bookstore, a Barnes & Noble bookstore, and a Georgia Tech-themed Waffle House.[57][61]"
    text2 = text2.decode('utf-8')

    print id.compare(Idea(text2).generate())
