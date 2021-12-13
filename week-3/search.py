# linear search

def linear_search(item, list):
  for i in range(len(list)):
    if list[i] == item:
      return i
  return -1

def linear_search_(item, list):
  for index, elt in enumerate(list):
    if elt == item: return index
  return -1

print(linear_search(15, [4, 5, 9, 29, 123, 98, -3, -65, 92, 6, 15]))

def binary_search(target, list_):
  list = sorted(list_)
  low = 0
  high = len(list_) -1
  while (low <= high):
    mid = (high + low) // 2
    if list[mid] < target :
      low = mid + 1
    elif list[mid] > target:
      high = mid -1
    else: return mid
  return -1

print(binary_search(15, [4, 5, 9, 29, 123, 98, -3, -65, 92, 6, 15]))
def binary_search_(item, list, low, high):

  if low > high: return -1
  mid = (low + high) // 2
  if list[mid] < item:
    return binary_search_(item, list, mid + 1, high)
  elif list[mid] > item:
    return binary_search_(item, list, low, mid-1)
  else: return mid
print(binary_search(5, [4, 4, 9, 29, 123, 15, 98, -65, 92, 6, 15, 4, 4, 9, 29, 123, 5, 98, -65, 92, 6, 15, ]))
#jprint(binary_search(55, [4, 4, 9, 29, 123, 98, -3, -65, 92, 6, 5]))
#print(binary_search(15, [4, 5, 6, 7, 8, 10, 15, 33, 65, 72, 75]))
list_ =  [4, 4, 9, 29, 123, 98, -3, -65, 92, 6, 5]
low = 0
high = len(list_) -1
list = sorted(list_)
print(binary_search_(5, list, low, high))