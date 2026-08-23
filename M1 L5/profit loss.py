cost = int(input("Enter cost price: "))
selling = int(input("Enter selling price: "))

if selling > cost:
    print("Profit")
elif selling < cost:
    print("Loss")
else:
    print("No profit, no loss")