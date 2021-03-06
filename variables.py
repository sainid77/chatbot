# coding=utf-8


PATH = 'C:\Users\yann\Documents\Mes fichiers\Cours\GeorgiaTech\Fall 2016\CS   7637 - Knowledge based AI\Project3\Data\\'

SLACK_BOT_TOKEN = 'xoxb-100786786962-4QVO6gqENojSxqAAPr6jZw6k'

BOT_ID = 'U2YP4P4UA'
BOT_NAME = 'alexa'
READ_WEBSOCKET_DELAY = 1    # 1 second delay between reading from firehose


# Intelligence variables
# Selection of the right type of input

# When generating from knowledge
IDEA_NEW = 0
IDEA_TOO_WIDE = 1
IDEA_TOO_FAR = 2
IDEA_NO = 3

THRESHOLD_DISP = 2
THRESHOLD_NB = 50




NAME_CLASSIFIERS = [
    "kNN",
    # "Random forest",
    "MultinomialNB"]#,
    # "BernoulliNB"]

NAME_CLASSIFIERS2 = [
    "Ridge Classifier",
    "Perceptron",
    "Passive-Aggressive",
    "kNN",
    "Random forest",
    "MultinomialNB",
    "BernoulliNB",
    "NearestCentroid"]

SAVED_CONCEPTS = 'knowledge_concept.csv'

MAIN_ATTRIBUTE = ['NNP']#, 'NNS', 'JJ', 'NN', 'VBG', 'VBN', 'VBP', 'VBZ' ]

ALL_ATTRIBUTE = ['NNP', 'POS', 'IN', 'CD', ',', ':', 'NNS', 'JJ', 'DT', 'PRP', 'NN', 'VBP', 'VBN', '.', 'CC', 'WDT', 'VBZ', '(', ')', 'RB', 'VBD', 'PRP$', 'TO', 'VBG', 'MD', 'VB', 'JJR', 'WP', 'NNPS', 'JJS', 'RP', 'WRB', 'RBR', 'PDT', 'RBS', '$', 'EX', '``', "''", 'WP$']

WEIGHT_SENTENCE =   {'NNP': 1,
                     'POS': 1,
                     'IN': 1,
                     'CD': 1,
                     ',': 1,
                     ':': 1,
                     'NNS': 1,
                     'JJ': 1,
                     'DT': 1,
                     'PRP': 1,
                     'NN': 1,
                     'VBD': 1,
                     'VBN': 1,
                     '.': 1,
                     'CC': 1,
                     'WDT': 1,
                     'VBZ': 1,
                     '(': 1,
                     ')': 1,
                     'RB': 1,
                     'PRP$': 1,
                     'TO': 1,
                     'VBG': 1,
                     'MD': 1,
                     'VB': 1,
                     'JJR': 1,
                     'WP': 1,
                     'NNPS': 1,
                     'JJS': 1,
                     'RP': 1,
                     'WRB': 1,
                     'RBR': 1,
                     'PDT': 1,
                     'RBS': 1,
                     '$': 1,
                     'EX': 1,
                     '``': 1,
                     "''": 1,
                     'WP$': 1,
                     'DEFAULT': 1}
