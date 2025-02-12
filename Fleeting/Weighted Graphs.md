20250211172605

Tags: [[Graph]]

A weighted [[Graphs|graph]] is different from [[Directed Graphs|directed graphs]] and [[Undirected Graphs|undirected graphs]] in the sense that the edges are not all 1 unit length.

## Edge Length
When running breadth-first search at the basic level, the assumption is that the edge length are all the same, 1. So, when edge length varies, these edges can be reduced down to unit length pieces. ![[Pasted image 20250211134522.png]]

## Dijkstra's Algorithm
[[Dijkstra’s Algorithm|Dijkstra's algorithm]] can be used to determine the shortest path for unsigned weighted graphs. It is a $O(m\log n)$ algorithm. 

## Signed Graphs
A subset of weighted graphs is signed graph, where negative edge lengths exist. Dijkstra's algorithm is not helpful in this scenario, as the shortest path to and from any point would have to pass through shorter points along the way. This no longer holds for paths with negative length. 

## Bellman-Ford Algorithm
The [[Bellman-Ford Algorithm]] is what's used for signed graphs. The