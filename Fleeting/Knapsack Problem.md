20250331213600

Tags: [[Problem]]

The knapsack problem is a class of problem that takes a set of items, each with a weight and value, and determines which items are to be included in the "knapsack" so that the total weight is less than or equal to the max weight of the knapsack while maximizing for value.

## Formalism
The formal representation of the knapsack problem would be in the form of a summation. 
```ad-formula
#### General Form of a Knapsack Problem
The variables are weight $w_{i}$, value $v_{i}$, maximum weight capacity $W$, and item $x_{i}$. 
#### $$\begin{gather} \text{maximize } \sum_{i = 1}^{n} v_{i}x_{i} \\ \text{subject to } \sum_{i = 1}^{n} w_{i}x_{i} ≤ W \end{gather}$$
```

## 0-1 Knapsack Problem
The 0-1 knapsack problem is the most basic form of the knapsack problem. It restricts the number of item $x_{i}$ allowed in the "knapsack" to 0 or 1. 
```ad-formula
#### General Form of a 0-1 Knapsack Problem
The maximum function remains the same. The constraints of this problem are 
#### $$x_{i} \in \{ 0, 1 \}$$
```

#### Procedure
The procedure for solving 0-1 problems is to create a table consisting of the items being selected and all possible integer weights. This is known as the tabulation approach. Create a table of weight columns and For every single item that would not fit the weight limit, the table entry would be 0. Any table that fits the weight would have the entry set to the value of the item. The maximum possible value is selected for each entry, so comparisons to the entry one row above would be made. 
```ad-example
A knapsack has max weight 5. The following table are the items available in terms of weight and value.

|Weight     |Items     |
| --- | --- |
| 5 | 60 |
| 3 | 50 |
| 4 | 70 |
| 2 | 30 |
This will translate to the following weight-item table.

|        | 0   | 1   | 2   | 3   | 4   | 5   |
| ------ | --- | --- | --- | --- | --- | --- |
| Item 1 | 0   | 0   | 0   | 0   | 0   | 60  |
| Item 2 | 0   | 0   | 0   | 50  | 50  | 60  |
| Item 3 | 0   | 0   | 0   | 50  | 70  | 70  |
| Item 4 | 0   | 0   | 30  | 50  | 70  | 80  |
which shows the the optimal value to be obtained is 80. 
```

## Bounded Knapsack Problem
The bounded knapsack problem restricts the number of items allowed in the "knapsack" to some natural number $c$.
```ad-formula
#### General Form of a Bounded Knapsack Probelm
The constraints of this problem are
#### $$x_{i} \in \{ 0, 1, 2, \dots, c \}$$
```

## Unbounded Knapsack Problem
The unbounded knapsack problem restricts the number of items allowed in the "knapsack" to all natural numbers.
```ad-formula
#### General Form of a Unbounded Knapsack Problem
The constraints of this problem are
#### $$x_{i} \in \mathbb{N}$$
```

#### Procedure
Solving an unbounded knapsack problem also involves the use of tabulation. First, sort the items by their weight. Then, set the rows to the weights possible and the columns to the items. Set the entirety of the first row to entirely how much of the first item the "knapsack" can carry at every single weight. For every other block, calculate the maximum by comparing the value one row above (not taking the item) and the item plus whatever weights came before (taking the item), given that it fits within the weight constraints.

```Python
def unbounded_knapsack(weight : int, array : list[int, int]):
  knapsack = [[0 for x in range(weight + 1)] for y in range(len(array))]
  array = sorted(array, key=lambda x: x[0])
  value = 1
  heft = 0

  for i in range(weight + 1):
    knapsack[0][i] = array[0][1] * (i // array[0][0])

  for item in range(1, len(array)):
    for kgs in range(weight + 1):
      if (array[item][heft] <= kgs):
        not_taken = knapsack[item - 1][kgs]
        taken = array[item][value] * (kgs // array[item][heft]) + knapsack[item][kgs % array[item][heft]]
        knapsack[item][kgs] = max(taken, not_taken)  
      else:
        knapsack[item][kgs] = knapsack[item - 1][kgs]

  return knapsack[len(array) - 1][weight]

weight = 8
items = [[5, 10], [1, 1], [2, 4], [3, 7]]
print(unbounded_knapsack(weight=weight, array=items))
```

```ad-example
The table below defines the items with the values and weights.

| Value | Weight |
| ----- | ------ |
| 1     | 1      |
| 4     | 2      |
| 7     | 3      |
| 10    | 5      |
Then, initialize the table so that the first row is filled.

|      | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/1  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| 2/4  |     |     |     |     |     |     |     |     |     |
| 3/7  |     |     |     |     |     |     |     |     |     |
| 5/10 |     |     |     |     |     |     |     |     |     |
Fill in every index, and when that's done, the bottom right index is the maximum value for the weight constraints.

|      | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/1  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| 2/4  | 0   | 1   | 4   | 5   | 8   | 7   | 12  | 13  | 16  |
| 3/7  | 0   | 1   | 4   | 7   | 8   | 11  | 14  | 15  | 18  |
| 5/10 | 0   | 1   | 4   | 7   | 8   | 11  | 14  | 15  | 18  |
```

___
# References
[[Algorithms]]
