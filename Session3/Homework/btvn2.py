print("Hello, my name is Hiep and these are my sheep sizes")
sheep = [5,7,300,90,24,50,75]
print(sheep)

#choose the biggest sheep to shear
print("Now my biggest sheep has size",end=" ")
print(max(sheep), end=" ")
print("let's sheer it")

#when your biggest shear, the size return to 8
index_max = sheep.index(max(sheep))
sheep[index_max] = 8
print("After shearing, here is my flock")
print(sheep)

#every sheep grow in one month
print("One month has passed, here is my flock")
i = 0
for i in range(len(sheep)):
    sheep[i] = sheep[i] + 50
    i = i + 1
print(sheep)