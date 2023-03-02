""" Skeleton for Customer
"""
# %%
import numpy as np
import pandas as pd

matrix_in = pd.read_csv('../data/transition_matrix.csv')
matrix_in.info()
matrix_in.set_index('location',inplace= True)
locations_in = matrix_in.index
pmatrix = np.array(matrix_in)

# %%

#transition_probability_matrix
class Customer:
    def __init__(self,id, location='entrance')-> None:
        """_summary_

        Args:
            id (_type_): _description_
            state (_type_): _description_
        """

        self.id = id
        self.location = location 
        self.active = True

    def __repr__(self) -> str:
        
        return f"Customer {self.id} is at {self.location}."

    def next_location(self,locations,matrix):
        self.location = np.random.choice(locations, 1, p=list(matrix.loc[self.location]))[0]
        return self.location
    

    def is_active(self):
        if self.location == 'checkout':
            self.active = False
        return None
    


# %%
