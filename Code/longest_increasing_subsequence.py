def longest_increasing_subsequence_size(array : list[int]) -> int:
  LIS = [1] * len(array)

  for i in range(len(array) - 1, -1, -1):
    for j in range(i + 1, len(array)):
      if (array[i] < array[j]):
        LIS[i] = max(LIS[i], 1 + LIS[j])
  
  return max(LIS) 

array = [5, 2, 8, 6, 3, 6, 9, 7]
print(longest_increasing_subsequence_size(array))
