# 행렬
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 대각합 계산
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))

print("대각합 :", diagonal_sum)