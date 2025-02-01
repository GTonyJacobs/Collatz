# Collatz
I have been interested in the Collatz conjecture for many years, and finally decided to collect some of my work into a repository here for easy sharing. This is a work-in-progress, and I hope to continue adding content.

The Collatz function is expressed in various ways. I will use the following notations for different versions of it:

C(n), for any integer n
* = 3n+1 if n is odd
* = n/2 if n is even

T(n), for any integer n 
* = (3n+1)/2 if n is odd
* = n/2 if n is even

S(n), for any *odd* integer n
* = (3n+1)/2^v
where v=v_2(3n+1) is the largest integer such that 2^v is a divisor of 3n+1. It is also known as the 2-adic valuation of 3n+1. 

To start out, here is some basic Python code for evaluating the Collatz function. I've written the function in a way that we can vary the parameters, so rather than "3n+1" as a rule, we allow for "Kn+d". Initially, however, we will stick with K=3 and d=1. The following code generates the trajectory of a starting n, and outputs all odd numbers until we reach 1, also tracking the number of divisions by 2 that follow each odd step.

[Basic trajectory generator](/scripts/Basic_trajectory_generator.py)
