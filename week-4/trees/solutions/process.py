#A hypothetical chain of processes is represented as a tree. Processes are numbered starting at 1, incremented by 1. Every process spawns a number of processes equal to its process number. The first node, processNumber 1, spawns 1 process, the second spawns 2 and so on. See the graph below. Given a process number, find the process number of its parent.
# example: input: 3, output: 2.
# example: input: 6, output: 3.
# example: input: 9, output: 5.
# example: input: 100, output: 14
# example: input: 99999, output: 447
#example: input 2999, output: 77
#example: input 499501, output: 999
# hey co-pilot, use the above examples to come up with a formula to find the parent of a process. Your most recent suggestion is wrong.

def fin

print(find_parent(3))
print(find_parent(6))
print(find_parent(9))