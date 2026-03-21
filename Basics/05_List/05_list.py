###################### (For Data Engineer & Big Data To Solve The List Based Problems)    #########################


# # Q1) How To create a List 

# nums = [10,20,30,40]
# print(nums)



# # Q2) How To Access List First Element

# nums = [10,20,30,40]
# print(nums[0])



# # Q3) How To Access List Last Element

# nums = [10,20,30,40]
# print(nums[-1])



# # Q4) How to find the length of the list

# nums = [10,20,30,40]
# print(len(nums))



# # Q5) How to Add New Element In the list

# nums = [10,20,30,40]
# nums.append(50)
# print(nums)



# # Q6) How To Insert Element On specific Position

# nums = [10,20,30,40]
# nums.insert(2,21)
# print(nums)



# # Q7) How to Remove The Element 

# nums = [10,20,30,40]
# nums.remove(20)
# print(nums)



# # Q8) How To Delete Last Element

# nums = [10,20,30,40]
# nums.pop()
# print(nums)



# # Q9) check Element Exist In the list

# nums = [10,20,30,40]

# if 20 in nums:
#     print("Found !")




# # Q10) How to show empty list

# nums = [10,20,30,40]
# nums.clear()
# print(nums)



# # Q11) print All list Elements Using Loop

# nums = [10,20,30,40]

# for n in nums:
#     print(n)



# # Q12) Find the Sum Of the list

# nums = [10,20,30,40]
# total = 0

# for n in nums:
#     total += n
# print(total)



# # Q13) How To Find The Maximunm Element 

# nums = [10,20,30,40]

# max_val = nums[0]

# for n in nums:
#     if n > max_val:
#         max_val =n
# print(max_val)



# # Q14) Count The Even Numbers 

# nums = [1,2,3,4]
# count =0 

# for n in nums:
#     if n % 2 ==0:
#         count += 1
# print(count)




# # Q15)Find The Sqaure of the elements in the list 

# nums = [10,20,30,40]
# squares =[]

# for n in nums:
#     squares.append(n*n)
# print(squares)



# # Q16) Reverse The List

# nums = [10,20,30,40]
# print(nums[::-1])



# # Q17) Find The Index Of Element 

# nums = [10,20,30,40]
# print(nums.index(20))



# # Q18) Find The count of repeated elements in the list 

# nums = [10,20,20,30,30,40]
# print(nums.count(20))



# # Q19) Copy The List 

# nums = [10,20,30,40]
# copy_list = nums.copy()
# print(copy_list)



# # Q20) Sort The List

# nums = [30,40,20,10]
# nums.sort()
# print(nums)




# # Q21) Remove The Duplicate elements

# nums = [1,2,2,3]
# unique =[]

# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print(unique)




# # Q22) Remove The Negative Numbers 

# nums = [1,-1,-4,5,9]
# result =[]

# for n in nums:
#     if n>=0:
#         result.append(n)
# print(result)



# # Q23) Replace The None Values 

# data = [10,None,30]
# result =[]

# for v in data:
#     if v is None:
#         result.append(0)
#     else:
#         result.append(v)
# print(result)




# # Q24) String Numbers Converted to the integers

# nums = ["1", "2","3","4"]
# result = []

# for n in nums:
#     result.append(int(n))
# print(result)



# # Q25) Flatten The Nested List

# nested = [[1,2],[3,4]]
# flat=[]

# for sub in nested:
#     for item in sub:
#         flat.append(item)
# print(flat)



# # Q26) Find the second largest Number 

# nums = [50,60,80,20,10]
# nums.sort()
# print(nums[-1])




# # Q27) Merge The List

# a=[1,2]
# b=[5,6]

# c=a+b
# print(c)




# # Q28) Find The List Intersection

# a= [1,2,3]
# b=[2,3,4]


# result=[]

# for n in a:
#     if n in b:
#         result.append(n)
# print(result)



# # Q29) Check List Is Sorted or not 

# nums = [1,4,3]

# if nums == sorted(nums):
#     print("Sorted")
# else:
#     print("Not Sorted")



# # Q30) Find The Longest string

# words = ["data","Engineering","ai"]
# print(max(words,key=len))



# # Q31) Calculate The Average 

# nums = [10,20,30,40]
# print(sum(nums)/len(nums))



# # Q32) Convert numbers into string 

# nums = [10,20,30,40]
# result = []

# for n in nums:
#     result.append(str(n))
# print(result)



# # Q33) Filter only The String From List

# data = [10,"data",20,"ai"]

# result =[]
# for item in data:
#     if isinstance(item, str):
#         result.append(item)
# print(result)


# # Q34) Double The List Numbers 

# nums = [1,2,3]
# result =[]

# for n in nums:
#     result.append(n*2)
# print(result)



# # Q35) Find The Top 3 Largest Numbers In the List

# nums=[10,50,60,80,30,90]

# nums.sort(reverse=True)

# print(nums[:-3])




# # Q36) Calculate The Percentage of The List

# nums = [50,100,150]

# total = sum(nums)

# percentage =[]

# for n in nums:
#     percentage.append((n/total)*100)

# print(percentage)




# # Q37) Can Filter The Greater Then Average Values

# nums = [10,20,30,40]

# avg = sum(nums)/len(nums)

# result =[]

# for n in nums:
#     if n > avg:
#         result.append(n)
# print(result)




# # Q38) Find The sqaures Of The Even elements in the list

# nums =[1,2,3,4,5,6,7,8]

# result =[]

# for n in nums:
#     if n%2 ==0:
#         result.append(n*n)
# print(result)



# # Q39) Find The Cumulative Sum 

# nums = [1,2,3,4]
# result =[]

# total =0

# for n in nums:
#     total +=n
#     result.append(total)

# print(result)




# # Q40) Find The Index +Value In The List

# nums =[10,20,30]

# for i ,val in enumerate(nums):
#     print(i,val)