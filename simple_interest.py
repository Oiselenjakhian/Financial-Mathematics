# Print out the purpose of the program
print("This program computes the compound amount using simple interest")
print("Reference: An Undergraduate Introduction to Financial Mathematics (Page 2)\n")

# Ask the user for the initial deposit
principal = float(input("Please enter the initial deposit: "))

# Ask the user for the rate as a percentage
rate = float(input("Please enter the rate: "))

# Ask the user for the number of years
years = float(input("Please enter the number of years: "))

# Compute the compounded amount
rate = rate / 100
compounded_amount = principal * ((1 + rate)**years)
print("\nThe compounded amount is:", round(compounded_amount, 2))

