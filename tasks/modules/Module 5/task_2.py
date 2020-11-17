"""This module displays and adds to hero's inventory."""

import random
from collections import defaultdict
from dataclasses import dataclass, field
from sys import exit

from pyinputplus import inputMenu

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


@dataclass
class Food:
    """Dataclass to create hero's food items."""

    name: str
    stamina_recover: int
    quantity: str


class Inventory:
    """Class for dealing with hero's inventory, like adding and displaying."""

    def __init__(self):
        """Inventory list with basic items and food, prefilled for every hero."""
        self.inventory = [
            Item('rope', 4.5, 6.0, 1), Item('torch', 6.2, 3.8, 3), Item('gold coin', 1.0, 1.0, 15),
            Item('dagger', 3.5, 4.0, 1), Item('arrow', 1.4, 2.8, 9)
        ]
        self.food = [
            Food('apple', 1, 5), Food('banana', 2, 3), Food('steak', 8, 1)
        ]

    def _weight_all_items(self):
        items_weight = []
        for item in self.inventory:
            items_weight.append(item.total_weight)
        return sum(items_weight)

    def _get_quantity_of_all_items(self):
        item_total = 0
        for item in self.inventory:
            item_total += item.quantity
            print(f"{item.quantity} x {item.name}")
        return item_total

    def display_inventory(self):
        print("\n##########################\nInventory:")

        item_total = self._get_quantity_of_all_items()
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

        return self.inventory

    def remove_from_inventory(self, item_name):
        for item in self.inventory:
            if item.name == item_name and item.quantity > 0:
                item.quantity = item.quantity - 1
            if item.quantity == 0:
                self.inventory.remove(item)

    def remove_from_food(self, food_name):
        for item in self.food:
            if item.name == food_name and item.quantity > 0:
                item.quantity = item.quantity - 1
            if item.quantity == 0:
                self.food.remove(item)
            return item.stamina_recover


class Hero(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.stamina = 10

    def stats(self):
        print("\n##########################")
        print(f"STATS:\nStamina: {self.stamina}")
        print("Items: ")
        for item in self.inventory:
            print(f"* {item.quantity} x {item.name}")
        print("Food: ")
        for item in self.food:
            print(f"* {item.quantity} x {item.name}(can recover {item.stamina_recover} stamina)")
        print("##########################\n")


class Game(Hero):
    def __init__(self):
        self.a, self.b, self.c = "X", " ", "X"
        self.d, self.e, self.f = " ", "X", " "
        self.g, self.h, self.i = "H", " ", " "
        Hero.__init__(self)
        self.hero_position = {"x": 0, "y": 2}
        self.treasures_on_board = [Item('rope', 4.5, 6.0, 1), Item('torch', 6.2, 3.8, 1),
                                   Item('gold coin', 1.0, 1.0, 1),
                                   Item('dagger', 3.5, 4.0, 1), Item('arrow', 1.4, 2.8, 1)]
        self.board = [[self.a, self.b, self.c],
                      [self.d, self.e, self.f],
                      [self.g, self.h, self.i]]

    def print_board(self):
        print('\n+---+---+---+')
        print(f'| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |')
        print('+---+---+---+')
        print(f'| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |')
        print('+---+---+---+')
        print(f'| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |')
        print('+---+---+---+\n')

    def move_action(self, action):
        if action == "move up":
            self.move(0, -1)
        elif action == "move down":
            self.move(0, 1)
        elif action == "move left":
            self.move(-1, 0)
        elif action == "move right":
            self.move(1, 0)

    def move(self, x, y):
        new_position = {"x": self.hero_position["x"] + x, "y": self.hero_position["y"] + y}
        if (new_position["x"] or new_position["y"]) < 0 or (new_position["x"] or new_position["y"]) > 2:
            print("Move not possible - EDGE OF BOARD")
            self.print_board()
        elif self.board[new_position["y"]][new_position["x"]] == "X":
            rand_item = random.choice(self.treasures_on_board)
            print(f"New item found: {rand_item.name}")
            self.add_to_inventory([rand_item])
            print("Item added to inventory")
            self.changes_after_move(new_position)
        else:
            self.changes_after_move(new_position)

    def changes_after_move(self, new_position):
        self.board[self.hero_position["y"]][self.hero_position["x"]] = " "
        self.board[new_position["y"]][new_position["x"]] = "H"
        self.hero_position = new_position
        self.stamina = self.stamina - 2
        self.print_board()

    def check_if_can_move(self):
        if self.stamina < 2:
            print(f"Sorry boss :( your stamina is only {self.stamina}!!"
                  "Just eat something")
            return False
        total_weight = self._weight_all_items()
        if total_weight >= MAX_INVENTORY_CAPASITY:
            print(f"Your inventory is too heavy to move({total_weight}kg). Drop something")
            return False
        return True

    def play(self):
        possible_actions = ["stats", "move up", "move down", "move left",
                            "move right", "eat", "drop item", "map", "exit"]
        action = ""
        while action != "exit":
            action = inputMenu(possible_actions, "Choose action\n")
            if action == "exit":
                exit()
            elif action == "stats":
                self.stats()
            elif action == "drop item":
                items_to_remove = []
                for item in self.inventory:
                    items_to_remove.append(item.name)
                item_to_remove = inputMenu(items_to_remove,
                                           "Which item should be dropped(q=1)?\n")
                self.remove_from_inventory(item_to_remove)
                self.display_inventory()
            elif action == "move up":
                abbility_to_move = self.check_if_can_move()
                if abbility_to_move:
                    self.move_action(action)
            elif action == "move down":
                abbility_to_move = self.check_if_can_move()
                if abbility_to_move:
                    self.move_action(action)
            elif action == "move left":
                abbility_to_move = self.check_if_can_move()
                if abbility_to_move:
                    self.move_action(action)
            elif action == "move right":
                abbility_to_move = self.check_if_can_move()
                if abbility_to_move:
                    self.move_action(action)
            elif action == "eat":
                items_to_eat = []
                for item in self.food:
                    items_to_eat.append(item.name)
                item_to_eat = inputMenu(items_to_eat, "Which item would you like to eat?\n")
                gained_stamina = self.remove_from_food(item_to_eat)
                self.stamina += gained_stamina
            elif action == "map":
                self.print_board()


if __name__ == '__main__':
    game = Game()
    game.play()
