20250109131327

Tags: [[Algorithm]], [[Graph]]

Breadth-first search is a method of traversing through a [[Graphs|graph]] to find out information about it. 

## Procedure
The steps of a breadth-first search algorithm of a graph $G(V, E)$ are as follows.
1. Initialize a Boolean list where everything is set to false and is the size of the graph
2. Have a queue to keep track of the vertices $\in V$ that need to be visited
	- The queue in the beginning of the loop should only consist of an arbitrary node $e \in E$ 
3. Remove a vertex from the front of the queue
4. If it hasn't been visited yet, visit it and mark the vertex
5. Iterate through all the neighbors and add them to the queue
6. Repeat steps 3-5 until the queue is finally empty

## Implementation
```Python
marked = [False] * G.size()
def bfs(G, v):
	queue = |v|
	while len(queue) > 0:
		v = queue.pop(0)
		if not marked|v|:
			visit(v)
			marked|v| = True
			for w in G.neighbors(v):
				if not marked|w|:
					queue.append(w)
```

## Runtime Complexity
The overall runtime complexity of breadth-first search is linear with $O(|V| + |E|)$ for a graph $G(V, E)$.
___
# References
[[Breadth First Search (BFS)- Visualized and Explained]]
[[Graph Algorithm Part 1]]
[[Graph Algorithm Part 2]]
