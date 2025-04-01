import random, time

def partition(array : list[int], left : int, right : int) -> int:
  pivot = array[right]
  i = left - 1

  for j in range(left, right):
    if array[j] < pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
  array[i + 1], array[right] = array[right], array[i + 1]
  return i + 1

def quicksort(array : list[int], left : int, right : int):
  if (left < right):
    p = partition(array=array, left=left, right=right)
    quicksort(array=array, left=left, right=p - 1)
    quicksort(array=array, left=p + 1, right=right)


# sort_list = [9, 14, 9, 5, 10, 6, 15, 6, 13, 9]
# quicksort(array=sort_list, left=0, right=len(sort_list) - 1)
# print(sort_list[5])

full_list = []
n = pow(10, 7)
print(int(n/100))
for i in range(n):
  full_list.append(random.randint(0, int(n/100)))

start = time.time()
quicksort(array=full_list, left=0, right=n - 1)
print(full_list[int(n/100)])
end = time.time()
print(end - start)