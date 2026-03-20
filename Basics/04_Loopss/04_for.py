####################    (For Data Engineer & Big Data Solve The For Loop Problems)    ###############################

#############    (For Loop)    ##################

# # Q1) print all items in a list 

# data = [10,20,30,40]
# for item in data:
#     print(item)



# # Q2) print index + Value 

# data = [10,20,30,40]
# for i , val in enumerate(data):
#     print(i , val)


# # Q3) sum all numbers in list 

# data = [1,2,5,6,8]
# total =0 
# for num in data:
#     total += num 
# print(total)


# # Q4) Find Max value manually 

# data = [10,20,30,40]
# max_val = data[0]
# for num in data:
#     if num > max_val:
#         max_val = num
# print(max_val)



# # Q5) count even numbers 

# data = [1,5,9,2,8,6]
# count =0 
# for num in data:
#     if num % 2 == 0:
#         count += 1
# print(count)



# # Q6) Create new list with squares

# data = [2,4,6,8]
# squares =[]
# for num in data:
#     squares.append(num**2)
# print(squares)



# # Q7) Remove The Negative Numbers 

# nums = [5,-2,8,-1]
# positive =[]
# for n in nums:
#     if n>0:
#         positive.append(n)
# print(positive)


# Q8) count Duplicates 

# nums = [1,1,2,2,3,3,3]

# freq ={}
# for n in nums:
#     freq[n]= freq.get(n,0) + 1
# print(freq)




# # Q9) Filter Numbers > 50

# nums = [50,40,80,90,110]
# result =[]

# for n in nums:
#     if n >50:
#         result.append(n)
# print(result)



# # Q10) Reverse list Manually 

# nums = [1,2,3,4]
# rev =[]
# for i in range(len(nums)-1, -1 , -1):
#     rev.append(nums[i])
# print(rev)



# # Q11) print keys 

# d= {"a":1, "b":2}
# for key in d:
#     print(key)


# # Q12) Print Values 

# d= {"a":1, "b":2}
# for values in d.values():
#     print(values)



# # Q13) Print key-value pair

# d= {"a":1, "b":2}
# for k,v in d.items():
#     print(k,v)



# # Q14) Sum Dictionary values 

# d= {"a":1, "b":2}
# total = 0

# for sum in d.values():
#     total += sum
# print(total)




# # Q15) Find key with max value

# d= {"a":1, "b":2, "c":3,}
# max_key = max(d, key=d.get)
# print(max_key)




# # Q16) Count frequency of characters

# text = "data"
# freq ={}
# for ch in text:
#     freq[ch]= freq.get(ch,0)+1
# print(freq)


# # Q17) Merge 2 dictionaries

# d1 = {"a":2}
# d2 = {"b":4}

# for k,v in d2.items():
#     d1[k] =v
# print(d1)




# # Q18) Remove The key values < 2

# d=[1,2,0,3]
# new = {}
# for k,v in d.items():
#     if v >= 2:
#         new[k] = v
# print(new)



# # Q19) convert list to dictionary 

# keys = ["a","b"]
# vals= [10,20]

# result ={}
# for i in range(len(keys)):
#     result[keys[i]] = vals[i]
# print(result)



# # Q20) Nested Dictionary loop 

# data = {"emp1":{"salary":5000},"emp2":{"salary":4000}}
# for emp in data:
#     print(emp, data[emp]["salary"])




# # Q21) Read File line by line 

# with open("data.txt") as f:   ## Suppose txt file is exist in the system
#     for line in f:
#         print(line.strip()) 




# # Q22) count lines

# count =0
# with open("data.txt") as f:   ## Suppose txt file is exist in the system
#     for line in f:
#         count += 1
# print(count)




# # Q23) count words in file 

# words = 0
# with open("data.txt") as f:  ## Suppose txt file is exist in the system
#     for line in f:
#         words += len(line.split()) 
# print(words)



# # Q24) find longest word 

# longest = ""

# with open("data.txt") as f:  ## Suppose txt file is exist in the system
#     for line in f:
#         for word in line.split():
#             if len(word) >len(longest):
#                 longest = word
# print(longest)




# # Q25) count specific word 

# count =0

# with open("data.txt") as f:  ## Suppose txt file is exist in the system
#     for line in f:
#         if "data" in line:
#             count += 1
# print(count)




# # Q26) strip spaces from list

# names =[" Ram", "Shyam"]
# clean =[]
# for n in names:
#     clean.append(n.strip())
# print(clean)



# Q27) convert string into int

# nums = ["1","2","3","4"]
# result=[]
# for n in nums:
#     result.append(int(n))
# print(result)




# # Q28) Replace Null Values 

# data =[10,None,20]
# clean=[]
# for val in data:
#     if val is None:
#         clean.append(0)
#     else:
#         clean.append(val)
# print(clean)



# # Q29) Lowercase all string 

# words = ["DATA","ENGINEER"]
# result = []
# for w in words:
#     result.append(w.lower())
# print(result)



# # Q30) Remove Duplicates 

# nums = [1,1,2,2,3]
# unique =[]
# for u in nums:
#     if u not in unique:
#         unique.append(u)
# print(unique)



# # Q31) Flatten nested list 

# nested =[[1,2],[3,4]]
# flat=[]
# for sub in nested:
#     for item in sub:
#         flat.append(item)
# print(flat)




# # Q32) count rows manually 

# rows = [[1,2],[3,4],[5,6]]
# count=0
# for r in rows:
#     count +=1
# print(count)




# # Q33) Filter records 

# data = [{"age":25}, {"age":40}]
# result = []
# for d in data:
#     if d["age"] >30:
#         result.append(d)
# print(result)




# # Q34) count condition matches

# data = [{"age":25}, {"age":40}]
# count = 0
# for d in data:
#     if d["age"] >30:
#         count += 1
# print(count)




# # Q35) Generate ID's

# for i in range(1,6):
#     print(f"Emp{i:02}")




# # Q36) Retry mechanism 

# for attempt in range(5):
#     print("Trying...")



# # Q37) Paginated API simulation

# for page in range(1,6):
#     print(f"Fetching page{page}")



# # Q38) Create log entries 

# for i in range(5):
#     print(f"Log Entry{i}")


# # Q39) Batch Processing 

# data = list(range(1,21))
# for i in range(0,len(data),5):
#     batch =data[i:i+5]
#     print(batch)



# # Q40) validate emails 

# emails =["a@gmail.com","wrongmail"]
# for e in emails:
#     if "@" in e:
#         print("Valid")
#     else:
#         print('Invalid')



# # Q41) Check Missing values 

# data = [1,None,3]
# for i, val in enumerate(data):
#     if val is None:
#         print("Missing at",i)



# # Q42) Convert List to CSV line 

# row =["Ram",25,"Pune"]
# line=""
# for item in row:
#     line += str(item) + ","
# print(line[:-1])



# # Q44) Progress tracker 

# for i in range(1,11):
#     print(f"{i*10}% Complete")



# # Q45) Basic password validation

# pwd = input("Enter The Password :")
# has_digit =False
# for ch in pwd:
#     if ch.isdigit():
#         has_digit = True
# print("Valid" if has_digit else "Invalid")