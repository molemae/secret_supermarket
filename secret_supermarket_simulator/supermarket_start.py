
from customer import Customer
import numpy as np
import pandas as pd

matrix = pd.read_pickle('../data/entry_prob')
matrix

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """
    DISTRIBIUTION = matrix.copy()
    def __init__(self, name):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.name = name

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
            print(cus_string)
            printlist.append(cus_string)

        return None

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.minutes = self.minutes + 1
        for customer in self.customers:
            customer.next_location()
        return None
    
    def add_new_customers(self):
        '''Adds new customer for every minute. 
        '''
        P = Supermarket.DISTRIBIUTION
        
        n  = np.random.choice(a=np.array(P['New_Cus_per_min']),p=np.array(P['Prob']))
        for i in range(n):
            self.last_id += 1
            self.customers.append(Customer(self.last_id))

        return None

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        for customer in self.customers:
            if not customer.active:
                self.customers.remove(customer)
        return None



