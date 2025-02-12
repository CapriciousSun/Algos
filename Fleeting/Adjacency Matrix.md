20250206153017

Tags: [[Graph]]

 An adjacency matrix is used to mathematically show the connections between graphs. 

## Notation
For an adjacency matrix, if nodes $i$ and $j$ have a connection, then $A_{ij}$ would be equal to 1. Otherwise it would be 0. So for a [[Graphs#Direction|undirected graph]] with 4 nodes, where nodes 1, 2, and 4 are connected and node 3 is connected to node 4, the adjacency matrix would be $$\begin{pmatrix}
0 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 \\
1 & 1 & 1 & 0
\end{pmatrix}$$
where the rows indicate each node and the columns indicate every other node. 

## Runtime Complexity
An adjacency matrix has a few characteristics with its [[Big O Notation#General Complexities|runtime complexities]].
- Its space is proportional to $Θ(n^{2})$, where $n = |V|$
- Checking if $(u, v)$ is an edge takes $Θ(1)$ time
- Identifying all edges takes $Θ(n^{2})$ time

___
## References
[[Algorithms.pdf]]
