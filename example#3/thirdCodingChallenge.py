# Develop by Ludwing Hernandez
# This is de code for Third coding challenge

# statement of required libraries
# Library for generate random numbers
import random

# Function to fill coins value  and sort them in ascending way
def fillAndSorterCoins(coins):
  # variable to determinate if some number change of position
  swapped = True
  # cicle to fill the values of coins
  for i in range(0,9):
    coins.append(random.randint(0,100))
    # cicle to sort the coins values in ascending order
  while swapped:
    swapped = False
  # cicle to reorder the list of numbers
    for j in range(0,len(coins)-1):
      # condition to determinate which number is less than another
      if coins[j] > coins[j+1]:
        # if there is a change of position que keep in the cicle while
        swapped = True
        coins[j], coins[j+1] = coins[j+1], coins[j]
  # return the list of coins values
  return coins

# Function to determinate the lowest value of change
def lowestChange(coins):
  # variable to start the minimum change
  minChangeValue = 1
  # for to look each value of coins in the list
  for i in range(0,len(coins)):
    # condition to determinate the maximum value posible
    if coins[i] > minChangeValue:
      break
    # counter to determine the minimum change posible
    minChangeValue += coins[i]
  return minChangeValue
# Begin of algorithm
# statement of list of coins
coins= []

# call to the function to fill and sort the value of coins
coins = fillAndSorterCoins(coins)
print('-----------------------------------------------------------------------------')
print('Coins sorted by asending value')
print(coins)

# Call to the function to determinate the lowest value of change that we can't give
lowestChangeValue = lowestChange(coins)
print('-----------------------------------------------------------------------------')
print('lowest change that we cant give')
print(lowestChangeValue)