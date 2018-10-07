inventory = {
    'gold' : [500],
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

#create a key moi la 'pocket'
inventory["pocket"] = ["seashell", "strange berry", "lint"]

#remove('dagger') from the list of items stored under the 'backpack' key.
inventory["backpack"].remove("dagger")


inventory["gold"].append(50)

print(inventory)