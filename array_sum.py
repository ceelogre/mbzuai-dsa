import random
# given a 2d array, calculate the sum of all the numbers in the array
# example:
# sum_of_array([[1,2,3],[4,5,6]]) => 21

def sum_2d(arr):
  sum = 0
  for i in arr:
    for j in i:
      sum  += (j)
  return sum
print(sum_2d([[4,5], [9,5]]))
print(sum_2d([[-2,-3,-4],[-5,-6,-7]]))
print(sum_2d([[1,2,3],[4,5,6]]))

# gnerate random numbers between 1000000000 and 9999999999
# and print the number of digits in the number
random_array = []
for i in range(1000):
  rows = []
  for j in range(1000):
    rows.append(random.randint(1000000000, 9999999999))
  random_array.append(rows)
print(sum_2d(random_array))
#given a 2d array, return a list of pairs of numbers that add up to the target value.
#example:
#return_sum([[1,2,3],[4,5,6]], 7) => [[2,5],[1,6], [3,4]]
