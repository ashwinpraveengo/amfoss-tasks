t=int(input())
x=0
y=0
z=0
for i in range(t):
    x1,y1,z1=map(int,input().split())
    x+=x1
    y+=y1
    z+=z1
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")