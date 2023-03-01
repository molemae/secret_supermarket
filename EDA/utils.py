''' All the functions we need to use will be stored here.'''
# %%
# Import 
import os
import pandas as pd
import numpy as np
#%%

# function: read in files 
def read_concat(path='data/customer/',date_col='timestamp'):
    """ Read in csv-files in subfolder, set datetime to index, 
     give new customer_no, concat all data_frames into one."""    
    filelist = os.listdir(path=path)
    for idx,file in enumerate(filelist):
        # read data
        df = pd.read_csv(filepath_or_buffer=path+file,sep=";")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp')

        # create df for return 
        if idx == 0:
            df_all = df
        else:
            # generate new Customer No:
            df['customer_no'] += max_day_no
            # Concat
            df_all = pd.concat([df_all,df])
        max_day_no = df['customer_no'].max()
    df_all = df_all.sort_index()
    return df_all

# Resampling 
def resample_cus(df):
    ''' Resampling the input data to get one data point per minute per customer '''
    df = df.groupby('customer_no').resample('1T').ffill()
    df = df.set_index(df.index.droplevel())
    return df

# %%



# add entrance row and checkout row if it is missing:
def add_entr_checkout(df):
    """ Add entrance row and checkout if checkout is missing"""
    # function: set index to timestamp:
    def index_to_timestamp(df,index=['index','level_0']):
        """ Reset index and drop colum index if created"""
        df = df.reset_index().set_index('timestamp').drop(index,axis=1,errors='ignore')
        return df

    df = df.reset_index()
    # add entry
    ent = df.groupby('customer_no').nth(0)
    ent['timestamp']  += pd.DateOffset(minutes=-1)
    ent['location'] = 'entrance'

    # get customer where last location not checkout:
    lloc=df.groupby('customer_no').nth(-1)
    mask=list(lloc['location']!='checkout')
    lloc = lloc[mask]
    # create missing checkout data
    lloc['timestamp'] += pd.DateOffset(minutes=1)
    lloc['location'] = 'checkout'

    # reset indexes to timestamp

    df = index_to_timestamp(df)
    ent = index_to_timestamp(ent)
    lloc = index_to_timestamp(lloc)

    # concat input df, entry and checkout columns
    out = pd.concat([df,lloc,ent]).sort_values(['customer_no','timestamp'])
    # return out
    return out


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