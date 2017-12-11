from gensim import corpora, models, similarities
import numpy as np

def preprocessing():
    j=0
    i=0
    a=np.full((30,11000), "               ")
    stopWords=set(['the','a','an','but','to','as','in','and'])
    temporary=open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt','r')
    for line in temporary:
        b=line.lower().split()
        for i in range(len(b)):
            data=b[i]
            if(any(word in stopWords for word in b)):
                continue
            else:
                a[i][j]=data
        j=j+1
    with open('C:\\Users\\A\\Horror and Suspense\\data\\parsing.txt','w') as f:
        f.seek(0)
        a=np.core.defchararray.strip(a)
        for j in range(len(a[0])):
            for i in range(len(a)):
                f.write(a[i][j]+" ")
      
    #start to make a dictionary that reflects suspense
    #use dictionary synonyms
    websterSynonyms=[["anxiety","apprehension","confusion","doubt","insecurity","tension","thriller",'uncertainty','chiller','dilemma','eagerness','expectancy','expectation','grabber','hesitancy','hesitation','impatience','indecision','indecisiveness','irresolution','perplexity','potboiler','wavering'],
                    ["b","j"]]
    #["anxiety","apprehension","confusion","doubt","insecurity","tension","thriller"]#,'uncertainty','chiller','dilemma','eagerness','expectancy','expectation','grabber','hesitancy','hesitation','impatience','indecision','indecisiveness','irresolution','perplexity','potboiler','wavering']
    dictionary=corpora.Dictionary(websterSynonyms)
    dic=dictionary.doc2bow(a)  
    corpus=corpora.textcorpus.TextCorpus(input='C:\\Users\\A\\Horror and Suspense\\data\\parsing.txt')
    #lsi = models.lsimodel.LsiModel(corpus, id2word=dictionary, num_topics=10)
    corpora.MmCorpus.serialize('C:\\Users\\A\\Horror and Suspense\\data\\corpora.mm',corpus)
    tfIDF=models.TfidfModel(corpus)
    print(dic)
    #similarity=similarities.MatrixSimilarity(tfIDF[corpus],0)
    #similarity=similarities.Similarity('\temp',tfIDF[corpus],500)
    #query=similarity['suspense']
#for line in toUse:
    
       # print(word)
        #if word in stoplist:
            #toUse.write(' ')
preprocessing()