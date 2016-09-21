"""
My first program with python
Говнокод во всей красе:D
"""


def polinom(n):
    a=[]
    pol=0
    for i in range(n):
        print "Enter of", i, "element: "
        a.append(input())
    print "List A = ", a
    for i in range(n): #main loop
        pol+=a[i]*(x**i)
    return pol

x=input("Input point X:  ")
n=input("Input N:  ")
result = polinom(n)

print "Polinom = ", result
