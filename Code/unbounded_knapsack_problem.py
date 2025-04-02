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