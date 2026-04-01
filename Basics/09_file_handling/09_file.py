####################    (For Data Engineer & Big Data Solve The Python File Handling Problems)    ###############################


### Syntax

# file = open("File_Name", "mode")


# BASE SETUP (RUN THIS FIRST)

file_name = "example.txt"

valid_data = []
invalid_data = []

with open("example.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = [p.strip() for p in line.split(",")]

        try:
            price = int(parts[3])
            valid_data.append({
                "id": parts[0],
                "name": parts[1],
                "category": parts[2],
                "price": price
            })
        except:
            invalid_data.append(parts)




## Q1) Read The Entire Data 

# file = open("C:\Desktop\Python\Git_Core_Python\core-python-practice\example.txt","r")

# const = file.read()
# print(const)
# file.close 



## Q2) Read First Line 

# file = open("C:\Desktop\Python\Git_Core_Python\core-python-practice\example.txt",'r')

# content = file.readline()

# print(content)
# file.close()



# # Q3) Read the entire data in List format 

# file = open("C:\Desktop\Python\Git_Core_Python\core-python-practice\example.txt",'r')

# content = file.readlines()
# print(content)
# file.close()



# # Q4) Write to a file 

# file = open('example2.txt','w') ## Create a new file 




# # Q5) write a txt on the new file 

# file = open('example2.txt','w')
# file.write("Hello, Rushi")
# file.close()



# # ## Q6) Used Append Mode

# file = open("C:\Desktop\Python\Git_Core_Python\example2.txt",'a')

# file.write("\n,How Are you ?")
# file.close()
 


# # Q7) count Total records 

# print(len(valid_data) + len(invalid_data))



# # Q8) count valid records 

# print(len(valid_data))



# # Q9) count invalid records 

# print(len(invalid_data))


# # Q10) print All Product names

# for items in valid_data:
#     print(items["name"])


# # Q11) print all price 

# for items in valid_data:
#     print(items['price'])



# Q12) Get all Categories 

# for items in valid_data:
#     print(items['category'])




# # Q13) convert all prices to list 

# prices = [items['price'] for items in valid_data]
# print(prices)



# # Q14) print first record

# print(valid_data[0])



# # Q15) print last record

# print(valid_data[-1])


# # Q16) check invalid rows 

# print(invalid_data)


# # Q17) print product ids 

# for items in valid_data:
#     print(items['id'])


# # Q18) print raw invalid lines 

# for item in invalid_data:
#     print(item)


# # Q19) Find Total sales 

# print(sum(item['price'] for item in valid_data))



# # Q20) Find Average price 

# total = sum(item['price'] for item in valid_data)

# print(total/len(valid_data))



# # Q21) Find Maximum price 

# print(max(item['price'] for item in valid_data))



# # Q22) Find Minimum Price 

# print(min(item['price'] for item in valid_data))


# # Q23) Electronic items names

# for item in valid_data:
#     if item['category'] == "Electronics":
#         print(item)



# Q24) count Electronics 

print(sum(1 for i in valid_data if i['category'] == "Electronics"))









