import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


df = pd.read_csv("singer.csv")
print("基础数据:\n",df.head())
#该为8水平的目标变量 voice.part

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import cross_val_score

import graphviz
y = df['voice.part']
x = df['height'].values.reshape(-1,1)
#一定要转化为列向量
print(df['voice.part'])
clf = DecisionTreeClassifier(random_state=0)	#criterion = 'gini'
clf = clf.fit(x,y)
dot_data = tree.export_graphviz(clf,out_file=None)
graphs = graphviz.Source(dot_data)
graphs.render("singerDecisionTree")


#检测 误判率
pred = clf.predict(x)
print(pred)
val = np.mean(clf.predict(x) != y)
print("误判率 = ",val)
