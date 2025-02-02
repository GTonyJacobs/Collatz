def collatz_step(numer,multiplier,denom):
    numer = multiplier * numer + denom
    v2 = (numer & -numer).bit_length() - 1
    numer >>= v2
    return numer,v2
    
def collatz_trajectory(seed):
    n=seed
    trajectory=[]
    v2_vector=[]
    while n>1:
        n,v=collatz_step(n,3,1)
        trajectory.append(n)
        v2_vector.append(v)
    return trajectory, v2_vector

## Enter desired starting value here
seed=1137

trajectory, v2_vector=collatz_trajectory(seed)
odd_steps=len(trajectory)
even_steps=sum(v2_vector)
print(f"trajectory of {seed}: {trajectory}")
print(f"divisions at each step: {v2_vector}")
print(f"number of odd steps = {odd_steps}")
print(f"number of even steps = {even_steps}")
