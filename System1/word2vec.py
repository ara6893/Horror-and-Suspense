from gensim import models #importing stuff, necessary for functionality

assert models.doc2vec.FAST_VERSION > -1 #recommended by package for faster results

#doc=models.doc2vec.TaggedLineDocument() #creates an object that will go into the analysis
#vocab=models.doc2vec.TaggedLineDocument()     #serves as the corpus, will eventually hold more documents

docs=[]
doc=[]
words=''
tags=0
i=0
finalTrainNum=0
with open('C:\\Users\\A\\Horror and Suspense\\data\\sentenceDoc.txt') as f:
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

model=models.Doc2Vec(dm=1,min_alpha=.05, dm_concat=1, size=400, window=3, negative=0,sample=1e-4, hs=0, iter=25)               #initializing model without a corpus, easier to add vocab later on
model.build_vocab(docs)                                             #eventually this will add all documents in our corpus
model.train(doc,total_examples=model.corpus_count, epochs=model.iter) #trains with the suspense dataset
model.save('C:\\Users\\A\\Horror and Suspense\\data\\doc2vec.model') #saves for use in another file
def returnTheEnd():
    return finalTrainNum