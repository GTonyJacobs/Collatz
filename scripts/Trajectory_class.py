def collatz_step(numer,multiplier,denom):
    numer = multiplier * numer + denom
    v2 = (numer & -numer).bit_length() - 1
    numer >>= v2
    return numer,v2

class CollatzTrajectory:
    def __init__(self, seed):
        self.seed = seed
        self.odd_steps = 0
        self.even_steps = 0
        self.traj_max = seed
        self.odd_steps_to_max = 0
        self.even_steps_to_max = 0
        self.total_steps = 0
        self.compute_trajectory()

    def compute_trajectory(self):
        """Compute trajectory statistics without storing full trajectory."""
        n = self.seed
        while n > 1:
            n, v2 = collatzStep(n, 3, 1)  # Apply the step transformation
            self.odd_steps += 1
            self.even_steps += v2
            if n > self.traj_max:
                self.traj_max = n
                self.odd_steps_to_max = self.odd_steps
                self.even_steps_to_max = self.even_steps

        self.total_steps = self.odd_steps + self.even_steps  # Sum steps

    def __repr__(self):
        return (f"The trajectory of {self.seed}: \n"
                f"- Reaches 1 after {self.odd_steps} odd steps, and "
                f"{self.even_steps} even steps.\n"
                f"- Has a max value of {self.traj_max}, attained in {self.odd_steps_to_max} odd "
                f"and {self.even_steps_to_max} even steps.")


if __name__ == "__main__":
    ## Enter starting value here
    seed=31

    print(CollatzTrajectory(seed))

