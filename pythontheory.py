"""
d={x:x**2 for x in range(1,51) if x%5==0}
d[55]=3025
d.update({2:4,3:9})#updates the old dict and adds new dict at the end
d.pop(10)#deletes the specified key
print(d)
"""
"""l=eval(input())
d={}
for i in l:
    c=0
    for j in l:
        if i==j:
            c=c+1
    d.update({i:c})            
print(d)
"""
"""l=eval(input())
d=dict.fromkeys(l)
s=set(l)
for i in s:
    d[i]=l.count(i)
print(d)"""
"""
#FUNCTIONS
def add(a,b):
    print(a+b)
x=int(input())
y=int(input())
add(x,y)

def name(fname,lname):
    print(fname,lname)
i=input("Enter first name")
j=input("Enter last name")
name(i,j)
"""
"""
#lambda function
add = lambda x,y:x+y
print(add(4,5))
"""
"""
#wap for countdown timer using recursive function
def timer(n):
    for i in range(1,n+1):
        print(i)
    print("Time Over")
n=int(input("Enter time limit of counter"))
timer(n)
"""
"""
def countdown(n):
    if n==0:
        print("0 - time up")
    else:
        print(n)
        countdown(n-1)
n=int(input("Enter time limit of counter"))
countdown(n)
"""
n=int(input())
for i in range(1,n+1):
    if i%2==1:
        print(1)
    elif i%2==0:
        print(2)