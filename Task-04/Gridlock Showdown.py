t = int(input())
for i in range(t):
    g=[list(input().strip()) for j in range(3)]
    w=None
    for i in range(3):
        if g[i][0]==g[i][1]==g[i][2]!='.':
            w = g[i][0]  
            break
        if g[0][i]==g[1][i]==g[2][i]!='.':
            w = g[0][i]
            break
    if not w and g[0][0]==g[1][1]==g[2][2] != '.':
        w=g[0][0]  
    if not w and g[0][2]==g[1][1]==g[2][0] != '.':
        w =g[0][2] 
    if w:
        print(w)
    else:
        print("DRAW")
