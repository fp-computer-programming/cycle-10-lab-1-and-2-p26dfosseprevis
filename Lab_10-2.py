#Create a Python file named lab_10-2.py
#Using the same approach as lab 1, write a program that prints all the numbers that are multiples of 3 in a list. Be sure your program uses a continue statemen

num = []
while 1:
    a = int(input("num: "))
    if a == -1:
        print(num)
        break
    if a % 3 != 0:
        continue
    else:
        num.append(a)

    