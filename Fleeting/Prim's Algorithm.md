20250212012315

Tags: [[Algorithm]]

Prim's algorithm is a [[Greedy Algorithms|greedy algorithm]] used to find the [[Greedy Algorithms#Minimum Spanning Tree|MST]] of a graph. 

## Procedure
The procedure for Prim's algorithm is relatively simple, mostly centered around avoiding cycles.
1. Start with an arbitrary node $v \in V$
2. Initialize a stack that keeps track of the nodes visited and edges in the MST
3. Find the neighbor of node $v$ with the smallest possible edge length, visit it, and record it in the stack
4. Find the neighbor with the next smallest possible edge length and repeat
5. Every time the addition of an edge creates a cycle, ignore it
6. Repeat $|V| - 1$ times

## Implementation
![[Pasted image 20250212012944.png]]

![[Pasted image 20250212013053.png]]

## Runtime Complexity
The runtime complexity of Prim's algorithm is $O(|V|^{2})$ when using an [[Adjacency Matrix|adjacency matrix]] and $O((|V| + |E|)\log|V|)$ when using an adjacency list. 
___
# References
[[Algorithms]]
