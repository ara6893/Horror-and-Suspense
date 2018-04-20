# -*- coding: utf-8 -*-

from gensim import models #importing stuff, necessary for functionality

assert models.doc2vec.FAST_VERSION > -1 #recommended by package for faster results

doc=models.doc2vec.TaggedLineDocument('C:\\Users\\A\\Horror and Suspense\\data\\boom.txt') #creates an object that will go into the analysis
vocab=models.doc2vec.TaggedLineDocument('C:\\Users\\A\\Horror and Suspense\\data\\boom2.txt')     #serves as the corpus, will eventually hold more documents
model=models.Doc2Vec(dm=1, dm_concat=1, size=150, window=3, negative=5,sample=1e-4, hs=0)               #initializing model without a corpus, easier to add vocab later on
model.build_vocab(vocab)                                             #eventually this will add all documents in our corpus
for epoch in range(10):                                              #10 test runs
    model.train(doc,total_examples=model.corpus_count, epochs=epoch) #trains with the suspense dataset
model.save('C:\\Users\\A\\Horror and Suspense\\data\\doc2vec.model') #saves for use in another file