import random, time

def partition(array : list[int], left : int, right : int, pivotIndex : int) -> int:
  pivotVal = array[pivotIndex]
  array[pivotIndex], array[right] = array[right], array[pivotIndex]
  tempIndex = left
  for i in range(left, right - 1):
    if (array[i] < pivotVal):
      array[tempIndex], array[i] = array[i], array[tempIndex]
      tempIndex += 1
  array[right], array[tempIndex] = array[tempIndex], array[right]
  return tempIndex

def randomized_selection(array : list[int], left : int, right : int, k: int) -> int:
  if (left == right):
    return array[left]
  pivotIndex = random.randint(left + 1, right)
  pivotIndex = partition(array=array, left=left, right=right, pivotIndex=pivotIndex)
  if (k == pivotIndex):
    return array[k]
  elif (k < pivotIndex):
    return randomized_selection(array=array, left=left, right=pivotIndex - 1, k=k)
  else:
    return randomized_selection(array=array, left=pivotIndex + 1, right=right, k=k)

# sort_list = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
# kth_index = randomized_selection(sort_list, 0, len(sort_list) - 1, 5)
# print(kth_index)
# sort_list.sort()
# print(sort_list)

full_list = []
n = pow(10, 7)
for i in range(n):
  full_list.append(random.randint(0, int(n/100)))

start = time.time()
nth = randomized_selection(array=full_list,left=0, right=n - 1, k=int(n / 2))
print(nth)
end = time.time()
print(end - start)