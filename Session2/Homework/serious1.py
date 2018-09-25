hc = int(input("Enter your height in cm "))
w = int(input("Enter your weight in kg "))

hm = hc/100

BMI = w / (hm*hm)

print(BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:    
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")

