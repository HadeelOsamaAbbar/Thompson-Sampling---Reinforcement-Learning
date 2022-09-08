


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random,math
# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
N=10000
d=10
adsSellect=[]
numRewards_0=[0]*d
numRewards_1=[0]*d
total=0

for n in range(N):
    maxthompson=0
    ad=0
    for i in range(d):
        rndBeta=random.betavariate(numRewards_1[i]+1, numRewards_0[i]+1)
        
        if maxthompson<rndBeta:
           maxthompson =rndBeta
           ad=i
    adsSellect.append(ad) 
    rew=dataset.values[n,ad]
    if rew==1:
        numRewards_1[ad]=numRewards_1[ad]+1
    else:
        numRewards_0[ad]=numRewards_0[ad]+1
    total=total+rew
plt.hist(adsSellect)







