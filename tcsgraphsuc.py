def line(n,arr):
    if(n==1):
        arr.append(1)
        return
    else:
        c=0
        for j in range(2,int(n/2)+1):
            if(n%j==0):
                c=int(n/j)
                arr.append(c)
                line(c,arr)
                break
        if(c==0):
            line(1,arr)
z=[int(x) for x in input().split(" ")]
a=z[0]
b=z[1]
fa=[a]
fb=[b]
line(a,fa)
line(b,fb)
fbs=set(fb)
h=0
for r in fa:
  if(r in fbs):
    h=r
    break
size=fa.index(h)+fb.index(h)
print(size,end="")
