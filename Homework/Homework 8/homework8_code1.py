dataset =  [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], 
            [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104],
            [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]

def knapsack(W : int, array : list[list[int, int]]):
  array.sort(key=lambda i: (i[1] / i[0]))
  maxVal = 0.0
  sack_array = []

  for i in array:
    if i[0] <= W:
      W -= i[0]
      maxVal += i[1]
      sack_array.append(i)

  return maxVal

ans1 = knapsack(W=100, array=dataset)
ans2 = knapsack(W=200, array=dataset)
ans3 = knapsack(W=300, array=dataset)
print(ans1)
print(ans2)
print(ans3)