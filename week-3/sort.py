import random
import time
# bubble sort algorithm
def bubble_sort(L):
  swapped = True
  while swapped == True:
    swapped = False
    for i in range(len(L) - 1):
      if L[i] > L[i+1]:
        temp = L[i]
        L[i] = L[i+1]
        L[i+1] = temp
        swapped = True
  return L

def selection_sort(L):
  for i in range(len(L)):
    max_ = i
    for j in range(i+1, len(L)):
      if L[j] > L[max_]:
        max_ = j
    if max_ != i:
      L[i], L[max_] = L[max_], L[i]

  return L
#L = [43, 93, 96, 6,34,78,5, 43]
# generate a large dataset and put it in a list variable L
L = [random.randint(0,100) for i in range(10000)]


def quick_sort(L):
  if len(L) <= 1:
    return L

  pivot = L[0]
  L.remove(pivot)
  left = []
  right = []
  for i in range(len(L)):
    if L[i] < pivot:
      left.append(L[i])
    else:
      right.append(L[i])
  
  return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(L):
  # stopping condition
  if len(L) == 1:
    return L
  mid = len(L) // 2
  left = L[0:mid]
  right = L[mid:]
  return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
  result = []
  while len(left) != 0 and len(right) != 0:
    if left[0] <= right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  while len(left) != 0:
    result.append(left.pop(0))
  while len(right) != 0:
    result.append(right.pop(0))

  return result

# print(bubble_sort(L)) => [5, 6, 34, 43, 78, 93, 96]
# print(bubble_sort(L))
#print(selection_sort(L))
print(time.ctime())
(merge_sort(L))
print(time.ctime())

print('-----------------\n')
print(time.ctime())
(bubble_sort(L))
print(time.ctime())