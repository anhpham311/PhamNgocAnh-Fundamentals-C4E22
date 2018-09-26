# nested conditionals are conditionals that are nested within another conditionals

n = str(input("Enter your gender (F or M): "))
m = int(input("Enter your age: "))

if n == "F":
    if m < 30:
        print("Baby once more time")
    else:
        print("Bye bye Baby girl")
else:
    if m < 30:
        print("New kids on the block")
    else:
        print("Bye bye Baby boy")

print()