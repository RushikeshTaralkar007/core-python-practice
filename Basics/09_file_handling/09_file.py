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



# # Q24) count Electronics 

# print(sum(1 for i in valid_data if i['category'] == "Electronics"))



# # Q25) Count Clothing

# print(sum(1 for i in valid_data if i['category'] == "Clothing"))



# # Q26) Count Accessories 

# print(sum(1 for i in valid_data if i["category"] == "Accessories"))



# # Q27) Items above 20000

# print([i for i in valid_data if i['price']>20000])



# # Q28) count items > 20000

# print(sum(1 for i in valid_data if i['price']>20000))




# # Q29) items <= 20000

# print([i for i in valid_data if i['price'] <= 20000])


# # Q30) Get Only The product names > 20000

# print([i['name'] for i in valid_data if i['price'] > 20000])




# # Q31) category wise count 

# cat_count ={}

# for i in valid_data:
#     cat_count[i['category']]=cat_count.get(i['category'],0)+1

# print(cat_count)




# # Q32) Category wise sales 

# sales ={}

# for i in valid_data:
#     sales[i['category']] = sales.get(i['category'],0) + i['price']
# print(sales)




# # Q33) Get all product names in list 

# names = [i["name"] for i in valid_data]
# print(names)



# # Q34) Find Laptop price 

# for i in valid_data:
#     if i['name'] == 'Laptop':
#         print(i['price'])




# # Q35) Find Product Less then 20000

# print([i for i in valid_data if i['price'] < 20000])



# # Q36) sum of electronic sales 

# print(sum(i['price'] for i in valid_data if i['category'] == "Electronics"))



# # Q37) Get Unique Category 

# print(set(i['category'] for i in valid_data))



# # Q38) sort by price ascending 

# print(sorted(valid_data, key=lambda x:x['price']))



# # Q39) sort by price descending 

# print(sorted(valid_data, key=lambda x:x['price'], reverse=True))



# # Q40) Top 3 expensive 

# print(sorted(valid_data, key=lambda x:x['price'], reverse=True)[:3])



# # Q41) Bottom 3 cheapest 

# print(sorted(valid_data , key=lambda x:x['price'])[:3])



# # Q42) write a clean data 

# with open("clean.txt",'w') as f:
#     for i in valid_data:
#         f.write(str(i)+ "\n")



# # Q43) write invalid data 

# with open('clean.txt','w') as f:
#     for i in invalid_data:
#         f.write(str(i)+"\n")



# # Q44) find most expensive product 

# print(max(valid_data, key=lambda x:x['price']))



# # Q45) find most expensive product 

# print(min(valid_data, key=lambda x:x['price']))



# # Q46) Group by category 

# group ={}

# for i in valid_data:
#     group.setdefault(i['category'],[]).append(i)
# print(group)



# # Q47) Count invalid entries 

# print(len(invalid_data))



# # Q48) Add new column : High & Low 

# for i in valid_data:
#     i['type'] ="High" if i['price'] >20000 else "Low"
# print(valid_data)



# # Q49) Get High Category names

# print([i["name"] for i in valid_data if i["price"]>20000])



# # Q50) Create summary dictionary 

# summary ={
#     "total" : len(valid_data) + len(invalid_data),
#     "valid" : len(valid_data),
#     "invalid" : len(invalid_data)
# }

# print(summary)


