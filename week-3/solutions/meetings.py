#Given a collection of time intervals, [start, end], merge and return the overlapping intervals sorted in ascending order of their start times
#Example

#intervals = [[7, 7], [2, 3], [6, 11], [1, 2]]

#The interval [1, 2] merges with [2, 3] while [7, 7] merges with [6, 11]. There are no more overlapping intervals. The answer is [[1, 3], [6, 11]].

def merge_sort(L):
  if len(L) == 1:
    return L
  middle = len(L) // 2
  left = L[0:middle]
  right = L[middle:]
  return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
  results = []

  while (len(left) > 0 and len(right) > 0):
    if left[0] > right[0]:
      results.append(right.pop(0))
    else:
      results.append(left.pop(0))
  while(len(left) > 0):
    results.append(left.pop(0))
  while(len(right) > 0):
    results.append(right.pop(0))
  return results

def merge_intervals(intervals):
    if len(intervals) == 0:
        return []
    intervals = merge_sort(intervals)
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged

merge_intervals([[7, 7], [2, 3], [6, 11], [1, 2]])

# The algorithm starts with the first interval and compares it to the other intervals.
# If the start time of the current interval is less than or equal to the end time of the previous interval, then the start time of the current interval is updated to the larger of the two.
# If the start time of the current interval is greater than the end time of the previous interval, then the current interval is added to the list of merged intervals.
# The algorithm continues until all intervals have been compared.
# The algorithm is O(n^2) because it compares all intervals to all other intervals.