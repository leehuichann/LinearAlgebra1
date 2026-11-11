import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# ==========================================
# 1. 수치 연산 및 콘솔 결과 출력
# ==========================================
v1 = np.array([0, 1, 1])
v2 = np.array([1, 0, 1])
v3 = np.array([1, 1, 2])

print("=" * 50)
print(" [선형대수학 10주차 과제 - 벡터 연산 결과 출력] ")
print("=" * 50)
print(f"주어진 벡터:")
print(f"  v1 = {v1}")
print(f"  v2 = {v2}")
print(f"  v3 = {v3}\n")

# 선형종속 검증 (v3 = v1 + v2)
is_dependent = np.array_equal(v3, v1 + v2)
print(f"1. v1 + v2 = {v1 + v2}")
print(f"   v3 == v1 + v2 여부: {is_dependent} (선형종속 성립)\n")

# 평면 방정식 검증 (x + y - z = 0)
plane_check_v1 = v1[0] + v1[1] - v1[2]
plane_check_v2 = v2[0] + v2[1] - v2[2]
plane_check_v3 = v3[0] + v3[1] - v3[2]

print("2. 평면 방정식 (x + y - z = 0) 대입 검증:")
print(f"   v1 대입: {v1[0]} + {v1[1]} - {v1[2]} = {plane_check_v1}")
print(f"   v2 대입: {v2[0]} + {v2[1]} - {v2[2]} = {plane_check_v2}")
print(f"   v3 대입: {v3[0]} + {v3[1]} - {v3[2]} = {plane_check_v3}")
print("   => 세 벡터 모두 평면 x + y - z = 0 위에 존재함")
print("=" * 50)

# ==========================================
# 2. 3차원 그래프 시각화
# ==========================================
fig = plt.figure(figsize=(9, 7), dpi=150)
ax = fig.add_subplot(111, projection='3d')

# 평면 생성 (z = x + y)
s_val = np.linspace(-0.2, 1.5, 10)
t_val = np.linspace(-0.2, 1.5, 10)
S, T = np.meshgrid(s_val, t_val)
X = T
Y = S
Z = S + T

# 평면 그리기
surf = ax.plot_surface(X, Y, Z, alpha=0.3, color='cyan', edgecolor='none')

# 원점에서 각 벡터로 향하는 화살표 그리기
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='blue', linewidth=2.5, arrow_length_ratio=0.08, label=r'$v_1 = (0, 1, 1)$')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='green', linewidth=2.5, arrow_length_ratio=0.08, label=r'$v_2 = (1, 0, 1)$')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='red', linewidth=2.5, arrow_length_ratio=0.08, label=r'$v_3 = (1, 1, 2) = v_1 + v_2$')

# 벡터 끝점에 텍스트 라벨 표시
ax.text(v1[0], v1[1], v1[2] + 0.1, r'$v_1(0,1,1)$', color='blue', fontweight='bold')
ax.text(v2[0], v2[1], v2[2] + 0.1, r'$v_2(1,0,1)$', color='green', fontweight='bold')
ax.text(v3[0], v3[1], v3[2] + 0.1, r'$v_3(1,1,2)$', color='red', fontweight='bold')

# 축 범위를 조절하여 깔끔하게 보기
ax.set_xlim([-0.2, 1.8])
ax.set_ylim([-0.2, 1.8])
ax.set_zlim([-0.2, 2.5])

# 축 라벨 및 제목 설정
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title(r'Visualization of $v_1, v_2, v_3$ and Plane $V: x + y - z = 0$', pad=15)
ax.legend(loc='upper left')

# 카메라 시점 조절 (고도 20도, 방위각 45도)
ax.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()