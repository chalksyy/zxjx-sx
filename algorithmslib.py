# 项目所用到的周边算法库
import matplotlib.pyplot as plt

#轮廓系数法求k值
def coc(df,group):
    s=0
    llist=[]
    for i in range(0,len(df.columns)):
        a=0
        #最大距离
        b=142
        for j in group:
            if i in j:
                llist=j
                break
        for j in llist:
            if i!=j:
                # 欧氏距离计算
                a+=dist(df.iloc[i].tolist(),df.iloc[j].tolist())
        # 组内不相似度求平均值
        if a!=0:
            a/=len(llist)-1
        # 组间不相似度求最小值
        for j in group:
            if j!=llist:
                for k in j:
                    # 欧氏距离计算
                    dic=dist(df.iloc[i].tolist(),df.iloc[k].tolist())
                    if dic<b:
                        b=dic
        s+=(b-a)/max(a,b)
    return s/len(df.columns)



# 计算适应度
# df为要处理的数据
# c为簇心
# lt为簇心所属的点的集合列表
def fit(df,lt,c):
    #k值为负相关指数
    sum=0
    for i in lt:
        sum+=dist(df.iloc[i].tolist(), c)
    return 1/sum

#欧氏距离计算
#lt为一个维度DataFrame的各个特征值
#c为簇心点,以列表的形式存储
def dist(lt,c):
    dis=0
    for i in range(0,len(lt)):
        dis+=(lt[i]-c[i])**2
    return dis**0.5

#有权重的欧氏距离
#lt为一个维度DataFrame的各个特征值
#c为簇心点,以列表的形式存储
#w为权重
def wdist(lt,c,w):
    dis=0
    for i in range(0,len(lt)):
        dis+=w[i]*((lt[i]-c[i])**2)
    return dis**0.5

#计算各个簇的权重系数
#df为要处理文件
def widget(df):
    mean=[]
    kwight=[]
    s=0
    # 取一条数据，然后把此数据的所有维度加起来为sum，sum/数据总数=meam
    for i in range(0,len(df.columns)):
        sum=0
        for j in range(0,len(df)):
            sum+=df.iloc[j].tolist()[i]
        mean.append(sum/len(df))

    # 取一条数据，然后把此数据的（所有维度-所在维度的mean）的平方加起来为gs
    for k in range(0,len(df.columns)):
        gs=0
        for j in range(0,len(df)):
            gs+=(df.iloc[j].tolist()[k]-mean[k])**2
        kwight.append(gs)
        s+=gs
    # for i in kwight:
    #     i/=s

    return kwight


#中位点的计算
#df为要计算的文件
#lt为存放各簇心对应的点
def mesPoint(df,lt):
    point=[]
    for i in range(0,len(df.columns)):
        sum=0
        for j in range(0,len(lt)):
            sum+=df.iloc[lt[j]].tolist()[i]
        point.append(sum/len(lt))
    return point

#判断簇心是否改变了
def check(cluster,mesPo):
    flag=True
    for i in (0,len(cluster)-1):
        if cluster[i]!=mesPo[i]:
            flag=False
            break
    return flag

# 将作业成绩分为五档
def psConverF(n):
    s=""
    if n>=90:
        s="优秀"
    elif n>=80:
        s="良好"
    elif n>=70:
        s="中等"
    elif n>=60:
        s="及格"
    else:
        s="不及格"
    return s

# 将课堂完成的分为四档
def psConver(n):
    s=""
    if n>=0.85:
        s="完成度高"
    elif n>=0.6:
        s="完成度良好"
    elif n>=0.55:
        s="完成度一般"
    else:
        s="完成的差劲"
    return s

# 将回帖数分为三档
def psConverPt(n):
    s=""
    if n>=10:
        s="对知识点了解深入"
    elif n>5:
        s="对知识点有些许理解"
    else:
        s="对知识点没有深入了解"
    return s

# 将数值转化为标签
def switchLevel(statis,group):
    lt = []
    for i in statis[group]:
        tlt = []
        tlt.append(psConverF(i[1]))
        if i[2] > 1:
            tlt.append("提交")
        else:
            tlt.append("未提交")
        tlt.append(i[3])
        tlt.append(psConver(i[4]))
        tlt.append(i[5])
        tlt.append(psConverPt(i[6]))
        tlt.append(i[7])
        tlt.append(i[8])
        lt.append(tlt)
    return lt

# 给直方图加上数值显示
def auto_text(rects):
    for rect in rects:
        plt.text(x=rect.get_x()+0.3, y=rect.get_height(), s=rect.get_height(), ha='left', va='bottom')