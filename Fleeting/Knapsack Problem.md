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
Solving an unbounded knapsack problem also involves the use of tabulation. Set the entirety of the first row to entirely how much of the first item the "knapsack" can carry at every single weight. For every single block, calculate the max value that can be obtained by not taking and taking the current item. Compare those, to find the max of that. Once that's finished, the max value will be found at the last row's last column. 
```ad-example
A kna
```

