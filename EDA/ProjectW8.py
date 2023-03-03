
# %%

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import datetime as dt

# %%

df1 = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/supermarketData/monday.csv', parse_dates=True, sep=';')

# Convert to Date and Time
df1['timestamp'] = pd.to_datetime(df1['timestamp'])
# df1.info()

# %%
# ## Calculate the total number of customers in each section
df1.groupby(['location'])[['customer_no']].count().plot(kind='bar', title='Total no of customers in each section')

# df1.groupby(['location'])['customer_no'].count().plot(kind='bar')
# df1.groupby(['location', 'customer_no']).count()      #
# df1['customer_no'].unique()       # Unique customers        
# %%
# ## Calculate the total number of customers in each section over time

df_sub = df1.groupby(['location', 'timestamp'])[['customer_no']].count()


# %%
## Display the number of customers at checkout over time

df_checkout = df1[df1['location']=='checkout']

df_checkout.groupby('timestamp')[['customer_no']].count().plot(kind='line')

# Min and Max custormer ata given time
#df_checkout.groupby('timestamp')[['customer_no']].count().min()
# %%
# ## Calculate the time each customer spent in the market

df_cus = df1.groupby('customer_no')[['timestamp']].count() 

# %%
# -------------------- Customers with minimun location visits
#  
df_visit4= df1.groupby('customer_no')[['location']].count()#.plot(kind='bar', title='Total no of customers in each section')
# 
# and PRINT them
print(' > 1 & < 6    : ',df_visit4[(df_visit4['location'] > 1) & (df_visit4['location'] < 6)].count())
print(' >=6 & < 10   : ',df_visit4[(df_visit4['location'] >= 6) & (df_visit4['location'] < 10)].count())
print(' >=10 & < 15  : ',df_visit4[(df_visit4['location'] >= 10) & (df_visit4['location'] < 15)].count())
print(' >= 15        : ',df_visit4[(df_visit4['location'] >= 15)].count() )

# 
dfloc_mean = np.mean(df_visit4['location'])
print('mean : ', dfloc_mean)

dfloc_std = np.std(df_visit4['location'])
print('std : ', dfloc_std)

# Calculating probability density function (PDF)
pdf = stats.norm.pdf(df_visit4['location'].sort_values(), dfloc_mean, dfloc_std)


# Drawing a graph
plt.plot(df_visit4['location'].sort_values(), pdf)
plt.xlim([0,20])  
plt.xlabel("locations visited ", size=12)    
plt.ylabel("Frequency", size=12)                
plt.grid(True, alpha=0.3, linestyle="--")
plt.title('Distribution of number of Ailes visited')
plt.show()

# %% 
# ----------------Time spent by customers
#
#from datetime import datetime  
df_time4= df1.groupby('customer_no')[['timestamp']].count()#.plot(kind='bar', title='Total no of customers in each section')
df_time4['in'] = df1.groupby('customer_no')[['timestamp']].first()
df_time4['out'] = df1.groupby('customer_no')[['timestamp']].last()
df_time4['time spent'] = ((df_time4['out'] - df_time4['in'])) *24 * 60
df_time4['difMIN'] = df_time4['time spent'].astype(str).str[0:2].astype(int)

# Statstic calculation
dftime4_mean = np.mean(df_time4['difMIN'])
print('mean : ', dftime4_mean)

dftime4_std = np.std(df_time4['difMIN'])
print('std : ', dftime4_std)

# Calculating probability density function (PDF)
pdf_time = stats.norm.pdf(df_time4['difMIN'].sort_values(), dftime4_mean, dftime4_std)

# Drawing a graph
plt.plot(df_time4['difMIN'].sort_values(), pdf_time)
plt.xlim([0,55])  
plt.xlabel("Time spent ", size=12)    
plt.ylabel("Frequency", size=12)                
plt.grid(True, alpha=0.3, linestyle="--")
plt.title('Distribution of time spent in Supermarket')
plt.show()

# & PRINT them
print(' > 1 & < 15    : ',df_time4[(df_time4['difMIN'] > 1) & (df_time4['difMIN'] < 15)].count())
print(' >=15 & < 30   : ',df_time4[(df_time4['difMIN'] >= 15) & (df_time4['difMIN'] < 30)].count())
print(' >=30 & < 45  : ',df_time4[(df_time4['difMIN'] >= 30) & (df_time4['difMIN'] < 45)].count())
#print('<10 : ',df_time4[(df_time4['location'] > 0) & (df_time4['location'] < 10)].count())
#print(' > 10 : ',df_time4[(df_time4['location'] >= 10)].count() )
print(' >= 45        : ',df_time4[(df_time4['difMIN'] >=45)].count() )

# %%
df_avg = df1.groupby('customer_no')[['timestamp']].mean()
df_avg
#df_cus
# %%
#df_cus[df_cus['timestamp']< 2]      # Custumers that didnt checkout
df_cus['in'] = df1.groupby('customer_no')[['timestamp']].first()
df_cus['out'] = df1.groupby('customer_no')[['timestamp']].last()
df_cus['time spent'] = (df_cus['out'] - df_cus['in'])   # Time spent in the supermarket
print('Max time spent',df_cus['time spent'].max())
print('Min time spent',df_cus['time spent'].min())

