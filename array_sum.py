import random
from functools import reduce
# given a 2d array, calculate the sum of all the numbers in the array
# example:
# sum_of_array([[1,2,3],[4,5,6]]) => 21

def sum_2d(arr):
 # flatten the array
 l = reduce(lambda x,y: x+y, arr)
 sum = reduce(lambda x,y: x+y, l)
 return sum
print(sum_2d([[4,5], [9,5]]))
print(sum_2d([[-2,-3,-4],[-5,-6,-7]]))
print(sum_2d([[1,2,3],[4,5,6]]))

#given a 2d array, return a list of pairs of numbers that add up to the target value.
#example:
#return_sum([[1,2,3],[4,5,6]], 7) => [[2,5],[1,6], [3,4]]
def return_sum_pairs(l, target_value):
  l_one, l_two = l
  pairs = []
  for item_one in l_one:
    for item_two in l_two:
      if item_one + item_two == target_value:
        pairs.append([item_one, item_two])
  return pairs
print(return_sum_pairs([[1,2,3], [4,5,6]], 7))