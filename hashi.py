import sys
from itertools import product as I
a=sys.stdin.read().split()

P=list(I(range(len(a)),range(len(a[0])))) #这个是map 坐标点, 不包含islands信息
E={p:[]for p in P}
Q = {}
for i,j in P:
    if a[i][j].isnumeric():
        Q[(i, j)] = int(a[i][j])
    elif a[i][j] != '.':
        Q[(i, j)] = ord(a[i][j]) - 87
    
F=[] #表示两岛相邻 [(x, y), (x, y)], [], ...

for p,c in Q.items(): #p is coord (x, y), c is the islands number
    for i,j in((0,1),(1,0)):
        #p是岛坐标, q是p岛行列上的点
        q=p[0]+i,p[1]+j;   e=[p,0] 
        while q in P: #没有越界
            E[q]+=[e] #因为e是个list, 下面修改e形成pair导致这里也会自动更新
            #如果相邻点也是岛
            if q in Q: e[1]=q;E[p]+=[e];F+=[e];break #存储p岛与 q岛
            q=q[0]+i,q[1]+j

E={x:[x for x in y if x[1]!=0]for x,y in E.items()} #两个岛之间能够形成桥的地方会带上岛pairs的value, 如果这个地方没有桥要通过则会为空
C=[E[p] for p in P if p not in Q and len(E[p])>1] #找出找出两桥交叉的部位
m=[]
T=len(Q)+6*len(F)+len(C) #这个应该表示元素总量, 4 应该表示这对桥的往返*这对桥的长度
s=0
l={}

#生成subsets, m为subsets表.
#周围可选岛屿
for p,c in Q.items():
    e=E[p];u=len(e)*3 #u乘2是因为0, 1, 2这三个数二进制表示需要用2个长度
    for t in I(*((0,1,2,3)for x in e)): #这里会生成一个笛卡尔积, 长度/元素数量对应这个岛能和邻居连接的数量. 比如(0,0)这个岛能和右, 下两个邻居相连所以有两个slots. 每个slot的0, 1, 2表示桥的数量.
        if sum(t)!=c:continue
        r=[0]*T;r[s+u]=1
        for i,x in enumerate(t):k=s+i*3;r[k:k+3]=((1,1,1),(0,1,1),(0,0,1),(0,0,0))[x] #这三个二进制数是用来表示这个岛相连的几座桥按顺序要建造的lanes的数量. 11 表示0, 01表示1, 00表示2. (因为我们最多lane是三所以需要还需要额外加上10 b) || 但是为啥用(1, 1)而不是(1, 0)?
        m+=[r]
    l[p]=s;s+=u+1

z=len(m)
#处理交叉的桥
for e in F:
    p,q=e; r=[0]*T
    c,d=l[p]+E[p].index(e)*3,l[q]+E[q].index(e)*3 #这个*2 刚好对应上边这里的(1, 1), (0, 1), (0, 0)的位置
    t1=r[:]; t2=r[:]; r[c]=r[d]=1 #t是r的copy
    for i,u in enumerate(C):r[T-len(C)+i]=int(e in u) #这里最后len(C) 个元素表示当前这对路是否处于交叉路
    t1[c+1]=t1[d+1]=1; t2[c+2]=t2[d+2]=1;  m+=[r,t1, t2]

def I(x,d):
    y=d[x]
    while y!=x: yield y;    y=d[y]
def A(c):
    len[R[c]],R[len[c]]=len[c],R[c] #这是按照从左往右的顺序, 除掉c左边的列
    for x in I(c,D):
        for y in I(x,R):U[D[y]],D[U[y]]=U[y],D[y]
def B(c):
    for x in I(c,U):
        for y in I(x,len):U[D[y]],D[U[y]]=y,y
    len[R[c]],R[len[c]]=c,c
def S():
    c=R[h]
    if c==h:yield[]
    A(c)
    for r in I(c,D):
        # print(r, list(I(c, D)))
        for x in I(r,R):A(C[x])
        for t in S():yield[r[0]]+t
        for x in I(r,len):B(C[x])
    B(c)
len,R,U,D,C={},{},{},{},{} 
h=T
len[h]=R[h]=D[h]=U[h]=h
#T项, 对于len 和 R来说是左右的指示:(515 左边是514, 514左边是513这样)
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
s = list(S())
b=list(map(list,a))
for e in s[0]:
    if e<z:continue
    (i,j),(x,y)=F[(e-z)//3]
    if j==y:
        for r in range(i+1,x):
            if b[r][j] == '"': b[r][j] = "#"
            elif b[r][j] == '|': b[r][j] = '"'
            else: b[r][j] = "|"
    else:
        for r in range(j+1,y):
            if b[i][r] == '=': b[i][r] = "E"
            elif b[i][r] == '-': b[i][r] = '='
            else: b[i][r] = "-"
print('\n'.join(''.join(l)for l in b).replace('.',' '))