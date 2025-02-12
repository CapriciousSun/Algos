20250212014605

Tags: [[Graph]]

An adjacency list is a collection of arrays corresponding to the individual nodes and the nodes that its connected to. 

## Notation
![[Pasted image 20250212014927.png]]

## Runtime Complexity
An adjacency matrix has a few characteristics with its [[Big O Notation#General Complexities|runtime complexities]].
- Its space is proportional to $Θ(|V| + |E|)$
- Checking if $(u, v)$ is an edge takes $Θ(degree(u))$ time, where $degree$ is the number of neighbors $u$ has
- Identifying all edges takes $Θ(|V| + |E|)$ time
___
# References
[[Algorithms]]
