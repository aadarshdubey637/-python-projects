menu={
    "pizza":40,
    "salad":50,
    "coffe":80,
    "burger":60,
    "pasta":50,
}
print("Welcome to Our Restaurant..!")
print("pizza:40\nsalad:50\ncoffe:80\nburger:60\npasta:50")

order_total=0
item_1=input("Enter The Name Of Item You  Want To Order :")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"YOur Item {item_1} has been added to your order ")
else:
    print(f"Your item {item_1} is not avaiable yet!")

another_order=input("Do you want to add another item? (yes/no)")
if another_order=="yes":
    item_2=input("Enter the name of second item =")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Order item {item_2} is not avaialable!")

    print(f"The Total amount of item to pay is {order_total}")
