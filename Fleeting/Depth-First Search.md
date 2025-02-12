202501131310101

Tags: [[Algorithm]], [[Graph]]

Depth-first search differs from [[Breadth-First Search|breadth-first search]] in the sense that DFS goes to the furthest node possible before tracing itself back to previous nodes, and then going to the furthest node again.

## Procedure
The method of a depth-first search algorithm are in the following steps. 
1. Initialize a Boolean list where everything is set to false and is the size of the graph
2. Have a stack to keep track of the vertices $\in V$ that needs to be visited
	- In the beginning of the loop, the only vertex in the stack should be the arbitrary starting vertex
3. Remove the last vertex of the stack
4. If it hasn't been visited yet, visit it and mark the vertex
5. Iterate through all the neighbors and add them to the stack
6. Repeat until the stack is empty

## Implementation
```Python
marked = [False] * G.size()
def dfs(G, V):
	stack = |v|
	while len(stack) > 0:
		v = stack.pop()
		if not marked|v|:
			visit(v)
			marked|v| = True
			for w in G.neighbors(v):
				if not marked|v|:
					stack.append(v)
```

![[Pasted image 20250212015307.png]]

## Runtime Complexity
The runtime complexity of a depth first search is linear, as it is the combination of $O(|E|) + O(|V|) = O(|V| + |E|)$. 

## DFS Tree
A DFS tree is a top-down visualization of a graph, where the initial starting node is level 1, and every other level is +1 distance from the starting node. 
#### Edges
In a DFS tree, there are three kinds of connecting edges aside from tree edges.
![[Pasted image 20250210130207.png|300]]
1. Forward edges, which go from a node to a non-child descendant
2. Back edges, which go from a node to an ancestor
3. Cross edges, which go from a node to another node on the same level
___
[[Algorithms]]
