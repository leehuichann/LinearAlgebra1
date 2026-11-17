import numpy as np

# 주어진 벡터
u = np.array([1, -1, 0], dtype = float)
v = np.array([2, -1, 2], dtype = float)

# 내적과 벡터의 길이
dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

if norm_u == 0 or norm_v == 0:
    raise ValueError("영벡터가 포함되면 각도를 정의할 수 없습니다.")

# cos(theta) = 내적 / 두 벡터의 길이의 곱
cos_theta = dot_product / (norm_u * norm_v)
cos_theta = np.clip(cos_theta, -1.0, 1.0)

# 라디안을 각도를 구한 뒤 도 단위로 변환
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print(f"내적\t\t\t= {dot_product: .6f}")
print(f"u의 길이\t\t= {norm_u: .6f}")
print(f"v의 길이\t\t= {norm_v: .6f}")
print(f"cos(theta)\t\t= {cos_theta: .6f}")
print(f"각도(라디안)\t\t= {theta_rad: .6f}")
print(f"각도(도)\t\t= {theta_deg: .6f}")