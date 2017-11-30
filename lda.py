#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:44:31 2017

@author: jinhu
"""

#from nltk.tokenize import RegexpTokenizer
#from stop_words import get_stop_words
#from nltk.stem.porter import PorterStemmer
from gensim import corpora
import gensim
import jieba
# load user dict
jieba.load_userdict('userdict.txt')
import re
import pandas as pd


def runlda(doc_set, topic_num, words_num):
    preprocessed_texts = []
    # create English and Chinese stop words list
    stop = [line.strip() for line in open('stopwords.txt').readlines()]
    
    
    p = re.compile("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+")
                   
    for doc in doc_set: # doc must be a string
        # remove all punctions and blanks
        ndoc = re.sub(p, "", doc)
        # split words in each doc
        split_doc = jieba.lcut(ndoc, cut_all = False)
        #[i for i in jieba.cut(ndoc, cut_all=False)]

        # remove stop words from tokens
        stopped_doc = [i for i in split_doc if not i in stop]
        # add preprocessed docs into list
        preprocessed_texts.append(stopped_doc)
        
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(preprocessed_texts)
    
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in preprocessed_texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=topic_num, id2word = dictionary, passes=20)
    #print(ldamodel.print_topics(num_topics=topic_num, num_words=words_num))
    
    # return a list of topics and words, format: [(topic number, weight*words)]
    return(ldamodel.print_topics(num_topics=topic_num, num_words=words_num))




if __name__ == "__main__":
    
    raw_data = pd.read_csv('./Results/4a_content_vote>50.csv').append(pd.read_csv('./Results/4b_content_20_50.csv'))
    data = raw_data[['aid','content']].dropna()# need to remove all nan value in content column
    docs = data['content']
    x = runlda(docs.tolist(), 10, 15)
    