"""This module displays and adds to hero's inventory."""

from collections import defaultdict

# Program's constants
MAX_INVENTORY_CAPASITY = 80
HEAVY_WEIGHT_THRESHOLD = 70
LIGHT_WEIGHT_THRESHOLD = 60
RUBBISH = ['chewed gum', 'rubbish', 'used tissue']

inventory_dict = {
    'rope': 1, 'torch': 6, 'gold coin': 42,
    'dagger': 1, 'arrow': 12}
dragon_loot_list = [
    'gold coin', 'chewed gum', 'dagger', 'gold coin',
    'gold coin', 'ruby', 'rubbish', 'chewed gum', 'used tissue']


def should_skip_item(item):
    """Check if item is unusable for hero's needs."""
    if item in RUBBISH:
        return True
    return False


def display_inventory(inventory):
    """Display hero's inventory.

    This function:
    - displays all of the inventory items
    - sums them
    - shows warning if hero is carrying too much
    """
    print("\nInventory:")
    item_total = 0
    for item_name, item_count in inventory.items():
        item_total += item_count
        print(f"{item_count} {item_name}")

    print(f"\nTotal number of items: {item_total}")

    if LIGHT_WEIGHT_THRESHOLD <= item_total < HEAVY_WEIGHT_THRESHOLD:
        print(
            "\nCAUTION: Your backpack weighs a lot, "
            "your stamina runs out quicker!")
    elif HEAVY_WEIGHT_THRESHOLD <= item_total < MAX_INVENTORY_CAPASITY:
        print(
            "\nCAUTION: Your equipment is very heavy, "
            "you are moving slower than usual!")
    elif item_total >= MAX_INVENTORY_CAPASITY:
        print("\nCAUTION: You are overloaded, can't move!")


def add_to_inventory(inventory, added_items):
    """Use this function to add items to hero's inventory.

    This function:
    - adds to inventory valuable items
    - throws out rubbish
    """
    skipped = defaultdict(int)
    added_items_count = 0

    for item in added_items:
        item_not_useable = should_skip_item(item)
        if item_not_useable:
            skipped[item] += 1
        elif item in inventory:
            inventory[item] += 1
            added_items_count += 1
        else:
            inventory[item] = 1
            added_items_count += 1
            print(
                f"\n\nFound new item !{item}! => adding to inventory!\n"
                )

    print(f"Added {added_items_count} items to the inventory")
    print("\nSkipped:")
    for item_name, item_count in skipped.items():
        print(f"{item_count} {item_name}")

    return inventory


inventory_dict = add_to_inventory(inventory_dict, dragon_loot_list)
display_inventory(inventory_dict)
