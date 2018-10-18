s = str(input("Please enter a string: "))
def remove_dollar_sign(s):
    newstr = s.replace("$","")
    return newstr

print(remove_dollar_sign(s))

