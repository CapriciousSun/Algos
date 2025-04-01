20250330220832

Tags: [[Algorithm]]

Dynamic algorithms solve problems by solving many subproblems that form the solution to the final problem

## The Subproblem
Subproblems are smaller problems that make up the bigger dynamic problem. By looking at the solutions to these subproblems, you are looking at every single possible answer to each case of the larger problem and solving for them. 

## Longest Increasing Subsequences
The longest increasing subsequences applies to an unsorted sequence of numbers, with the job being to find the longest sequence of increasing numbers. The sequence of numbers can be represented as a [[Directed Graphs#Directed Acyclic Graph|DAG]], with every connection being an subsequence. 
![[Pasted image 20250401162919.png|800]]
#### Procedure
This algorithm for calculating the longest path for a DAG of $n$ length
```Python
for i in range(n)
	L(j) = 1 + max()
```
