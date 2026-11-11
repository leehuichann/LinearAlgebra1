import numpy as np

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("실습 7-1")

A = np.array([
    [2, 3],
    [3, -6]
], dtype=float)

# 특성다항식의 계수 계산
coefficients = np.poly(A)

# 고유값 계산
eigenvalues = np.linalg.eigvals(A)

# 허수 부분이 0인 계산 결과를 실수로 변환
eigenvalues = np.real_if_close(eigenvalues)

# MATLAB 화면처럼 고유값을 -7, 3 순서로 정렬
eigenvalues = np.sort(eigenvalues)

print("poly(A) =")
print(coefficients)
print("\neig(A) =")
print(eigenvalues.reshape(-1, 1))


print("\n실습 7-2")

A = np.array([
    [3, 2],
    [3, -2]
], dtype=float)

# 고유값과 고유벡터 계산
eigenvalues, X = np.linalg.eig(A)

# 허수 부분이 0인 계산 결과를 실수로 변환
eigenvalues = np.real_if_close(eigenvalues)
X = np.real_if_close(X)

# MATLAB 화면처럼 고유값을 4, -3 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

# 고유값을 대각행렬로 변환
lamda = np.diag(eigenvalues)

print("X =")
print(X)
print("\nlamda =")
print(lamda)


print("\n실습 7-3")

A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1]
], dtype=float)

# 고유값과 고유벡터 계산
eigenvalues, X = np.linalg.eig(A)

# 허수 부분이 0인 계산 결과를 실수로 변환
eigenvalues = np.real_if_close(eigenvalues)
X = np.real_if_close(X)

# MATLAB 화면처럼 고유값을 2, 1, -1 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

# 고유값을 대각행렬로 변환
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("X =")
print(X)
print("\nlamda =")
print(lamda)


print("\n실습 7-4")

A = np.array([
    [0, 0, 0],
    [0, 2, 5],
    [0, 0, -1]
], dtype=float)

B = np.array([
    [4, 0, 0],
    [0, 0, 0],
    [1, 0, -3]
], dtype=float)

# 두 행렬의 고유값 계산
eigenvalues_A = np.linalg.eigvals(A)
eigenvalues_B = np.linalg.eigvals(B)

# 허수 부분이 0인 계산 결과를 실수로 변환
eigenvalues_A = np.real_if_close(eigenvalues_A)
eigenvalues_B = np.real_if_close(eigenvalues_B)

# MATLAB 화면처럼 고유값을 세로로 출력
print("eig(A) =")
print(eigenvalues_A.reshape(-1, 1))
print("\neig(B) =")
print(eigenvalues_B.reshape(-1, 1))
