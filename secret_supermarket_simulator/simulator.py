import numpy as np
import pandas as pd
from customer import Customer
from supermarket_start import Supermarket


if __name__ == "__main__":
    secret_supermarket = Supermarket("Ultra Secret Supermarkt")
    
    while secret_supermarket.is_open():
        secret_supermarket.add_new_customers()
        secret_supermarket.print_customers()
        secret_supermarket.next_minute()
        secret_supermarket.remove_exitsting_customers()
    
