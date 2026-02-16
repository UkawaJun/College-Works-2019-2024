class my_class(object):
    pass
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def Fold(u,Z=10,seed = 8888):
    u = np.array(u).reshape(-1)
    id = np.array(len(u))
    zid =[]
    ID = []
    np.random.seed(seed)
    for i in np.unique(u):
        n = sum(u == i)
        ID.extend(id[u == i])
        k = ( list(range(Z)) * int(n/Z+1))
        np.random.shuffle(k)
        zid.extend(k[:n])
    zid = np.array(zid)
    ID=np.array(ID)
    zid = zid[np.argsort(ID)]
    return zid
def  CCV(clf,x,y,zid):
    y_pred = np.array(y)
    #j has z kinds of values
    for j in np.unique(zid):
        clf.fit(x[zid!=j],y[zid!=j])
        y_pred[zid == j]=clf.predict(x[zid == j])
    error = np.mean(y != y_pred)
    return (error,y_pred)

def RFold(n,z,seed):
    zid = (list(range(z))*int(n/z+1))[:n]
    np.random.seed(seed)
    np.random.shuffle(zid)
    return np.array(zid)
def RCV(reg,x,y,zid):
    y_pred = np.zeros(len(y))
    for j in np.unique(zid): #j has z kinds of values
        reg.fit(x[zid != j],y[zid != j])
        y_pred[zid == j] = reg.predict(x[zid == j])
    return( y_pred )