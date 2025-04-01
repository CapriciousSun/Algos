dataset =  [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], 
            [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104],
            [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]

def knapsack(W : int, array : list[list[int, int]], i=0):
  sack_array = [[0] * W] * len(dataset)
  selected_array = []

  for i in range(1, len(dataset)):
    sack_array[i][0] = 0
    for j in range(1, W):
      if (j >= dataset[i][0]):
        sack_array[i][j] = max(dataset[i][1] + sack_array[i - 1][j - dataset[i][0]], sack_array[i - 1][j])
      else:
        sack_array[i][j] = sack_array[i - 1][j]

  return sack_array[len(dataset) - 1][W - 1]
ans1 = knapsack(W=100, array=dataset)
ans2 = knapsack(W=200, array=dataset)
ans3 = knapsack(W=300, array=dataset)
print(ans1)
print(ans2)
print(ans3)
