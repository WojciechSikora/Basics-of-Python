"""Module gathers input from user and prints sandwich ingredients and price."""

from pyinputplus import inputMenu, inputYesNo, inputInt

# Program's constants
BREAD_TYPE = {'wheat': 1.5, 'white': 1.0, 'sourdough': 2.0}
PROTEIN_TYPE = {'chicken': 2.0, 'turkey': 3.0, 'ham': 1.5, 'tofu': 2.0}
CHEESE_TYPE = {'cheddar': 2.5, 'Swiss': 3.0, 'mozzarella': 2.75}
SAUCE_TYPE = {'mayo': 0.5, 'mustard': 0.75, 'lettuce': 1.0, 'tomato': 1.25}


def sandwich_preparation():
    """Get ingredients from user and calculate price."""
    total_price = 0
    chosen_cheese = "no"
    chosen_sauce = "no"
    print("Hello Hungry Stranger!\n")
    number_of_sandwiches = inputInt(
        "How many sandwiches would you like?  ", min=1)
    chosen_bread = inputMenu([*BREAD_TYPE])
    chosen_protein = inputMenu([*PROTEIN_TYPE])
    add_cheese = inputYesNo("Would you like to add cheese?  ")
    if add_cheese == "yes":
        chosen_cheese = inputMenu([*CHEESE_TYPE])
        total_price += number_of_sandwiches*CHEESE_TYPE[chosen_cheese]
    add_sauce = inputYesNo("Would you like to add sauce?  ")
    if add_sauce == "yes":
        chosen_sauce = inputMenu([*SAUCE_TYPE])
        total_price += number_of_sandwiches*SAUCE_TYPE[chosen_sauce]
    total_price += number_of_sandwiches*(
        BREAD_TYPE[chosen_bread]+PROTEIN_TYPE[chosen_protein])
    print(
        f"Great choice!\nYou have ordered: {number_of_sandwiches} "
        f"sandwich(es)\nYour sandwich(es) will consist of "
        f"{chosen_bread} bread, {chosen_protein}, {chosen_cheese} cheese "
        f"and {chosen_sauce} sauce and will cost you only: ${total_price}")


sandwich_preparation()
