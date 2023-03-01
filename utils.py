# TODO: implemet Supermarket and blabalba
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