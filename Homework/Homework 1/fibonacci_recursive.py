import time

def fibonacci(n) -> int:
  if n <= 1:
    return n
  else:
   	return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(44):
  start_time = time.time()
  print(fibonacci(i))
  print(time.time() - start_time)