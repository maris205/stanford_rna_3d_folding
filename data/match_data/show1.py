# -*- coding: utf-8 -*-
# @Time    : 2025/3/6  22:50
# @Author  : mariswang@rflysim
# @File    : show1.py
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg'、'WebAg

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# 加载数据
df = pd.read_csv("train_labels.csv")

# 提取目标并排序
target = "1SCL_A"
r1107 = df[df["ID"].str.startswith(target)].sort_values("resid")

# 创建碱基颜色映射字典（可自定义颜色）
base_colors = {
    'G': '#FF0000',  # 红色
    'U': '#00FF00',  # 绿色
    'C': '#0000FF',  # 蓝色
    'A': '#FFD700'   # 金色
}

# 生成颜色序列
colors = r1107['resname'].map(base_colors).values

# 提取坐标
coords = r1107[['x_1', 'y_1', 'z_1']].values
x, y, z = coords[:,0], coords[:,1], coords[:,2]

# 创建画布
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# 绘制带颜色编码的散点图
scatter = ax.scatter(x, y, z,
                    c=colors,  # 使用映射的颜色序列
                    marker='o',
                    s=50,
                    depthshade=True,  # 启用深度阴影
                    label='Residues')

# 绘制骨架连线（保持原有蓝色）
ax.plot(x, y, z, 'b--', alpha=0.5, linewidth=1, label='Backbone')

# 创建图例代理
legend_elements = [plt.Line2D([0], [0],
                            marker='o',
                            color='w',
                            label=base,
                            markerfacecolor=color,
                            markersize=10)
                 for base, color in base_colors.items()]

# 添加图例
ax.legend(handles=legend_elements, title="Nucleobases", loc='upper left')

# 设置坐标轴和标题
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis', fontsize=12)
ax.set_zlabel('Z Axis', fontsize=12)
ax.set_title(f'3D Structure of {target} with Nucleobase Coloring', fontsize=14)

# 调整视角
#ax.view_init(elev=25, azim=-60)  # 优化后的视角参数

ax.view_init(elev=25, azim=35)

plt.tight_layout()
plt.show()