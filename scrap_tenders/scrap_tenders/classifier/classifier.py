from textblob.classifiers import NaiveBayesClassifier
import os

def classify(desc):
    with open(os.path.join(os.path.abspath('.'), 'classifier/train.json'), 'r') as fp:
        cl = NaiveBayesClassifier(fp, format='json')
        classification = cl.classify(desc)

    return classification
