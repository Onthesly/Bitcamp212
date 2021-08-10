import matplotlib.pyplot as plt
import numpy as np

methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36']    # 보간 방법
grid = np.random.rand(5, 5)                                         # 0~1사이 임의 난수 생성

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(8,6))            # 서브 플롯들 생성

for ax, method in zip(axs.flat, methods):                           # 서브 플롯 순회
    ax.imshow(grid, interpolation=method, cmap='gray')               # 명암도 영상 표시
    ax.set_title(method)                                            # 서브 플롯 제목
plt.tight_layout(), plt.show()                                      # 여백 없음, 윈도우 띄움