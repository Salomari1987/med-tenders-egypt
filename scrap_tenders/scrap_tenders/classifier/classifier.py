from textblob.classifiers import NaiveBayesClassifier
import os

def classify(desc):
    try:
        fp = open(os.path.join(os.path.abspath('.'), 'classifier/train.json'), 'r')
    except Exception:
        fp = open('train.json', 'r')
    cl = NaiveBayesClassifier(fp, format='json')
    classification = cl.classify(desc)

    return classification
