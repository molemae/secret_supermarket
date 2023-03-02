# %%
# import  
from random import choices

# see here
herpaderk 

def mcmc(state, p_dict) -> int:
    
    '''
    Run a Markov Chain Monte Carlo Simulation to simulate the probability
        
    Args:
        state: Initial state of the airplane in Markov chain.

        p-dict: Transition probabilities for each state.

    Returns:
        List of visiting states.

    '''
    idx = 0
    while state!='crashed':
        idx += 1
        state = choices(states, p_dict[state])[0]
        print(state)
        if state == 'crashed':
            return idx

states = ['airport', 'air', 'crashed']
p_in = {
    'airport': [0.4, 0.6, 0.0],
    'air': [0.8, 0.19999, 0.00001],
}

# print(f"crashed after {len(mcmc('airport', p))} days of service")
f"crashed after {mcmc('airport', p_in)} days of service"
# %%
