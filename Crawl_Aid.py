# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:02:01 2017

@author: roger
"""
import csv
from zhihu_oauth import ZhihuClient
import pandas as pd


client = ZhihuClient()
client.load_token('token.pkl')

df = pd.read_csv('./Results/qid.csv')
x = list(df["Qid"])  #1275

qid1 = x[0:100]
qid2 = x[100:200]
qid3 = x[200:300]
qid4 = x[300:400]
qid450 = x[400:450]
qid500 = x[450:500]
qid550 = x[500:550]
qid600 = x[550:600]
qid650 = x[600:650]
qid700 = x[650:700]
qidmax = x[700:]
qid_remaining = [49661986, 49624489, 49614406, 49588754, 49579852, 49577747, 49561174, 49548161, 49538908, 49516348, 49515002, 49484493, 49478533, 49441737, 49439369, 49438979, 49420618, 49400575, 49394628, 49355053, 49351339, 49346875, 49301812, 49277249, 49273891, 49252316, 49228281, 49226335, 49222398, 49217578, 49145180, 49139651, 49103740, 49095043, 49094935, 49077474, 49034531, 49032553, 49024310, 49018555, 49010890, 49006431, 49004731, 48973334, 48972697, 48969402, 48968306, 48968096, 48967516, 48960565, 48957798, 48948437, 48943854, 48943088, 48940941, 48940041, 48923160, 48921139, 48920437, 48899851, 48893926, 48885046, 48874602, 48873447, 48873194, 48859301, 48859159, 48839355, 48837619, 48827798, 48823531, 48802753, 48802105, 48798133, 48794624, 48792191, 48789881, 48786542, 48776674, 48770250, 48767470, 48687446, 48682583, 48647262, 48606994, 48562568, 48505863, 48504714, 48495103, 48481145, 48428424, 48423073, 48393957, 48303405, 48281274, 48276858, 48276395, 48273917, 48190782, 48160014, 48019991, 47967903, 47903315, 47889482, 47885569, 47877337, 47872357, 47869191, 47863493, 47759222, 47757826, 47656089, 47652379, 47644653, 47642204, 47556909, 47552910, 47531438, 47525173, 47494232, 47486339, 47479886, 47479366, 47479200, 47478049, 47476748, 47464615, 47438110, 47426679, 47424630, 47418450, 47342174, 47320978, 47313981, 47309302, 47288960, 47283568, 47279105, 47265854, 47250301, 47223120, 47201087, 47181476, 47168997, 47166787, 47164091, 47162950, 47160575, 47150028, 47122011, 47116392, 47113421, 47094646, 47076268, 47067798, 47046496, 47043721, 46990026, 46962767, 46929173, 46885275, 46882273, 46835995, 46794896, 46781032, 46766251, 46765282, 46736213, 46686128, 46586707, 46585713, 46580452, 46572382, 46546708, 46518786, 46458819, 46450578, 46336837, 46327417, 46322863, 46309212, 46271094, 46269179, 46258260, 45995887, 45828085, 45720339, 45621711, 40362216, 40359500, 40358571, 40290987, 40283263, 40262081, 40256301, 40201059, 40127730, 40109880, 40068111, 40051181, 39913666, 39809450, 39712331, 39697559, 39399831, 39238483, 39116826, 38734099, 38634033, 38574272, 38470837, 38339461, 37412915, 37144912, 37142496, 36978739, 36752930, 36479862, 36452698, 36285516, 36099547, 35702117, 35595457, 35433226, 35367500, 35210878, 35134422, 35062190, 35012924, 35004585, 34893663, 34370944, 34225657, 33488763, 33259890, 32207070, 31592568, 31365240, 31337752, 30966406, 30158223, 29735498, 29582607, 29550579, 29525971, 29519716, 29518811, 29511036, 29508808, 29448162, 27255630, 25951351, 23863606, 19930380]
qid_run = qid_remaining[200:]

rows = []
fail_qid = []


counter = 1


for qid in qid_run:
	try:
		ans = client.question(int(qid)).answers
		for v in ans:
			rows.append((v._id, qid, v.voteup_count, v.comment_count))
		print ("success {0}".format(counter))
		counter += 1
	except:
		# if crawl failed, append qid to list fail_qid[]
		fail_qid.append(qid)
		print ("fail {0}".format(counter))
		counter += 1
		print (fail_qid)
		continue


output_file = "./answers.csv"
headers = ["aid", "qid", "voteup_count", "comment_count"]
with open(output_file,'a') as f:
	f_csv = csv.writer(f)
	#f_csv.writerow(headers)
	f_csv.writerows(rows)






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


#output_file = "./question.csv"
#headers = ["Qid", "Followers", "Created_time", "Answer_count"]

# rows = []
# for v in questions:
# 	rows.append((v._id, v.follower_count, v.created_time, v.answer_count))

# with open(output_file,'a') as f:
# 	f_csv = csv.writer(f)
# 	f_csv.writerow(headers)
# 	f_csv.writerows(rows)
