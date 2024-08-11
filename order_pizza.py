def choose():
    print("Thank you for choosing Great Pizza Deliveries!")
    print("Please choose what you would like to add onto your Pizza.")
    size = input('What pizza size do you want? Choose between Small, Medium, Large.\n')  # What size pizza do you want? "S", "M", or "L"
    add_pepperoni = input("Do you want to add pepperoni on your pizza? Choose Yes or No.\n")  # Do you want pepperoni? "Y" or "N"
    extra_cheese = input("Do you want extra cheese? Choose Yes or No.\n")  # Do you want extra cheese? "Y" or "N"

    bill = 0
    if size == "Small":
        bill += 15
    elif size == "Medium":
        bill += 20
    else:
        bill += 25

    if add_pepperoni == "Yes":
        if size == "Small":
            bill += 2
        else:
            bill += 3
            if extra_cheese == "Yes":
                bill += 1

    print(f"Your final bill is: ${bill}.")
    
choose()