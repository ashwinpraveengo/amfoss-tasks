t = int(input())
for i in range(t):
    n = int(input())
    l = -1
    while n % 2 == 0:
        lp = 2
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            lp = i
            n //= i
    if n > 2:
        lp = n
    print(lp)