#@author: Mangaliso M. Mngomezulu
#description: normalizing measurements


#null hypothesis: two population's mean brain volumes are equal. The two populations are men and women
#we run a t test (statistical measure) to prove this. A t far from 0 inidcates that the hyposthesis is true

import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

#we make use of the OASIS dowoloaded csv dataset
#we customly pick the first 100
df = pd.read_csv('././datasets/oasis_brain_measurements.txt', nrows =100)

#select the sex attribute as specified and also choose the brain_vol attribute from the data
brain_m = df.loc[df.sex == 'M', 'brain_vol']
brain_f = df.loc[df.sex == 'F','brain_vol']

#print(df.head)
#print(brain_m)
results = ttest_ind(brain_m, brain_f)


#finding a correlation of two attributes
correlation = df[['brain_vol','skull_vol']].corr()

print("Correlation:",correlation)

print("t test:",results)

#add brain volume to skull volume ratio
df['brain_norm']=df.brain_vol / df.skull_vol

#comparing the normalized data
brain_m = df.loc[df.sex == 'M', 'brain_norm']
brain_f = df.loc[df.sex == 'F','brain_norm']
results = ttest_ind(brain_m, brain_f)
print(results)