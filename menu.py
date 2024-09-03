# menu of restaurant

menu = {
    "Pizzaa": 20,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80,

}

#greeting customers

print("Welcome To Our Restaurant ")
print("Pizzaa: RS20\nPasta: RS50\nBurger: RS60\nSalad: RS70\nCoffee: RS80")

order_total = 0

item_1 = input("Enter The Name Of Item You Want To Order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    

else:
    print(f"Order item {item_1} is not avialable yet")

another_order = input("Do you want add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
        
    else:
        print(f"Ordered item {item_2} is not avaialable!")


print(f"The total amount of items to pay is {order_total}")

