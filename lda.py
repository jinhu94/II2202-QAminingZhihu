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
    print(ldamodel.print_topics(num_topics=topic_num, num_words=words_num))
    
    # return a list of topics and words, format: [(topic number, weight*words)]
    #return(ldamodel.print_topics(num_topics=topic_num, num_words=words_num))
    theta_matrix=[]
    for i in preprocessed_texts:
        topic_dist = ldamodel.get_document_topics(dictionary.doc2bow(i))
        dic={}
        for j in topic_dist:
            dic[j[0]] = j[1]
        theta_matrix.append(dic)
    #theta_matrix = ldamodel.get_document_topics(dictionary.doc2bow(preprocessed_texts[1]))
    return theta_matrix





if __name__ == "__main__":
    
    #ans = "印象中，最开始听说“LDA”这个名词，是缘于rickjin在2013年3月写的一个LDA科普系列，叫LDA数学八卦，我当时一直想看来着，记得还打印过一次，但不知是因为这篇文档的前序铺垫太长（现在才意识到这些“铺垫”都是深刻理解LDA 的基础，但如果没有人帮助初学者提纲挈领、把握主次、理清思路，则很容易陷入LDA的细枝末节之中），还是因为其中的数学推导细节太多，导致一直没有完整看完过。"
    #ans1 = "在这一小节中，本文介绍如何用 Spark 训练朴素贝叶斯分类模型，这一流程的输入是文本的特征向量及已经标记好的分类标签。在这里本文得到的是分类模型及文本分类的正确率。"
    #ans2 = "这意味着什么呢？我们知道，标准差其实衡量了数据个体之间的离散程度，也可以解释为大部分的数值和其平均值之间的差异。因此这么大的标准差可以说明知乎用户之间的差距可能略大于整个银河系（雾），同时也说明绝大部分用户的数值和平均值有很大的差距，要么大得离谱（比如张佳玮），要么小得可怜（比如我"
    #x = runlda([ans, ans1, ans2], 3, 3)
    
    raw_data = pd.read_csv('./Results/4a_content_vote>50.csv').append(pd.read_csv('./Results/4b_content_20_50.csv'))
    data = raw_data[['aid','content']].fillna('no content')#.dropna()# need to remove all nan value in content column
    docs = data['content']
    x = runlda(docs.tolist(), 7, 10)
    df = pd.DataFrame(x).fillna(0)
    #df.to_csv('topic_theta_matrix.csv')
    