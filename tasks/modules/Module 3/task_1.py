"""Module gathers input from user and prints sandwich ingredients and price."""

from pyinputplus import inputMenu, inputYesNo, inputInt

# Constants mapping type of product to its price
INGREDIENTS_INFORMATIONS = [
    [
        'bread',
        'mandatory',
        {
            'wheat bread': 1.5,
            'white bread': 1.0,
            'sourdough bread': 2.0}],
    [
        'proteine',
        'mandatory',
        {
            'chicken': 2.0,
            'turkey': 3.0,
            'ham': 1.5,
            'tofu': 2.0}],
    [
        'cheese',
        'optional',
        {
            'cheddar cheese': 2.5,
            'Swiss cheese': 3.0,
            'mozzarella cheese': 2.75}],
    [
        'sauce',
        'optional',
        {
            'mayo': 0.5,
            'mustard': 0.75,
            'lettuce sauce': 1.0,
            'tomato sauce': 1.25}]]


def prepare_sandwich():
    """Get ingredients from user and calculate price."""
    order = {}
    print(
        "Hello Hungry Stranger!\n"
        "Please choose ingredients for your sandwich\n")
    for item in INGREDIENTS_INFORMATIONS:
        ingredients_list = item[2]
        if item[1] == 'optional':
            add_ing = inputYesNo(f"Would you like to add {item[0]}?  ")
            if add_ing == 'yes':
                ingredient_item = inputMenu([*ingredients_list])
                order.update({ingredient_item: item[2][ingredient_item]})
            else:
                ingredient_item = "no"
        else:
            ingredient_item = inputMenu([*ingredients_list])
            order.update({ingredient_item: item[2][ingredient_item]})
    number_of_sandwiches = inputInt(
        "How many sandwiches would you like?  ", min=1)
    print(
        "Great choice! \n"
        f"You have ordered: {number_of_sandwiches} sandwich(es)\n"
        f"Your sandwich(es) will consist of:\n{list(order)}\n"
        "and will cost you only:"
        f"${sum(order.values()) * number_of_sandwiches}")


if __name__ == '__main__':
    prepare_sandwich()
