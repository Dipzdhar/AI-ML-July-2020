import pandas as pd
dataset=pd.read_excel("correlation.xlsx",sheet_name=1)
from scipy.stats import pearsonr
print(dataset)
dataset.Attrition.replace(('Yes', 'No'), (1, 0), inplace=True)
stats,p= pearsonr(dataset.Attrition,dataset.DistanceFromHome)
print("correlation between Attrition and Distance from home : ",stats,p)

stats,p= pearsonr(dataset.Attrition,dataset.Age)
print("correlation between Attrition and Age : ",stats,p)

stats,p= pearsonr(dataset.Attrition,dataset.Education)
print("correlation between Attrition and Education : ",stats,p)

stats,p= pearsonr(dataset.Attrition,dataset.JobLevel)
print("correlation between Attrition and Job level : ",stats,p)

import matplotlib.pyplot as plt
plt.scatter(dataset.Attrition,dataset.DistanceFromHome)


