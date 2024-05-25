# Develop by Ludwing Hernandez
# This is de code for second coding challenge
# My MD5 Hash's number is 9

# statement of required libraries
# Library for generate random numbers
import random

# function to reorder the list of numbers
def reorderNumbers(list):
  # variable to determinate if some number change of position
  swapped = True
  # cicle to reorder the list of numbers
  while swapped:
    swapped = False
    # cicle to look each number of the list 
    for i in range(0, len(list)-1):
    # condition to determinate which number is less than another
      if list[i] > list[i+1]:
        # if there is a change of position que keep in the cicle while
        swapped = True
        list[i], list[i+1] = list[i+1], list[i]
  # return of the list of numbers reordered
  return list

# function to calculate the square of numbers in the orginal list and sort them
def squareNumbers(list):
  # new list to save the list of numbers without numbers outside the range [0-99]
  newList = []
# Cicle to look each number
  for i in range(len(list)):
    # calculate the square of numbers
    list[i] = list[i]**2
    # condition to check if the square's number is inside the range
    if list[i] < 99:
      # creation of new list of numbers with numbers inside the range
      newList.append(list[i])
  # print the list of square numbers in disorder
  print('--------------------------------------------------') 
  print('List of square numbers in disorder')
  print(newList)
  # call to the function to reorder the list of square numbers
  reorderList = reorderNumbers(newList)
  # return of final list of square numbers
  return reorderList

# begin of algorithm
# statement of matrix
listOfNumbers =[]
# cicle to fill the matrix with random numbers
for i in range(0,9):
  listOfNumbers.append(random.randint(-10,10))

# print the original list of numbers
print('--------------------------------------------------')
print('Original List of numbers:')
print(listOfNumbers)

# call to function to reorder the list of numbers 
listOfNumbers = reorderNumbers(listOfNumbers)
# print of the original list of numbers sorted by ascending order
print('--------------------------------------------------')
print('Original List of numbers sorted in ascending order :')
print(listOfNumbers)

# call to the function to generate a new list of numbers with his squares
listOfNumbers = squareNumbers(listOfNumbers)
print('--------------------------------------------------')
print('Final List of numbers sorted in ascending order :')
print(listOfNumbers)