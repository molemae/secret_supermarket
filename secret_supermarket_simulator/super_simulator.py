# %%
from supermarket_start import Supermarket

sec_super = Supermarket("Secret_Supermarket")

if __name__ == "__main__":
    
    while sec_super.is_open():
        sec_super.add_new_customers()
        sec_super.next_minute()
        sec_super.print_customers()
        sec_super.remove_exitsting_customers()
# %%
