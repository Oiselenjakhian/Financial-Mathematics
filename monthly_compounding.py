# Print out the purpose of the program
print("This program computes the compound amount using monthly compounding")
print("Reference: An Undergraduate Introduction to Financial Mathematics (Page 3)\n")

# Ask the user for the principal amount
principal = float(input("Please enter the principal amount: "))

# Ask the user for the rate as a percentage
rate = float(input("Please enter the rate: "))

# Ask the user for the number of years as a decimal value
years = float(input("Please enter the number of years as a decimal value: "))

# Compute the compound amount (Page 3)
r_n = rate / (12 * 100)
nt = years * 12
factor = (1 + r_n) ** nt
compound_amount = principal * factor
print("\nThe compound amount is:", round(compound_amount, 2))
