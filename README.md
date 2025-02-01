# The Collatz conjecture
I have been interested in the Collatz conjecture for many years, and finally decided to collect some of my work into a repository here for easy sharing. This is a work-in-progress, and I hope to continue adding content.

The Collatz function is expressed in various ways. I will use the following notations for different versions of it:

For any integer n,

$$
C(n) =
\begin{cases} 
    3n+1, & \text{if } n \text{ is odd} \\ 
    \frac{n}{2}, & \text{if } n \text{ is even} 
\end{cases}
$$

For any integer n,

$$
T(n) =
\begin{cases} 
    \frac{3n+1}{2}, & \text{if } n \text{ is odd} \\ 
    \frac{n}{2}, & \text{if } n \text{ is even} 
\end{cases}
$$

For any *odd* integer n

$$
S(n) = \frac{3n+1}{2^v}
$$

where $v=v_2(3n+1)$ is the largest integer such that $2^v$ is a divisor of $3n+1$. The function $v_2$ is also known as the 2-adic valuation.

The Collatz conjecture states that for any positive integer as a starting value, iterating $C(n)$ will eventually produce the value $1$. Equivalently, iterating $T(n)$ from any positive integer starting value will eventually lead to $1$, or iterating $S(n)$ on any odd positive integer starting value will eventually lead to $1$.

"C" stands for Collatz, after Lothar Collatz, the originator of the conjecture. "T" stands for Terras, after Riho Terras, who published an important paper on the conjecture in 1976, in which he used this "shortcut" version of the function. "S" stands for Syracuse. The problem was studied extensively at Syracuse University in the 1950s, and this version of the function is sometimes called the Syracuse Function. In the initial programs listed below, we use the Syracuse function, and we call it, by abuse of notation, the Collatz function. Such is life.

To start out, here is some basic Python code for evaluating the Collatz function. I've written the function in a way that we can vary the parameters, so rather than "3n+1" as a rule, we allow for "Kn+d". Initially, however, we will stick with K=3 and d=1. The following code generates the trajectory of a starting n, and outputs all odd numbers until we reach 1, also tracking the number of divisions by 2 that follow each odd step.

* [Basic trajectory generator](/scripts/Basic_trajectory_generator.py)

Now, we will sometimes wish to look at the statistics of many trajectories, so it is useful to define a CollatzTrajectory class, which stores useful parameters of a trajectory without having to remember every single number that's in it. Here is some code that implements such a class, along with a trivial call of it for illustration.

* [Trajectory class](/scripts/Trajectory_class.py)
