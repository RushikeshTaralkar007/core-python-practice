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




# # Q21) Wwrite a fuction to calculate average 

# def average(lst):
#     return sum(lst) / len(lst)

# print(average([10,20,30,40]))




# # Q22) Write a recursive factorial fuction 

# def factorial(n):
#     if n==1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))



# # Q23) Write a fuction to remove duplicates from a list 

# def remove_duplicates(lst):
#     return list(set(lst))

# print(remove_duplicates([1,2,2,3,3]))



# # Q24) Write a fuction to check prime number 

# def is_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# print(is_prime(7))



# # Q25) Write a fuction to generate Fibonacci series 

# def fibonacci(n):
#     a,b = 0,1

#     for i in range(n):
#         print(a)
#         a,b = b,a+b
# fibonacci(5)




# # Q26) Write a fuction to count words in a sentence 

# def count_words(s):
#     return len(s.split())

# print(count_words("Python Is Powerful"))




# # Q27) Write a fuction to find minimum in list

# def minimum(lst):
#     return min(lst)

# print(minimum([3,0,2,8,6,9]))



# # Q28) Write a fuction to sort a list 

# def sort_list(lst):
#     lst.sort()
#     return lst

# print(sort_list([5,6,1,2]))




# # Q29) Write a fuction to check if list is empty 

# def is_empty(lst):
#     return len(lst) == 0

# print(is_empty([]))



# # Q30) Write a fuction to convert list to dictionary 

# def list_to_dict(keys,values):
#     return dict(zip(keys,values))

# print(list_to_dict(["a","b"],[1,3]))



# # Q31) Write a fuction to clean whitespace from string 

# def clean_txt(text):
#     return(text.strip())

# print(clean_txt(" Data "))



# # Q32) Write a fuction to convert dictionary values to integers 

# def convert_int(d):
#     return {k:int(v) for k,v in d.items()}

# print(convert_int({"a":'10',"b":'20'}))



# # Q33) Write a fuction to calculate total sales from records 

# def total_sales(records):
#     total =0

#     for r in records:
#         total += r["Sales"]

#     return total 

# data =[{"Sales":100},{"Sales":200}]

# print(total_sales(data))




# # Q34) Write a fuction to filter records with sales > 100


# def filter_sales(data):
#     result =[]
    

#     for d in data:
#         if d["sales"] >100:
#             result.append(d)
#     return result



# # Q35) Write a fuction to count frequency of elements 

# def frequency(lst):
#     freq ={}

#     for i in lst:
#         freq[i] = freq.get(i,0) + 1

#     return freq

# print(frequency([1,1,2,3]))



# # Q36) Write a fuction to flatten nested list 

# def flatten(lst):
#     result=[]

#     for sub in lst:
#         for item in sub:
#             result.append(item)
#     return result

# print(flatten([[1,2],[3,4],[5,6]]))




# # Q37) Write a fuction to calculate moving average 

# def moving_avg(lst):
#     result =[]

#     for i in range(1,len(lst)):
#         result.append((lst[i] + lst[i-1] /2))
#     return result

# print(moving_avg([10,20,30,40]))



# # Q38) Write a fuction to validate email 

# def validate_email(email):
#     return "@" in email and "." in email

# print(validate_email("test@gmail.com"))



# # Q39) Write a function to mask phone number

# def phone(num):
#     return num[:2] + "******" + num[-2:]
# print(phone("8720833556"))



# # Q40) Write a function to convert list of dict to dict by id

# def index_id(data):
#     result ={}
#     for d in data:
#         result[d["id"]] =d
#     return result

# print(index_id([{"id":1,"name":"Rushi"},{"id":2,"name":"Ram"}]))



# # Q41) Write a function to calculate percentage

# def percentage(values):
#     total = sum(values)
#     return [(v/total)*100 for v in values]
# print(percentage([50,100,200]))



# # Q42) Write a function to find second largest number

# def second_lar(lst):
#     lst = list(set(lst))
#     lst.sort()
#     return lst[-2]

# print(second_lar([10,20,30,50,60,70]))



# # Q43) Write a function to check password strength

# def strong_pass(p):
#     return len(p) >= 8

# print(strong_pass("abcd@123"))



# Q44) Write a function to convert list of strings to uppercase

# def upper_list(lst):
#     return [x.upper() for x in lst]

# print(upper_list(["data", "engineer"]))



# # Q45) Write a function to remove null values from dictionary

# def remove_null(d):
#     return {k:v for k,v in d.items() if v is not None}

# print(remove_null({"a":10,"b":20,"c":None}))




# # Q46) Write a function to group numbers by even and odd

# def group_num(lst):
#     result = {"even":[], "odd":[]}
#     for i in lst:
#         if i%2 == 0:
#             result["even"].append(i)
        
#         else:
#             result["odd"].append(i)
#     return result
# print(group_num([1,2,3,4,5]))



# # Q47) Write a function to find common elements between lists

# def common(a,b):
#     return list(set(a) & set(b))
# print(common([1,2,3],[2,3,4]))



# # Q48) Write a function to generate OTP

# import random 

# def generate_otp():
#     return random.randint(1000, 9999)

# print(generate_otp())



# # Q49) Write a function to check if list is sorted

# def is_sorted(lst):
#     return lst == sorted(lst)

# print(is_sorted([1,2,3]))



# # Q50) Write a function to count records

# def count_record(data):
#     return len(data)

# print(count_record([{"a":1},{"b":2}]))