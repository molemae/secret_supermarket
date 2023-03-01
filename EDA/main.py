# %%
from utils import read_concat,resample_cus,add_entr_checkout

# %%
# get and concat data
df = read_concat(path='../data/customer/')
df = resample_cus(df)
df = add_entr_checkout(df)
df.head()
# %%

with open(df, mode='w') as file:
    file.write('../data/probability_matrix.csv')

# %%
