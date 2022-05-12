#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'x':[1,2,5,3],
    'y':[2,1,2,0]
})  
def kmeans(df , k):
    cluster1 =[]
    cluster2 =[]
    clustercentroid1 = [df.iloc[1].values[0] , df.iloc[1].values[1]]
    clustercentroid2 = [df.iloc[2].values[0] , df.iloc[2].values[1]]
    labels = [0,0,0,0]
    n=0
    while(n<2):
        for i in range(0 , df.shape[0]):
            onedist = euclideandist(clustercentroid1 ,  df.iloc[i].values)
            print("the distance of ", i , "with 1st cluster is " , onedist)
            twodist = euclideandist(clustercentroid2 ,  df.iloc[i].values)
            print("the distance of ", i , "with 2st cluster is " , twodist)
            if onedist<=twodist:
                labels[i]=0
                cluster1.append([df.iloc[i].values[0] , df.iloc[i].values[1]])

            else:
                labels[i]=1
                cluster2.append([df.iloc[i].values[0] , df.iloc[i].values[1]])
        xcen = 0 
        ycen = 0 
        for i in cluster1:
               xcen = i[0]+xcen
               ycen = i[1]+ycen
               clustercentroid1 = [xcen/len(cluster1)  , ycen/len(cluster1)]
        xcen = 0 
        ycen = 0
        for i in cluster2:
               xcen = i[0]+xcen
               ycen = i[1]+ycen
               clustercentroid2 = [xcen/len(cluster2)  , ycen/len(cluster2) ]
        n+=1
        print("the cluster one contains" , cluster1)
        print("the updated centroid for cluster one is " , clustercentroid1)
        print("the cluster two contains" , cluster2)
        print("the updated centroid for cluster two is " , clustercentroid2)
        clusterone = cluster1
        clustertwo = cluster2
        cluster1 =[]
        cluster2 =[]
    colors = ["red","blue"]
    
    plt.scatter(df.iloc[:,0], df.iloc[:,1], c=np.array(colors)[labels])
  

    return labels , clusterone , clustertwo ,clustercentroid1 , clustercentroid2
    
def euclideandist(x, y):
    sumx = (x[0] - y[0])**2
    sumy = (x[1] - y[1])**2
    return np.sqrt(sumx + sumy)
    

