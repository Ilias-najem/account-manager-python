Customer_Name = str(input("What is your name? : "))
Current_Sold = float(input("What is your current account balance? : "))
Transactions = []

running = True

print(f"Hello {Customer_Name}, welcome to your bank account!")

while running:
    user_response = input("Would you like to make a deposit, make a withdrawal, or log out? : ")
    user_response1 = user_response.upper()

    if user_response1 == "DEPOSIT":
        deposit = float(input("How much is your deposit? : "))
        Current_Sold = Current_Sold + deposit

    elif user_response1 == "WITHDRAWAL":
        withdrawal = float(input("How much is your withdrawal? : "))

        if withdrawal <= Current_Sold:
            Current_Sold = Current_Sold - withdrawal
        else:
            print("Your withdrawal amount exceeds your account balance.")

    elif user_response1 == "LOG OUT":
        running = False
        print("You have logged out of your account.")

    else:
        print("Invalid choice. Please try again.")

print(f"Your final balance is {Current_Sold} euros.")