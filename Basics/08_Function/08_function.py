####################    (For Data Engineer & Big Data Solve The Python Function Problems)    ###############################


# # Q1) How do you define a function in python 

# def greet():
#     name = input("Enter The Name :")
#     print("Hello",name)

# greet()



# # Q2) How do yoy create a fuction with parameters 

# def greet(name):
#     print("Hello",name)
# greet("Rushikesh")



# # Q3) Write a fuction to return the sum of two numbers 

# def add(a,b):
#     return a+b
# print(add(5,3))



# # Q4) Write a fuction to calculate the sqaure of a number

# def square(n):
#     return n*n
# print(square(4))



# # Q5) Write a function to check if a number is even 

# def is_even(n):
#     return n%2 ==0
# print(is_even(10))



# # Q6) write a fuction to calculate factorial 

# def factorial(n):
#     fact =1
#     for i in range(1,n+1):
#         fact *=i
#     return fact 

# print(factorial(5))



# # Q7) Write a fuction to return the maximum of two numbers 

# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(maximum(10,5))


# # Q8) write a fuctuion to return the length of a string 

# def string_length(s):
#     return len(s)
# print(string_length("python"))



# # Q9) write a fuction that converts a string to uppercase 

# def to_upper(text):
#     return text.upper()
# print(to_upper("data engineer"))


# # Q10) write a fuction that prints numbers from 1 to N

# def print_numbers(n):
#     for i in range(1,n+1):
#         print(i)
# print_numbers(5)



# # Q11) Write a fuction to calculate the sum of a list 

# def list_sum(lst):
#     return sum(lst)

# print(list_sum([1,2,3,4]))



# # Q12) Write a fuction to count ina vowels in a sting 

# def count_vowels(s):
#     vowels ="aeiou"
#     count =0

#     for c in s.lower():
#         if c in vowels:
#             count +=1
    
#     return count
# print(count_vowels("Rushikesh Taralakr"))



# # Q13) Write a fuction to reverse a string 

# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("Python"))



# # Q14) Write a fuction to check palindrome string 

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))



# # Q15) Write a fuction to return the largest number in a list 

# def largest(lst):
#     return max(lst)
# print(largest([4,6,62,89]))



# # Q16) Write a fuction with default parameters 

# def greet(name = "Guest"):
#     print("Hello",name)

# greet()



# # Q17) Write a function that accepts multiple arguments 

# def total(*numbers):
#     return sum(numbers)
# print(total(1,2,3,4))



# # Q18) Write a fuction that accepts multiple values

# def cal(a,b):
#     return a+b , a*b

# s ,m = cal(4,5)

# print(s,m)



# # Q19) Write a lambda fuction for square 

# square = lambda x: x*x

# print(square(5))



# # Q20) Write a fuction to filter even numbers from list 

# def even_numbers(lst):
#     result=[]

#     for i in lst:
#         if i %2 ==0:
#             result.append(i)
#     return result

# print(even_numbers([1,56,20,35,22,10,9,8]))



