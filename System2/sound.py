# -*- coding: utf-8 -*-
import numpy as np
import math
import wave, struct, math
import os
import doc2vec
import System1.addfiles

a=System1.addfiles.returnBoundaries()
cluster1,cluster2,cluster3= doc2vec.kMeansAndVisual()
sampleRate = 44100.0 # hertz
duration = a[1]-a[0] #2*(a[1]-a[0])      # seconds
frequency = [440.0,390,340]    # hertz
b=np.fromfile('C:\\Users\\A\\Horror and Suspense\\data\\suspenseArray.txt', sep=" ")
wavef = wave.open('sound.wav','w')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2) 
wavef.setframerate(sampleRate)

def returnSound():
    for i in range(int(duration * sampleRate)):
        value =np.random.randint(0,30000)
        data = struct.pack('<h', value)
        wavef.writeframesraw( data )

    wavef.close()
    os.system("sound.wav")

#need to create a file with length of the script