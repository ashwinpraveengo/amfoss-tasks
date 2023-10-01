def even_fibonacci_sum(limit):
    a, b = 1, 2 
    even_sum = 0  
    while a <= limit:
        if a % 2 == 0:
            even_sum += a  
        a, b = b, a + b 
    return even_sum
t = int(input())
for j in range(t):
    n = int(input())
    result = even_fibonacci_sum(n)
    print(result)   
