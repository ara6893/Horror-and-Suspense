# -*- coding: utf-8 -*-
import os
a=0
n=1
listing = os.listdir('C:\\Users\\A\\Horror and Suspense\\data')
def callFile(n):
    data=''
    print(listing[n])
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt','w')
    with open('C:\\Users\\A\\Horror and Suspense\\data\\'+listing[n],'r') as f:
        for line in f:
            data = line
            datum.write(data)     
    datum.close()
    f.close()
def returnFile(n):
    data=''
    a=[]
    b=[]
    print(listing[n])
    datum=open('C:\\Users\\A\\Horror and Suspense\\data\\inUse.txt','w')
    with open('C:\\Users\\A\\Horror and Suspense\\data\\'+listing[n],'r') as f:
        for line in f:
            data = line
            b.append(data)
            a.append(b)
    datum.close()
    f.close()
    return a
def numLines(n):
    a=0
    callFile(n)
    with open('C:\\Users\\A\\Horror and Suspense\\data\\'+listing[n],'r') as f:
        for line in f:
            a=a+1
            print(a)
            
print(returnFile(3))