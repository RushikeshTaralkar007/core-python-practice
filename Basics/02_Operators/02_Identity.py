#############    (Identity & Membership Operators)    ##################


# Q1) Compare two tuples using is 

a = (1,2)
b = (1,2)
print( a is b)


# Q2) Assign tuple reference 

a= (1,2)
b= a
print(a is b)


# Q3) check if variable is not None 

x= "Data"
print(x is not None)


# Q4) Comapre Large Integers identity 

a = 1000
b = 1000
print( a is b)


# Q5) Membership in set 

s= {10,20,30}
print(20 in s)

# Q6) Membership in string case sensitive

print("d" in "Data")


# Q7) Not in dictionary keys

d = {"a":1, "b": 2}
print("c"not in d)



# Q8) Compare two copied dictionaries

a = {"x": 1}
b = a.copy() 
print(a is b)



# Q9) Compare equality vs identity in dict

a = {"x": 1}
b = {"x": 1}
print(a == b)
print(a is b)



# Q10) check substing not present 

print("AI" not in "Data Science")



# Q11) check a string is present or not

text = "Engineer"
print("Eng" in text)


# Q12) check number in the set exist

print(5 not in {1,6,8})


# Q13) check is equality 

x = 569
y = 456
print( x is b)


# Q14) check the symbol equality 

a= []
b =[]
print(a == b)


a= []
b ={}
print(a == b)


a= []
b =[]
print(a is b)


