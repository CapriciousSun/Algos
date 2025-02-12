20250212013953

Tags: [[Algorithm]]

Kosaraju's algorithm is a [[Greedy Algorithms|greedy algorithm]] used to break down a [[Directed Graphs|directed graph]] to its constituent [[Directed Graphs#Strongly Connected Components|SCCs]].

## Procedure
So the steps of Kosaraju's algorithm are as follows
1. Perform a DFS to define priorities in the graph, where the later the DFS visits the node, the higher the priority ![[Pasted image 20250210163535.png]]The stack here would be $[3, 4, 7, 8, 6, 5, 2, 1]$
2. Reverse the graph and the stack![[Pasted image 20250210163607.png]]The stack here would be $[1, 2, 5, 6, 8, 7, 4, 3]$
3. Perform a DFS on $G^{R}$, starting with the reverse order stack. Every node that the DFS visits should be removed from the stack
Using this algorithm, every time DFS has been called on the reverse graph would result in SCC being discovered. 

## Implementation
![[Pasted image 20250212014333.png]]

![[Pasted image 20250212014351.png]]

## Runtime Complexity
The [[Big O Notation|runtime complexity]] of Kosaraju's algorithm is $O(V + E)$
___
# References
[[Algorithms]]
