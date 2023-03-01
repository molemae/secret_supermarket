""" Skeleton for Customer
"""

#transition_probability_matrix
class Customer:
    def __init__(self,id, location)-> None:
        """_summary_

        Args:
            id (_type_): _description_
            state (_type_): _description_
        """

        self.id = id
        self.location = location 

    def __repr__(self) -> str:
        
        return f"{self.id},{self.location}"

    def next_location(self,matrix):
        """Here"""
        return None
    

    def is_active(self):

        return None
    


    ----- 
Customer