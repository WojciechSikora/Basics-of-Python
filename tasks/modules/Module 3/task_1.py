"""Module gathers input from user and prints sandwich ingredients and price."""

from dataclasses import dataclass
from typing import Dict
from pyinputplus import inputMenu, inputYesNo, inputInt


@dataclass
class Ingredient:
    """Dataclass to match product name with it's price and types."""

    name: str
    choices: Dict[str, float]
    required: bool = False


# Constants mapping type of product to its price
INGREDIENTS_INFORMATIONS = [
    Ingredient(
        name='bread',
        choices={'wheat bread': 1.5, 'white bread': 1.0, 'sourdough bread': 2.0},
        required=True),
    Ingredient(
        name='proteine',
        choices={'chicken': 2.0, 'turkey': 3.0, 'ham': 1.5, 'tofu': 2.0},
        required=True),
    Ingredient(
        name='cheese',
        choices={'cheddar cheese': 2.5, 'Swiss cheese': 3.0, 'mozzarella cheese': 2.75}),
    Ingredient(
        name='sauce',
        choices={'mayo': 0.5, 'mustard': 0.75, 'lettuce sauce': 1.0, 'tomato sauce': 1.25})]


def prepare_sandwich():
    """Get ingredients from user and calculate price."""
    order = {}
    print(
        "Hello Hungry Stranger!\n"
        "Please choose ingredients for your sandwich\n")
    for item in INGREDIENTS_INFORMATIONS:
        if item.required:
            ingredient_item = inputMenu(list(item.choices.keys()))
            order[ingredient_item] = item.choices[ingredient_item]
        else:
            add_ing = inputYesNo(f"Would you like to add {item.name}?  ")
            if add_ing == 'yes':
                ingredient_item = inputMenu(list(item.choices.keys()))
                order[ingredient_item] = item.choices[ingredient_item]
    number_of_sandwiches = inputInt(
        "How many sandwiches would you like?  ", min=1)
    print(
        "Great choice! \n"
        f"You have ordered: {number_of_sandwiches} sandwich(es)\n"
        f"Your sandwich(es) will consist of:\n{list(order)}\n"
        "and will cost you only: "
        f"${sum(order.values()) * number_of_sandwiches}")


if __name__ == '__main__':
    prepare_sandwich()
