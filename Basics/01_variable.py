###################   (Day 1)    ###################

# Q1) Print The Name 

name = "Rushikesh Taralkar"
print("Name :", name)

# Q2) Store integer and print its type

num =25
print(type(num))


# Q3) Store float Value 

price = 88.99
print(price)

# Q4) store string

city = "Pune"
print(city)

# Q5) Multiple Variable Assignment

a,b,c=1,2,3
print(a,b,c)

# Q6) Assign same value to multiple variables

x = y = z = 100
print(x,y,z)

# Q7) Swap Two Variables

a = 5
b = 10
a,b = b,a 
print("a :",a,"b :",b)

# Q8) Addition/ substraction/ Multiplication / Division of Two Variables 

x=10
y=20
print(x+y)
print(x-y)
print(x*y)
print(x/y)

# Q9) Concatenate Strings

first = "Data"
second = "Engineer"
print(first + " "+ second)

# Q10) Convert into a Float Value

x=10
print(float(x))


###################   (Day 2)    ###################

# Q11) convert string into int

num = "25"
print(int(num))


# Q12) check Variable type 

x= "Rushi"
print(type(x))



## Q13) Take Input From User 

# name = input("Enter Your Full Name :")
# print("Full Name :", name)



# # Q14) Add Two User Inputs 

# num1 = int(input("Enter The Num1 :"))
# num2 = int(input("Enter The Num2 :"))
# print("Addition :",num1+num2)



# # Q15) Check if variable is even or odd

# num = int(input("Enter The Number :"))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# Q16) Find Maximum Of Two Variables 

x=5
y=8
print(max(x , y))

# # Q17) Calculate Area Of Rectangle

# length = int(input("Enter The Length :"))
# width = int(input("Enter The Width :"))
# area = length * width 
# print("Area Of Rectangle : ",area)

# # Q18) Calculate Simple Interest 

# Amount = int(input("Enter The Amount :"))
# Rate = float(input("Enter The Rate :"))
# Time = float(input("Enter The Year :"))
# S_I= (Amount * Rate * Time ) / 100
# print("Simple Interest :", S_I)


# # Q19) Check Variable Is Positive , negative or zero

# num = int(input("Enter The Number :"))
# if num> 0:
#     print("Number Is Positive")
# elif num<0:
#     print("Number Is Negative")
# else:
#     print("Number Is Zero")


# Q20) string Length 

name = "Rushikesh"
print(len(name))


###################   (Day 3 )    ###################

# Q21) Convert String to Uppercase 

text = "data"
print(text.upper())

# Q22) check variable exists

x= 10
print("x" in globals())

# Q23) Delete Variable 

x= 10
del x

# Q24) use f-string 

name = "Rushikesh"
age =20
print(f"My Name Is {name} and My Age Is {age}")

# Q25) check type using isinstance()

x=10
print(isinstance(x , int))

# Q26) Multiple Two Variables 

a=5
b=20
print(a*b)

# # Q27) calculate the sqaure of number

# x=int(input("Enter The Number:"))
# print(x **2)


# Q28) check string is numeric 

x = '123'
print(x.isdigit())

# Q29) Boolean variable example 

is_active =True
print(type(is_active))

# Q30) type casting float to int

x=10.8
print(int(x))

# # Q31) use input and print datatype

# x= input("Enter The Value:")
# print(type(x))

# Q32) Assign list to variables 

num = [1,2,3]
print(num)

# Q33) Assign dictionary to variable

student = {"name": "Rushikesh", "age": 20}
print(student)

# Q34) use id function()

x= 10
print(id(x))

# Q35) check memory address difference 

a= 10
b= 10
print(id(a))
print(id(b))

# Q36) Mutable and immutable example 

a=10
b=a
a=20
print(b)  ##  Its a Immutable Example 

# Q37) list mutability 

a= [1,2,3]
b =a
a.append(4)
print(b)

# Q38) global variable example 

x=10

def show():
    print(x)
show()

# Q39) Local variable example 

def test():
    y=5
    print(y)
test()

# Q40) use global keyword

x=5

def change():
    global x
    x=20
change()
print(x)

# Q41) constatnt variable convention

PI = 3.14

# Q42) Dynamic typing example 

x=10
x="python"
print(x)

# Q43) check reference behaviour 

a=[1,2]
a.append(3)
b=a.copy()
print(b)

# Q44) None Type VAriable 

x=None
print(type(x))

# Q45) check multiple conditions 

a=20
b=55
c=30

print(a < b < c)

a=20
b=30
c=50

print(a < b < c)

# Q46) use walrus operator 

if (n := 5) >3:
    print(n)

# Q47) variable shadowing 

x=10

def test():
    x=20
    print(x)
test()
print(x)



# Q48) swap without third variable 

a = 5
b = 7
a = a+b
b = a-b
a = a-b
print("a:",a,'b:', b)

# Q49) check identity and eqality 

a =[1,2]
b =[1,2]
print(a == b)
print(a is b)

