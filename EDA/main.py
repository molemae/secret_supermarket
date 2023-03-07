# %%
from utils import read_concat,resample_cus,add_entr_checkout,transition_probbability_matrix

# %%
# get and concat data
df = read_concat(path='../data/customer/')
df = resample_cus(df)
df = add_entr_checkout(df)
matrix = transition_probbability_matrix(df)


# %%
# pickle cleaned data
df.to_pickle('../data/cus_concat_res_entr_checkout')

# %%
matrix.to_csv('../data/transition_matrix.csv')

# %%
