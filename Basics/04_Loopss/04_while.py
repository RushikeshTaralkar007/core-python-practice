####################    (For Data Engineer & Big Data Solve The While Loop Problems)    ###############################

#############    (While Loop)    ##################




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




# # Q22) count Uppercase Letters 

# text = "DataEngineer"
# i=0
# count=0
# while i<len(text):
#     if text[i].isupper():
#         count +=1
#     i +=1

# print(count)



# # Q23) Mask Phone Number 

# phone = input("Enter The Number :")
# i =0
# masked = ""
# while i <len(phone):
#     if i<6:
#         masked += "*"
#     else:
#         masked += phone[i]
#     i += 1
# print(masked)



# # Q24) Count Words 

# text = "data engineer roadmap"
# words = text.split()
# i =0
# while i <len(words):
#     print(words[i])
#     i +=1



# # Q25) Retry mechanism (3 attempts)

# attempt = 1 
# while attempt <= 3:
#     print("Trying...")
#     attempt +=1



# # Q26) Retry until success

# success = False 
# attempt =0
# while not success and attempt <5:
#     attempt +=1
#     print("Attempt",attempt)
#     if attempt ==3:
#         success=True



# # Q27) paginated API simulation 

# page =1
# while page <= 5:
#     print("Fetching page ",page)
#     page += 1



# # Q28) Batch Processing 

# data = list(range(1,21))
# i = 0
# while i < len(data):
#     print(data[i: i+5])
#     i += 5



# # Q29) Progress Tracker 

# progress = 0
# while progress <= 100:
#     print(progress,"%")
#     progress += 25


# # Q30) Generate OTP 

# import random

# otp =""
# i = 0
# while i<4:
#     otp += str(random.randint(0,9))
#     i += 1
# print(otp)




# # Q31) validate password digit check 

# password = "Data@123"
# i =0
# has_digit = False
# while i <len(password):
#     if password[i].isdigit():
#         has_digit=True
#     i += 1
# print(has_digit)





# # Q32) count rows manually 

# rows = [[1,2],[3,4]]
# i=0
# while i<len(rows):
#     print(rows[i])
#     i += 1




# # Q33) Log Generator 

# i =1
# while i <= 5:
#     print(f"Log Entry {i}")
#     i +=1



# # Q34) Stop when value Found 

# nums = [5,10,15,20]
# i =0

# while i <len(nums):
#     if nums[i]==10:
#         break
#     print("Number Has Found ")

#     i += 1



# # Q35) Skip Negative Values 

# nums = [1,-1,2,-6]
# i =0

# while i < len(nums):
#     if nums[i] <0:
#         i +=1 
#         continue
#     print(nums[i])
#     i +=1




# # Q36) Manual Search 

# nums = [4,8,15]
# i =0

# found = False
# while i < len(nums):
#     if nums[i] ==8:
#         found = True 
#     i += 1
# print(found)




# # Q37) count duplicates 

# nums = [1,2,2,3]
# i =0

# freq = {}
# while i <len(nums):
#     freq[nums[i]] = freq.get(nums[i],0) +1
#     i += 1
# print(freq)



# Q38) Validate Numeric String 

# text = "12345"
# i =0
# valid = True
# while i < len(text):
#     if not text[i].isdigit():
#         valid = False
#     i += 1
# print(valid)