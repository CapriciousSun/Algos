## Question 1
The answer should be $\text{T}(n^{2} - n)$. This is because the actual time is $\frac{n^{2}}{2} - \frac{n}{2}$, and since coefficients are ruled out. then the worst case time for this question is $n^{2} - n$. This function takes a number and prints n - 1 of it recursively. So, if the input n is 10, then the result would be 45, since it's $9 + 8 \dots + 2 + 1$, which is 45. $\frac{10^{2}}{2} - \frac{10}{2}$ is also 45.

## Question 2
The answer here should be $\text{T}(n^{2} + n)$. The actual time is $\frac{n^{2}}{2} + \frac{n}{2}$. The reasoning for ruling out the coefficients is the same, but this function is different in the sense that it takes a number and prints it out, then recursively does so for n - 1 cases. So, if the input n is 10, then the result would be 55, since it's $10 + 9 + \dots + 2 + 1$, which is 55. $\frac{10^{2}}{2} + \frac{10}{2}$ is also 55. 

## Question 3
![[Pasted image 20250116163926.png]]
