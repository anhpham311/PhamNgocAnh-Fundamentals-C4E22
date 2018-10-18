x = int(input("Please input x axis: "))
y = int(input("Please input y axis: "))

a = [x,y]
h = [140, 60, 100, 200]

def is_inside(a,h):
    if 140 < x < 240 and 60 < y < 260:
        print("TRUE")
    else:
        print("FALSE")
    return a
    
print(is_inside(a,h))
