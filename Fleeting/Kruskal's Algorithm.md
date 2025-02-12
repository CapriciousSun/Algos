20250212011439

Tags: [[Algorithm]]

Kruskal's algorithm is a [[Greedy Algorithms|greedy algorithm]] meant for finding [[Greedy Algorithms#Minimum Spanning Tree|MSTs]]. 
## Procedure
The steps for Kruskal's algorithm is sporadic, with a focus on finding the global minimum in terms of edge length. 
1. Initialize a stack for the vertices and edges visited
2. Find the lightest edge and add it to the stack
3. Every time the addition of a new edge creates a cycle, remove it
4. Repeat until all edges have been visited or removed

## Implementation
![[Pasted image 20250212011454.png]]

![[Pasted image 20250212011511.png]]

## Runtime Complexity
The [[Big O Notation|runtime complexity]] of Kruskal's is $O(E\log E)$. 
___
# References
[[Algorithms]]
