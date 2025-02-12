20250109121950

Tags:

Informally, a graph is a mathematical structure representing relationships. They are also called, networks, with the nodes and connections between the nodes defining the networks. 

## Notation
Formally, a graph is any collection of vertices and edges, noted as $G(V, E)$. $V$ is set of all the vertices (or nodes) within the graph. $E$ is a set of all the edges (or arcs) within the graph. The size of these two parameters is noted by $|V|$ and $|E|$. 

## Distance
The distance calculation between nodes is done breadth first. First, any node's distance from itself is 0, and then every other node by its side is added by 1 and repeated. By assigning distances, the path back can be found with the numbers assigned. The algorithm for doing so has an input of an undirected graph $G = (V, E)$ and a start node $s \in V$. The output is the distances from s to all nodes v. This allows the following to be found
1. The shortest paths
2. All connected components
3. The distance to all other nodes in the connected component

## Connections
The shortest path between two nodes is called the geodesic path. If two nodes are not connected, the distance between them is infinite. 

## Connected Graph
A connected graph is a graph where every single node can reach every other node in the graph. The formal definition is nodes u and v are connected, if $\exists$ a path connection u and v, and that a graph is connected if all nodes are connected with each other. The fundamental question to ask when given a connected graph is, if there are nodes s and t, is there a path from s to t and how to find the geodesic path between them. 
___
# References
[[Graph Algorithm Part 1]]
[[Algorithms]]
