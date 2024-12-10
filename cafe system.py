# cafe_menu = {
#     "Espresso": 100,
#     "Americano": 120,
#     "Latte": 150,
#     "Cappuccino": 150,
#     "Mocha": 170,
#     "Hot Chocolate": 140,
#     "Green Tea": 90,
#     "Black Tea": 80,
#     "Herbal Tea": 100,
#     "Iced Coffee": 160,
#     "Iced Tea": 130,
#     "Smoothie": 180,
#     "Muffin": 70,
#     "Croissant": 60,
#     "Bagel": 50,
#     "Scone": 60,
#     "Cookie": 30,
#     "Cake Slice": 120,
#     "Sandwich": 200,
#     "Salad": 150
# }

# total = 0
# for item, price in cafe_menu.items(): 
#     print(f"{item}: {price} INR")


# item_1 = input("good morning sir what would you like to have : ")

# if item_1 in cafe_menu:
#     print(f"{item_1} has been added to order")
#     total += cafe_menu[item_1]
# else :
#     print("please select something from menu")

# another = input("do you need anything else (yes|no):")
# if another.lower() == "yes":
#     item_2 = input("order your second order :")
#     if item_2 in cafe_menu:
#         print(f"{item_2} has been added")
#         total += cafe_menu[item_2]
#     else :
#         print("please select something from menu")

# print(f"{total}")



cafe_menu = {
    "espresso": 100,
    "americano": 120,
    "latte": 150,
    "cappuccino": 150,
    "mocha": 170,
    "hot chocolate": 140,
    "green tea": 90,
    "black tea": 80,
    "herbal tea": 100,
    "iced coffee": 160,
    "iced tea": 130,
    "smoothie": 180,
    "muffin": 70,
    "croissant": 60,
    "bagel": 50,
    "scone": 60,
    "cookie": 30,
    "cake slice": 120,
    "sandwich": 200,
    "salad": 150
}

def display_menu():
    print("Cafe Menu:")
    for item, price in cafe_menu.items():
        print(f"{item}: {price} INR")

total = 0

while True:
    display_menu()
    
    
    item = input(f"Good morning sir, what would you like to have (or type 'exit' to finish your order): ")

    if item.lower() == 'exit':
        break

    if item in cafe_menu:
        print(f"{item} has been added to your order.")
        total += cafe_menu[item]
    
    else:
        print("Please select something from the menu.")

    another = input("Do you need anything else (yes|no): ").lower()
    if another == 'no':
        break
    
print(f"Total: {total} INR")
print("Thank you for visiting! Have a great day!")
