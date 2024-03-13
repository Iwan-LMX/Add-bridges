#!/usr/bin/python3
import sys
from itertools import product
#----------------------------------------------------------------------#
#----------------------------Dancing Algorithm-------------------------#
#----------------------------------------------------------------------#
def Line(x,d):
    y=d[x]
    while y != x:
        yield y;    y=d[y]
def DFS(c):
    L[R[c]], R[L[c]] = L[c], R[c] 
    for x in Line(c,D):
        for y in Line(x,R): U[D[y]], D[U[y]] = U[y], D[y]
def Back(c):
    for x in Line(c,U):
        for y in Line(x,L): U[D[y]], D[U[y]] = y, y
    L[R[c]], R[L[c]] = c, c
def Dancing():
    global findAnswer
    c=R[h]
    if c==h:    findAnswer=True;    yield []
    if findAnswer:  return

    DFS(c)
    for r in Line(c,D):
        for x in Line(r,R):DFS(C[x])
        for t in Dancing():yield[r[0]]+t
        for x in Line(r,L):Back(C[x])
    Back(c)

#----------------------------------------------------------------------#
#--------------------------Read Input & Store--------------------------#
#----------------------------------------------------------------------#
islands = {}
bridge_pair=[] 
map_origin=sys.stdin.read().split()
points=list(product(range(len(map_origin)),range(len(map_origin[0]))))
occupy={p:[]for p in points}

for i,j in points:
    if map_origin[i][j].isnumeric():
        islands[(i, j)] = int(map_origin[i][j])
    elif map_origin[i][j] != '.':
        islands[(i, j)] = ord(map_origin[i][j]) - 87
    
for pos, coord in islands.items(): #p is coord (x, y), c is the islands number
    for i,j in((0,1),(1,0)):
        q=pos[0]+i,pos[1]+j;   e=[pos,0] 
        while q in points: 
            occupy[q]+=[e] 
            if q in islands: 
                e[1]=q;occupy[pos]+=[e]; bridge_pair+=[e]
                break
            q=q[0]+i,q[1]+j

occupy={x:[x for x in y if x[1]!=0]for x,y in occupy.items()}
cross=[occupy[p] for p in points if p not in islands and len(occupy[p])>1]

#----------------------------------------------------------------------#
#---------------------Convert islands information to sets -------------#
#----------------------------------------------------------------------#
dancing_map=[];     line_start={}
set_len=len(islands)+6*len(bridge_pair)+len(cross)
start=0

#1. enumerate all ways to build bridges 
for p,c in islands.items():
    e=occupy[p];    u=len(e)*3 
    for t in product(*((0,1,2,3)for x in e)):
        if sum(t)!=c:continue
        r=[0]*set_len;r[start+u]=1
        for i,x in enumerate(t):k=start+i*3;r[k:k+3]=((1,1,1),(0,1,1),(0,0,1),(0,0,0))[x]
        dancing_map+=[r]
    line_start[p]=start; start+=u+1

z=len(dancing_map) #record the amount of sets from 1.

#2. processing for coss bridges
for e in bridge_pair:
    p, q = e;    r = [0]*set_len
    c, d = line_start[p]+occupy[p].index(e)*3, line_start[q]+occupy[q].index(e)*3
    t1=r[:]; t2=r[:] 
    r[c] = r[d] = 1
    for i,u in enumerate(cross): #record if this bridge is crossed 
        r[set_len - len(cross)+i] = int(e in u)
    t1[c+1]=t1[d+1]=1;  t2[c+2]=t2[d+2]=1
    dancing_map+=[r,t1, t2]

#----------------------------------------------------------------------#
#-------------------------Generate Dancing Links-----------------------#
#----------------------------------------------------------------------#
h = set_len
L,R,U,D,C={},{},{},{},{}  #Left, Right, Up, Down, Column of nodes in dancing table
L[h] = R[h] = D[h] = U[h] = h

for c in range(set_len):
    R[L[h]], R[c], L[h], L[c] = c, h, c, L[h]
    U[c] = D[c] = c
for i, line in enumerate(dancing_map):
    l = 0 #left of the line
    for c in Line(h,R):
        if line[c]:
            r = i, c #right of the line
            D[U[c]], D[r], U[c], U[r], C[r]=r, c, r, U[c], c
            if l==0: L[r] = R[r] = l = r 
            R[L[l]], R[r], L[l], L[r] = r, l, r, L[l] 

#----------------------------------------------------------------------#
#-------------------------Print out the Answer-------------------------#
#----------------------------------------------------------------------#
answer=list(map(list,map_origin))
findAnswer = False;     dancing_res = list(Dancing())
for e in dancing_res[0]:
    if e<z:continue
    (i,j),(x,y)=bridge_pair[(e-z)//3]
    if j==y:
        for r in range(i+1,x):
            if answer[r][j] == '"': answer[r][j] = "#"
            elif answer[r][j] == '|': answer[r][j] = '"'
            else: answer[r][j] = "|"
    else:
        for r in range(j+1,y):
            if answer[i][r] == '=': answer[i][r] = "E"
            elif answer[i][r] == '-': answer[i][r] = '='
            else: answer[i][r] = "-"
print('\n'.join(''.join(l)for l in answer).replace('.',' '))