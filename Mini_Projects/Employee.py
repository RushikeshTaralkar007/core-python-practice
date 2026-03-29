############################     MINI PROJECT 3 (Week 3)      ###############################

################################  Employee Data Processing System   ##################################
#######################   Used Python : Dictionary & Fuction  ############################


## Input Data 

employees =[
    {"id":1, "name":"Rushi", "age":21, "salary":60000},
    {"id":2, "name":"Tejas", "age":None, "salary":50000},
    {"id":3, "name":"Samarth", "age":22, "salary":40000},
    {"id":4, "name":"Ayush", "age":24, "salary":None},
    {"id":5, "name":"Viki", "age":23, "salary":80000},
    {"id":6, "name":"Om", "age":None, "salary":50000},
    {"id":7, "name":"Adity", "age":30, "salary":20000},
    {"id":8, "name":"Shyam", "age":32, "salary":None},
    {"id":9, "name":"Ram", "age":35, "salary":50000},
    {"id":10,"name":"Amit", "age":21, "salary":70000}
]



## Clean Data 

def clean_data(data):
    for emp in data:
        if emp["age"] is None:
            emp["age"] =0
        
        if emp["salary"] is None:
            emp["salary"] =0

    return data



## Add Bonus 

def add_bonus(data):
    for emp in data:
        emp["bonus"] = emp["salary"] *0.10
    return data



## Calculate average salary 

def average_salary(data):
    valid = [e["salary"] for e in data if e["salary"]>0]
    return sum(valid)/ len(valid)



## Find Top Employee 

def top_emp(data):
    emp = max(data, key=lambda x:x["salary"])
    return f"{emp['name']} (salary: {emp['salary']})"




## Filter Employees > 50 K

def filter_employees(data):
    result = []

    for emp in data:
        if emp['salary'] > 50000:
            result.append(emp)
    return result 



## Add Salary Categoty 

def salary_category(data):
    for emp in data:
        if emp['salary'] >60000:
            emp["category"] ="High"
        elif emp['salary'] >40000:
            emp['category'] ="Medium"
        else:
            emp['category']= "Low"
    return data



## Fix Employee As Valid Or Invalid 

def mark_status(data):
    for emp in data:
        if emp['salary'] ==0:
            emp['status'] = "Invalid"
        else:
            emp['status']="Valid"
    return data



## Convert list into dictionary 

def index_id(data):
    result = {}

    for emp in data:
        result[emp["id"]] =emp
    return result



### Generate Report 

def generate_report(data):
    print("\n------------------------- Employee Report ----------------------------")

    
    print(f"{'Name':<15} {'Salary':<10} {'Bonus':<10} {'Net':<12} {'Category':<10} Status")
    print("-" * 70)


    for emp in data:
        net = emp["salary"] + emp["bonus"]

        print(f"{emp['name']:<15} {emp['salary']:<10} {emp['bonus']:<10} {net:<12} {emp['category']:<10} {emp['status']}")





## Add summary section 

def summary(data):
    total= len(data)
    valid = len([emp for emp in data if emp['salary'] >0 ])
    invalid = total - valid 

    print("\n ---- Summary ----")

    print("Total Employees :",total)
    print("Valid Records :", valid)
    print("Invalid Records :", invalid)
    


def export_report(data):
    with open("employee_report.txt","w") as f:
        for emp in data:
            f.write(str(emp) + "\n")



employees = clean_data(employees)

salary_category(employees)

employees = add_bonus(employees)


print("Average Salary :",average_salary(employees))

print("Top Employees :", top_emp(employees))

filtered = filter_employees(employees)

mark_status(employees)

indexed = index_id(employees)

generate_report(employees)

summary(employees)

export_report(employees)





