# kmeans算法主体

import algorithmslib as ab
import pso
import random

#k-means算法
#df为输入多维数据，以DataFrame形式存储
#k为所定义的簇的数量
#n为Pso算法迭代上限
#q为k-means算法迭代上限
def k_means(df,k,n,q):
    #存储簇心的列表
    cluster=[]
    print("pso算法开始运行，开始寻找初始簇心：")
    for i in range(0,k):
        print("开始寻找第",i+1,"个聚类中心")
        cluster.append(pso.Pso(df,k,n)) # 参数相同，为什么pso得到的簇心不同呢？
        print("第",i+1,"个聚类中心已经找到")
    print("pso算法运行完毕，所找到的初始",k,"个簇心分别为：")
    for i in cluster:
        print(i)
    #用于存放各簇的中位点
    # mesPo=[]
    #存放各特征值的权重
    w=ab.widget(df)
    print("w:", w)
    #迭代轮数
    c=1

    print("K-means算法开始迭代：")
    #各点关联到簇心
    while c<q:
        print("进行第",c,"次迭代")
        # 存储各簇心所属的点
        group = []
        # 初始化group
        for i in range(0, k):
            group.append([])
        for i in range(0,len(df)):
            # 读取一条数据
            llist=df.iloc[i].tolist()
            # 计算此数据和簇心的距离
            min=ab.wdist(llist,cluster[0],w)
            m=0
            # 寻找最小的距离，将最小的距离保存到group中
            for j in range(1,k):
                dic=ab.wdist(llist,cluster[j],w)
                if min>dic:
                    min=dic
                    m=j
            group[m].append(i)

        #算出中位点（即新的簇心）
        mesPo=[] # 用于存放各簇的中位点
        for i in range(0,len(group)):
            # 如果此簇为空，则没必要重新计算簇心，如果不为空则重新计算簇心
            if len(group[i])!=0:
                mesPo.append(ab.mesPoint(df,group[i])) # 调用计算簇心的函数
            else:
                mesPo.append(cluster[i]) # 簇为空则不用重新计算，还是原来的簇心

        # 如果簇心没有变化，则循环结束
        if ab.check(cluster,mesPo)==True:
            break
        # 将mespo赋值给cluster用于返回
        cluster=mesPo
        # 循环次数+1
        c+=1

    # 返回簇心列表和分组列表
    return cluster,group
