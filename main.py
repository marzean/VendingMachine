menu = {
    "maui": {
        "food_items": {
            "rice": 150,
            "salmon": 80,
            "avocado": 25,
        },
        "price": 15,
    },
    "hula": {
        "food_items": {
            "rice": 150,
            "tuna": 80,
            "avocado": 25,
        },
        "price": 12,
    },
    "honolulu": {
        "food_items": {
            "rice": 150,
            "chicken": 80,
            "avocado": 25,
        },
        "price": 10,
    }
}

storage = {
    "rice": 500,
    "salmon": 200,
    "tuna": 200,
    "chicken": 200,
    "avocado": 200,
}
total_balance = 0


def storage_check(ordered_items):
    """This function will check if the machine has enough items to make the food"""
    for item in ordered_items:
        if ordered_items[item] > storage[item]:
            print(f"There is not enough {item}, not possible to make food, refunding money")
            return False

        else:
            return True


def asking_money(ordered_food):
    """This function will ask the customer for money and calculate the money"""
    print(f"You have ordered {customer_order} and the price is ${ordered_food['price']}")
    print(f"please insert the money")
    total = int(input("how many 10 dollar notes")) * 10
    total += int(input("how many 5 dollar notes")) * 5
    total += int(input("how many 2 dollar notes")) * 2
    total += int(input("how many 1 dollar notes")) * 1
    print(f"total paid ${total} .")
    return total


def return_money(price_paid, ordered_food):
    """This function will return the customer money if its needed"""
    if price_paid >= ordered_food["price"]:
        return_money = price_paid - ordered_food["price"]
        print(f" Here is your change ${return_money}")
        global total_balance
        total_balance += ordered_food["price"]
        return True
    else:
        """If customer enters less money , machine will let customer know how much short"""
        short_money = ordered_food["price"] - price_paid
        print(f"That's not enough money, you are ${short_money} short.")
        return False


def serve_food(ordered_food,ordered_food_ingredients):
    """This function will serve the customer food and deduct form storage"""
    for items in ordered_food_ingredients:
        storage[items] -= ordered_food_ingredients[items]
    print(f"Collect your {ordered_food} from the box. Enjoy!")





machine_is_on = True


while machine_is_on:
    """when machine is ON, customer can place order"""
    customer_order = input("Hey, welcome! Which poke bowl would you like to order? (maui/hula/honolulu)").lower()
    """if the owner enter keyword 'off' in the machine, machine will turn off"""
    if customer_order == "off":
        shut_down = input("Do you want to shut down the machine? yes/no").lower()
        if shut_down == "yes":
            machine_is_on = False
        else:
            machine_is_on = True
    """if the owner enter keyword 'status' in the machine, machine will show the status off
    the storage"""
    if customer_order == "status":
        for item in storage:
            print(f"Amount of {item} left {storage[item]} gm.")
        print(f" Total balance right now ${total_balance}")

    else:
        """when customer enters a name of the food from the menu, process will start"""
        bowl_ingredients = menu[customer_order]['food_items']
        storage_check(bowl_ingredients)
        customer_paid = asking_money(menu[customer_order])
        return_money(customer_paid, menu[customer_order])
        serve_food(customer_order, bowl_ingredients)
