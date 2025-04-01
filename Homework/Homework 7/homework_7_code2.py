import random, time

def partition(array : list[int], left : int, right : int) -> int:
  i = left + 1
  while (i <= right):
    j = i
    while (j > left and array[j - 1] > array[j]):
      array[j - 1], array[j] = array[j], array[j - 1]
    i = i + 1
  return left + int((right - left) / 2)

def select(array : list[int], left : int, right : int, n : int) -> int:
  if (right - left < 5):
    return partition(array=array, left=left, right=right)
  for i in range(left, right, 5):
    subRight = i + 4
    if (subRight > right):
      subRight = right
    median = partition(array=array, left=i, right=subRight)
    array[median], array[left + ((i - left) // 5)] = array[left + ((i - left) // 5)], array[median]
  mid = ((right - left) // 10) + left + 1
  return select(array=array, left=left, right=left + ((right - left) // 5), n=mid)

def nth_smallest(array : list[int], n : int) -> int:
  index = select(array=array, left=0, right=len(array), n=n)
  return array[index]

sort_list = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
kth_index = nth_smallest(sort_list, 10)
print(kth_index)
sort_list.sort()
print(sort_list)



# full_list = []
# n = pow(10, 7)
# for i in range(n):
#   full_list.append(random.randint(0, int(n/100)))

# start = time.time()
# nth = nth_smallest(array=full_list, n=int(n / 2))
# print(nth)
# end = time.time()
# print(end - start)