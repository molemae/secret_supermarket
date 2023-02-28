# %%
# Import 
import os

import pandas as pd
import numpy as np

import seaborn as sns

#%%
path = 'data/customer/'
filelist = os.listdir(path=path)

# %%
def resample_cus(df):
    df = df.groupby('customer_no').resample('1T').ffill()
    df = df.set_index(df.index.droplevel())
    return df
    

# %%
# add checkout:
def add_checkout(df_r):
    for cus in df_r['customer_no'].unique():
        sliced = df_r[df_r['customer_no']== cus]
        if sliced.iloc[-1]['location']!='checkout':
            print('Look here: ',cus)
            print(sliced)

            # get last timestamp
            ts = sliced.index[-1] + pd.DateOffset(minutes=1)
            
            c_row = {'timestamp':ts,
                    'customer_no':cus,
                    'location':'checkout'
                    } 
            
            c_df = pd.DataFrame(data=c_row,index=[1])
            c_df = c_df.set_index(['timestamp'])
            print('-------------------------------------')
            print(type(df_r))
            print('\n',type(c_df))
            df_r = pd.concat([df_r,c_df])
    return df_r

add_checkout(df)

# %% 















    # for cus in df_r['customer_no'].unique():
    #     if df_r.loc[[cus]].iloc[-1]['location']!='checkout':
    #         print('Look here: ',cus)
    #         print(df_r.loc[[cus]])
    #         df_r.loc[[cus]]
    #         # get last timestamp
    #         ts_last = df_r.loc[[1]].index.droplevel()[-1]
    #         ts = ts_last + pd.DateOffset(minutes=1)
            
    #         c_row = {'timestamp':ts,
    #                 'customer_no':cus,
    #                 'location':'checkout'
    #                 } 
            



# %%
df_list=list()
for idx,file in enumerate(filelist):
    df = pd.read_csv(filepath_or_buffer=path+file,sep=";")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')


    # resample
    df = resample_cus(df)

 
    ##
    df_r.set_index(df_r.index.droplevel())

    pd.DateOffset(minute=1)
    ##
    # generate new Customer No:
    if 'max_day_no' in locals():
        print('Iteration ',idx,':',max_day_no)
        df['customer_no']
    max_day_no = df['customer_no'].max()
    # append into list of dfs
    df_list.append(df)
    # append all dfs into one
    if idx == 0:
        df_all = df
    else:
        df_all = pd.concat([df_all,df])
del max_day_no
df = df_list[0]
df_all.info()

#%% 
df.head()
locations = df['location'].unique()
no_of_customers = len(df['customer_no'].unique())


# %%
def eda_day(df):
    locations = df['location'].unique()
    
    # Calculate the total number of customers in each section
    cus_total = len(df['customer_no'].unique())
    cus_total_per section df.groupby(['location'])['customer_no'].sum()

    # Calculate the total number of customers in each section over time
    cus_per_section = df.groupby(['location','timestamp'])['customer_no'].count()

# %%
