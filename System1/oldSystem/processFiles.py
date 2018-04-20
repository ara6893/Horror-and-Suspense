from gensim import corpora, models, similarities
import numpy as np
import operator as op
import pyspark
def preprocessing():
    j=0
    data=' '
    #i=0
    a=[]
    #a=np.full((30,11000), "               ")
    #stopWords=set(['the','a','an','but','to','as','in','and'])
    #temporary=open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt','r')
    #for line in temporary:
    #    b=line.lower().split()
    #    for i in range(len(b)):
    #        data=b[i]
    #        if(any(word in stopWords for word in b)):
    #            continue
    #        else:
    #            a[i][j]=data
    #    j=j+1
    #with open('C:\\Users\\A\\Horror and Suspense\\data\\parsing.txt','w') as f:
    #   f.seek(0)
    #   a=np.core.defchararray.strip(a)
    #   for j in range(len(a[0])):
    #       for i in range(len(a)):
    #           f.write(a[i][j]+" ")
      
    #start to make a dictionary that reflects suspense
    #use dictionary synonyms
    websterSynonym=["anxiety apprehension confusion doubt insecurity tension thriller uncertainty chiller dilemma eagerness expectancy expectation grabber hesitancy hesitation impatience indecision indecisiveness irresolution perplexity potboiler"]
    websterSynonyms=["anxiety apprehension confusion doubt insecurity tension thriller uncertainty chiller",
                     "dilemma eagerness expectancy expectation grabber hesitancy hesitation impatience",
                     "indecision indecisiveness irresolution perplexity potboiler"]
    texts = [[word.lower() for word in text.split()] for text in websterSynonyms]
    dictionary=corpora.Dictionary(texts)
    corpus=corpora.textcorpus.TextCorpus(input='C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt')
    dictionary.save('C:\\Users\\A\\Horror and Suspense\\data\\visualEx.txt')
    #lsi = models.lsimodel.LsiModel(corpus, id2word=dictionary, num_topics=10)
    corpora.MmCorpus.serialize('C:\\Users\\A\\Horror and Suspense\\data\\corpora.mm',corpus)
    tfIDF=models.TfidfModel(corpus)
    str1=' '.join(websterSynonym).split()
    txt=dictionary.doc2bow(str1)
    compareTo=tfIDF[txt]
    similarity=similarities.Similarity('C:\\Users\\A\\Horror and Suspense\\data\\temp',tfIDF[corpus],9000)
    query=similarity[compareTo]
    sims = sorted(enumerate(query), key=lambda query: query[1])
    print(sims)
    for item in sims:
        if item[1]<=0:
            continue
        else:
            a.append(item[0])
        #if item[]==0:
         #   continue
        #else:
    visualHelp(a)
        #    a.append(item)
#for line in toUse:
    
       # print(word)
        #if word in stoplist:
            #toUse.write(' ')
    return a, sims
preprocessing()