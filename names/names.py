import time
import os
from binary_search_tree import BinarySearchTree
start_time = time.time()
print(os.getcwd())
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# dll_names_1 = BinarySearchTree(names_1[0])
# dll_names_2 = BinarySearchTree(names_2[0])

# # Replace the nested for loops below with your improvements
# for i in names_1:
#     dll_names_1.insert(i)
# for i in names_2:
#     dll_names_2.insert(i)


# def check_for_dupes(name):
#     if dll_names_2.contains(name):
#         duplicates.append(name)
dll_names_1 = {}
dll_names_2 = {}
for i in range(len(names_1)):
    dll_names_1[i] = names_1[i]
for i in range(len(names_2)):
    dll_names_2[names_2[i]] = i

for i in range(len(names_1)):
    if dll_names_1[i] in dll_names_2:
        key = dll_names_1[i]
        duplicates.append(dll_names_1[i])


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did no9  t write yourself.
