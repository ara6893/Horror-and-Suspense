# -*- coding: utf-8 -*-
import os
import nltk.data
import numpy as np
from nltk.corpus import stopwords
n=0
listing = os.listdir('C:\\Users\\A\\Horror and Suspense\\data\\Scripts')
for i in range(len(listing)):
    print(i,listing[i])
def callLine(n):
    a=1
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','r')
    for line in datum: #loops through document, sees if line is same as desired line and returns that
        if a==n:
            return line
        a=a+1
    datum.close()
    
def callLineOld(n):
    a=1
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\forLineNum.txt','r')
    for line in datum: #loops through document, sees if line is same as desired line and returns that
        if a==n:
            return line
        a=a+1
    datum.close()
    
def visualHelp(a=[]):
    data=' '
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\parsing.txt','w')
    for i in range(len(a)): #prints the elements of the array a, in terms of the inUse document
        data=callLine(a[i]) #this could get complicated with many different documents
        datum.write(data)
    datum.close()
    
def callFile1(): #writes all the scripts in the database to a single file 'inUse' for use later
    data=''       #initializing this for use later    
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\forLineNum.txt','w') #writing to this one
    for doc in listing:
        with open('C:\\Users\\A\\Horror and Suspense\\data\\Scripts\\'+doc,'r') as f: #from this script
            for line in f:
                if not line.split(): #python logic that deletes empty arrays
                    continue
                if line.split()=='<b><!--\n':
                    continue
                data=line.lower()
                wordTokens=data.split()
                stopWords = set(stopwords.words('english'))
                filteredSentence = [w for w in wordTokens if not w in stopWords]
                data=' '.join(filteredSentence)
                print(filteredSentence)
                datum.write(data)
    datum.close()
    f.close()
    
def callFile2(doc,n): #same as callFile1() but this one deletes all new lines, leaving a long single line document
    data=''       #initializing this for use later    
    a=1
    writing=open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt','w') #writing to this one
    with open('C:\\Users\\A\\Horror and Suspense\\data\\Scripts\\'+doc,'r') as f: #from this script
        for line in f:
            if not line.split(): #python logic that deletes empty arrays
                continue
            data = line
            data = data.strip('\n') #removes new lines so string is single line
            a=a+1
            data=line.lower()
            wordTokens=data.split()
            stopWords = set(stopwords.words('english'))
            stopWords.discard('no')
            stopWords.add('int.')
            stopWords.add('ext.')
            stopWords.add('1')
            stopWords.add('2')
            stopWords.add('3')
            stopWords.add('4')
            stopWords.add('5')
            stopWords.add('6')
            stopWords.add('7')
            stopWords.add('8')
            stopWords.add('9')
            stopWords.add('0')
            stopWords.add('/')
            stopWords.add('int./ext.')
            filteredSentence = [w for w in wordTokens if not w in stopWords]
            data=' '.join(filteredSentence)#merges together all the data with spaces in between
            writing.write(data+' ') #writes to a file with spaces between the old lines   
    makeSentences()
    with open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDocBetween.txt','r') as f:
        for line in f:
            n=n+1
    with open('C:\\Users\\A\\Horror and Suspense\\data\\scriptBoundaries.txt','a') as f:
        f.write(str(n)+'\n')
    writing.close()
    f.close()
    return n
    
def makeSentences(): #makes the single line file into a bunch of sentences, seperated by a new line. Allows for more accurate application in the Doc2Vec model. 
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') #the object that will detect the sentence boundaries
    fp = open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt')
    data = fp.read()
    b=tokenizer.tokenize(data) #makes each into a new sentence
    newFile=open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDocBetween.txt','w')
    for line in b:
        newFile.write(line+'\n') #makes each sentence on a new line in the sentenceDoc text file
    masterFile=open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','a')
    for line in b:
        masterFile.write(line+'\n')
    return b

def figureItOut(): #takes the documents and combines them with the callFile2 method
    n=0
    a=0
    with open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','w') as f:
        f.write('')
    with open('C:\\Users\\A\\Horror and Suspense\\data\\scriptBoundaries.txt','w') as f:
        f.write('0\n')
    for doc in listing:
        n=callFile2(doc,n)
        print(a)
        a+=1

def returnBoundaries():
    b=[]
    with open('C:\\Users\\A\\Horror and Suspense\\data\\scriptBoundaries.txt','r') as f:
        for line in f:
            b.append(int(line))
    return b

def helpMe():
    stopWords = set(stopwords.words('english'))
    print(stopWords)
    stopWords.discard('no')
    print(stopWords)