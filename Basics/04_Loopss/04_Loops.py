####################    (For Data Engineer & Big Data Solve The All Loop Problems Like While , For Nested + Pattern Problems)    ###############################

#############    (While Loop)    ##################

###################  ( Day 1 )   ###################


# # Q1) Print 1-10

# i = 1
# while i<= 10:
#     print(i)
#     i += 1



# # Q2) print 10-1

# i = 10
# while i>= 1:
#     print(i)
#     i -= 1



# # Q3) Even Number (1-50)

# i = 2
# while i<= 50:
#     print(i)
#     i += 2



# Q4) odd Number (1-50)

# i = 1
# while i <= 50:
#     print(i)
#     i += 2



# # Q5) sum till 100

# i = 1
# total = 0

# while i <100:
#     total += i
#     i += 1


# print(total)




# # Q6) Factorial 

# num = 6
# fact = 1
# i = 1

# while i <= num:
#     fact *= i
#     i += 1
# print(fact)





# # Q7) Multiplication Table (7)

# i = 1
# while i <= 10:
#     print("7 *", i , "=", 7*i)
#     i += 1



# # Q9) count Digit 

# num = 12345658
# count = 0

# while num >0:
#     num //= 10
#     count += 1

# print(count)



# # Q10) Reverse Number 

# num = 12345
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10

# print(rev)




# # Q11) Iterate Through string 

# text = "data"
# i =0
# while i< len(text):
#     print(text[i])
#     i += 1



# # Q12) find max in list 

# nums = [10,40,30]
# i = 0
# max_val = nums[0]
# while i < len(nums):
#     if nums[i] >max_val:
#         max_val = nums[i]
#     i += 1
# print(max_val)



# # Q13) Remove Negatives

# nums = [5, -1,7,-2]
# i =0
# while i<len(nums):
#     if nums[i] <0:
#         nums.pop(i)
#     else:
#         i += 1

# print(nums)




# # Q14) Generate IDs

# i = 1
# while i<= 5:
#     print(f"EMP{i:03}")
#     i += 1




# # Q15) Replace None With 0

# data = [1,None,3]
# i =0
# while i<len(data):
#     if data[i] is None:
#         data[i]=0
#     i += 1
# print(data)




# # Q16) Strip Spaces From list

# names= ["Ram","Shyam"]
# i=0
# while i< len(names):
#     names[i] = names[i].strip()
#     i += 1
# print(names)



# # Q17) convert string list to integer

# nums = ["1","2","3"]
# i =0
# while i <len(nums):
#     nums[i]=int(nums[i])
#     i += 1
# print(nums)



# # Q18) Rermove The Duplicates

# nums = [1,2,2,3]
# unique=[]
# i =0
# while i<len(nums):
#     if nums[i] not in unique:
#         unique.append(nums[i])
#     i +=1
# print(unique)



# # Q19) count missing values 

# data = [1,None,2,None,None]
# i=0
# count=0
# while i <len(data):
#     if data[i] is None:
#         count +=1
#     i +=1
# print(count)



# # Q20) Valid Emails 

# emails =["a@gmail.com","Wrong"]
# i=0
# while i<len(emails):
#     if "@" in emails[i]:
#         print("Valid")
#     i +=1



# # Q21) Filter Age >30

# data =[{"age":25},{"age":40}]
# i=0
# while i<len(data):
#     if data[i]["age"]>30:
#         print(data[i])
#     i +=1


