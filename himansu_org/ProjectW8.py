
# %%

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# %%

df1 = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/supermarketData/monday.csv', parse_dates=True, sep=';')
#df_tue = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/supermarketData/tuesday.csv', parse_dates=True, sep=';')
#df_wed = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/supermarketData/wednesday.csv', parse_dates=True, sep=';')
#df_thu = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/supermarketData/thursday.csv', parse_dates=True, sep=';')
#df_fri = pd.read_csv('/home/myunix/TahiniTensor/spiced_projects/week8/supermarketData/friday.csv', parse_dates=True, sep=';')

#df.head(2)
# %%
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
#df_cus

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


