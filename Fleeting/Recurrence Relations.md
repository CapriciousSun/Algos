20250401235544

Tags: [[Algorithm]]

Divide and conquer algorithms tend to follow the pattern of tackling a problem with size $n$ with subproblems of size $\frac{n}{b}$ and then combining them in $O(n^{d})$. 

## The Master Theorem
The master theorem dictates the runtime complexity of a divide and conquer algorithm, defined as $T(n) = aT([n/b]) + O(n^{d})$ for some constants $a > 0$, $b > 1$, $d \geq 0$. 
```ad-formula
#### The Master Theorem Formula
#### $$T(n) = \begin{cases}{} O(n^{d}) : d > log_{b}(a) \\ O(n^{d}\log(n)) : d = log_{b}(a) \\ O(n^{log_{b}(a)}) : d < log_{b}(a) \end{cases}$$
```

___
# References
[[Algorithms]]
