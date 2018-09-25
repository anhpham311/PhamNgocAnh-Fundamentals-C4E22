n = int(input("Enter a number: "))

h = int((n-1)/2)
m = int(n/2)

if n % 2 == 1: 
    for i in range(0,h):
        print("x",end=" ")
        print("*",end=" ")
    print("x")
else:
    for i in range(0,m):
        print("x",end=" ")
        print("*",end=" ")

print()