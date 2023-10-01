x=list('AMFOSS')
t=int(input())
for i in range(t):
    y=input()
    y=y.upper()
    l=list(y)
    c=0
    for i in range(6):
        if x[i]!=l[i]:
            c+=1
    print(c)