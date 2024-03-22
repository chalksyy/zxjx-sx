# 该程序是Kmeans算法的主程序
import random

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import algorithmslib as ab
import K_means

# 该程序段是已知k值输入后的聚类算法

# 读取数据
df=pd.read_csv("./student_for_kmeans.csv")
# 获得聚类之后的簇列表和簇心列表
clusterB,groupB=K_means.k_means(df, 47, 200, 100)
# 轮廓系数法，看轮廓系数
n=ab.coc(df,groupB)
print(n)
print(clusterB)
print(groupB)

#该程序段是用与找到最佳的k值
# 通过初步确定k的大致取值再将k值在这个范围区间内使用轮廓系数法找到最佳的取值
# print("Max:",n)
# print("Group:")
# for i in groupB:
#     print(i)
# k=0
# Max=0
# clusterB=[]
# groupB=[]
# for i in range(30,70):
#     print("k=",i,"时")
#     cluster,group=K_means.k_means(df,i,200,100)
#     n=ab.coc(df,group)
#     if n>Max:
#         Max=n
#         k=i
#         clusterB=cluster
#         groupB=group
# print("k:",k)
# print("max:",Max)

# 这部分代码是用于降维输出的

# 定义标志，即可视化的图案
markers = ['+', 'x', 's', 'p', 'o', '^', 'v', '.']
# 定义颜色，即可视化的颜色
colorlist = ['r', 'k', 'b', 'y', 'm', 'c', 'g', 'yellowgreen', 'blueviolet', 'brown', 'burlywood', 'cadetblue',
                 'chartreuse', 'chocolate',
                 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod',
                 'darkgray', 'darkgreen',
                 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon',
                 'darkseagreen',
                 'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray',
                 'dodgerblue',
                 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod']
# 把数据降维到2维
tsne = TSNE(n_components=2)
point = clusterB
a = np.array(point)
p = np.array(df)
a = tsne.fit_transform(a)
p = tsne.fit_transform(p)
# 将降维后的数据可视化
for i in range(0, len(groupB)):
    plt.scatter(a[i][0], a[i][1], marker=markers[1], color=colorlist[i])
    for j in groupB[i]:
        plt.scatter(p[j][0], p[j][1], marker=markers[4], color=colorlist[i])
plt.show()

