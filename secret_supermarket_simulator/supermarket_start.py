from customer import Customer
import pandas as pd

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, name):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.name = name

    def __repr__(self):
        if self.is_open():
            return f'''It is {self.get_time()}: the Supermarket {self.name} currently has {len(self.customers)} customers.'''
        else:
            return 'The Supermarket is closed now.'
        
    def is_open(self):
        return self.get_time() != "10:00"

    def get_time(self):
        """current time in HH:MM format,
        """
        hour = 7 + self.minutes // 60
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
            cus_df = pd.concat([cus_df,cur_cus]).to_csv(f'../data/out/{filename}.csv',header=False,mode='a')

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
                print(f'removing last customers:{customer}')
                customer.location = 'checkout'
                customer.active = False
                self.remove_exitsting_customers()
        return None
    
    def add_new_customers(self):
        '''Adds new customer for every minute. 
        TODO: using poisson distribiution instead of always one new
        '''
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



