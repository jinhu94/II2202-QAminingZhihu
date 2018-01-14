#data
questions <- read.csv("/home/roger/Dropbox/KTH/II2202/Zhihu/Results/0_all_questions.csv")
q_follow_all=questions[,2]
q_ans_all=questions[,4]

all_answers <- read.csv("/home/roger/Dropbox/KTH/II2202/Zhihu/Results/2_qid_answers.csv")
vote <- all_answers[["voteup_count"]] #62894
vote20 = vote[vote>20]

df<-read.csv("/home/roger/Dropbox/KTH/II2202/Zhihu/Results/6_Processed_vote>20.csv")
length = df$length
img = df$img_count

# deal with results of topic modeling and form theta matrix
#topic<-read.csv("/home/jinhu/Dropbox/II2202/Zhihu/theta_matrix.csv")
topic<-read.csv("/home/roger/Dropbox/KTH/II2202/Zhihu/theta_matrix.csv")
topic<-topic[,2:8]
theta7<-topic
# add dummy variables, threshold as 0.14(7*0.02)
for (i in 1:7) {
  theta7[,i][which(theta7[,i]>=0.14)]<-1
  theta7[,i][which(theta7[,i]<0.14)]<-0}

data_regression<-cbind(theta7,x2)
names(data_regression)<-c("topic1","topic2","topic3","topic4","topic5","topic6","topic7","a_created_time","length","img_count","link_count","p_follower","p_answer","q_followers","q_created_time","q_answer")
#poisson_scale<-glm(y~topic1+topic2+topic3+topic4+topic5+topic6+topic7+scale(x2),data=data_regression,family=poisson())
nb_scale<-glm.nb(y~topic1+topic2+topic3+topic4+topic5+topic6+topic7+scale(x2),data=data_regression, maxit=100000)
linear<-lm(scale(y)~topic1+topic2+topic3+topic4+topic5+topic6+topic7+scale(x2),data=data_regression)

# Plot 0
vote11 <- vote[vote>10]
hist(vote11,breaks=34406,xlim=c(11,100),right=T,xaxt="n",yaxt="n",xlab="# of upvotes",main="")
axis(side=1,at=seq(10,100,5))
axis(side=2)

#Plot 1
hhist<- function(x,binsize=1,xlim=c(0,100)){
  breaks = round((max(x)-min(x))/binsize)
  hist(x,breaks=breaks,xlim=xlim)
}
hhist(vote11)

# Plot2 Powerlaw
library(poweRlaw)
pllot<- function(x,xlab="# of upvotes"){
  pl = displ$new(x)
  plot(pl,pch=20,cex=.3,col="blue",xlab=xlab,ylab="ccdf")
}
pllot(vote+1)

# Plot3 CCDF
ccdf<- function(x,xlab="",xlim=NA,pch=20){
  f<-ecdf(x)
  plot(sort(x), 1-f(sort(x)),pch=pch,cex=.3,xlab=xlab,ylab="ccdf",col="blue",
       xlim=xlim,cex.lab=.9,cex.axis=.9)
}
#===============================
i = 3
while(i<=ncol(df)){
  print(names(df)[i])
  print(sd(df[,i]))
  i=i+1
}
#================================

y<-df$a_voteup
x<-df[,4:13]
x2<-df[,5:13]
#var(y)/mean(y)
#qcc.overdispersion.test(y, type = "poisson")
#p值为0，果然该数据存在过度离势的情况，可以用类泊松模型对数据进行分析。
#offset(log(data_regression$existing_days+1))
poisson<-glm(y~a_comment+a_created_time+length+img_count+link_count+p_follower+p_answer+q_followers+q_answer,
             data=df, offset(log(df$q_created_time+1)),family=poisson())
poi<-coef(poisson)

quasipoisson<-glm(y~a_comment+a_created_time+length+img_count+link_count+p_follower+p_answer+q_followers+q_created_time+q_answer,
             data=df, family=quasipoisson())
qua<- coef(quasipoisson)
l
library(MASS)
nb.model<-glm.nb(y~a_comment+a_created_time+length+img_count+link_count+p_follower+p_answer+q_followers+q_created_time+q_answer,
                 data=df,maxit = 100000)
nb = coef(nb.model)

nb_scale<-glm.nb(y~scale(x2))
nb_sc<-coef(nb_scale)

poi_scale<-glm(y~scale(x),family=poisson())
poi_sc<-coef(poi_scale)

linear<-lm(scale(y)~scale(x))
lc <- coef(linear)
data.frame(qua,poi_sc,nb,nb_sc,lc)

logLik(poi_scale)
logLik(nb_scale)
AIC(poi_scale)
AIC(nb_scale)
BIC(poi_scale)
BIC(nb_scale)
library(rms)
vif(poi_scale)
vif(nb_scale)
