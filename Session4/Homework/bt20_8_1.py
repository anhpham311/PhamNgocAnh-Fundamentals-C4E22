getint = str(input("Enter a string: "))

getint = getint.lower()

letter_counts = {}

for letter in getint:
    letter_counts[letter] = letter_counts.get(letter,0) + 1

letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)