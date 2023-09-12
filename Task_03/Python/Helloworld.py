x=int(input("Enter number : "))
def prime():
  p=0
  for i in range(2,x):
    if x%i==0:
      p=1
      break
  if p==1:
    print("NOT PRIME")
  else:
    print("PRIME NUMBER!")
prime()
