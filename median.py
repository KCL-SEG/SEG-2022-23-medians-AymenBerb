"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from operator import index

def getMedian(listOfNumbers):
    result = 0
    listOfNumbers.sort()
    if (len(listOfNumbers) % 2 == 1):
        # If the number of elements inside the list is odd, we take the element at the exact middle of the list.
        result = listOfNumbers[len(listOfNumbers) // 2]
    else:
        indexOfFirstMiddleNumber = int((len(listOfNumbers) / 2) - 1)
        #If the number of element inside the list is even, we perform the average of the two middle numbers.
        result = (listOfNumbers[indexOfFirstMiddleNumber] + listOfNumbers[indexOfFirstMiddleNumber + 1]) / 2
    return result

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(getMedian(numbers))
