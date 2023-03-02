
import numpy as np
import pandas as pd

matrix_in = pd.read_csv('../data/transition_matrix.csv')
matrix_in.set_index('location',inplace= True)

class Customer: 
    PROBABILITIES= matrix_in.copy()
    def __init__(self,id)-> None:
        """_summary_
        Args:
            id (_type_): _description_
            state (_type_): _description_
        """

        self.id = id
        self.location = 'entrance' 
        self.active = True

    def __repr__(self) -> str:
        
        return f"Customer {self.id} is at {self.location}."

    def next_location(self):
        if self.active:
            locations = Customer.PROBABILITIES.columns
            self.location = np.random.choice(a=locations, p=Customer.PROBABILITIES.loc[self.location])
            self.active = (self.location != 'checkout')
        return None    
