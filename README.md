# The Collatz conjecture
For many years, since I was about 13 years old, I have explored the world of the Collatz conjecture. This page is here to invite you into this exploration, and to show you some of the steps that I've taken.

It all starts with a game that we can play with whole numbers:

* If $n$ is odd, then $n$ → $3n+1$
* If $n$ is even, then $n$ → $\frac{n}{2}$

Example: Let's start with $n=7$. Then we have:

* 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 → 4 → 2 → 1 → 4  → . . .

There's not much point going further, is there? This seems to have gotten stuck in a "loop", and we're just going to see 4 → 2 → 1 now, over and over again, forever.

The **Collatz Conjecture** is the claim that this always happens, that we always reach 1 and start looping, whether we start with 7 or any other positive integer.

Why not try it yourself? Here's a program that will let you input a starting number, and you can see how its "trajectory" – the sequence of numbers that we generate from it – develops! Just click the "Open in Colab" button below:

[![Trajectory Finder](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GTonyJacobs/Collatz/blob/main/intro_trajectory_finder.ipynb)
