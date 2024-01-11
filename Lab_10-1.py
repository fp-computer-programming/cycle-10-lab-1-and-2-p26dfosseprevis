#Create a Python file named lab_10-1.py
#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Using a while loop, write a program that prompts the user to input a number.
#If the user inputs a number, add that to the sum of the previous numbers entered.
#If the user enters -1, the program should end and display the sum of all the numbers entered.
#Be sure the program uses a break statement

num = 0
while 1:
    a = int(input("number: "))
    if a == -1:
        print(num)
        break
    else:
        num += a
        
