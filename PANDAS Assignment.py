#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[3]:


df


# In[110]:


df.dtypes


# In[82]:


df


# In[92]:


# Find out how many male and female passenger are onboarded

print("The total male passenger in the ship are ",len(df[df["Sex"]=="male"]),"\n"
,"The total female passenger in the ship are ",len(df[df["Sex"]=="female"]))


# In[107]:


#Find out how many surrived we have
#Find out how many casulity we have

print("The total number of people survived are ",len(df[df["Survived"]==1]))
print("The total number of people casulity are ",len(df[df["Survived"]==0]))
print("The total are ",len(df[df["Survived"]==1])+len(df[df["Survived"]==0]))


# In[112]:


# Find out name of person who is eldest one

df[df["Age"]==max(df["Age"])]["Name"]


# In[113]:


df.columns


# In[124]:


#Find out the how many passenger do we have in first ,second ,third class

print("The Total number os first  class passenger is ",  len(df[df["Pclass"]==1]))
print("The Total number os second class passenger is ", len(df[df["Pclass"]==2]))
print("The Total number os third  class passenger is ",  len(df[df["Pclass"]==3]))


# In[167]:


#Find out how many persons whos name starts with s
l=[]
for i in df["Name"]:
    if i[0]=="S":
        l.append(i)
print(l)
print(len(l))


# In[175]:


df[["SibSp","Parch"]]


# In[182]:


#Try to  create new column which is summation of "Sibsp" and "Parch"

df["Sum_of_Sibsp_&_Parch"]=(df["SibSp"] +df["Parch"])


# In[186]:


df


# In[192]:


# How many persons do we have below age 25
print("The total num of people whose age is below 25 is ",len(df[df["Age"]<25]))


# In[312]:


df[df["Age"]<25].to_csv("AGE.csv")


# In[448]:


#How many persons died whose age is less than 40
l=[]
for i in df[df["Age"]<40].index:
    for j in df[df["Survived"]==0].index:
        if i==j:
            l.append(i)
print(l)
print(len(l))


# In[446]:


#How many persons died whose age is less than 40
ind=(df[df["Age"]<40])
(ind["Survived"]==0)
l=[]
for i in (ind["Survived"]==0):
    if i == True:
        l.append(i)

print(len(l))


       


# # From a cabin column seprate txt and numeric value
#  
# for i in df[df["Cabin"].notnull()].index:
#     q=df["Cabin"][i]
#     for j in q:
#         if j==str:
#             print(q)
#             
# #NOT ABLE TO COMPLETE            

# In[780]:


df["Cabin"][1]


# In[779]:


df[df["Cabin"].notnull()]


# In[762]:


[df["Cabin"]]


# In[743]:


for i in df[["Cabin"]].index:
    print(i)


# #  Another Bank data set

# In[316]:


df1=pd.read_csv(r"C:\Users\lohit\Downloads\bank\bank.csv",sep=';')


# In[317]:


df1.columns


# In[318]:


df1


# In[337]:


for i in [(df1[["housing","loan"]]=="yes")]:
    print(i)


# In[361]:


l=[]
for i in df1[ df1["housing"]=="yes"].index:
    for j in df1[ df1["loan"]=="yes"].index:
        if i==j:
            l.append(j)
            
print(l)
print(len(l))            


# In[356]:


df1[df1["loan"]=="yes"]


# In[374]:


df1["education"].unique()


# In[372]:


df1


# In[676]:


#how many camaign available in this data set
s=[]
for i in df1["campaign"]:
    s.append(i)
    se=set(s)
print(se)    
    
    


# In[678]:


df1["campaign"].unique()


# In[393]:


#how many users do we have with housing and personal loan 
l=[]
for i in df1[ df1["housing"]=="yes"].index:
    for j in df1[ df1["loan"]=="yes"].index:
        if i==j:
            l.append(j)
            
print(l)
print("The total number of users having both personal and housing loan are  ",len(l))    


# In[402]:


#how many persons do we have whose age is 60+

print("The total number of persons whose age is 60+ are " ,len(df1[df1["age"]>60].index))


# In[426]:


#in which month we have trageted most of the customer


df1[["month"]].describe()


# In[538]:


l=[]
for i in df1[df1['month']=="may"].index:
    l.append(i)
print(l)
print("The total number of custmer are joined in month of may are " ,len(l))


# In[461]:


df1["month"].unique()


# In[527]:


def month(a):
    l=[]
    for i in df1[df1['month']==a].index:
        l.append(i)
    return("The total number of custmer are joined in month of {} are ".format(a) ,len(l))
        


# In[514]:


def month1(a):
    l=[]
    for i in df1[df1['month']==a].index:
        l.append(i)
    return(len(l))
        


# In[500]:


month("apr")


# In[536]:


l=[]
for i in df1["month"].unique():
    l.append(month(i))
l


# In[519]:


l=[]
for i in df1["month"].unique():
    l.append(month1(i))
print(sum(l))


# In[473]:


min(df1["month"])


# In[550]:


# Which mode of call is giving you more result
for i in df1["contact"].describe():
    for j in df1["contact"].unique():
        if i==j:
            print(i)
    


# In[548]:


df1["contact"].unique()


# In[580]:


for i in df1["contact"].unique():
    q=len(df1[df1['contact']==i].index)
    print("The total num of custmer contact through {} mode are ".format(i),q)


# In[624]:


# How many Entrepreneur do we have in the list and make them seperate column for them

df1["Extra_Loan"]=(df1["job"]=="entrepreneur")


# In[668]:


# How many custmers do we have negative balance
l=[]
bal=df1[df1["balance"]<0].index
for i in bal:
    l.append(i)
print(l)
print("The toal number of custmer's having negative balance are ",len(l))


# In[667]:


(df1[df1["balance"]<0]


# In[ ]:





# In[703]:


#prepare group of data based on education

for i in df1["education"].unique():
    w=df1[df1["education"]==i].index
    q=len(df1[df1["education"]==i].index)
    print("The custmers who are having {} education are ".format(i),q,"\n","they are",w)


# In[ ]:




