# -*- coding: utf-8 -*-

from gensim import models #importing stuff, necessary for functionality
import sklearn
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
import numpy as np
assert models.doc2vec.FAST_VERSION > -1 #recommended by package for faster results
import matplotlib.pyplot as plt
#doc=models.doc2vec.TaggedLineDocument() #creates an object that will go into the analysis
#vocab=models.doc2vec.TaggedLineDocument()     #serves as the corpus, will eventually hold more documents

numClusters=4

docs=[]
doc=[]
words=''
tags=0
i=0
finalTrainNum=0
with open('C:\\Users\\A\\Horror and Suspense\\data\\masterSuspense.txt') as f:
    for line in f:
        words= line.split()
        tags=[i]
        docs.append(models.doc2vec.TaggedDocument(words,tags))
        i+=1
with open('C:\\Users\\A\\Horror and Suspense\\data\\extractedSuspense.txt') as f:
   for line in f:
       words=line.split()
       tags=[i]
       doc.append(models.doc2vec.TaggedDocument(words,tags))
       i+=1
       finalTrainNum=i

model=models.Doc2Vec(dm=1,min_alpha=.05, dm_concat=1, size=200, window=3, negative=0,sample=1e-4, hs=0, iter=20)               #initializing model without a corpus, easier to add vocab later on
model.build_vocab(docs)                                             #eventually this will add all documents in our corpus
#trains with the suspense dataset
model.save('C:\\Users\\A\\Horror and Suspense\\data\\doc2vec2.model') #saves for use in another file

def returnTheEnd():
    return finalTrainNum
def callLine(n):
    a=1
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\masterSuspense.txt','r')
    for line in datum: #loops through document, sees if line is same as desired line and returns that
        if a==n:
            return line
        a=a+1
    datum.close()
    
def kMeansAndVisual():
    x=TruncatedSVD(random_state=1,n_components=2)
    trainArray = np.zeros((int(len(model.docvecs)/2), 200))
    testArray= np.zeros((int(len(model.docvecs)/2), 200))
    print(len(model.docvecs))
    for i in range(int(len(model.docvecs)/2)):
        trainArray[i]=model.docvecs[i]
    for i in range(int(len(model.docvecs)/2)):
        testArray[i]=model.docvecs[int(len(model.docvecs)/2)+i]
    classifier=sklearn.cluster.KMeans(n_clusters=3, random_state=1)
    x.fit(trainArray)
    xTrain=x.transform(trainArray)
    classifier.fit(trainArray)
    '''
    for i in range(len(xTrain)):
        if classifier.labels_[i] == 1:
            c1 = plt.scatter(xTrain[i,0],xTrain[i,1],c='r',s=2, marker='+')
        elif classifier.labels_[i] == 0:
            c2 = plt.scatter(xTrain[i,0],xTrain[i,1],c='g',s=2,marker='o')
        elif classifier.labels_[i] == 2:
            c3 = plt.scatter(xTrain[i,0],xTrain[i,1],c='b',s=2,marker='*')
            
    '''
    cluster1=[]
    cluster2=[]
    cluster3=[]
    xTrainNew=x.inverse_transform(xTrain)
    for i in range(len(xTrain)):
        if classifier.labels_[i] == 1:
            cluster1.append(trainArray[i])
        elif classifier.labels_[i] == 0:
            cluster2.append(trainArray[i])
        elif classifier.labels_[i] == 2:
            cluster3.append(trainArray[i])
    print(classifier.score(testArray))
    plt.savefig('plot.png')
    array1=np.asarray(cluster1)
    array2=np.asarray(cluster2)
    array3=np.asarray(cluster3)
    print(len(array1[0]),len(array2),len(array3))
    return array1,array2,array3

def musicClusters():
    cluster1,cluster2,cluster3=kMeansAndVisual()
def helpFind():
    array1,array2,array3=kMeansAndVisual()
    a=[]
    b=[]
    c=[]
    for value in array1:
        for i in range(len(model.docvecs)):
            if value[0]==model.docvecs[i][0]:
                a.append(i)
    for value in array2:
        for i in range(len(model.docvecs)):
            if value[0]==model.docvecs[i][0]:
                b.append(i)
    for value in array3:
        for i in range(len(model.docvecs)):
            if value[0]==model.docvecs[i][0]:
                c.append(i)
    return a,b,c
def arrayTransfer(a):
    aNew=[]
    z=0
    with open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt','r') as f:
        for line in f:
            for i in range(len(a)):
                if callLine(a[i])==line:
                    aNew.append(z)
            z+=1 
            print(z)
    return aNew

#a,b,c=helpFind()
#print(arrayTransfer(a),arrayTransfer(b),arrayTransfer(c))