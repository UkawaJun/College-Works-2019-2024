import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print(os.getcwd())
#os.chdir("D:/hl")

df = pd.read_csv("simple4.csv")

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import cross_val_score

import graphviz

#-------------------------------------------

print(df)
print("初始数据")

#转换为哑元变量
X = pd.get_dummies(df.iloc[:,1:],drop_first= False)
y = df.iloc[:,0]
print(X,'\n',y)


clf = DecisionTreeClassifier(random_state=0)	#criterion = 'gini'
clf = clf.fit(X,y)
dot_data = tree.export_graphviz(clf,out_file = None,
	feature_names= X.columns,rounded = True,filled = True)
graph = graphviz.Source(dot_data)
graph.render("simple4py")
graph

#检测 误判率
pred = clf.predict(X)
print(pred)
val = np.mean(clf.predict(X) != y)
print("误判率 = ",val)

