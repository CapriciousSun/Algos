import time

def fibonacci(n) -> int:
  if n <= 1:
    return n
  
  total = 0
  first = 1
  second = 0

  for i in range(2, n + 1):
    total = first + second
    second = first
    first = total
  
  return total

print(fibonacci(60))