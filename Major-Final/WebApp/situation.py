from __future__ import division
import nltk
from textblob import TextBlob
from sets import Set
import nltk
from nltk import word_tokenize
from nltk import Tree
from nltk.grammar import CFG
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
import string , re
import wordpolarity

s = "I do bad things for good people."
mystring = s.translate(None , string.punctuation)
#print s.parse()

b = TextBlob(mystring)
print b.sentiment.polarity


g = str(b.parse())
x = g.split()

word_list = []

mystr = mystring.split()

space_list = x
main_list = []
#print (space_list)

for word in space_list:
    new_list = word.split("/")
    main_list.append(new_list)

a={}

k = 0

for i in main_list:
    xy = i[2].split("-")
    if len(xy) > 1 :
       #print xy[1]
       a[mystr[k]] = xy[1]
    else:
        a[mystr[k]] = xy[0]

    k = k + 1

myset  = Set()

total_words=0

n1 = b.ngrams(n=1)

for i in n1:
    total_words+=1
    if a[i[0]] == "VP" :
        myset.add(i[0])
        #print "this " , i[0]


n2 = b.ngrams(n=2)

for i in n2:
    if i[0]=="ADVP" and i[1]=="VP":
        myset.add(i[0])
        myset.add(i[1])
    elif i[0]=="VP" and i[1]=="ADVP":
        myset.add(i[0])
        myset.add(i[1])
    elif i[0]=="ADJP" and i[1]=="VP":
        myset.add(i[0])
        myset.add(i[1])
    elif i[0]=="VP" and i[1]=="NP":
        myset.add(i[0])
        myset.add(i[1])
    else:
        pass

    #print i[0],i[1]


n3 = b.ngrams(n=3)

for i in n3:
    if i[0]=="VP" and i[1]=="ADVP" and i[2]=="ADJP" :
        myset.add(i[0])
        myset.add(i[1])
        myset.add(i[2])
    elif i[0]=="VP" and i[1]=="ADJP" and i[2]=="NP":
        myset.add(i[0])
        myset.add(i[1])
        myset.add(i[2])
    elif i[0]=="ADVP" and i[1]=="ADJP" and i[2] == "NP":
        myset.add(i[0])
        myset.add(i[1])
        myset.add(i[2])
    else:
        pass

positive_words=0
negative_words =0
neutral_words = 0

for i in myset:
    polarity =  wordpolarity.somefunction(i)
    if polarity > 0:
        positive_words+=1
    elif polarity < 0:
        negative_words+=1
    else:
        neutral_words+=1


if total_words > 0:
    positive_ratio = positive_words / total_words
    negative_ratio = negative_words / total_words

    print positive_ratio , negative_ratio

    situation_score = positive_ratio - negative_ratio

    print "situation score" , situation_score