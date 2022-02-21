n = int(input())
f = int(input())
c=0
for i in range(1,n):
    if n%i==0:
        c=c+1
if n<=500 and c==1 and f%2==0:
    print ("Y")
else:
    print("n")