drinks = { #arbitary
    "espresso": {
        "price": "2.5",
        "ingrediants": {
            "milk": "100", # in ml
            "water": "100", # in ml
            "coffee": "36"}, # in gm
    
    },

    "latte": {
        "price": "3",
        "ingrediants": {
            "milk": "150", # in ml
            "water": "150", # in ml
            "coffee": "62"}, # in gm
    },

    "cappuccino": {
        "price": 4,
        "ingrediants": {
            "milk": "175", # in ml
            "water": "150", # in ml
            "coffee": "48"}, # in gm
    },

    
}

milk = 500 #ml
water = 500 #ml
coffee = 100 #gm
sufficient_ingrediants = True

def counter():
    global drinks

    drink = input(f"Choose a drink.\nespresso \nlatte \ncappuccino\n\n").lower()
    if drink not in ["espresso", "latte", "cappuccino"]:
        print("Invalid entry.")
        return counter()
    
    price = int(drinks[drink]["price"])
    print(f"That will be $ {price}")

    def input_amount():
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            return (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01) #total coins paid to machine
        except ValueError:
            print("invalid entry!")
            return input_amount()
     
    total_amount = input_amount()
    if price == total_amount:
        return True, drink, 0
    if price < total_amount:
        return True, drink, total_amount - price
    if price > total_amount:
        return False, drink, total_amount
     
def check_ingrediants(drink):
    global milk, water, coffee, drinks
    ingrediants = drinks[drink]["ingrediants"]
    milk_needed, water_needed, coffee_needed = int(ingrediants["milk"]), int(ingrediants["water"]), int(ingrediants["coffee"])
    if milk > milk_needed and water > water_needed and coffee > coffee_needed:
        milk - milk_needed
        water - water_needed
        coffee - coffee_needed
        return True
    else:
        return False
     
while sufficient_ingrediants:
    if milk < 100 or water < 100 or coffee < 36:
        print("Machine out of stock.")
        sufficient_ingrediants = False
        continue
    order, drink, change = counter()
    if order:
        availibility = check_ingrediants(drink)
        if not availibility:
            print(f"Sorry we have run out of the stock to prepare a {drink}")
            print(f"Have your refund of $ {change}")
        else:
            print(f"Thankyou, have your {drink}.")
            if change > 0:
                print(f"Here is your remaining change of {change}")
    else:
        print("Transaction failed, insufficient amount.")
        print(f"Have your refund of $ {change}")
