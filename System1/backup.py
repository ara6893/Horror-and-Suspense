# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:07:17 2018

@author: A
"""

# -*- coding: utf-8 -*-
import os
import nltk.data
import numpy as np
n=1
listing = os.listdir('C:\\Users\\A\\Horror and Suspense\\data\\Scripts')

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
    a=1
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\forLineNum.txt','w') #writing to this one
    for doc in listing:
        with open('C:\\Users\\A\\Horror and Suspense\\data\\Scripts\\'+doc,'r') as f: #from this script
            for line in f:
                if not line.split(): #python logic that deletes empty arrays
                    continue
                if line.split()=='<b><!--\n':
                    continue
                data = line 
                data= ' '.join(data.split())
                datum.write(data)
    datum.close()
    f.close()
    
def callFile2(): #same as callFile1() but this one deletes all new lines, leaving a long single line document
    data=''       #initializing this for use later    
    a=1
    writing=open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt','w') #writing to this one
    for doc in listing:
        with open('C:\\Users\\A\\Horror and Suspense\\data\\Scripts\\'+doc,'r') as f: #from this script
            for line in f:
                if not line.split(): #python logic that deletes empty arrays
                    continue
                data = line
                data = data.strip('\n') #removes new lines so string is single line
                data= ' '.join(data.split()) #merges together all the data with spaces in between
                a=a+1
                print(a)
                writing.write(data+' ') #writes to a file with spaces between the old lines
    writing.close()
    f.close()
    
def makeSentences(): #makes the single line file into a bunch of sentences, seperated by a new line. Allows for more accurate application in the Doc2Vec model. 
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') #the object that will detect the sentence boundaries
    fp = open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt')
    data = fp.read()
    b=tokenizer.tokenize(data) #makes each into a new sentence
    newFile=open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','a')
    for line in b:
        newFile.write(line+'\n') #makes each sentence on a new line in the sentenceDoc text file
    return b
def defineBoundary():
    #array=np.array((200,1,1),dtype=[('scriptName','S10',200),('beginningLine','int8'),('endLine','int8')])
    #print(array.dtype.names)
    n=1
    b=[]
    array1=[]
    array2=[]
    array3=[]
    str1=[]
    str2=[]
    int1=[]
    with open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','r') as f:
        for line in f:
            b.append(line)
    for doc in listing:
        lineNumber=n
        array2.append(lineNumber)
        with open('C:\\Users\\A\\Horror and Suspense\\data\\Scripts\\'+doc,'r') as f: #from this script
            for line in f:
                if not line.split(): #python logic that deletes empty arrays
                    continue
                n=n+1
        array1.append(doc)
        
        array3.append(n)
            #tupleNumPy=(doc,lineNumber,n)       #need to update for the sentenceDoc value, will be more readable and accurate. Match text and finish the cosine ranking today
    for element in array2:
        string1=callLineOld(element)
        string1=' '.join(string1.split())
        str1.append(string1)
        #str2.append(callLineOld(n))
    print(str1)
    print(array2)
    for x in range(len(b)):
        str3=b[x]
        for element in str1:
            if element in str3:
                int1.append(x)
    print(int1, file=open('C:\\Users\\A\\Horror and Suspense\\data\\visualArray.txt','w'))
    print('complete')
    #for x in range(len(b)-1):
     #   str3=b[x-1]+b[x]+b[x+1]
      #  for element in str1:
       #     if element in str3:
        #        int1.append(x)
    #with open('C:\\Users\\A\\Horror and Suspense\\data\\visualArray.txt','w') as f:
        #int1.tofile(f)
