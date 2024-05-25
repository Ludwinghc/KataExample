# Develop by Ludwing Hernandez
# This is de code for first coding challenge
# My MD5 Hash's number is 9

# required libraries
# Library for generate random numbers
import random

# function for complete the list of numbers
def fillArrayNumbers(list):
  # cicle to fill the array with random numbers
  for i in range(0, 9):
    list.append(random.randint(0,100))
  return list

# function for delete the digit 9 from the list of numbers
def deletDigit(list):
  # cicle to look each number of the list
  for i in range(0, len(list)):
    result=0
    # in form of power of 10
    pivot=1
    # new list to delete 0 from the list of numbers
    newlist =[]
    # use a temporal variable to delete the digit of the number
    numTemp = list[i]
    # cicle to delete the digit 9 from the number selected
    # using division 
    while numTemp >0:
      residue = numTemp%10
      # condition to catch the number that we want to conserve
      if residue != 9:
        result=result+residue*pivot
        pivot=pivot*10
      numTemp = numTemp//10
    list[i] = result
  # cicle to delete the  0 from the list of numbers
  for j in range(0, len(list)):
    if list[j] != 0:
      newlist.append(list[j])
  return newlist

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


# begin of algorithm
# array variable  empty list
list = []

# call to the function to complete the array variable
list= fillArrayNumbers(list)
# print list after call to fillArrayNumbers
print('--------------------------------------------------')
print('Original List of numbers:')
print(list)


# call to the function to delete the digit 9 from the list of numbers
list=deletDigit(list)
# print list after call to deleteDigit
print('--------------------------------------------------')
print('New List of numbers: ')
print(list)

# call to the function to reorder the list of numbers
list= reorderNumbers(list)
# print list after call to reorderNumbers
print('--------------------------------------------------')
print('Final List of numbers: ')
print(list)



