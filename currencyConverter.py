#Lean Techniques Intern Showcase
#Aidan Cross / crossa@iastate.edu / 515 - 851 - 0770

#Convert currency into exact change 
def convertCurrency(user_val):

    #Number of fifties
    num_fifties = int(user_val // 50)
    user_val -= num_fifties * 50

    #Number of twenties 
    num_twenties = int(user_val // 20)
    user_val -= num_twenties * 20

    #Number of tens
    num_tens = int(user_val // 10)
    user_val -= num_tens * 10

    #Number of fives
    num_fives = int(user_val // 5)
    user_val -= num_fives * 5

    #Number of ones
    num_ones = int(user_val // 1)
    user_val -= num_ones * 1

    #Number of quarters
    num_quarters = int(user_val // 0.25)
    user_val -= num_quarters * 0.25

    #Number of dimes
    num_dimes = int(user_val // 0.10)
    user_val -= num_dimes * 0.10

    #Number of nickels
    num_nickels = int(user_val // 0.05)
    user_val -= num_nickels * 0.05

    #Number of pennies
    num_pennies = int(user_val // 0.01)
    user_val -= num_pennies * 0.01

    return num_fifties, num_twenties, num_tens, num_fives, num_ones, num_quarters, num_dimes, num_nickels, num_pennies

#Print exact currency amounts
def printValues(num_fifties, num_twenties, num_tens, num_fives, num_ones, num_quarters, num_dimes, num_nickels, num_pennies):
    print(f"Fifty(s): {num_fifties}")
    print(f"Twenty(s): {num_twenties}")
    print(f"Ten(s): {num_tens}")
    print(f"Five(s): {num_fives}")
    print(f"One(s): {num_ones}")
    print(f"Quarter(s): {num_quarters}")
    print(f"Dime(s): {num_dimes}")
    print(f"Nickel(s): {num_nickels}")
    print(f"Penny(s): {num_pennies}")

#Main function & formatting    
def main():
    print("-" * 65)
    print("Currency Converter")
    print("-" * 65)
    user_val = float(input("Enter the amount desired in USD: "))
    print("-" * 65)
    print(f"You entered ${user_val}, which in the smallest amount of change is:")
    result = convertCurrency(user_val)
    printValues(*result)
    print("-" * 65)

if __name__ == "__main__":
    main()