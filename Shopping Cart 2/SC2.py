done = False

print("--! Welcome to your Shopping Cart !--")
print("Make a selection according to these choices!")
print("1 to add a product to your cart,")
print("2 to remove a product from your cart,")
print("3 to see all products in your cart,")
print("4 to checkout (will remove all products),")
print("0 to quit")

selection = int(input("Make your choice:"))

cart_items = []

while done != True:
    if selection == 1:
        print("What would you like to add:")
        cart_items.append(input())
        selection = int(input("Make your choice:"))

    elif selection == 2:
        print("What would you like to remove:")
        cart_items.remove(input())
        selection = int(input("Make your choice:"))

    elif selection == 3:
        print("Your cart consists of:")
        print(cart_items)
        selection = int(input("Make your choice:"))

    elif selection == 4:
        print("Checkout successful!")
        cart_items.clear()
        selection = int(input("Make your choice:"))

    elif selection == 0:
        done = True

        
