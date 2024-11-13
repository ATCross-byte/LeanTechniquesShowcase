The following code in the currency converter works to find the smallest amount of change for a given amount from use input.

The first function works to find the largest dollar bill amount that can go into the amount given, and subtract that total from the initial amount.
This process repeats for each amount from fifties to pennies.
At the end of the function all values are returned. 

The second function takes all of the returned values and stores them into separate print functions. Ex. Input = 50, Output = Fifty(s): 1

Finally the main function helps to create a more appealing output, takes user input, and connects the functions to make the whole file run properly. 

if __name__ == "__main__": main() / allows the file to run and be tested. 