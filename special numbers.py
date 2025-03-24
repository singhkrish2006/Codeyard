"""
#WAP to check whether a number is a prime number or not
x=int(input("Enter a number to check:"))
if x>1:
    for i in range(2,(x//2)+1):
        if x%i==0:
            print(x,"is not a prime number")
            break
        else:
            print(x,"is a prime number")
else:
    print("1 is not a prime number")
"""
"""
#WAP to check whethwe a number is an Amstrong number or not
i=0
n=int(input("Enter a number to check:"))
t=n
while t>0:
    a = t%10
    i += a**3
    t //= 10
if n==i:
    print(n,"is an Amstrong number")
else:
    print(n,"is not an Amstrong number")
"""
"""
#WAP to check whether a number is a perfect square or not
n=int(input("Enter a number to check:"))
if n>1:   
    for i in range(1,n):
        if i**2==n:
            print(n,"is a perfect square of",i)
            break
else:
    print("1 is a pperfect square of itself")
"""
#WAP to check whether a number is a palindrome or not
n=int(input("Enter a number to check:"))
r=0
a=n
while n>0:
    r1=n%10
    r=r*10+r1
    n//=10
if a==r:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")





















