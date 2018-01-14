# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:02:01 2017

@author: roger
"""
import csv
from zhihu_oauth import ZhihuClient

client = ZhihuClient()

client.load_token('token.pkl')

# #Start from a question
# question1 = client.question(20251786)
# #https://www.zhihu.com/question/20251786
# print ("title: {0}".format(question1.title))
# print ("created_time: {0}".format(question1.created_time))
# allTopics = question1.topics
# for item in allTopics:
# 	print (item.name)

# #Get all answers
# allAnswers = question1.answers
# counter = 5

# for item in allAnswers:
#     if counter >=0:
#     	print ("content: {0}".format(item.content))
#     	print ("created_time: {0}".format(item.created_time))
#     	print ("voteup_count: {0}".format(item.voteup_count))
#     	print ("thanks_count: {0}".format(item.thanks_count))
#     	print ("author: {0}".format(item.author.name))
#     	counter-=1


# a1 = client.answer(143216281)
# #https://www.zhihu.com/question/20251786/answer/143216281
# print (a1.author.answer_count)
# # author’s profile and influence.
# print ("name: {0}".format(a1.author.name))
# print ("collected_count: {0}".format(a1.author.collected_count))
# print ("favorited_count: {0}".format(a1.author.favorited_count))
# print ("follower_count: {0}".format(a1.author.follower_count))
# print ("voteup_count: {0}".format(a1.author.voteup_count))
# #print ("is_best_answerer: {0}".format(a1.author.is_best_answerer))


output_file = "./question.csv"
headers = ["Qid", "Followers", "Created_time", "Answer_count"]

#https://www.zhihu.com/topic/20019119/top-answers
topic1 = client.topic(20019119)
questions = topic1.unanswered_questions
rows = []
for v in questions:
	rows.append((v._id, v.follower_count, v.created_time, v.answer_count))

with open(output_file,'a') as f:
	f_csv = csv.writer(f)
	f_csv.writerow(headers)
	f_csv.writerows(rows)
