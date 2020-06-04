"""This module displays and adds to hero's inventory."""

inventoryDict = {
    'rope': 1, 'torch': 6, 'gold coin': 42,
    'dagger': 1, 'arrow': 12}
dragonLootList = [
    'gold coin', 'chewed gum', 'dagger', 'gold coin',
    'gold coin', 'ruby', 'rubbish', 'chewed gum', 'used tissue']


def display_inventory(inventory):
    """Use this function to display hero's inventory.

    This function:
    -displays all of the inventory items,
    -sums them
    -shows warning if hero is carrying too much
    """
    print("\nInventory:")
    item_total = 0
    for item_name, item_count in inventory.items():
        item_total = item_total+item_count
        print("{} {}".format(item_count, item_name))

    print("\nTotal number of items: {}".format(item_total))

    if 59 < item_total < 70:
        print(
            "\nCAUTION: Your backpack weighs a lot,\
 your stamina runs out quicker!")
    elif 69 < item_total < 80:
        print(
            "\nCAUTION: Your equipment is very heavy,\
 you are moving slower than usual!")
    elif item_total > 79:
        print("\nCAUTION: You are overloaded, can't move!")


def add_to_inventory(inventory, added_items):
    """Use this function to add items to hero's inventory.

    This function:
    -adds to inventory valuable items,
    -throws out rubbish
    """
    rubbish = ['chewed gum', 'rubbish', 'used tissue']
    skipped = {}
    added_items_count = 0

    for item in added_items:
        if item in rubbish:
            if item in skipped:
                skipped[item] += 1
            else:
                skipped[item] = 1
        elif item in inventory:
            inventory[item] += 1
            added_items_count += 1
        elif item not in inventory and item not in rubbish:
            inventory[item] = 1
            print(
                "\n\nFound new item !{}! => adding to inventory!\n"
                .format(item))

    print('Added {} items to the inventory'.format(added_items_count))
    print("\nSkipped:")
    for item_name, item_count in skipped.items():
        print("{} {}".format(item_count, item_name))

    return inventory


inventoryDict = add_to_inventory(inventoryDict, dragonLootList)
display_inventory(inventoryDict)
