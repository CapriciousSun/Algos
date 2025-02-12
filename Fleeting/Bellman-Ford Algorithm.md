20250211181411

Tags: [[Algorithm]]

The Bellman-Ford algorithm is a dynamic algorithm that works on [[Weighted Graphs#Signed Graphs|signed weighted graphs]]. 

## Procedure
The procedure for the Bellman-Ford algorithm is different than [[Dijkstra’s Algorithm|Dijkstra's algorithm]] because of the multiple iterations needed to execute it, instead of trying to solve everything in one go.
1. Start at an arbitrary node $v \in V$
2. Initialize a stack that keeps track of the vertices and edges that have been visited
3. Visit the neighbors of node $v$ and record their distances
4. If separate collections of edges lead to the same node but with a shorter length, that should be recorded instead
5. This should be repeated until all edges have been visited
The reason this is called an iterative solution is because the searching happens once at every iteration there's a set limit to how many iterations there are to perform ($|V| - 1$). 

## Implementation
![[Pasted image 20250212005858.png]]

## Negative Cycles
A negative cycle occurs when the distance between two nodes continuously decrease without stopping. The way to detect a negative cycle is to perform $|V|$ iterations and seeing if the distance between nodes decreased. 

## In DAGs
In a [[Directed Graphs#Directed Acyclic Graph|DAG]], the algorithm needs to be slightly altered, namely, by including a linearization step by [[Depth-First Search|depth-first search]] and then visiting the vertices in the sorted order. ![[Pasted image 20250212010108.png]]

## Runtime Complexity
The [[Big O Notation|runtime complexity]] of Kruskal's algorithm is $O(VE)$. 
___
# References
[[Algorithms]]
