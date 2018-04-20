from gensim import models
from System1 import addfiles,word2vec
import numpy as np
import random
import os
from sklearn.linear_model import LogisticRegression
#n=
listing = os.listdir('C:\\Users\\A\\Horror and Suspense\\data\\Scripts')
array=np.zeros((400000,1,2)) #an array to hold all the similarDocument tuple values, 1st value is number of similarDoc objects, second is num rows then columns
b=[]

model=models.Doc2Vec.load('C:\\Users\\A\\Horror and Suspense\\data\\doc2vec.model') #loads model
def createRankingArray(): #creates an array that has all the script lines as inputs, outputting their most related line number and cosine values
    n=0
    with open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','r') as f:
        for line in f:
            inferVector=model.infer_vector(line.split()) #generates a vector for comparison with the model
            similarDocuments = model.docvecs.most_similar([inferVector], topn = 10) #predicts similar paragraph vectors

            for doc in similarDocuments: #loops over similarDocuments tuple
                array[n,0,0]=doc[0] #writes first column as tuple with 10 objects, all line nums
                array[n,0,1]=doc[1] #writes second column as tuple with 10 objects all cosine similarity
            n=n+1                   #defines the number the array is on
            print(n)
    array.tofile('C:\\Users\\A\\Horror and Suspense\\data\\numPy.txt', sep=" ") #writes the numPy array to a file
def getKey(item):
    return item[0]
def getKey2(item):
    return item[1]
def manageRankingArray():
    a=np.fromfile('C:\\Users\\A\\Horror and Suspense\\data\\numPy.txt',sep=" ")
    a.reshape((400000,1,2))
    n=0
    b=[]
    c=[]
    b.append(a[0])
    for element in a[:]:
        #if a[n]==a[n+1]:
            #continue   
        if element<1:
            c.append(element)
        else:
            b.append(element)
        n+=1
    d=list(zip(b, c))
    d=sorted(d, key=getKey)
    return d

def scriptBoundaries(d,start=int,end=int):
    #x=tuple(n[start:end] for n in d)
    #print(x)
    a=[]
    b=[]
    i=0
    x=end-start
    #for n in range(len(d)):
    #    if d[n][0]==start:
    #        i=n
    #        break
    #    if d[n][0]+3>=start and d[n][0]-3<=start:
    #        i=n
    #        break
    #print(i)
    for n in range(x):
        try:
            i=d[start+n][0]
        except IndexError:
            print('something happened')
            break
        a.append(d[start+n])
    y=int(len(a)/30)
    #number of results
    print(y)
    a=sorted(a,key=getKey2, reverse=True)
    for n in range(y):
        b.append(a[n])
    return b
    #extractedData=a[:,[0]]
def something():
    g=[]
    with open('C:\\Users\\A\\Horror and Suspense\\data\\scriptBoundaries.txt','r') as f:
        for line in f:
            g.append(int(line))
#d=manageRankingArray()
    b=manageRankingArray()
    n=0
    for n in range(len(g)-1):
        print(scriptBoundaries(b,g[n],g[n+1]))
        n+=1
def extractLineNumber(scriptNumber=int):
    g=[]
    a=[]
    b=0
    with open('C:\\Users\\A\\Horror and Suspense\\data\\scriptBoundaries.txt','r') as f:
        for line in f:
            g.append(int(line))
#d=manageRankingArray()
    d=manageRankingArray()
    print(len(d),scriptNumber,g[scriptNumber])
    b=scriptBoundaries(d,g[scriptNumber],g[scriptNumber+1])
    for element in b:
        a.append(element[0])
    addfiles.visualHelp(a)
    return(a)
    
def everythingToOneFile():
    n=0
    a=np.zeros(1)
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\masterSuspense.txt','w')
    for doc in listing:
        a=np.append(a,extractLineNumber(n))
        n+=1
        with open('C:\\Users\\A\\Horror and Suspense\\data\\parsing.txt','r') as f:
            for line in f:
                datum.write(line)
        print(len(a))
    a.tofile('C:\\Users\\A\\Horror and Suspense\\data\\suspenseArray.txt', sep=" ")
#datum=open('c:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','w')
#with open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDocCopy.txt','r') as f:
#    for line in f:
#        if not line.split():
#            continue
#        datum.write(line)

#thing=model.infer_vector('The Alien moves closer.  '.split())
#similar=model.docvecs.most_similar([thing], topn = 10)
#print(similar)
def createRankingArray2(): #creates an array that has all the script lines as inputs, outputting their most related line number and cosine values
    n=0
    with open('C:\\Users\\A\\Horror and Suspense\\data\\boom.txt','r') as f:
        for line in f:
            inferVector=model.infer_vector(line.split()) #generates a vector for comparison with the model
            similarDocuments = model.docvecs.most_similar([inferVector], topn = 10) #predicts similar paragraph vectors

            for doc in similarDocuments: #loops over similarDocuments tuple
                array[n,0,0]=doc[0] #writes first column as tuple with 10 objects, all line nums
                array[n,0,1]=doc[1] #writes second column as tuple with 10 objects all cosine similarity
            n=n+1                   #defines the number the array is on
            print(n)                #visual aid
            array.tofile('C:\\Users\\A\\Horror and Suspense\\data\\numPy.txt', sep=" ") #writes the numPy array to a file