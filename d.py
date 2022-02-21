from traceback import print_tb


a=int(input())

c=input()

if c == 'k':
    b=int(input())
    a=a/1024
    a=round(a,b)
    print(a)
elif c == 'b':
    a=a*1024
    print(a)

    from traceback import print_tb


# a=int(input())

# c=input()

# if c == 'k':
#     b=int(input())
#     a=a/1024
#     print("{0:.%}".format(a) %b)
# elif c == 'b':
#     a=a*1024
#     print(a)