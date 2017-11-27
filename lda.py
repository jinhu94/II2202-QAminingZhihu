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
from snownlp import SnowNLP


def lda(doc_set, stop, texts):
    for doc in doc_set: # doc must be a string
        
        
        # split words in each doc
        split_doc = [i for i in jieba.cut(doc, cut_all=False)]

        # remove stop words from tokens
        stopped_doc = [i for i in split_doc if not i in stop]
        # add preprocessed docs into list
        texts.append(stopped_doc)
        
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
    print(ldamodel.print_topics(num_topics=3, num_words=3))
    return(ldamodel.print_topics(num_topics=3, num_words=3))

def sentiment(doc,):
    s = SnowNLP(ans)
    positive_prob = s.sentiments
    return positive_prob

#if "__name__"=="__main__":
ans = "对于数据科学家，无论是数据分析还是数据挖掘来说，Pandas是一个非常重要的Python包。它不仅提供了很多方法，使得数据处理非常简单，同时在数据处理速度上也做了很多优化，使得和Python内置方法相比时有了很大的优势。"
ans1 = "开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率."
# create English stop words list
stop = [line.strip() for line in open('stopwords.txt').readlines() ]

texts = []
lda([ans, ans1], stop, texts)
#print(x)