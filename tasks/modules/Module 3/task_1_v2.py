"""Module gathers input from user and prints sandwich ingredients and price."""

from pyinputplus import inputMenu, inputYesNo, inputInt

# Program's constants
INGREDIENTS_INFORMATIONS = [
    ['bread', 'mandatory', {'wheat': 1.5, 'white': 1.0, 'sourdough': 2.0}],
    ['proteine', 'mandatory', {'chicken': 2.0, 'turkey': 3.0, 'ham': 1.5, 'tofu': 2.0}],
    ['cheese', 'optional', {'cheddar': 2.5, 'Swiss': 3.0, 'mozzarella': 2.75}],
    ['sauce', 'optional', {'mayo': 0.5, 'mustard': 0.75, 'lettuce': 1.0, 'tomato': 1.25}]]


def sandwich_preparation():
    """Get ingredients from user and calculate price."""
    total_price = 0
    order = []
    print("Hello Hungry Stranger!\nPlease choose ingredients for your sandwich\n")
    for item in range(len(INGREDIENTS_INFORMATIONS)):
        ingredient_type = INGREDIENTS_INFORMATIONS[item][0]
        ingredients_list = INGREDIENTS_INFORMATIONS[item][2]
        if INGREDIENTS_INFORMATIONS[item][1] == 'optional':
            add_ing = inputYesNo(f"Would you like to add {ingredient_type}?  ")
            if add_ing == 'yes':
                ingredient_item = inputMenu([*ingredients_list])
                total_price += INGREDIENTS_INFORMATIONS[item][2][ingredient_item]
            else:
                ingredient_item = "no"
        else:
            ingredient_item = inputMenu([*ingredients_list])
            total_price += INGREDIENTS_INFORMATIONS[item][2][ingredient_item]
        order.append([ingredient_type, ingredient_item])
    number_of_sandwiches = inputInt(
        "How many sandwiches would you like?  ", min=1)
    print(
        f"Great choice!\nYou have ordered: {number_of_sandwiches} sandwich(es)\n"
        "Your sandwich(es) will consist of: ")
    for i in range(len(order)):
        print(f"{order[i][1]} {order[i][0]}")
    print(f"and will cost you only: ${total_price*number_of_sandwiches}")


sandwich_preparation()
