stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item_name, item_count in inventory.items():
        item_total = item_total+item_count
        print("{} {}".format(item_count, item_name))

    print("\nTotal number of items: {}".format(item_total))
    
    if (item_total >= 60 and item_total <= 69):
        print("\nCAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
    elif (item_total >= 70 and item_total <= 79):
        print("\nCAUTION: Your equipment is very heavy, you are moving slower than usual!")
    elif item_total >=80:
        print("\nCAUTION: You are overloaded, can't move!")

display_inventory(stuff)