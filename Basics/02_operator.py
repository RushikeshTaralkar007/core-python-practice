#############    (Arithmatic Operators)    ##################

###################  ( Day 1 )   ###################

a= 10
b=5

# Q1) Add Two Numbers 

print(a+b)

# Q2) Substract Two Numbers 

print(a-b)

# Q3) Multipilication of Two Numbers 

print(a*b)

# Q4) Division Of Two Numbers 

print(int(a/b))
print(a/b)

# Q5) Floor Division

print(a // b)

# Q6) Float Division

print(5.5 // 3)

# Q7) Square Of Number 

x=7
print(x ** 2)

# Q8) cube of number 
print(2 **3)

# Q9) Modulus 

print(10 % 2)

# Q10) Power Operator 
print(4 **3)

# Q11) Combined Operator 
print(2+3 * 4)

# Q12) Brackets Priority 
print((2+3) *4)

# Q13) Negative Multiplication

print(-5 * 3)

# Q14) Float Addition 

print(2.5 +3.6)

# Q15) Remainder check even/ odd

num = 8
print(num % 4)

# Q16) Calculate Area

length = 8
width = 5
print("Area:",length*width)

# Q17) BMI Formula 

weight = 60
height = 1.7
print(weight / (height ** 2))

# Q18) Add 3 Number
print(2+3+8)

# Q19) Multiple Subtraction

print(2-5-8)

# Q20) Mixed Division

print(20 // 6)

# Q21) Power With FLoat 

print(4 ** 0.5)

# Q22) Zero Multiplication
print(10 *0)

# Q23) Modulus Example 

print(25 % 5)

# Q24) Division Result Type 

print(type(10 / 2))

# Q25) Floor Result Type 

print(type(10 // 2))

# Q26) Negative Modulus 
print(-10 % 3)

# Q27) Exponent Chain 

print(2** 2** 2)

# Q28) Large Multiplication

print(12506 * 2658)

# Q29) Decimal Precision
print(0.1 + 0.2)

# Q30) Complex Expression 
print((5+3) * 2+4 -5/2)


#############    (Comparision Operators)    ##################

###################  ( Day 2 )   ###################

# Q31) Equal check 

print(5 == 5)
print(5 == 4)

# Q32) Not Equal

print(5 != 4)
print(4 != 4)

# Q33) Greater than

print(10 > 5) ## True 
print(10 < 5) ## False 

# Q34) Less Than


print(10 > 5) ## True 
print(10 < 5) ## False 

# Q35) Greater Equal 

print(20 >= 10)

# Q35) Less Equal 

print(50 <= 100)

# Q36) compare string 

print("a" == "a")


# Q37) compare different string type

print("a" == "b")

# Q38) compare Float

print(2.5 == 2.3)
print(2.5 > 2.3)

# Q39) compare Negative Number 

print(-5 > -2)

# Q40) chain Comaparision 

print( 4 < 25 < 65)

# Q41) comapre length 

print(len("python") == 6)

# Q42) compare booleans 

print(True == 1)

# Q43) compare False

print(False == 0)

# Q44) comapre list eqaulity 

print([1,2] == [1,3])

print([3,2] == [3,2])

# Q45) comapre list ineqaulity 

print([3,2] != [3,2])

# Q46) compare uppercase 

print("A" > "a")

# Q47) Compare Ascii

print(ord("A") < ord("B"))

# Q48) compare input number 

num = 10
print(num > 4)

# Q49) Nested comparision 

print(5 < 10 and 10 < 20)

# Q50) compare zero 

print(0 == False )

# Q51) compare None 

print( None == None)

# Q52) comapre float precision

print(0.3 + 0.2 == 0.5)

# Q53) comapre string length 

print(len("data") > len("AI"))

# Q54) comapre user age 

age = 20
print(age >= 18)

# Q55) Compare dictionary equality

print( {a:1} == {a:1})

# Q56) compare tuple 

print((1,2) <(1,3))

# Q57) compare mixed numbers 

print(5.0 == 5)

# Q58) compare negative equality 

print(-10 == -10)

# Q59) complex comparison

print( 5*2 > 3+6)


#############    (Logical  Operators)    ##################

###################  ( Day 3 )   ###################


# # Q60) Check number between 10 and 20

# num = int(input("Enter The number :"))
# print(num>=15 and num <20)


# # Q61) Check divisible by 3 AND 5

# num = int(input("Enter The Number :"))
# print(num % 3 == 0 and num % 5 ==0)


# # Q62) Pass if marks >=40 AND attendance >=75

# marks = int(input("Enter The marks :"))
# Attendence  = int(input("Enter The Attendence :"))

# print(marks >= 40 and Attendence >=75)


# # Q63) Eligible for job (age >18 OR experience >2)

# age = int(input("Enter The Age :"))
# exp = int(input("Enter The Expence :"))

# print( age > 18 and exp > 2)



# Q64) NOT operator

is_logged_in = False
print(not is_logged_in)

# Q65) Complex condition

a= 5
b= 10
print(a<b and b<20 or a==5)

# Q65) Short-circuit example

print(False and 10/0)

# Q66) OR short-circuit

print(True or 10/0)

# # Q67) check password 

# password = input("Enter Password :")
# print(len(password) >= 8 and "@" in password)


# # Q68) Check vowel

# ch = input("Enter The Character :")
# print(ch in "aeiou" and ch.islower())


# # Q69) Nested logical

# Age = int(input("Enter The Age :"))
# salary = int(input("Enter The Salary :"))

# print((age > 18 and salary > 30000) and salary<50000)


# # Q70) Check leap year logic

# year = int(input("Enter The Year :"))
# print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


# Q71) Truthy check

print(bool([]) or bool("python"))

# Q72) Empty string check

Name = ""
print(not Name)

# Q73) Check uppercase and digit

x= "A1"
print(x[0].isupper() and x[1].isdigit())

# Q74) Login check 

username = "admin"
password = "1234"

print( username == "admin" and password == "1234" )

# Q75) Complex logical chaining

x= 10
print((x >5 and x<20) and not (x == 10))



# # Q76) Check if number is even OR divisible by 9

# num = int(input("Enter The Number :"))

# print(num % 2==0 or num % 9 == 0)

# # Q77) Check strong password (≥8 chars AND uppercase AND digit)


# password = "Admin123"
# print(len(password) >= 8 any(c.isupper() for c in password) and any(c.isdigit() for c in password))



# Q78) Check if at least two numbers are positive

a , b , c = 5,-2,3

print((a > 0 and b>0) or (a>0 and c>0) or (b>0 and c>0))

# Q79) Check if salary is between 30000–80000 OR experience > 5

salary = 25000
exp = 6
print((30000 <= salary <= 80000) or exp > 5)

# # Q80) Check if number is divisible by 2 AND 3 but NOT 6

# num = int(input("Enter The Number :"))
# print((num % 2 ==0 and num % 3 == 0) and not num % 6 != 0)



#############    (Assignment Operators)    ##################

###################  ( Day 4 )   ###################


# Q81) increase marks by 15

marks =70
marks += 15
print(marks)

# Q82) Decrease stock by 3

stock = 20
stock -= 3
print(stock)

# Q83) Triple a number 

x=4
x *=3

print(x)

# Q84) divide salary by 2

salary = 40000
salary /= 2
print(salary)

# Q85) Floor divide 50 by 6

x=50
x //=6
print(x)

# Q86) find the remainder when divided by 4

x = 22
x % 4 == 0

print(x)

# Q87) Raise to cube 

x= 3
x **= 3
print(x)

# Q88) increase balance in loop 

balance = 0 
for i in range(5):
    balance += 100
print(balance)

# Q89) Deduct GST 18 %

price = 1000
price = price * 0.18
print(price)

# 90) increase by 10% then multiple by 2 

x=100
x += x * 0.10
x *= 2
print(x)

# Q91) first Substract then half of number 

x=40
x -= x/2 
print(x)

# Q92) Multiple by (x+1)

x= 5
x *= (x+1)
print(x)

# Q93) Add 5 then Square 

x= 3
x += 5
x **= 2
print(x)

# Q94) Halve Repeatedly 

x = 64
x /= 2
x /= 2
print(x)


# Q95) Modulus Chain 

x =100
x %= 30
x %= 4

print(x)

# Q96) Bank Deductuction 

balance = 5000
withdraw = 1000
balance -= withdraw
print(balance)



#############    (Identity & Membership Operators)    ##################


# Q97) Compare two tuples using is 

a = (1,2)
b = (1,2)
print( a is b)


# Q98) Assign tuple reference 

a= (1,2)
b= a
print(a is b)

# Q99) check if variable is not None 

x= "Data"
print(x is not None)

# Q100) Comapre Large Integers identity 

a = 1000
b = 1000
print( a is b)

# Q101) Membership in set 

s= {10,20,30}
print(20 in s)

# Q102) Membership in string case sensitive

print("d" in "Data")

# Q103) Not in dictionary keys

d = {"a":1, "b": 2}
print("c"not in d)

# Q104) Compare two copied dictionaries

a = {"x": 1}
b = a.copy() 
print(a is b)


# Q105) Compare equality vs identity in dict

a = {"x": 1}
b = {"x": 1}
print(a == b)
print(a is b)

# Q106) check substing not present 

print("AI" not in "Data Science")


# Q107) check a string is present or not

text = "Engineer"
print("Eng" in text)

# Q108) check number in the set exist

print(5 not in {1,6,8})

# Q109) check is equality 

x = 569
y = 456
print( x is b)

# Q110) check the symbol equality 

a= []
b =[]
print(a == b)


a= []
b ={}
print(a == b)


a= []
b =[]
print(a is b)


