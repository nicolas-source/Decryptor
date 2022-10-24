'''
Allows scoring of text using n-gram probabilities
17/07/12
Cite: http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
'''
from math import log10

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        for line in open(ngramfile):
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)

        self.L = len(key)
        self.N = sum(self.ngrams.values())
        # self.N = sum(iter(self.ngrams.values()))

        # self.N = sum(self.ngrams.itervalues())
        """
        In Python 3, direct iteration over mappings works the same way as it does in Python 2.
        There are no method based equivalents
        - the semantic equivalents of d.itervalues() and d.iteritems() in Python 3
        are iter(d.values()) and iter(d.items()).
        """

        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       
