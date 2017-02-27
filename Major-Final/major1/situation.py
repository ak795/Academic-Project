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

blob = TextBlob("waiting forever")
#for sentence in blob.sentences:
print (blob.sentiment.polarity)
print (blob.polarity)


  #    print (sentence.pos_tags)


#b = TextBlob("I havve goood speling!")
#print( b.correct() )

#s1 = "I love waiting forever for my doctor."
#s = " my talents include getting ill , procrastinating and feeling sorry for myself"
s = "I hate australia in cricket, because they always win."
mystring = s.translate(None , string.punctuation)
#s = TextBlob(s)
#print s.parse()

b = TextBlob(mystring)

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

for i in mystr:
    print i , a[i]

myset  = Set()

total_words=0;

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

print ("\n values in set:  ")

positive_words=0
negative_words=0
neutral_words=0

for i in myset:
    polarity =  wordpolarity.somefunction(i)
    print (polarity)
    if polarity > 0:
        positive_words+=1
    elif polarity < 0:
        negative_words+=1
    else:
        neutral_words+=1


print "Total words=",total_words
print (positive_words)
print (negative_words)

positive_ratio = positive_words / total_words
negative_ratio = negative_words / total_words

situation_score = positive_ratio - negative_ratio

print "\n\nSituation Score = ",situation_score
