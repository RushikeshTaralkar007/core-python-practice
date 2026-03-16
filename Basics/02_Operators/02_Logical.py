#############    (Logical  Operators)    ##################


# # Q1) Check number between 10 and 20

# num = int(input("Enter The number :"))
# print(num>=15 and num <20)


# # Q2) Check divisible by 3 AND 5

# num = int(input("Enter The Number :"))
# print(num % 3 == 0 and num % 5 ==0)


# # Q3) Pass if marks >=40 AND attendance >=75

# marks = int(input("Enter The marks :"))
# Attendence  = int(input("Enter The Attendence :"))

# print(marks >= 40 and Attendence >=75)


# # Q4) Eligible for job (age >18 OR experience >2)

# age = int(input("Enter The Age :"))
# exp = int(input("Enter The Expence :"))

# print( age > 18 and exp > 2)



# Q5) NOT operator

is_logged_in = False
print(not is_logged_in)

# Q6) Complex condition

a= 5
b= 10
print(a<b and b<20 or a==5)

# Q7) Short-circuit example

print(False and 10/0)

# Q8) OR short-circuit

print(True or 10/0)



# # Q9) check password 

# password = input("Enter Password :")
# print(len(password) >= 8 and "@" in password)



# # Q10) Check vowel

# ch = input("Enter The Character :")
# print(ch in "aeiou" and ch.islower())


# # Q11) Nested logical

# Age = int(input("Enter The Age :"))
# salary = int(input("Enter The Salary :"))

# print((age > 18 and salary > 30000) and salary<50000)


# # Q12) Check leap year logic

# year = int(input("Enter The Year :"))
# print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


# Q13) Truthy check

print(bool([]) or bool("python"))

# Q14) Empty string check

Name = ""
print(not Name)

# Q15) Check uppercase and digit

x= "A1"
print(x[0].isupper() and x[1].isdigit())


# Q16) Login check 

username = "admin"
password = "1234"

print( username == "admin" and password == "1234" )

# Q17) Complex logical chaining

x= 10
print((x >5 and x<20) and not (x == 10))



# # Q18) Check if number is even OR divisible by 9

# num = int(input("Enter The Number :"))

# print(num % 2==0 or num % 9 == 0)



# # Q19) Check strong password (≥8 chars AND uppercase AND digit)


# password = "Admin123"
# print(len(password) >= 8 any(c.isupper() for c in password) and any(c.isdigit() for c in password))



# Q20) Check if at least two numbers are positive

a , b , c = 5,-2,3

print((a > 0 and b>0) or (a>0 and c>0) or (b>0 and c>0))

# Q21) Check if salary is between 30000–80000 OR experience > 5

salary = 25000
exp = 6
print((30000 <= salary <= 80000) or exp > 5)



# # Q22) Check if number is divisible by 2 AND 3 but NOT 6

# num = int(input("Enter The Number :"))
# print((num % 2 ==0 and num % 3 == 0) and not num % 6 != 0)