# %%
# ## Calculate the total number of customers in the supermarket over time.

df_time = df1.groupby('timestamp')[['customer_no']].count()
df_time.plot(kind='line' , title='Tot no of cus over time in supermarket')
print('Max no of customer checked out at certain time : ',df_time['customer_no'].max())
print('Min no of customer checked out at certain time : ',df_time['customer_no'].min())

# %%

# ## Our business managers think that the first section customers visit follows
#  a different pattern than the following ones. Plot the distribution of customers
#  of their first visited section versus following sections (treat all sections visited
#  after the first as “following”).

#df1.groupby('customer_no')[['location']].first()

df_first_second = df1.groupby('customer_no')[['location']].nth([0,1])   # 1st & 2nd

# ------------- EDA completed -------------------

# %%

# load pickel file for probability matrix calculation

dataframe = pd.read_pickle(r'/home/myunix/TahiniTensor/spiced_projects/week8/cus_con_res_ent_check')

def transition_probbability_matrix(dataframe):
    df = dataframe

    '''This line making a new column in our dataframe with shifting the column 'location' to up'''
    df['location2'] = df['location'].shift(-1)

    '''The location2 needs some cleaning, replacing entrance with chechout. '''
    df['location2'].replace(to_replace='entrance', value='checkout', inplace=True)
    df['location2'].replace(to_replace= np.nan, value='checkout', inplace=True)

    '''Here we creat the transition matrix (probability matrix)'''
    mat = pd.crosstab(df['location'], df['location2'], normalize=0)
    return mat

Pmatrix = transition_probbability_matrix(dataframe)


# %%


# %% -------------------- Prediction and Original ----
# Distribution calculation and Plots

df1_pred = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/secret_supermarket_simulator/day1.csv', parse_dates=True, sep=',')
df1_orig = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/supermarketData/monday.csv', parse_dates=True, sep=';')

#df.head(2)
# %%
# Convert to Date and Time
df1_pred['timestamp'] = pd.to_datetime(df1_pred['Time'])
df1_orig['timestamp'] = pd.to_datetime(df1_orig['timestamp'])
# df1_pred.info()

# %%
# ## Calculate the total number of customers in each section
df1_pred.groupby(['Location'])[['Customer']].count().plot(kind='bar', title='Total no of customers in each section')
df1_orig.groupby(['location'])[['customer_no']].count().plot(kind='bar', title='Total no of customers in each section')

# %%

# -------------------- Customers with minimun location visits
#  
df_visit_pred= df1_pred.groupby('Customer')[['Location']].count()#.plot(kind='bar', title='Total no of customers in each section')
df_visit4= df1_orig.groupby('customer_no')[['location']].count()#.plot(kind='bar', title='Total no of customers in each section')

# %%
print(' > 1 & < 6    : ',df_visit_pred[(df_visit_pred['Location'] > 1) & (df_visit_pred['Location'] < 6)].count())
print(' >=6 & < 10   : ',df_visit_pred[(df_visit_pred['Location'] >= 6) & (df_visit_pred['Location'] < 10)].count())
print(' >=10 & < 15  : ',df_visit_pred[(df_visit_pred['Location'] >= 10) & (df_visit_pred['Location'] < 15)].count())
#print('<10 : ',df_visit_pred[(df_visit_pred['Location'] > 0) & (df_visit_pred['Location'] < 10)].count())
#print(' > 10 : ',df_visit_pred[(df_visit_pred['Location'] >= 10)].count() )
print(' >= 15        : ',df_visit_pred[(df_visit_pred['Location'] >= 15)].count() )

# %%
dflocpred_mean = np.mean(df_visit_pred['Location'])
dflocorig_mean = np.mean(df_visit4['location'])
print('mean : ', dflocpred_mean)

dflocpred_std = np.std(df_visit_pred['Location'])
dflocorig_std = np.std(df_visit4['location'])
print('std : ', dflocpred_std)

# Calculating probability density function (PDF)
pdf_pred = stats.norm.pdf(df_visit_pred['Location'].sort_values(), dflocpred_mean, dflocpred_std)
pdf_orig = stats.norm.pdf(df_visit4['location'].sort_values(), dflocorig_mean, dflocorig_std)

# Drawing a graph
plt.plot(df_visit_pred['Location'].sort_values(), pdf_pred, label='Predicted')
plt.plot(df_visit4['location'].sort_values(), pdf_orig, label='Original')

plt.xlim([0,20])  
plt.xlabel("Locations visited ", size=12)    
plt.ylabel("Frequency", size=12)                
plt.grid(True, alpha=0.3, linestyle="--")
plt.title('Distribution of number of Ailes visited by customers')
plt.legend(loc='upper right')
plt.show()


# plt.plot(df_time_pred['Time'].sort_values(), pdf_time_pred, label='Predicted')
# plt.plot(df_time_orig['timestamp'].sort_values(), pdf_time_orig, label='Original')

# plt.xlim([0,20])  
# plt.xlabel("Locations visited ", size=12)    
# plt.ylabel("Frequency", size=12)                
# plt.grid(True, alpha=0.3, linestyle="--")
# plt.title('Distribution of number of Ailes visited by customers')
# plt.legend(loc='upper right')
# plt.show()

