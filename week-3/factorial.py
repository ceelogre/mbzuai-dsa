def factorial(n):
  # n * n-1 * n-2...
  if n <= 1: 
    return 1
  else: 
    return n * factorial(n-1)

print(factorial(5))