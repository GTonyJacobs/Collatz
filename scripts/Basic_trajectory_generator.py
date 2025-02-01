def collatzStep(numer,multiplier,denom):
    numer = multiplier * numer + denom
    v2 = 0
    while numer % 2 == 0:
        numer //= 2
        v2 += 1
    return numer,v2
    
def collatzTrajectory(seed):
    n=seed
    trajectory=[]
    v2_vector=[]
    while n>1:
        n,v=collatzStep(n,3,1)
        trajectory.append(n)
        v2_vector.append(v)
    return trajectory, v2_vector

## Enter desired starting value here
seed=1137

trajectory, v2_vector=collatzTrajectory(seed)
L=len(trajectory)
W=sum(v2_vector)
print(f"trajectory of {seed}: {trajectory}")
print(f"divisions at each step: {v2_vector}")
print(f"number of odd steps = {L}")
print(f"number of even steps = {W}")
