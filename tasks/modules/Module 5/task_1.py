"""This module displays and adds to hero's inventory."""

from collections import defaultdict
from dataclasses import dataclass, field

RUBBISH = ['chewed gum', 'rubbish', 'used tissue']
MAX_INVENTORY_CAPASITY = 80
HEAVY_WEIGHT_THRESHOLD = 70
LIGHT_WEIGHT_THRESHOLD = 60


@dataclass
class Item:
    """Dataclass to create hero's inventory items."""

    name: str
    unit_weight: float
    price: float
    quantity: int
    total_weight: float = field(init=False)

    def __post_init__(self):
        """Automatically calculate total weight of one kind of item."""
        self.total_weight = round((self.unit_weight * self.quantity), 2)


class Inventory:
    """Class for dealing with hero's inventory, like adding and displaying."""

    def __init__(self):
        """Inventory list with basic items prefilled for every hero."""
        self.inventory = [
            Item('rope', 4.5, 6.0, 1), Item('torch', 6.2, 3.8, 6), Item('gold coin', 1.0, 1.0, 35),
            Item('dagger', 3.5, 4.0, 1), Item('arrow', 1.4, 2.8, 12)]

    def _weight_all_items(self):
        items_weight = []
        for item in self.inventory:
            items_weight.append(item.total_weight)
        return sum(items_weight)

    def _get_quntity_of_all_items(self):
        item_total = 0
        for item in self.inventory:
            item_total += item.quantity
            print(f"{item.quantity} {item.name}")
        return item_total

    def display_inventory(self):
        print("\n##########################\nInventory:")

        item_total = self._get_quntity_of_all_items()
        print(f"\nTotal number of items: {item_total}")
        total_weight = self._weight_all_items()
        print(f"\nTotal weight of items: {total_weight}")

        if LIGHT_WEIGHT_THRESHOLD <= total_weight < HEAVY_WEIGHT_THRESHOLD:
            print(
                "\nCAUTION: Your backpack weighs a lot, "
                "your stamina runs out quicker!")
        elif HEAVY_WEIGHT_THRESHOLD <= total_weight < MAX_INVENTORY_CAPASITY:
            print(
                "\nCAUTION: Your equipment is very heavy, "
                "you are moving slower than usual!")
        elif total_weight >= MAX_INVENTORY_CAPASITY:
            print("\nCAUTION: You are overloaded, can't move!")

    def _check_if_new_item(self, item):
        for i in self.inventory:
            if item.name == i.name and item.unit_weight == i.unit_weight and item.price == i.price:
                return False
        return True

    def _add_to_quantity(self, item):
        for i in self.inventory:
            if item.name == i.name and item.unit_weight == i.unit_weight and item.price == i.price:
                i.quantity += item.quantity

    def add_to_inventory(self, added_items):
        skipped = defaultdict(int)
        added_items_count = 0

        for item in added_items:
            new_item = self._check_if_new_item(item)
            if item.name in RUBBISH:
                print(f"{item.name} is RUBBISH and is not going to be added to hero's inventory!")
                skipped[item.name] += 1
            elif new_item:
                self.inventory.append(item)
                added_items_count += item.quantity
                print(
                    f"**NEW ITEM: !{item.name}!** --> "
                    f"Adding {item.quantity} x {item.name} to hero's inventory"
                )
            else:
                self._add_to_quantity(item)
                added_items_count += item.quantity
                print(
                    f"Adding {item.quantity} x {item.name} to hero's inventory"
                )

        print(f"Added {added_items_count} items to the inventory")
        print("\nSkipped:")
        for item_name, item_count in skipped.items():
            print(f"{item_count} {item_name}")

        return inventory


if __name__ == '__main__':

    dragon_loot_list = [
        Item('gold coin', 1.0, 1.0, 1), Item('chewed gum', 0.2, 0.0, 1), Item('dagger', 3.5, 4.0, 1),
        Item('gold coin', 1.0, 1.0, 1), Item('gold coin', 1.0, 1.0, 1), Item('ruby', 2.5, 10.0, 1),
        Item('rubbish', 1.0, 0.0, 1), Item('chewed gum', 0.2, 0.0, 1), Item('used tissue', 0.1, 0.0, 1)]

    inventory = Inventory()
    inventory.add_to_inventory(dragon_loot_list)
    inventory.display_inventory()
