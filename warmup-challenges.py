#10 Warm up Challenges

# Challenge 1:
# Write a program that prints out all the elements of the list "numbers" that are less than 5.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list(filter(lambda x: x < 5, numbers)))

#Challenge 2:
#Write a Python program which will return true if the two given integer values are equal or their sum or difference is 5.
def equal_or_five(a, b):
  return True if a == b or a + b < 5 or a -b < 5 else False
print(equal_or_five(5,5))
print(equal_or_five(5,-5))
print(equal_or_five(-5,5))
print(equal_or_five(-5,-5))
print(equal_or_five(-5,9))
print(equal_or_five(9,9))
print(equal_or_five(5,9))
print(equal_or_five(19,9))
#Challenge 3:
#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
  d1,d2= x2-x1, y2-y1
  return d1,d2
print(distance(4,5,8,9))

#Challenge 4:
# Define a function named count that takes a single parameter. 
# The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these: "ba-na-na", "Data", "me-ta"
# Your function should count the number of syllables and return it.
# The call count("ho-tel") should return 2
print(len(list(filter(lambda x: x in ['a','e','i','o','u'], list("ho-tel")))))

#Challenge 5:
# Define a function named up_down that takes a single number as its parameter. 
# Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
# For example, calling up_down(0) should return (-1, 1).
def up_down(num):
  return num-1,num+1

print(up_down(5))
print(up_down(0))
#Challenge 6:
#Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones
#Your function should return the number of consecutive zeros in the string.
#For instance, with this input "1001101000110", the function will return 3.

#Challenge 7:
# Write a Python program to check whether variable is integer or string or float.
# If the variable is integer, print "Integer"
# If the variable is string, print "String"
# If the variable is float, print "Float"
# If the variable is boolean, print "Boolean"
def reveal_type(var):
  if type(var) == int:
    return "Integer"
  elif type(var) == str:
    return "String"
  elif type(var) == float:
    return "Float"
  else:
    return "Not int or string or float"

print(reveal_type(5))
print(reveal_type("Hello"))
print(reveal_type(5.5))
print(reveal_type(True))
#Challenge 8:
# Write a Python program to count and display the vowels of a given text.
def count_vowels(text):
  counter = 0
  for char in text:
    if char in ['a', 'i', 'u', 'e', 'o']:
      print(char)
      counter += 1
  return counter

print(count_vowels('the quick brown fox jumps over the lazy dog.'))

#Challenge 9:
#Write a Python program to count the occurrences of each characher in a given sentence
def count_chars(text):
  counter = dict()
  unique_chars = set(text)
  for char in unique_chars:
    # add char to dictionary
    counter[char] = text.count(char)
  return counter
print(count_chars('the quick brown fox jumps over the lazy dog.'))

#Challenge 10:
# Write a Python program which solve the equation:
# ax+by=c
# dx+ey=f
# Print the values of x, y where a, b, c, d, e and f are given.






#Assignment Day 1:
#Problem statement:
"""
The Fibonacci sequence is a series of numbers where every number is the sum of the two numbers before it. The first two numbers are 0 and 1:
You must write the fib() function which takes in a positive integer, n, and returns the n-th Fibonacci number. 
Your function must use any of the loops (for loop or while loop).
Sample input
n=7
Sample output
8
"""

def fib(n):
  a,b = 0,1
  for i in range(n):
    a,b = b, a+b

  return a
print(fib(6))