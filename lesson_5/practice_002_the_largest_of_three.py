# Find the max number from 3 values.
#
# Example: 124, 21, 32. Result = 124.

num_arr = [124, 21, 32]
max = num_arr[0]
for i in range(0, len(num_arr), 1):
    if max < num_arr[i]:
        max = num_arr[i]
print(max)




