20250330220832

Tags: [[Algorithm]]

Dynamic algorithms solve problems by solving many subproblems that form the solution to the final problem

## Subproblems
Subproblems are smaller problems that make up the bigger dynamic problem. By looking at the solutions to these subproblems, you are looking at every single possible answer to each case of the larger problem and solving for them. 

## Longest Increasing Subsequences
The longest increasing subsequences applies to an unsorted sequence of numbers, with the job being to find the longest sequence of increasing numbers. The sequence of numbers can be represented as a [[Directed Graphs#Directed Acyclic Graph|DAG]], with every connection being an subsequence. 
![[Pasted image 20250401162919.png|800]]
#### Subproblem
The subproblem here is expressed as $L(j) = 1 + max(L(i) : (i, j) \in E : i < j)$, where $i$ is the starting vertex and $j$ is the destination vertex. From that, the recurrence relation is simply looping through all the nodes. 

#### Procedure
One procedure for solving the longest increasing subsequence starts with the last index of the array, since it's the base case and nothing can come after it. For an array of size $n$, the representation here would be $LIS[n - 1] = 1$. Shifting to the left one unit, the possible sizes of increase subsequences is $LIS[n - 2] = 1, 1 + LIS[n - 1]$. Then, choosing between them utilizes the $max$ function, So at $LIS[n - 2]$, the representation is $max(1, 1 + LIS[n - 1])$. Shifting to the left one more unit, the longest subsequence is $max(1, 1 + LIS[n - 2], 1 + LIS[n - 1])$. What this forms is a recurrence relation, where at every index of the array, it is comparing the least possible number of increasing subsequences, 1, and all other previous indices' increasing subsequences. Hence, the subproblem of this procedure is $LIS[i]$. 
```Python
def longest_increasing_subsequence_size(array : list[int]) -> int:
  LIS = [1] * len(array)
  for i in range(len(array) - 1, -1, -1):
    for j in range(i + 1, len(array)):
      if (array[i] < array[j]):
        LIS[i] = max(LIS[i], 1 + LIS[j])
  return max(LIS)
  
array = [5, 2, 8, 6, 3, 6, 9, 7]
print(longest_increasing_subsequence_size(array))
```

#### Runtime Complexity
The runtime complexity of the above procedure is $O(n^{2})$. 

## Edit Distance
When aligning to similarly spelt words by their letters, there may be gaps. That gap is a "cost", and *edit distance* refers to the cost of the best possible alignment of the two words, or the total number of "edits", insertions, deletions, and substitutions, needed to transform the first word to the second.
![[Pasted image 20250401204235.png|800]]
#### Subproblem
The subproblem here is expressed as $E(i, j) = \min\{ 1 + E(i - 1, j), 1 + E(i, j - 1), \text{diff}(i, j) + E(i - 1 j - 1) \}$, where $i$ is some length less than or equal to the length of the first word and $j$ is some length less than or equal to length to the second word. 

#### Procedure
One procedure to solving edit distance is tabulation. For two words where $len(word1) = m$ and $len(word2) = n$, create a table with $m + 1$ rows and $n + 1$ columns. Each entry in this table represents how many operations are needed in order to end up with the same string. By the $m + 1$ columns and $n + 1$ rows, the numbers in each of the entries is the word length subtracted by the column or row index. Then, every single index is calculated by the minimum of the index to the right, to the bottom, and to the diagonal. These represent insertion, deletion, and replacement operations, respectively. For every single index that represents two different letters, add 1 to the minimum operation. If they represent the same letters, simply draw from the diagonal index.
```Python
def edit_distance(word1 : str, word2: str):

  table = [[0 for x in range(len(word2) + 1)] for y in range(len(word1) + 1)]

  for i in range(len(word2) + 1):
    table[len(word1)][i] = len(word2) - i
  for i in range(len(word1) + 1):
    table[i][len(word2)] = len(word1) - i

  for i in range(len(word1) - 1, -1, -1):
    for j in range(len(word2) - 1, -1, -1):
      if word1[i] == word2[j]:=
        table[i][j] = table[i + 1][j + 1]
      else:
        table[i][j] = 1 + min(table[i + 1][j], table[i][j + 1], table[i + 1][j + 1])

  return table[0][0]

word1, word2 = "abd", "acd"
print(edit_distance(word1, word2))
```

```ad-example
For two words "abd" and "acd", first line them up in a table

|     | a   | b   | d   |     |
| --- | --- | --- | --- | --- |
| a   |     |     |     | 3   |
| c   |     |     |     | 2   |
| d   |     |     |     | 1   |
|     | 3   | 2   | 1   | 0   |
This already has the sides initialized. Then, begin filling in the table from the bottom right to the top left.

|     | a   | b   | d   |     |
| --- | --- | --- | --- | --- |
| a   | 1   | 2   | 2   | 3   |
| c   | 2   | 1   | 1   | 2   |
| d   | 2   | 1   | 0   | 1   |
|     | 3   | 2   | 1   | 0   |
The answer is at the top left index, for this example, it is 1, which lines up with the number of operations needed.
```

#### Runtime Complexity
The runtime complexity of this procedure is $O(n^{3})$. 

## Knapsack Problem
The [[Knapsack Problem|knapsack problem]] takes a hypothetical "knapsack" to represent some container with a max *weight*. Then, a set of items are given, each with their own *values* and *weights* associated with it. Based on the constraints given, the question asks for the maximum value to be stuffed into the knapsack while remaining under the max weight. There are three classes of knapsack problems commonly, [[Knapsack Problem#0-1 Knapsack Problem|the 0-1 knapsack problem]], [[Knapsack Problem#Bounded Knapsack Problem|the unbounded knapsack problem]], and [[Knapsack Problem#Unbounded Knapsack Problem|the unbounded knapsack problem]]. 

## Chain Matrix Multiplication
One of the properties of matrix multiplication is associativity, which means $(A \times B) \times C$ and $A \times (B \times C)$, where $A$, $B$, $C$ are all some matrix. Depending on the order that these matrices are multiplied, they may have different costs. 
![[Pasted image 20250401224232.png|800]]
#### Subproblem
The subproblem here is expressed as $C(i, j) = \min_{i \leq k \leq j} \{ C(i, k) + C(k + 1, j) + m_{i - 1} \cdot m_{k} \cdot m_{j} \}$ where $i$ is the first vector and $j$ is the last vector in the chain. 
#### Procedure
One procedure for solving this is tabulation. Start by making a table with rows and columns equal to the number of matrices to be multiplied. Then, start multiplying matrices in terms of their dimensions, with 2 matrices and moving forward. Every index is filled with the price of multiplying the requisite matrices. 

```ad-example
The set of matrices are $\{ [2, 3], [3, 6], [6, 4], [4, 5] \}$. Start by initializing the table, where the diagonal line are all zero because a matrix multiplied by itself should have no cost.

|     | 0   | 1   | 2   | 3   |
| --- | --- | --- | --- | --- |
| 0   | 0   |     |     |     |
| 1   |     | 0   |     |     |
| 2   |     |     | 0   |     |
| 3   |     |     |     | 0   |
Find all the possible results of mulitplying 2 matrices together

|     | 0   | 1   | 2   | 3   |
| --- | --- | --- | --- | --- |
| 0   | 0   | 36  |     |     |
| 1   |     | 0   | 72  |     |
| 2   |     |     | 0   | 120 |
| 3   |     |     |     | 0   |
Then, find the results of multiply 3 matrices together. This would be found by finding the minimum of 2 potential solutions, either the first matrix multiplied by the results of the second and third, or the third with the result of the first and second. This is expressed as $min(0 \times (1 \times 2), (0 \times 1) \times 2)$

|     | 0   | 1   | 2   | 3   |
| --- | --- | --- | --- | --- |
| 0   | 0   | 36  | 84  |     |
| 1   |     | 0   | 72  | 132 |
| 2   |     |     | 0   | 120 |
| 3   |     |     |     | 0   |
Repeat this process for multiplying 4 matrices. 

|     | 0   | 1   | 2   | 3   |
| --- | --- | --- | --- | --- |
| 0   | 0   | 36  | 84  | 124 |
| 1   |     | 0   | 72  | 132 |
| 2   |     |     | 0   | 120 |
| 3   |     |     |     | 0   |
```

## Shortest Paths
The shortest paths problem looks for the shortest path from some start to some destination. This is typically represented as a graph, where nodes are locations and edges are paths with some distance. 
#### Subproblem
The subproblem here is expressed as $dist(v, i) = min_{(u, v) \in E} \{ dist(u, i - 1) + l(u, v) \}$, where $v$ is the destination vertex, $u$ is the vertex the traversal is currently at, $i$ is an integer less than or equal to $k$, the max number of edges allowed, and $l$ is the length of the edge from $u$ to $v$. 

#### Runtime Complexity
The runtime complexity of this procedure is $O(E + V\log(V))$. 

## Independent Sets in Trees
A set of nodes are independent within a graph if they don't have edges connecting any of them. So for the tree below, $\{ 1, 5 \}$ is an independent set. 
![[Pasted image 20250401232213.png|800]]
#### Subproblem
The subproblem here is expressed as $I(u)$, which represents the size of the largest independent set of subtree hanging from some vertex $u$. The recurrence relation of this problem is $I(u) = max \left\{  1 + \sum_{\text{grandchildren } w \text{ of } u} I(w), \sum_{\text{children } w \text{ of } u} I(w) \right\}$. 

#### Runtime Complexity
The runtime complexity of this procedure is $O(|V| + |E|)$. 