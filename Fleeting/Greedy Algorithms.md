20250212011159

Tags: [[Algorithm]]

Greedy algorithms are algorithms that make decisions based on the immediate and most obvious benefit. These algorithms build up solutions piece by piece.

## Minimum Spanning Tree
A minimum spanning tree (MST) is a subset of edges in a connected, edge-weighted tree that connects all the vertices without forming cycles and having minimum possible total edge weight. Therea are several algorithms that could produce a MST when given an edge weighted tree.
#### Prim's Algorithm
[[Prim's Algorithm|Prim's algorithm]] is a greedy algorithm that chooses some arbitrary root node and grows a tree by finding the cheapest node that the current tree can connect to.
#### Kruskal's Algorithm
[[Kruskal's Algorithm|Kruskal's algorithm]] starts with the cheapest edge globally and grows the tree by finding more expensive lines to connect and eventually, the lines begin to connect.

## Knapsack Problem
The [[Knapsack Problem|knapsack problem]] is a range of problems that focused on a hypothetical "knapsack" with a maximum weight, and items that be put in, each with a weight and value. The key to the problem is solving for the maximum value that would fit in the max weight. Knapsack problems tend to be solved with [[Dynamic Programming|dynamic programming]], because greedy algorithms do not look at every possible answer, just the local optimum.
___
# References
[[Algorithms]]
