#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:45:12 2017

@author: jinhu
"""
from snownlp import SnowNLP
import pandas as pd

# count positive probability of each answer, merge them into the 

def sentiment(doc):
    if doc == None:
        return -1
    else: 
        s = SnowNLP(doc)
        positive_prob = s.sentiments
        return positive_prob


    
if __name__ == "__main__":
    raw_data = pd.read_csv('./Results/4a_content_vote>50.csv').append(pd.read_csv('./Results/4b_content_20_50.csv'))
    data = raw_data[['aid','content']].dropna()
    senti = data['content'].apply(sentiment)
    dataWithSenti = pd.concat([data['aid'], senti], axis=1)
    dataWithSenti.to_csv("aid_senti.csv")
    