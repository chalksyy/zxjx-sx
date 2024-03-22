# PSO算法
import random
import algorithmslib as ab


# PSO算法主体
# df为要处理的数据集
# k为簇心个数
# n为pso迭代次数
def Pso(df,k,n):
    c=1
    #存储个体最优解位置
    pb=[]
    #存储个体最优解适应值
    pbf=[]
    #存储群体最优解位置
    gb=[]
    #存储群体最优解适应值
    gbf=0
    #存储各个点的速度
    v=[]
    #前一次迭代的惯性
    w=0.72
    #个体/群体最优解的惯性
    c1=1.49
    c2=1.49
    #用于寻找群体历史最优适应值
    # 随机产生k个簇心
    cluster=[]
    for i in range(0,k):
        # llist为一条数据
        llist=[]
        # lt为一条数据的各个特征值
        lt=[]
        # 初始化llist和lt
        for j in range(0,len(df.columns)):
            llist.append(random.random()*100)
            lt.append(0.0)
        v.append(lt)
        cluster.append(llist)
        pb.append(llist)
        pbf.append(0.0)

    while c<=n:
        if c%50==0:
            print("已迭代",c,"次")
        # 簇心对应点
        group = []
        # 关联簇心
        for i in range(0, k):
            group.append([])
        # 将数据中的各点关联到簇
        for i in range(0, len(df)):
            # 从df中取出一条数据
            llist = df.iloc[i].tolist()
            # 计算此数据到簇心距离
            min = ab.dist(llist, cluster[0])
            m=0
            # 寻找最小的距离，将最小的距离保存到group中
            for j in range(0, k):
                dic = ab.dist(llist, cluster[j])
                if min > dic:
                    min = dic
                    m = j
            group[m].append(i)
        # 个体、群体最优解进行迭代
        for i in range(0, k):
            fitness = 0
            # 如果此组不为空则计算适应度
            if len(group[i]) != 0:
                fitness = ab.fit(df, group[i], cluster[i])
            # 如果此适应度比个体最优解适应值更大，则保存到pbf中，并且将此簇心保存到pb中
            if fitness > pbf[i]:
                pbf[i] = fitness
                pb[i] = cluster[i]
            # 如果此适应度比群体最优解适应值更大，则保存到gbf中，并且将此簇心保存到gb中
            if gbf < fitness:
                gbf = fitness
                gb = cluster[i]
        # 计算速度
        r1, r2 = random.random(), random.random()
        for i in range(0, len(v)):
            for j in range(0, len(v[i])):
                v[i][j] = w * v[i][j] + c1 * r1 * (pb[i][j] - cluster[i][j]) + c2 * r2 * (gb[j] - cluster[i][j])
        # 更新簇心位置
        for i in range(0, k):
            for j in range(0, len(cluster[i])):
                cluster[i][j] += v[i][j]
                if cluster[i][j]>100:
                    cluster[i][j]=100
                elif cluster[i][j]<0:
                    cluster[i][j]=0
        c+=1
    return pb[0]