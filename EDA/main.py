# %%
from utils import read_concat,resample_cus,add_entr_checkout,transition_probability_matrix

# %%
# Transform data

# get and concat data
df = read_concat(path='../data/customer/')

# resample customer data  
df = resample_cus(df)

# Clean data by adding entrance and missing checkout data
df = add_entr_checkout(df)

# Calculate transition p
matrix = transition_probability_matrix(df)


# %%
# pickle cleaned data
# df.to_pickle('../data/transition_matrix.pkl')

# %%
# save transition probability matrix to csv
matrix.to_csv('../data/transition_matrix.csv')
