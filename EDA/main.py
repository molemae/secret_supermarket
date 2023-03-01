# %%
from utils import read_concat,resample_cus,add_entr_checkout,transition_probbability_matrix

# %%
# get and concat data
df = read_concat(path='../data/customer/')
df = resample_cus(df)
df = add_entr_checkout(df)
matrix = transition_probbability_matrix(df)

matrix


# %%
df.to_pickle('../data/cus_concat_res_entr_checkout')

# %%
# # open a file for writing
# with open('../data/transition_prob_matrix.csv', 'w') as f:
#     # write the DataFrame to the file
#     f.write(f, index=False)

