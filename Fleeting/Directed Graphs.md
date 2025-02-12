20250210131033

Tags: [[Graph]]

A directed [[Graphs|graph]] is one where the vertices point in one direction.

## Depth-First Search
A [[Depth-First Search|depth-first search]] can be used to decompose a directed graph into a [[Depth-First Search#DFS Tree|DFS tree]]. This helps list out all the levels as well as the relations between its [[Depth-First Search#Edges|edges]]. 

## Directed Acyclic Graph
A cycle in a directed graph is a circular path uncovered by a depth-first search. Hence, a directed acyclic graph (DAG) is a graph that is void of cycles. ![[Pasted image 20250210132456.png]]
#### Properties
There are certain properties that DAGs have as a result of its acyclic nature
###### Back Edges
DAGs have is that a depth-first search of one doesn't reveal back edges. The proof for this is that if $(u, v)$ is a back edge, then there is a cycle consisting of this edge with path $v$ to $u$ in the tree. This also means that it's possible to linearize (topologically sort) all DAGs
###### Level Numbers
DAGs have is that every edge leads to a vertex with a lower level number. Hence, ordering the nodes of a DAG requires linear time using a DFS
###### Sources and Sinks
Every DAG has at least one source and one sink. A sink is a vertex without any outgoing edges and a source is a vertex without any incoming edges. This property leads to an alternate approach to linearization, where one can start with finding a source, outputting it, deleting it, and repeating until the graph is empty. 

## Strongly Connected Components
Connectivity in a directed graph is more subtle than [[Undirected Graphs|undirected graphs]].
#### Definition
For two nodes $v$ and $u$, if there is a path from $u$ to $v$ and a path from $v$ to $u$, then they form a strongly connected component (SCC).
#### Meta-Graph
Every SCC can be shrunk down into a "meta-node", and the resulting "meta-graph" must be a DAG, since there's no cycles left. Hence, every directed graph is a DAG of its SCCs. 

## Kosaraju's Algorithm
The decomposition of a directed graph to its constituent SCCs turns out to be a very useful process. There is, in fact, a linear time algorithm for this process called [[Kosaraju's Algorithm|Kosaraju's algorithm]]. This algorithm is based on 3 properties.
1. If a DFS $explore$ subroutine has been run from $u$, then all the nodes reachable from $u$ have been visited once it terminates
2. The node that receives the highest $post$ number in a depth-first search must be the source of an SCC
3. If $C$ and $C'$ are both strongly connected components and there is an edge from a node in $C$ to a node in $C'$, then the highest $post$ number in $C$ is bigger than the highest $post$ number in $C'$
One thing to consider is that because of property 2, if we were to reverse a graph $G$, it would have the same SCCs as the original. But according to property 3, a sink in $G$ will be a source in $G^{R}$.
___
[[Algorithms]]
