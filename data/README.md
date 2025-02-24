File: denom_1_numer_-500000_500000.csv
* This file contains trajectory data from World 1 generated locally by World_mapper.py
* Each row corresponds to an *odd* starting value between seed_min=-500,000 and seed_max=500,000
* Columns, data types, and descriptions:
  * `seed`; int; the trajectory's starting value
  * `cycle_min`; int; the number of lowest absolute value in the trajectory's eventual cycle
  * `odd_steps`; int; the total number of odd steps from `seed` to `cycle_min`
  * `even_steps`; int; the total number of even steps from `seed` to `cycle_min`
  * `traj_min`; int; the smallest number, in absolute value, in the entire trajectory
  * `traj_max`; int; the largest number, in absolute value, in the entire trajectory
  * `odd_steps_to_max; int; the total number of odd steps from `seed` to `traj_max`
  * `even_steps_to_max; int; the total number of even steps from `seed` to `traj_max`
 
File cycle_list_ceiling_20K.csv
* This file contains cycle data for rational worlds from `denom` = 1 to `denom` = 799
* Only admissible denom values are included, that is, we must have `denom` ≡ ±1 (mod 6)
* Data generated locally by Cycle_list_by_denom.py
* Each row corresponds to a unique cycle
* Columns, data types and descriptions:
  * `denom`; int; the world number, or denominator, where the cycle occurs
  * `odd_steps`; int; also called "length", or "L", the number of odd steps in a cycle
  * `even_steps`; int; also called "weight", or "W", the number of even steps in a cycle
  * `min_numer`; int; the smallest number in the cycle, in absolute value
  * `natural_denom`; float (long int); the cycle's "natural world", that is, the value 2^W - 3^L
  * `defect`; float; a measure of the difference between the cycle's even/odd ratio and log(3)/log(2), namely: `defect` = 2^(W/L) - 3
  * `altitude`; float; harmonic mean of all odd numbers in the cycle
  * `neg_share`; float; 100*(proportion of negative seeds falling into the cycle), a percent measure of traffic
  * `pos_share`; float; 100*(proportion of positive seeds falling into the cycle), a percent measure of traffic
  * `is_reduced`; bool; flag for cycles that occur in worlds other than their natural world due to fraction reduction
  * `reduction_ratio`; float (long int); this is really `natural_denom`/`denom` and equals 1 for natural cycles
