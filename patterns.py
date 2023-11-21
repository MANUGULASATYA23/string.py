n=5
for i in range(0,n):
     for j in range(0,i):
        print(" *",end=" ")
     print("\r")


height = 5
for row in range(1, height+ 1):
    print(" " * (height - row) +"*" * row)

n=6
x=n-1
for i in range(1,n):
     for j in range(0,x):
        print(" ",end="")
     x=x-1
     for k in range(0, i):
         print("*", end=" ")
     print("\r")


def triangle(n):
    m = 0
    for i in range(0,n):
        for k in range(0, m):
            print(" ", end=" ")
        m=m+1
        for j in range(0, n):
            print("* ", end="")
        n=n-1
        print('\r')
triangle(5)




def trianglee(n):
    x = 0
    for j in range(0,n):
        for k in range(0, x):
            print("", end="")
        x=x+1
        for i in range(0, n):
            print("*", end=" ")
        n=n-1
        print('\r')
trianglee(5)


def trianglee(n):
    x = 0
    for j in range(0,n):
        lst=fibseries()
        for k in range(0, x):
            print(" ", end="")
        x=x+1
        for i in range(0, n):
            print(lst[i], end=" ")
        n=n-1
        print('\r')
def fibseries():
    return[0,1,1,2,3,5]
trianglee(6)




def trianglee(n):
    x = 0
    for j in range(0,n):
        lst=primeseries()
        for k in range(0, x):
            print(" ", end="")
        x=x+1
        for i in range(0, n):
            print(lst[i], end=" ")
        n=n-1
        print('\r')
def primeseries():
    return[1,2,3,5,7,9]
trianglee(6)


