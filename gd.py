aa1,bb2=map(int,input().split())
cc3=[]
dd4=[]
ee5=[int(aa1) for aa1 in input().split()]
for i in range(0,bb2):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        dd4.append(ee5[j])
    vj=sum(dd4)
    cc3.append(vj)
print(cc3[0])
for x in range(1,len(cc3)):
    print(cc3[x]- cc3[x- 1])
