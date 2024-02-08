MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ing):
    for item in order_ing:
        if order_ing[item] >= resources[item]:
            print(f"sorry not enough {item}")
            return False
    return True


def process_coins():
    print("insert coins")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def is_transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        return True
    else:
        print("not enouhg money")
        return False


def make_coffee(drink_name, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
    print(f"your drink {drink_name}")


is_in = True


while True:
    choice = input("What u want (espresso/latte/cappuccino)")
    if choice == "of ":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml]")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
