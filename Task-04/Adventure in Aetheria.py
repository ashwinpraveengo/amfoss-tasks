n=int(input())
times=list(map(int,input().split()))[:n]
c=0
for time in times:
  if times.count(min(times))>1:
    c=1
    j=time
    break
if c==1:
  print("Still Aetheria")
else:
  print(times.index(min(times))+1)