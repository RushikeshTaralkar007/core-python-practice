####################    (For Data Engineer & Big Data Solve The Python Exception Handling Problems)    ###############################


### Exception Handling is a process in Python used to handle runtime errors so that the program does not crash and continues to run smoothly.


# 1. try : Contains risky code (where error can occur)

# 2. except :Handles the error if it occurs

# 3. else Runs if no error occurs


# ## basic syntax 

# try:
#     x = 10 / 0
# except:
#     print("Error")
# else:
#     print("Success")



data =[]

with open("data.txt",'r') as file:
    for line in file:
        line = line.strip()
        data.append(line)

print("Raw Data :",data)



# # Q1) Convert all values to integer safely 

# for i in data:
#     try:
#         print(int(i))
#     except:
#         print("Invalid",i)



# # Q2) Handle ValueError Only 

# for i in data:
#     try:
#         print(int(i))
#     except ValueError:
#         print("ValueError:",i)



# # Q3) Ignore Invalid Values 

# for i in data:
#     try:
#         print(int(i))
#     except:
#         pass



# # Q4) Store Only Valid Integers 

# valid =[]
# for i in data:
#     try:
#         valid.append(int(i))
#     except:
#         pass

# print(valid)



# # Q5) Store invalid values 

# invalid =[]
# for i in data:
#     try:
#         int(i)
#     except:
#         invalid.append(i)
# print(invalid)



# # Q6) Handle division by zero

# for i in data:
#     try:
#         num = int(i)
#         print(100/num)
#     except ZeroDivisionError:
#         print("Cannot Divide By Zero")
#     except:
#         print("Invalid :",i)



# # Q7) Use Finally Block 

# try :
#     x= int("abc")
# except:
#     print("Error")
# finally:
#     print("Done")


# # Q8) use else block

# try:
#     x=int("10")
# except:
#     print("Error")
# else:
#     print("Success :",x)


# # Q9) Print Error Message 

# try:
#     int("abc")
# except Exception as e:
#     print(e)


# # Q10) Handle Multiple Exception 

# try:
#     x= int('abc')
#     y=10/0
# except ValueError:
#     print("Value Error")
# except ZeroDivisionError:
#     print("Division Error")



# # Q11) Raise Custom Error 

# x = -5
# if x<0:
#     raise ValueError("Negative Not Allowed")



# # Q12) Skip Negative Numbers 

# for i in data:
#     try:
#         num = int(i)
#         if num < 0:
#             raise ValueError
#         print(num)
#     except:
#         print("Skipped :",i)



# # Q13) Count Valid Numbers 

# count =0
# for i in data:
#     try:
#         int(i)
#         count += 1
#     except:
#         pass
# print(count)



# # Q14) Count Invalid Numbers 

# count =0 
# for i in data:
#     try:
#         int(i)
#     except:
#         count +=1
# print(count)



# # Q15) Replace Invalid with 0 

# clean =[]
# for i in data:
#     try:
#         clean.append(int(i))
#     except:
#         clean.append(0)
# print(clean)



# # Q16) Sum Valid Numbers 

# total =0

# for i in data:
#     try:
#         total += int(i)
#     except:
#         pass

# print(total)



# # Q17) Average Of Invalid Number

# nums =[]
# for i in data:
#     try:
#         nums.append(int(i))
#     except:
#         pass
# print(sum(nums)/len(nums))


# # Q18) Find Maximum

# nums =[]
# for i in data:
#     try:
#         nums.append(int(i))
#     except:
#         pass
# print(max(nums))



# # Q19) Find Minimum 

# nums =[]
# for i in data:
#     try:
#         nums.append(int(i))
#     except:
#         pass
# print(min(nums))



# # Q20) Handle Empty List Safely 

# nums=[]
# try:
#     print(sum(nums)/len(nums))
# except ZeroDivisionError:
#     print("No Data")



# # Q21) Convert And square Numbers 

# for i in data:
#     try:
#         print(int(i)**2)
#     except ValueError:
#         print("Error")



# # Q22) Filter Positive Numbers 

# for i in data:
#     try:
#         num = int(i)
#         if num >0:
#             print(num)
#     except ValueError:
#         pass



# # Q23) Handle File Not Found 

# try:
#     open("wrong.txt")
# except FileNotFoundError:
#     print("File Missing")


# # Q24) Nested Try 

# try:
#     try:
#         x= int('abc')
#     except:
#         print("Inner")
# except:
#     print("Outer")



# # Q25) Use Pass To ignore 

# try:
#     int('abc')
# except:
#     pass


# # Q26) Multiple exception in one line 

# try:
#     int('abc')
# except (TypeError,ValueError, ZeroDivisionError):
#     print("Error")


# # Q27) Custom Exception 

# class MyError(Exception):
#     pass


# # Q28) Raise Custom Exception 

# raise MemoryError("Custom")


# Q29) Logging Error 

# try:
#     int('abc')
# except Exception as e:
#     print("Logged :",e)


# # Q30) Safe Devision 

# def safe_div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Error"
# print(safe_div(10,0))


# # Q31) Exception In Function 

# def convert(x):
#     try:
#         return int(x)
#     except:
#         return None


