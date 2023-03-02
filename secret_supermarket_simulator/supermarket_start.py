"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
from customer import Customer

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, name, matrix):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.name = name
        self.matrix = matrix
        self.locations = list()

    def __repr__(self):
        return 'The current time is supermarket '

    def is_open(self):
        return self.get_time() != "22:00"

    def get_time(self):
        """current time in HH:MM format,
        """
        hour = 7 + self.minutes // 60
        minutes = self.minutes % 60
        timestamp = f"{hour:02d}:{minutes:02d}" 
        return timestamp

    def print_customers(self):
        """print all customers with the current time, id, location in CSV format.
        """
        printlist = []
        for customer in self.customers:
            cus_string = f"The customer {customer.id} is at {customer.location} at {self.get_time()}."
            printlist.append(cus_string)

        return printlist

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.minutes = self.minutes + 1
        for customer in self.customers:
            customer.next_location(self.matrix)
        return None
    
    def add_new_customers(self):
        self.last_id += 1
        self.customers.append(Customer(self.last_id,'entrance'))

        return None

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        return None

# if __name__ == "__main__":
    # Lidl = Supermarket("LIDL")
    # print(Lidl.get_time())