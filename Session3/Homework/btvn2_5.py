print("Hello, my name is Hiep and these are my sheep sizes")
sheep = [5,7,300,90,24,50,75]
print(sheep)
print()
for i in range(3):
    i = 1
    print("MONTH",end=" ")
    print(i,":")
    print("One month has passed, here is my flock")
    i = 0
    for i in range(len(sheep)):
        sheep[i] = sheep[i] + 50
        i = i + 1
    print(sheep)
    print("Now my biggest sheep has size",end=" ")
    print(max(sheep), end=" ")
    print("let's sheer it")
    index_max = sheep.index(max(sheep))
    sheep[index_max] = 8
    print("After shearing, here is my flock")
    print(sheep)
    print()

print("One month has passed, here is my flock")
i = 0
for i in range(len(sheep)):
    sheep[i] = sheep[i] + 50
    i = i + 1
print(sheep)

print("My flock has size in total:",end=" ")
print(sum(sheep))
print("I would get", end=" ")
print(sum(sheep),end=" ")
print("* 2$ =",end=" ")
print(sum(sheep) * 2)


