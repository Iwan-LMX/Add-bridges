import sys
from itertools import product as I
a=sys.stdin.read().split()

P=list(I(range(len(a)),range(len(a[0])))) #这个是map 坐标点, 不包含islands信息
E={p:[]for p in P}
Q={(i,j):int(a[i][j])for i,j in P if'.'!=a[i][j]} #Q是岛屿坐标与岛屿value
F=[] #表示这两岛间可以建桥 [(x, y), (x, y)], [], ...

#生成同行 / 同列 pairs
for p,c in Q.items(): #p is coord (x, y), c is the islands number
    #找到该岛所在行列第一个邻居
    for i,j in((0,1),(1,0)):
        #p是岛坐标, q是p岛行列上的点
        q=p[0]+i,p[1]+j;   e=[p,0] 
        while q in P: #没有越界
            E[q]+=[e] #因为e是个list, 下面修改e形成pair导致这里也会自动更新
            if q in Q: e[1]=q;E[p]+=[e];F+=[e];break #存储 pair
            q=q[0]+i,q[1]+j
E={x:[x for x in y if x[1]!=0]for x,y in E.items()} #两个岛之间能够形成桥的地方会带上岛pairs的value, 如果这个地方没有桥要通过则会为空
C=[E[p] for p in P if p not in Q and len(E[p])>1] #找出找出两桥交叉的部位
m=[] #m is the table of all subsets 
T=len(Q)+4*len(F)+len(C) #这个应该表示元素总量, 4F应该表示四个方向
s=0
l={}

#生成subsets, m为subsets表.
#周围可选岛屿
for p,c in Q.items():
    e=E[p];u=len(e)*2 #u乘2是因为0, 1, 2这三个数二进制表示需要用2个长度
    for t in I(*((0,1,2)for x in e)): #这里会生成一个笛卡尔积, 长度/元素数量对应这个岛能和邻居连接的数量. 比如(0,0)这个岛能和右, 下两个邻居相连所以有两个slots. 每个slot的0, 1, 2表示桥的数量.
        if sum(t)!=c:continue
        r=[0]*T;r[s+u]=1
        for i,x in enumerate(t):k=s+i*2;r[k:k+2]=((1,1),(0,1),(0,0))[x] #这三个二进制数是用来表示这个岛相连的几座桥按顺序要建造的lanes的数量. 11 表示0, 01表示1, 00表示2. (因为我们最多lane是三所以需要还需要额外加上10 b) || 但是为啥用(1, 1)而不是(1, 0)?
        m+=[r]
    l[p]=s;s+=u+1
z=len(m)
#处理交叉的桥
for e in F:
    p,q=e; r=[0]*T
    c,d=l[p]+E[p].index(e)*2,l[q]+E[q].index(e)*2 #这个*2 刚好对应上边这里的(1, 1), (0, 1), (0, 0)的位置
    t=r[:]; r[c]=r[d]=1 #t是r的copy
    for i,u in enumerate(C):r[T-len(C)+i]=int(e in u) #这里最后len(C) 个元素表示当前这对路是否处于交叉路
    t[c+1]=t[d+1]=1;m+=[r,t] 

def I(x,d):
    y=d[x]
    while y!=x: yield y;    y=d[y]
def A(c): #selecting which columns in these rows have 1
    len[R[c]],R[len[c]]=len[c],R[c]
    for x in I(c,D):
        for y in I(x,R):U[D[y]],D[U[y]]=U[y],D[y]
def B(c): #selecting which rows in these columns have 1
    for x in I(c,U):
        for y in I(x,len):U[D[y]],D[U[y]]=y,y
    len[R[c]],R[len[c]]=c,c
def S(): #algorithm X / dancing
    c=R[h]
    if c==h:yield[]
    A(c)
    for r in I(c,D):
        for x in I(r,R):A(C[x])
        for t in S():yield[r[0]]+t
        for x in I(r,len):B(C[x])
    B(c)
len,R,U,D,C={},{},{},{},{}#left, right, up, down, col
h=T
len[h]=R[h]=D[h]=U[h]=h
#似乎是一个环, 
for c in range(T):
    R[len[h]],R[c],len[h],len[c]=c, h, c, len[h] #len 是一个从T: T-1, T-1: T-2 ... 1:0, 0:T的环, R是一个 0:1, 1:2, ... , T-1 : T, T:0的环
    U[c]=D[c]=c #U D 分别是0:0, 1:1, ... , T:T的映射

#生成舞蹈链
for i,l in enumerate(m):
    s=0
    for c in I(h,R): #就是c in range(T+1):
        if l[c]:
            r=i,c
            D[U[c]],D[r],U[c],U[r],C[r]=r,c,r,U[c],c #U[c] 是这列的最新的up, d是这列的最新的down
            if s==0:len[r]=R[r]=s=r #舞蹈链的head
            R[len[s]],R[r],len[s],len[r]=r,s,r,len[s] #s一直代表这行的最左端, r代表最右端
#解舞蹈链并将bridge塞入, R存放的是right, len存放的是left
for s in S(): #s 是舞蹈链的解法, 这个值似乎可以表示x算法筛选过程中山掉的某个行或者列
    b=list(map(list,a))
    for e in s:
        if e<z:continue# z是sum(岛数量* 岛和周围邻居数量)
        (i,j),(x,y)=F[(e-z)//2]
        if j==y:
            for r in range(i+1,x):b[r][j]='|H'[b[r][j]=='|'] #似乎如果(r,j)位置有两次参与就是H, 一次参与就是|. 下面同样道理
        else:
            for r in range(j+1,y):b[i][r]='-='[b[i][r]=='-']
    print('\n'.join(''.join(l)for l in b).replace('.',' '))