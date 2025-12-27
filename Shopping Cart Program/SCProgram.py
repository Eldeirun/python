item = input("What item will you be buying:")
quantity = int(input("And how many units:"))
price = float(input("At what price (USD) per unit:"))

netPrice = price*quantity

print(f"Your total for {quantity} units of {item} comes out to {netPrice} US Dollars.")