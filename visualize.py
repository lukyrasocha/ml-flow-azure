import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

runs = pd.read_csv('runs.csv')

lin_reg = runs[runs['model_name']=='lin_reg']
knn_reg = runs[runs['model_name']=='knn']

lin_reg['ids'] = lin_reg.index
knn_reg['ids'] = knn_reg.index

lin_reg = lin_reg.loc[(lin_reg.ids != 17) & (lin_reg.ids !=18)]

plt.figure(1)
plt.title('Linear Regression Runs')
sns.barplot(x="ids", y="mean_r2", data=lin_reg,linewidth=2.5, facecolor=(1, 1, 1, 0),errcolor=".2", edgecolor=".2")
plt.savefig('lin_reg.png')
plt.figure(2)
plt.title('KNN Regression Runs')
sns.barplot(x="ids", y="mean_r2", data=knn_reg,linewidth=2.5, facecolor=(1, 1, 1, 0),errcolor=".2", edgecolor=".2")
plt.savefig('knn_reg.png')

print('Best Lin regression')
print(lin_reg[lin_reg['mean_r2'] == max(lin_reg['mean_r2'])])

print('Best KNN')
print(knn_reg[knn_reg['mean_r2'] == max(knn_reg['mean_r2'])])

