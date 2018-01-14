# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:02:01 2017

@author: roger
"""
import csv
from zhihu_oauth import ZhihuClient
import pandas as pd
from Content_analyze import content_analyze



client = ZhihuClient()
client.load_token('token.pkl')

df = pd.read_csv('./Results/3b_aid_vote_20_50.csv')
x = list(df["aid"]) 

x100 = x[4000:]

fail_aid = []
rows = []
counter = 4000
write_counter = 0

output_file = "./content_20_50.csv"
#headers = ["aid", "created_time", "length", "img_count", "link_count", "follower_count", "answer_count", "content"]
#with open(output_file,'a') as f:
#	f_csv = csv.writer(f)
#	f_csv.writerow(headers)


for aid in x100:

	try:
		a1 = client.answer(int(aid))
		(content, length, img_count, link_count) = content_analyze(a1.content)
		created_time = a1.created_time
		#follower_count = 38
		#answer_count = 20
		follower_count = a1.author.follower_count
		answer_count = a1.author.answer_count
		rows.append((aid, created_time, length, img_count, link_count, follower_count, answer_count, content))
		print ("success {0}".format(counter))
		counter += 1
		write_counter += 1
	except:
		fail_aid.append(aid)
		print ("fail {0}".format(counter))
		counter += 1
		print (fail_aid)
		continue

	if write_counter == 10:
		with open(output_file,'a') as f:
			f_csv = csv.writer(f)
			f_csv.writerows(rows)
		rows = []
		write_counter = 0
		print ("write done")


with open(output_file,'a') as f:
	f_csv = csv.writer(f)
	f_csv.writerows(rows)
	print ("finished")
