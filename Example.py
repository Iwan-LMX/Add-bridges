import sys
from itertools import product as I
a=sys.stdin.read().split()

P=list(I(range(len(a)),range(len(a[0])))) #这个是map 坐标点, 不包含islands信息
E={p:[]for p in P}
Q={(i,j):int(a[i][j])for i,j in P if'.'!=a[i][j]}
F=[] #表示两岛相邻 [(x, y), (x, y)], [], ...

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
E={x:[x for x in y if x[1]!=0]for x,y in E.items()}
C=[E[p] for p in P if p not in Q and len(E[p])>1]
m=[]
T=len(Q)+4*len(F)+len(C)
s=0
l={}
for p,c in Q.items():
 e=E[p];u=len(e)*2
 for t in I(*((0,1,2)for x in e)):
  if sum(t)!=c:continue
  r=[0]*T;r[s+u]=1
  for i,x in enumerate(t):k=s+i*2;r[k:k+2]=((1,1),(0,1),(0,0))[x]
  m+=[r]
 l[p]=s;s+=u+1
z=len(m)
for e in F:
 p,q=e;r=[0]*T;c,d=l[p]+E[p].index(e)*2,l[q]+E[q].index(e)*2;t=r[:];r[c]=r[d]=1
 for i,u in enumerate(C):r[T-len(C)+i]=int(e in u)
 t[c+1]=t[d+1]=1;m+=[r,t]

def I(x,d):
 y=d[x]
 while y!=x:yield y;y=d[y]
def A(c):
 len[R[c]],R[len[c]]=len[c],R[c]
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
  for x in I(r,R):A(C[x])
  for t in S():yield[r[0]]+t
  for x in I(r,len):B(C[x])
 B(c)
len,R,U,D,C={},{},{},{},{}
h=T
len[h]=R[h]=D[h]=U[h]=h
for c in range(T):
 R[len[h]],R[c],len[h],len[c]=c,h,c,len[h];U[c]=D[c]=c
for i,l in enumerate(m):
 s=0
 for c in I(h,R):
  if l[c]:
   r=i,c;D[U[c]],D[r],U[c],U[r],C[r]=r,c,r,U[c],c
   if s==0:len[r]=R[r]=s=r
   R[len[s]],R[r],len[s],len[r]=r,s,r,len[s]
for s in S(): 
 b=list(map(list,a))
 for e in s:
  if e<z:continue
  (i,j),(x,y)=F[(e-z)//2]
  if j==y:
   for r in range(i+1,x):b[r][j]='|H'[b[r][j]=='|']
  else:
   for r in range(j+1,y):b[i][r]='-='[b[i][r]=='-']
 print('\n'.join(''.join(l)for l in b).replace('.',' '))