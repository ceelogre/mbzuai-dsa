def restructure_array(arr, queries):
  # remove the first element
  cols_len = arr[0]
  rows_len = int(len(arr) / cols_len)
  # create a new array
  new_arr = []
  temp_arr = []
  for index in range (1, len(arr)):
    temp_arr.append(arr[index])
    if index % cols_len == 0 and index != 1:
      new_arr.append(temp_arr)
      temp_arr = []
  query_results = []
  for query in queries
    index_1, index_2 = query[0] - 1, query[1] - 1
    query_results.append(new_arr[index_1][index_2])

  return query_results

def restructure_array_(arr, queries):
  query_results = []
  for q in queries:
    r = q[0]
    c = q[1]
    arr_index = (r-1) * arr[0] + c
    query_results.append(arr[arr_index])
  return query_results

#print(restructure_array([5, 1,2,3,4,5,6,7,8,9,10], [[1,1], [1, 2], [2,1], [2,2]]))
#print(restructure_array([4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [[3,2], [2,1]]))
print(restructure_array_([2, 4, 1, 34, 12, -33, 78, 44, 65, -14, -92], [[4,1], [3,2], [5,1], [1,1]]))
print(restructure_array_([23,
1,
-38,
-18,
5,
-11,
23,
88,
-87,
-38,
65,
-38,
31,
32,
81,
-85,
90,
-22,
-6,
32,
69,
-52,
-26,
44,
10,
2], [[2, 1], [17, 1], [19, 1], [4, 1], [12, 1], [1, 1],[7, 1], [16, 1], [20, 1], [18, 1]]))