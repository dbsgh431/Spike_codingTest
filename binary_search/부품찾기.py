from input import input_N_list
from binary_search_basic import binary_search

N_array = input_N_list.generate_N_list()
M_array = input_N_list.generate_N_list()

print(N_array)
print(M_array)

N_array.sort()
for i in M_array:
    if binary_search(N_array, i, 0, len(N_array) - 1):
        print("yes")
    else:
        print("no")
