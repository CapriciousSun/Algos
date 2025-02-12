20250109121007

Tags:

Big-O notation describes the worst case performance of an algorithm. The notation is in $O(g(x))$, where $g(x)$ is all large enough values of $x$ to matter in computation. 

## General Complexities
There are a few general layers of Big-O complexity. 
- $O(1)$ is constant time, where no matter the size of $g(x)$, it'll remain the same. 
- $O(\log n)$ is logarithmic time, where as $g(x)$ increases, the complexity will increase until reaching a plateau and stopping
- $O(n)$ is linear time, where as $g(x)$ increases, complexity increases alongside it at an unchanging rate
- $O(n \log n)$ is linearithmic time, where as $g(x)$ increases, complexity increases alongside it slowly at first, but then increases faster
- $O(n^{2})$ is polynomial time, which is similar to linearithmic time, but faster
Those state above are considered "reasonable" computing times. There are also those that should not be considered. 
- $O(2^{2})$ is exponential time
- $O(n!)$ is factorial time

## Rules
There are a few rules that dictate interactions between complexities and which complexities takes priority over another. 
- Multiplicative constants can usually be removed, so $cn^{2} = O(n^{2})$
- Given any $a > b$, $n^{a}$ dominates $n^{b}$
- Any exponential dominates any polynomial
- Any polynomial dominates any logarithm

## Cases
There are other cases beyond Big-O. Big-Theta, which is the average case, and Big-Omega, which is the best case scenario. 

```ad-example
#### f(n) = $\sqrt{n}$ and g(n) = $log_{3}n$
Since any polynomial dominates any logarithm, in the long run, f = Ω(g)
```

```ad-example
f(n) = $n!$ and g(n) = 2^{n}
Since any factorial dominates exponential, f = Ω(g)
```
___
# References
[[Graph Algorithm Part 1]]
