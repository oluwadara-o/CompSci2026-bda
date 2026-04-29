from solutions.exercise_01_02_lib import my_len, my_sum

data = [10, 20, 30, 40, 50]


print(my_len(data))  # Output: 5
print(my_sum(data))  # Output: 150

matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    # Reset col_index for each new row.
    col_index = 0
    row_index += 1