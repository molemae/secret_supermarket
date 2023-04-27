
from customer import Customer
import os
import numpy as np
import pandas as pd

matrix = pd.read_pickle('../data/entry_prob')
matrix

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """
    DISTRIBIUTION = matrix.copy()
    def __init__(self, name,closing_time='22:00'):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.name = name
        self.closing_time = closing_time

    def __repr__(self):
        if self.is_open():
            return f'''It is {self.get_time()}: the Supermarket {self.name} currently has {len(self.customers)} customers.'''
        else:
            return f'It is {self.get_time()}:The Supermarket is closed now.'
        
    def is_open(self):
        return self.get_time() != self.closing_time

    def get_time(self):
        """current time in HH:MM format,
        """
        hour = 9 + self.minutes // 60
        minutes = self.minutes % 60
        timestamp = f"{hour:02d}:{minutes:02d}" 
        return timestamp

    def print_customers(self,filename):
        """print all customers with the current time, id, location in CSV format.
        """
        cus_df = pd.DataFrame(columns=['time','id','location'])
        cur_time = self.get_time()
        for customer in self.customers:
            cur_dict = {
                'time':[cur_time],
                'id':[customer.id],
                'location':[customer.location]
            }
            cur_cus = pd.DataFrame.from_dict(cur_dict)
            if not os.path.isfile(f'../data/out/{filename}.csv'):
                cus_df.to_csv(f'../data/out/{filename}.csv',index=False)
            cus_df = pd.concat([cus_df,cur_cus]).to_csv(f'../data/out/{filename}.csv',header=False,index=False, mode='a')

        return cus_df

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.minutes = self.minutes + 1
        if self.is_open():
            for customer in self.customers:
                customer.next_location()
        else:
            for customer in self.customers:
                customer.location = 'checkout'
                customer.active = False
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
        for customer in self.customers.copy():
            if not customer.active:
                self.customers.remove(customer)
        return None



