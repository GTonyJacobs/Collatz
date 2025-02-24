# Shortcuts: The Terras and Syracuse maps
Our original definition of the **Collatz map**, in the [Introduction](Intro.md), can be formalized this way:

$$
C(n) = \begin{cases}
3n+1 & \text{if }n\equiv 1\pmod{2} \\
\frac{n}{2} & \text{if }n\equiv 0\pmod{2}
\end{cases}
$$

## The Terras Map
A good first observation is that, when $$n$$ is odd, the value of $$3n+1$$ is always even, so an "odd step" is always followed by an "even step". After that, the trajectory could move on to another even step, or go back to an odd step, depending on the result of the first even step:

* 9 → 28 → 14 → 7 (odd, even, even)
* 7 → 22 → 11 → 34 (odd, even, odd)

Thus, we can tighten things up a bit by rolling together an odd step and the even step that immediately follows it. The first writer to publish work on the Collatz Conjecture, Riho Terras, did this, so we call this reformulation the **Terras map**, and we denote it $$T(n)$$:

$$
T(n) = \begin{cases}
\frac{3n+1}{2} & \text{if }n\equiv 1\pmod{2} \\
\frac{n}{2} & \text{if }n\equiv 0\pmod{2}
\end{cases}
$$

The above trajectory fragments, under the Terras map, turn into:

* 9 → 14 → 7
* 7 → 11 → 17

To distinguish which kind of trajectory we're talking about, we use the following notation:

* C: 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 → 4 → 2 → 1
* T: 11 → 17 → 26 → 13 → 20 → 10 → 5 → 8 → 4 → 2 → 1 → 2 → 1

Of course, the Collatz conjecture is equivalent to the claim that iterating $$T(n)$$ for any positive integer $$n$$ will eventually produce the value $$1$$.

## The Syracuse Map
For an even shorter shortcut, we can observe that each odd step is followed by *some number* of even steps, after which we obtain a new odd number. Thus, we can consider a map purely from one odd number to the next, where each step includes performing the $$3n+1$$ transformation, and then following it with as many divisions by $$2$$ as are needed to obtain another odd number. Another early researcher, Herbert Möller, talked about the **Syracuse map**, calling it $$S$$ and noting that it had been discussed at Syracuse University.

$$
S(n) = \frac{3n+1}{2^v}
$$

Here, $$v$$ is the unique exponent for which the result is an odd number. Möller used the letter $$a$$ instead of $$v$$, but we use $$v$$ here because formally, it represents the value $$v_2(3n+1)$$, i.e., the 2-adic valuation of $$3n+1$$.

Using the Syracuse map abbreviates an odd number's trajectory without changing its ultimate fate. Another way to state the Collatz conjecture is that, for every *odd* positive $$n$$, iterating $$S(n)$$ will eventually produce $$1$$. Comparing all three maps for the same number:

* C: 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 → 4 → 2 → 1
* T: 11 → 17 → 26 → 13 → 20 → 10 → 5 → 8 → 4 → 2 → 1 → 2 → 1
* S: 11 → 17 → 13 → 5 → 1 → 1
  [v] = [1, 2, 3, 4, 2]

The list of $$v$$ values under the Syracuse trajectory, which can be omitted when it's not needed, tells us the number of divisions by $$2$$ occurring between each pair of odd numbers.

## Code
* Trajectory Finders
  * Collatz Trajectory Finder: [![Collatz Trajectory Finder](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GTonyJacobs/Collatz/blob/main/scripts/intro_trajectory_finder.ipynb){:target="_blank"}
  * Terras Trajectory Finder: [![Terras Trajectory Finder](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GTonyJacobs/Collatz/blob/main/scripts/Terras_trajectory_finder.ipynb){:target="_blank"}
  * Syracuse Trajectory Finder: [![Syracuse Trajectory Finder](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GTonyJacobs/Collatz/blob/main/scripts/Syracuse_trajectory_finder.ipynb){:target="_blank"}
* Trajectory Length Scatterplots
  * Collatz Trajectory Length Scatterplot: [![Collatz Trajectory Length Scatterplot](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GTonyJacobs/Collatz/blob/main/scripts/Collatz_trajectory_length_scatterplot){:target="_blank"}
  * Terras Trajectory Length Scatterplot: [![Terras Trajectory Length Scatterplot](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GTonyJacobs/Collatz/blob/main/scripts/Terras_trajectory_length_scatterplot){:target="_blank"}
  * Syracuse Trajectory Length Scatterplot: [![Syracuse Trajectory Length Scatterplot](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GTonyJacobs/Collatz/blob/main/scripts/Syracuse_trajectory_length_scatterplot){:target="_blank"}
 
[Rerturn to Main Menu](../README.md)
