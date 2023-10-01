t=int(input())
for i in range(t):
    n=int(input())
    x=[]
    for i in range(1,n):
        if i%3==0:
            x.append(i)
        elif i%5==0:
            x.append(i)
    print(sum(x))  