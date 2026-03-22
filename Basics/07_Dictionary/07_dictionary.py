####################    (For Data Engineer & Big Data Solve The Python Dictionary Problems)    ###############################


# # Q1) How To Create a Dictionary

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# print(data)



# # Q2) How to access value from Dictionary

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# print(data["name"])



# # Q3) How To add new Key-value In The Dictionary

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# data["salary"] = 50000
# print(data)



# # Q4) How To Update The Value 

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# data["Age"]=20
# print(data)



# # Q5) How To Delete The Key

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# del data["City"]
# print(data)



# # Q6) How To Find The Length OF The Dictionary

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# print(len(data))



# # Q7) How To Print Sab keys 

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# print(data.keys())



# # Q8) If Check The Key Is Exist Or Not 

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# if "name" in data:
#     print("Key Exist")
# else:
#     print('Not Exist') 



# # Q9) Clear The Dictionary

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# data.clear()
# print(data)



# # Q10) How To Print Sab keys Using A Loop

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# for k in data:
#     print(k)



# # Q11) How To Print Sab Values Using Loop

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# for v in data.values():
#     print(v)



# # Q12) Print The Key-Value Pair 

# data = {"name":"Rushi","Age": 21,"City":"Pune"}
# for k,v in data.items():
#     print(k,v)



# # Q13) Sum Of The Dictionary Values 

# d= {"a":10,"b":20,"c":30}
# total =0

# for v in d.values():
#     total += v
# print(total)



# # Q14) Find The Maximum Values 

# d= {"a":10,"b":20,"c":30}
# print(max(d.values()))



# # Q15) Find The Minimum Value

# d= {"a":10,"b":20,"c":30}
# print(min(d.values()))



# # Q16) Count The Dictionary Values 

# d= {"a":10,"b":20,"c":30}
# print(len(d.values()))



# # Q17) Copy The Dictionary

# d= {"a":10,"b":20,"c":30}
# d2 = d.copy()
# print(d2)



# # Q18) Marge The Dictionary 

# d1={"a":1}
# d2={"b":2}

# d1.update(d2)
# print(d1)



# # Q19) Filter The Specific Value 

# data = {"a":10,"b":50,"c":20,"d":2}
# result ={}

# for k,v in data.items():
#     if v >= 15:
#         result[k] =v
# print(result)



# # Q20) Replace The Null Values In the Dictionary 

# data = {"a":10,"b":None}

# for k, v in data.items():
#     if v is None:
#         data[k]=0
# print(data)