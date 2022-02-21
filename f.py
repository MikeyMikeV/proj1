n = int(input())

a =[]

for i in range(0,n):
    a.append(int(input()))

for i in a:
    if i <= 10:
        print(1)
    elif i <= 25:
        print(2)
    elif i <= 45:
        print(3)
    else:
        print(4)
