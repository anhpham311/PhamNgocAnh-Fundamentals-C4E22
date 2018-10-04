shop = ["t-shirt","sweater"]
print(shop)

new_item = input("Enter new item: ")
shop.append(new_item)
print(shop)

update_position = int(input("Update position? "))
new_item = input("New item: ")
shop[update_position-1] = new_item
print(shop)

delete_position = int(input("Delete position? "))
shop.pop(delete_position-1)
print(shop)

