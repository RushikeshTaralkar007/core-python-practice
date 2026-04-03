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