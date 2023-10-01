s = input()
w = "hello"
c = 0
if len(s) < 5:
    print("NO")
else:
    for i in w:
        if i in s:
            s =s[s.index(i) + 1::]
            c = c + 1
    if c == len(w):
        print("YES")
    else:
        print("NO")