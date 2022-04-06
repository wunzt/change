# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 4/5/2022
# Description: Asks the user to input an amount of cents less than a dollar and prints the change required in the
#   fewest possible coins

print("Please enter an amount in cents less than a dollar.")
prime = int(input())
quarters = prime // 25
dimes = (prime % 25) // 10
nickels = ((prime - (quarters * 25)) % 10) // 5
pennies = (prime % 5) // 1
print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)