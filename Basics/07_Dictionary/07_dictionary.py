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



# # Q21) Mutiple The Dictionary Value 

# data = {"a":10, "b":20, "c":5}

# for k in data:
#     data[k]=data[k]*2
# print(data)



# # Q22) Convert The String Value Into Integer 

# data = {"a":"10", "b":"20","c":"30"}

# for k in data:
#     data[k]=int(data[k])
# print(data)



# # Q23) Lowercase The Dictionary Values 

# data = {"name ":"RUSHI", "City":"PUNE"}

# for k in data:
#     data[k] =data[k].lower()
# print(data)



# # Q24) Value Greater Than Thershold Filter 

# d= {"a":10, "b":20,"c":30}
# result={}

# for k,v in d.items():
#     if v > 20:
#         result[k]=v
# print(result)



# # Q25) Rename The Keys In The Dictionary 

# data = {"name":"Rushi","Age": 510000,"City":"Pune"}
# data["Salary"] = data.pop("Age")
# print(data)



# # Q26) Sqaure The Dictionary Values

# d= {"a":10, "b":20,"c":30}

# for k in d:
#     d[k] = d[k] ** 2
# print(d)



# # Q27) Swap The Keys or Values

# d= {"a":10, "b":20,"c":30}
# swapped ={}

# for k,v in d.items():
#     swapped[v]=k
# print(swapped)



# # Q28) Remove The Specific Key From Dictionary 

# d= {"name": "Rushi", "city":None}
# d.pop("city",None)



# # Q29) Find The Average Value OF The Dictionary 

# d= {"a":10, "b":20,"c":30}

# avg = sum(d.values())/ len(d)
# print(avg)


# # Q30) Extract The age From The List Of Records 

# data = [{"age":25,}, {"age": 30}, {"age":40}]
# ages =[]

# for d in data:
#     ages.append(d["age"])

# print(ages)



# # Q31) Count The Frequency From The Dictionary

# text = "data"
# freq={}

# for ch in text:
#     freq[ch] = freq.get(ch,0) +1
# print(freq)



# # Q32) Iterate The Nested dictionary

# data = {"emp1":{"salary":5000},"emp2":{"salary":7000}}

# for emp in data:
#     print(emp, data[emp]["salary"])




# # Q33) Filter The Record Age > 30

# data = [{"age":25},{"age":40}]

# result =[]

# for d in data:
#     if d["age"] >30:
#         result.append(d)
# print(result)



# # # Q34) Convert dictionary in the list

# data = {10,20,30,40}

# items = list(data)
# print(items)



# # Q35) Dictionary Keys Convert Into list

# d ={"a":10,"b":20,"c":30}

# keys = list(d.keys())
# print(keys)



# # Q36) Dictionary values Convert Into list

# d ={"a":10,"b":20,"c":30}

# values = list(d.values())
# print(values)



# # Q37) Calculate The Total Salary in The dictionary

# data = {"emp1":5000, "emp2":7000}

# print(sum(data.values()))



# # Q38_) Find The Maximum Salary Employee 

# data = {"emp1":5000, "emp2":7000}

# print(max(data, key = data.get))



# # Q39) Calculate The Percentage from The dictionary

# data = {"A":50, "B":100}
# total = sum(data.values())

# for k in data:
#     print(k, (data[k]/total)*100)



# # Q40) Print The JSON Style Record 

# record ={"id":101, "name":"Ram"}

# for k,v in record.items():
#     print(k,":",v)