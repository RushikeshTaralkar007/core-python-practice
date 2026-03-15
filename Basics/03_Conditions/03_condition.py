
#################    (Day 1)    ####################

# Q1) Check whether a number is positive, negative, or zero.

num = int(input("Enter The Number :"))

if num > 0:
    print("Positive Number")

elif num < 0:
    print("Negative Number")

else:
    print("Zero")






# Q2) Check if a number is even or odd.

num = int(input("Enter The Number"))

if num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")






# Q3) Find the largest of two numbers.

a= 10
b= 20

if a>b:
    print("A Is Largest")

else:
    print("B Is Largest")






# Q4) Find the largest of three numbers.

a = int(input("Enter The Number :"))
b = int(input("Enter The Number :"))
c = int(input("Enter The Number :"))

if a > b and a > c:
    print("a is Grater")

elif b> a and b>c:
    print("b is Grater")

else:
    print("c is Grater")





# Q5) Check if a year is leap year.

year = int(input("Enter The Year :"))

if year % 4 == 0 or year % 400 == 0:
    print(year, 'Is A Leap Year')

elif year % 100 != 0:
    print("Not A Leap Year !")

else:
    print("Invalid Input !!!")





# Q6) Check if age is eligible to vote (18+).

age = int(input("Enter The Age :"))

if age > 18:
    print("Eligible For Vote")

elif age < 18:
    print("Not Eligible")

else:
    print("Invalid Input !!!")





# Q7) Check if a number is divisible by both 3 and 5.

num = int(input("Enter The Number :"))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible By Both")

else:
    print("Not Divisible By Both")





# Q8) Check if character is vowel.

ch = input("Enter The Character :")

if ch.lower() in "aeiou":
    print("Vovel")
else:
    print("Its Not a Vovel")





# Q9) Check if string length > 5

str = input("Enter The string :")

if len(str) > 5:
    print("Long String")

else:
    print("Short String")





# Q10) Grade system (>=90 A, >=75 B, >=50 C, else Fail)

Marks = int(input("Enter The Marks :"))

if Marks >= 90:
    print("Garde A")
elif Marks >= 75:
    print("Grade B")

elif Marks >= 50:
    print("Garde C")

else:
    print("Fail !!!")




# Q11) Check if number is between 1–100.


num = int(input("Enter The Number :"))

if 1 <= num <= 100:
    print("Valid Range")

else:
    print("Out Of Range")



# Q12) Check if number is multiple of 7.

num = int(input("Enter The Number :"))

if num % 7 == 0:
    print("Multiple By 7")

else:
    print("Not Multiple")




# Q13) Check if password length >= 8.

password = input("Enter The Password :")

if len(password) > 8:
    print("valid Length")

else:
    print("Invalid Length")



# Q14) Check if temperature is freezing (<0).

temp = int(input("Enter The Temperature :"))

if temp <= 0:
    print("Freezing")
else:
    print("Normal")



# Q15) Check if a number is square number (perfect square).

import math 

num = int(input("Enter The Number :"))

if math.sqrt(num).is_integer():
    print("Perfect Square")

else:
    print("Not Perfect Sqaure")




# Q16) ATM Withdrawal (check sufficient balance)

balance = int(input("Enter The Balance Amount :"))
withdraw = int(input("Enter The Withdraw Amount :"))

if withdraw <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance !!!")



# Q17) Login validation

username = input("Enter The Username :")
password = input("Enter The Password :")

if len(username) > 8 and len(password) >= 8 and "@" in password:
    print("Login Succesfully !")

else:
    print("Invalid Credentials !!!")



# Q18) Check if number is positive even.

num = int(input("Enter The Number :"))

if num > 0 and num % 2== 0:
    print("Even Number ")

else:
    print("Odd Number")




# Q19) Check if string contains digit.

text = int(input("Enter The Text :"))

if any(c.isdigit() for c in text):
    print("Contains Digit ")
else:
    print("No Digit ")




# Q20) Check if a triangle is valid.

a = int(input("Enter The a number :"))
b = int(input("Enter The b number :"))
c = int(input("Enter The c number :"))

if a+b > c and a+c >b and b+c > a:
    print("Valid Triangle")

else:
    print("Invalid Triangle")