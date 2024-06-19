import math

def investment_calculator():
    # Input from user
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    # Calculate the total amount based on the type of interest
    if interest == "simple":
        A = P * (1 + r * t)
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
    else:
        print("Invalid interest type entered. Please enter 'simple' or 'compound'.")
        return

    # Output the total amount
    print(f"The total amount after {t} years is: {A}")

def bond_calculator():
    # Input from user
    P = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    i = annual_rate / 12
    n = int(input("Enter the number of months you plan to take to repay the bond: "))

    # Calculate the monthly repayment amount
    repayment = (i * P) / (1 - (1 + i) ** (-n))

    # Output the monthly repayment amount
    print(f"The monthly repayment amount is: {repayment}")

def main():
    # Menu for user to choose which calculation they want to perform
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # Perform the chosen calculation
    if choice == "investment":
        investment_calculator()
    elif choice == "bond":
        bond_calculator()
    else:
        print("Invalid choice. Please enter 'investment' or 'bond'.")

if __name__ == "__main__":
    main()