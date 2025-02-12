202502114132

Tags: [[Greedy Algorithms]]

Dijkstra's algorithm is a greedy algorithm used to choose the shortest path between nodes in a [[Graphs|graph]]. 

## Priority Queue
A priority queue is the kind of data structure used in Dijkstra's algorithm. There are four operations that it supports
1. Insertion, which adds a new element to the set
2. Decrease key, which decreases the key value of a specified element
3. Delete min, which finds the smallest key value and removes it from the set
4. Make queue, which builds a priority queue with the given elements and its key values

## Procedure
The procedure of Dijkstra's algorithm is somewhat similar to [[Breadth-First Search|breadth-first search]]. 
1. Start at an arbitrary node and initialize a queue for the distance between nodes
2. Set the distance between all nodes to infinity
3. Initialize distance from the starting node to all of its neighboring nodes
4. Visit the node that's the closest and update the queue based on new neighboring nodes discovered
5. Repeat for all the nodes in the priority queue until it is empty
![[Pasted image 20250211163903.png]]

## "Known Region"
What Dijkstra's algorithm shows when it explores more nodes is that it expands the region where more shortest paths are known, and this is called the known region. 

## Runtime Complexity
The complexity of Dijkstra's algorithm is linear time when abstracted, but in reality, it is $O(m\log n)$ time. In terms of a graph $G(V, E)$, it's time is expressed as $O((|V| + |E|)\log|V|)$. That is the fasted implementation of Dijkstra's priority queue system, using other methods results in varying times. The total time is calculated by $|V| \times deletemin + (|V| + |E|) \times insert$

| Implementation | Deletemin                                   | Decrease-Key                               | Total                                                              |
| -------------- | ------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------ |
| Array          | $O(\|V\|)$                                  | $O(1)$                                     | $O(\|V\|^{2})$                                                     |
| Binary Heap    | $O(\log\|V\|)$                              | $O(\log\|V\|)$                             | $O((\|V\| + \|E\|)\log(\|V\|))$                                    |
| d-ary Heap     | $O\left( \frac{d\log\|V\|}{\log d} \right)$ | $O\left( \frac{\log\|V\|}{\log d} \right)$ | $O\left( (\|V\| \cdot d + \|E\|) \frac{\log\|V\|}{\log d} \right)$ |
| Fibonacci Heap | $O(\log\|V\|)$                              | $O(1)$ amortized                           | $O(\|V\|\log\|V\| + \|E\|)$                                        |
___
# References
[[Algorithms]]
