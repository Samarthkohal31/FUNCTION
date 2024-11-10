def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

a=int(input("enter a number"))
fact(a)
