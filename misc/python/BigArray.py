#Big Array	
#Make an Array. Fill it with 19 random numbers from 20 to 90

#01 Print the Array from the beginning to the end
#02 Print the Array from the beginning to the end using a for-each loop
#03 What number is in the middle of the Array?
#04 What is the average of the first, last and middle numbers?
#05 Find the smallest and the largest number in the Array
#06 Switch the largest with smallest number. Print the list
#07 Create a new random from 1 to 10 and insert it in the middle slot. Print the numbers.
#08 Add 10 to every number in the List. Print all.
#09 Replace the 3rd element in the array with 5 and print the number that was ousted 
#10 What numbers are in the 50s?
#11 What numbers are multiples of 4?
#12 Is there a 60 in the list?
#13 Check to see if all of the elements from front to back are in the same order from back to front
#14 How many numbers are greater than the average?
#15 How many of the numbers are even?
#16 Copy all of the elements of the array into a new array but in reverse order
#17 Write a program to shift every element of an array to circularly right. E.g.-INPUT : 1 2 3 4 5 OUTPUT : 5 1 2 3 4
#18 Find the sum of all of the digits of all of the elements

import random

def main():
    #01 Print the Array from the beginning to the end
    print("01 Print the Array from the beginning to the end")
    array = []
    for i in range(19):
        array.append(random.randint(20,90))
    print(array)
    print()
    
    #02 Print the Array from the beginning to the end using a for-each loop
    print("02 Print the Array from the beginning to the end using a for-each loop")
    for i in array:
        print(i, end = " ")
    print()
    print()
    
    #03 What number is in the middle of the Array?
    print("03 What number is in the middle of the Array?")
    print(array[len(array)//2])
    print()
    
    #04 What is the average of the first, last and middle numbers?
    print("04 What is the average of the first, last and middle numbers?")
    print((array[0] + array[len(array)//2] + array[len(array)-1])/3)
    print()
    
    #05 Find the smallest and the largest number in the Array
    print("05 Find the smallest and the largest number in the Array")
    print("Smallest:", min(array))
    print("Largest:", max(array))
    print()
    
    #06 Switch the largest with smallest number. Print the list
    print("06 Switch the largest with smallest number. Print the list")
    largest = max(array)
    smallest = min(array)
    largestIndex = array.index(largest)
    smallestIndex = array.index(smallest)
    array[largestIndex] = smallest
    array[smallestIndex] = largest
    print(array)
    print()
    
    #07 Create a new random from 1 to 10 and insert it in the middle slot. Print the numbers.
    print("07 Create a new random from 1 to 10 and insert it in the middle slot. Print the numbers.")
    array.insert(len(array)//2, random.randint(1,10))
    print(array)
    print()
    
    #08 Add 10 to every number in the List. Print all.
    print("08 Add 10 to every number in the List. Print all.")
    for i in range(len(array)):
        array[i] += 10
    print(array)
    print()
    
    #09 Replace the 3rd element in the array with 5
    print("09 Replace the 3rd element in the array with 5")
    print("Ousted:", array[2])
    array[2] = 5
    print(array)
    print()

    #10 What numbers are in the 50s?
    print("10 What numbers are in the 50s?")
    for i in array:
        if i >= 50 and i <= 59:
            print(i, end = " ")
    print()

    #11 What numbers are multiples of 4?
    print("11 What numbers are multiples of 4?")
    for i in array:
        if i % 4 == 0:
            print(i, end = " ")
    print()

    #12 Is there a 60 in the list?
    print("12 Is there a 60 in the list?")
    if 60 in array:
        print("Yes")
    else:
        print("No")
    print()

    #13 Check to see if all of the elements from front to back are in the same order from back to front
    print("13 Check to see if all of the elements from front to back are in the same order from back to front")
    reverse = array[::-1]
    if array == reverse:
        print("Yes")
    else:
        print("No")
    print()

    #14 How many numbers are greater than the average?
    print("14 How many numbers are greater than the average?")
    average = sum(array)/len(array)
    count = 0
    for i in array:
        if i > average:
            count += 1
    print(count)
    print()

    #15 How many of the numbers are even?
    print("15 How many of the numbers are even?")
    count = 0
    for i in array:
        if i % 2 == 0:
            count += 1
    print(count)
    print()

    #16 Copy all of the elements of the array into a new array but in reverse order
    print("16 Copy all of the elements of the array into a new array but in reverse order")
    reverse = array[::-1]
    print(reverse)
    print()

    #17 Write a program to shift every element of an array to circularly right. E.g.-INPUT : 1 2 3 4 5 OUTPUT : 5 1 2 3 4
    print("17 Write a program to shift every element of an array to circularly right. E.g.-INPUT : 1 2 3 4 5 OUTPUT : 5 1 2 3 4")
    array.insert(0, array.pop())
    print(array)
    print()

    #18 Find the sum of all of the digits of all of the elements
    print("18 Find the sum of all of the digits of all of the elements")
    sum = 0
    for i in array:
        sum += sumDigits(i)
    print(sum)
    print()

if __name__ == "__main__":
    main()