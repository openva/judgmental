# -*- coding: utf-8 -*-

import os, re, time
import networkx as nx
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

# Elasticsearch endpoint: http://yqoffbyc.api.qbox.io

########## BASE CLASSES ##########

class Decision(object):

    def __init__(self, text):
        '''
        Initializes with text from a document.
        '''
        self.doc = text
        self.caseno = self._set_case_num()
        self.date = self._set_case_date()
        self.parties = None

    ########## PRIVATE ##########

    def _get_header(self):
        '''
        Gets the header section of a decision, which contains metadata.
        '''
        raise NotImplementedError

    def _clean(self, str):
        '''
        Private method. Mostly strips extraneous linebreaks and weird unicode chars.

        TODO:
        - Strip punctuation
        - Option for stopword removal
        - Other common NLP cleanup
        '''
        return ' '.join(word_tokenize(str)).decode('utf-8', errors='ignore')

    def _set_case_num(self):
        '''
        Sets a case number from the text. Will be different for every state.
        '''
        return None

    def _set_case_date(self):
        '''
        Returns the date of the case. Will be different for every state.
        '''
        return None

    def _set_case_parties(self):
        '''
        Sets parties involved. Will be different for every state.
        '''
        return None

    ########## PUBLIC ###########

    def as_json(self):
        raise NotImplementedError

    def get_key_sentences(self, n=5):
        '''
        Uses a simple implementation of TextRank to extract the top N sentences
        from a document.

        Sources:
        - Original paper: http://acl.ldc.upenn.edu/acl2004/emnlp/pdf/Mihalcea.pdf
        - Super useful blog post: http://joshbohde.com/blog/document-summarization
        - Wikipedia: http://en.wikipedia.org/wiki/Automatic_summarization#Unsupervised_keyphrase_extraction:_TextRank
        '''
        # Tokenize the document into sentences. More NLP preprocesing should also happen here. 
        sentence_tokenizer = PunktSentenceTokenizer()
        sentences = sentence_tokenizer.tokenize(self.doc)

        # Calculate word counts and TFIDF vectors
        word_counts = CountVectorizer(min_df=0).fit_transform(sentences)
        normalized = TfidfTransformer().fit_transform(word_counts) 

        # Normalized graph * its transpose yields a sentence-level similarity matrix
        similarity_graph = normalized * normalized.T
     
        nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
        scores = nx.pagerank(nx_graph)
        return sorted(((scores[i],s) for i,s in enumerate(sentences)),
                      reverse=True)[n]


########## STATE-SPECIFIC CLASSES ##########

class VirginiaDecision(Decision):
    '''
    Virgina-specific implementation of the MetaGetter.
    '''

    def _set_case_num(self):
        '''
        Grabs case numbers from VA cases. Needs MAJOR refinement!

        TODO:
        - Only attempt to detect record number from first page
        - Edge case handling and match testing
        '''
        return re.findall('Record No. (\w+)', self.doc[:200])

    def _set_case_date(self):
        '''
        Grabs dates from VA cases. Needs MAJOR refinement!
        '''
        datestr = re.findall('\w+ \d+, \d{4}', self.doc[:200])[0]
        return time.strptime(datestr, '%B %d, %Y')

    def _get_parties(self):
        # Doh, doesn't work yet
        pass



if __name__ == '__main__':
    infile = open('sample.txt', 'r').read()
    d = VirginiaDecision(infile)

    print d.date

