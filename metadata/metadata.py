# -*- coding: utf-8 -*-

import os, re
import networkx as nx
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

########## BASE CLASSES ##########

class BaseMetaGetter(object):
    '''
    A base metadata gathering class that can be extended on a state-by-state basis.
    Extend and implement new classes for each state (see Virgina below).
    '''

    def __init__(self, document):
        '''
        Requires an input document (represented as plain text).
        '''
        self.doc = self._clean(document)

    def _clean(self, str):
        '''
        Private method. Mostly strips extraneous linebreaks and weird unicode chars.

        TODO:
        - Strip punctuation
        - Option for stopword removal
        - Other common NLP cleanup
        '''
        return ' '.join(word_tokenize(str)).decode('utf-8', errors='ignore')

    def get_key_sentences(self, n=5):
        '''
        Uses a simple implementation of TextRank to extract the top N sentences
        from a document.

        Sources:
        - Original paper: http://acl.ldc.upenn.edu/acl2004/emnlp/pdf/Mihalcea.pdf
        - Super useful blog post: http://joshbohde.com/blog/document-summarization
        - Wikipedia: http://en.wikipedia.org/wiki/Automatic_summarization#Unsupervised_keyphrase_extraction:_TextRank
        '''
        sentence_tokenizer = PunktSentenceTokenizer()
        sentences = sentence_tokenizer.tokenize(self.doc)

        word_counts = CountVectorizer(min_df=0).fit_transform(sentences)
        normalized = TfidfTransformer().fit_transform(word_counts) 

        similarity_graph = normalized * normalized.T
     
        nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
        scores = nx.pagerank(nx_graph)
        return sorted(((scores[i],s) for i,s in enumerate(sentences)),
                      reverse=True)[n]

    def get_case_num(self):
        '''
        Returns a case number from the text. Will be different for every state.
        '''
        raise NotImplementedError

    def get_date(self):
        '''
        Returns the date of the case. Will be different for every state.
        '''
        raise NotImplementedError

    def get_parties(self):
        '''
        Returns parties involved. Will be different for every state.
        '''
        raise NotImplementedError


########## STATE-SPECIFIC CLASSES ##########

class VAMetaGetter(BaseMetaGetter):
    '''
    Virgina-specific implementation of the MetaGetter.
    '''

    def get_case_num(self):
        '''
        Grabs case numbers from VA cases. Needs MAJOR refinement!

        TODO:
        - Only attempt to detect record number from first page
        - Edge case handling and match testing
        '''
        return re.findall('Record No. (\w+)', self.doc[:1000])
