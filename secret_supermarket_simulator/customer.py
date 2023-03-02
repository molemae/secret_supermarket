""" Skeleton for Customer
"""
# %%
import numpy as np
import pandas as pd

matrix = pd.read_csv('../data/transition_matrix.csv')
matrix.info()
matrix.set_index('location',inplace= True)
locations = matrix.index
pmatrix = np.array(matrix)

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
        self.location = np.random.choice(locations, 1, p=list(matrix.loc[self.location]))
        return self.location
    

    def is_active(self):
        if self.location == 'checkout':
            self.active = False
        return None
    


# %%
