def sum_row_and_column(matrix, row_index, col_index):
    row_sum = sum(matrix[row_index])  # 获取行的所有数字的和
    col_sum = sum(row[col_index] for row in matrix)  # 获取列的所有数字的和
    overlap_value = matrix[row_index][col_index]  # 获取重复的值

    total_sum = (row_sum + col_sum - overlap_value) * 2

    remaining_sum = sum(sum(row) for row in matrix) - overlap_value

    final_sum = total_sum + remaining_sum
    return final_sum

# 示例二维数组
matrix = [
    [2, 3, 1, 4],
    [1, 2, 0, 3],
    [4, 2, 1, 7],
    [3, 1, 4, 2]
]

# 示例：获取第2行和第1列的数字和，并减去重复的值，然后乘以2并加上剩余的数组
row_index = 2
col_index = 3
result = sum_row_and_column(matrix, row_index, col_index)
print("最终结果：", result)
